#!/usr/bin/python


def debug(f):
    def wrapper(*args, **kwargs):
        print "called {2} {0} {1}".format(args, kwargs, f.__name__)
        return  f(*args, **kwargs)
    return wrapper
