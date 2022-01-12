import os
from functools import wraps


def exit_code():
    # wait() returns a tuple consisting of:
    # - the child PID
    # - 2 bytes: the higher byte = the exit code (if the signal number is 0)
    #            the lower byte = the signal number that killed the process
    return os.wait()[1] >> 8


def nondeterministic(function):
    @wraps(function)
    def wrapper(*args: list, **kwargs: list):
        # Creates a child process
        process_id = os.fork()

        # The child process calls the function and returns
        if process_id == 0:
            function(*args, **kwargs)
            return

        # The parent process waits for the process to end.
        return exit_code() != 0

    return wrapper


def choice(values=(True, False)):
    result = 0
    for value in values:
        # Creates a child process for each value
        process_id = os.fork()

        # The child process returns the value
        if process_id == 0:
            return value

        # The parent process exits if the exit code is not 0
        result = exit_code()
        if result != 0:
            break
    os._exit(result)


def success():
    os._exit(1)


def fail():
    os._exit(0)
