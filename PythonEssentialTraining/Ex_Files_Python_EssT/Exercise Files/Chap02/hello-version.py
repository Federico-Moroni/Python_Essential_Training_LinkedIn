#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

import platform  # module

# Before version 3 print was a statement and now is a function
print('This is python version {}'.format(platform.python_version()))
