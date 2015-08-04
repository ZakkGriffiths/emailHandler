#!/usr/bin/env python
import inspect, os
print "Script File Name:"
print inspect.getfile(inspect.currentframe())
print "Path to Script:"
print os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
