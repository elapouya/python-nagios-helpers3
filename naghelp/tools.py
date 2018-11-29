# -*- coding: utf-8 -*-
#
# Création : July 7th, 2015
#
# @author: Eric Lapouyade
#
"""This module provides many utility functions and classes"""

import signal
import naghelp
import time
import fcntl
import errno
import os

__all__ = ['Timeout', 'TimeoutError', 'Lockfile']


class TimeoutError(Exception):
    """Exception raised when a connection or a collect it too long to process.

    It may come from unreachable remote host, too long lasting commands, bad
    pattern matching on Expect/Telnet/Ssh for connection or prompt search steps.
    """
    pass


class Timeout:
    """Set an execution timeout for a block of code

    It uses process signals, it should not work on windows platforms.

    Args:

        seconds (int):
            Time in seconds after which a TimeoutError will be
            raised if the block has not finished its execution.
        error_message(str): String to pass to the TimeoutError exception.

    Raises:

        TimeoutError: When the block execution has not finished on-time.

    Examples:

        >>> with timeout(seconds=3):
        >>>     time.sleep(4)

    """
    def __init__(self, seconds=1, error_message='Timeout'):
        self.seconds = seconds
        self.error_message = error_message

    def handle_timeout(self, signum, frame):
        raise TimeoutError(self.error_message)

    def __enter__(self):
        signal.signal(signal.SIGALRM, self.handle_timeout)
        signal.alarm(self.seconds)

    def __exit__(self, type, value, traceback):
        signal.alarm(0)


class Lockfile:
    """Acquires a lock on a file, releases it at the end.

    It uses :func:`fcntl.lockf`. It will wait until the lock is acquired or a
    Timeout is reached.
    A file with a ``.lock`` extension will be created.

    Args:

        filename (str): The filename to lock (without the ``.lock`` extension)
        timeout (int): The time in seconds after which a TimeoutError is raised
            if the lock cannot be acquired. None= No timeout. 0= no wait

    Raises:

        TimeoutError: When the lock is not acquired on-time.

    """
    def __init__(self, filename, timeout=10, delay=0.1):
        self.is_locked = False
        self.lockfile = '%s.lock' % filename
        self.filename = filename
        self.timeout = timeout
        self.delay = delay
        file_path = os.path.dirname(filename)
        if not os.path.exists(file_path):
            os.makedirs(file_path)

    def acquire(self):
        self.start_time = time.time()
        naghelp.logger.debug('LOCK : acquiring %s ...', self.lockfile)
        while True:
            try:
                self.fd = open(self.lockfile, 'w')
                fcntl.lockf(self.fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
                break
            except IOError as e:
                if e.errno not in [errno.EACCES, errno.EAGAIN]:
                    raise
                if (time.time() - self.start_time) >= self.timeout:
                    raise TimeoutError("Timeout occurred for locking %s" %
                                       self.filename)
                time.sleep(self.delay)
        self.is_locked = True
        naghelp.logger.debug('LOCK : acquired in %.3f s (%s)',
                             time.time() - self.start_time, self.lockfile)

    def release(self):
        if self.is_locked:
            fcntl.lockf(self.fd, fcntl.LOCK_UN)
            self.fd.close()
            try:
                os.unlink(self.lockfile)
            except (OSError, IOError):
                pass
            self.is_locked = False
        naghelp.logger.debug('LOCK : released after %.3f s (%s)',
                             time.time() - self.start_time, self.lockfile)

    def __enter__(self):
        if not self.is_locked:
            self.acquire()
        return self

    def __exit__(self, type, value, traceback):
        if self.is_locked:
            self.release()

    def __del__(self):
        self.release()
