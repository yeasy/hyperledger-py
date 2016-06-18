import requests

import timeit


def test(url="http://127.0.0.1:80"):
    r = requests.get(url)
    return r

if __name__ == '__main__':
    print("Test starting...try 2000 times")
    duration = timeit.timeit("test()", number=2000,
                             setup="from __main__ import test")
    print("2000 times done, the time={}".format(duration))
