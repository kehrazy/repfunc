import time
import threading


def repfunc(interval, timeout):
    """Decorator that repeatedly calls a function at a specified interval until a specified timeout has been reached.

        Args:
            interval: A float representing the number of seconds between function calls.
            timeout: A float representing the number of seconds after which the function should stop being called.

        Returns:
            A decorator function that can be used to decorate other functions.
    """
    def decorator(func):
        """Decorator function that wraps the original function and repeatedly calls it at the specified interval until
        the specified timeout has been reached.

        Args:
            func: The function to be decorated.

        Returns:
            A new function that wraps the original function and repeatedly calls it at the specified interval until the
             specified timeout has been reached.
        """
        def wrapper(*args, **kwargs):
            """Function that wraps the original function and repeatedly calls it at the specified interval until the
            specified timeout has been reached.

            Args:
                *args: Arguments to be passed to the original function.
                **kwargs: Keyword arguments to be passed to the original function.

            Returns:
                A new thread object that runs the wrapped function at the specified interval until the specified timeout
                has been reached.
            """
            stop_time = time.time() + timeout

            def run_func():
                """Function that runs in a loop until the stop time has been reached.

                Inside this loop, it calls the original function with any arguments and keyword arguments that were
                passed to the wrapper function.

                After calling the function, it sleeps for the specified interval.
                """
                while time.time() < stop_time:
                    func(*args, **kwargs)  # call the original
                    time.sleep(max(0, interval))  # never negative

            repeating_thread = threading.Thread(target=run_func)  # define the looping thread
            repeating_thread.start()  # start the loop
            return repeating_thread  # return the thread object

        return wrapper

    return decorator