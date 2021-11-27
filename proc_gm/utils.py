import os
import random

DIR = os.path.dirname(os.path.realpath(__file__))
ROOT = os.path.dirname(DIR)

def root_path(path):
    return os.path.join(ROOT, *path.split('/'))

def rand_range(n):
    l = list(range(n))
    random.shuffle(l)
    return l
