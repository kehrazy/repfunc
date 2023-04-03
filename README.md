# repfunc

a decorator for something that repeats. a lot.

## Features
- Works.

## Installation
( does not work yet )
```commandline
pip install repfunc
```

## Example:
```python
import time

from repfunc import repfunc


@repfunc(timeout=5, interval=1)
def my_polling_thread():
    print("hi from the polling thread!")


if __name__ == '__main__':
    time_start = time.time()
    print("starting the polling thread...")
    poll_thread_future = my_polling_thread()
    print("waiting for the polling thread to finish...")
    poll_thread_future.join()
    time_end = time.time()
    print("done! took: {0:.5f}s".format(time_end - time_start))

```
