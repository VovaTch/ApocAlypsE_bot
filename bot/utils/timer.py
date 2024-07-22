from contextlib import contextmanager
from typing import Generator
import warnings
import time


@contextmanager
def time_enforcer(min_time: float) -> Generator:
    """
    Simple context manager to enforce the code to run at minimum `min_time` seconds

    Args:
        min_time (float): Minimum time to run

    Yields:
        Generator: Required for the context manager
    """
    time_s = time.time()
    yield
    elapsed_time = time.time() - time_s

    if elapsed_time < min_time:
        time.sleep(min_time - elapsed_time)
    else:
        warnings.warn(
            f"Execution time exceeded {min_time} seconds by {elapsed_time - min_time} seconds."
        )
