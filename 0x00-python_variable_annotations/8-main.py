#!/usr/bin/env python3

from _make_multiplier import make_multiplier

#make_multiplier = __import__('8-make_multiplier').make_multiplier
print(make_multiplier.__annotations__)
fun = make_multiplier(5)
print("{}".format(fun(2.2)))