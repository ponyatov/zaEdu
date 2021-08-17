import config

import os, sys, re
import datetime as dt

class Object():
    def __init__(self): pass
    def box(self, that): pass

    # \ dump
    def __repr__(self): pass
    def dump(self, cycle=[], depth=0, prefix=''): pass
    def head(self, prefix=''): pass
    def tag(self): pass
    def val(self): pass
    # / dump

    # \ operator
    def __getitem__(self, key): pass
    def __setitem__(self, key, that): pass
    def __floordiv__(self, that): pass
    # / operator


# \ primitive

class Primitive(Object): pass

class S(Primitive): pass

class Sec(S): pass

class Num(Primitive): pass

class Int(Num): pass

class Hex(Int): pass

class Bin(Int): pass

# / primitive

# \ container

class Container(Object): pass

# / container

# \ active

class Active(Object): pass

# / active

# \ meta

class Meta(Object): pass

class Module(Meta): pass

class Project(Module):
    def sync(self): pass


# / meta

# \ io

class IO(Object): pass

class Dir(IO): pass

class File(IO): pass

class Net(IO): pass

# / io

# \ pyproject

class PyProject(Project): pass

# / pyproject

# \ system init

if __name__ == '__main__':
    try:
        {
            'all': PyProject
        }[sys.argv[1]]().sync()
    except IndexError:
        PyProject().sync()

# / system init
