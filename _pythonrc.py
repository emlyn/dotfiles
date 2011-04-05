#from __future__ import print_function
#try:
#    from utils import *
#except ImportError:
#    print "Module utils not available."

import sys, os
sys.path.append(os.environ["HOME"] + "/lib")
del sys, os

try:
    import emlyn
    for sub in emlyn.__all__:
        m = __import__("emlyn." + sub, fromlist=["*"])
        for n in dir(m):
            if not n[0].isalpha(): continue
            globals()[n] = m.__getattribute__(n)
except ImportError:
    print("Emlyn library not available")

try:
    import readline
except ImportError:
    print("Module readline not available.")
else:
    class _History:
        def __init__(self):
            self.rl = readline
        def __getitem__(self, i):
            l = len(self)
            if i < 0: i = l+i
            if i >= l or i < 0: raise IndexError("history index out of range")
            return self.rl.get_history_item(i)
        def __len__(self):
            return self.rl.get_current_history_length()
        def __str__(self):
            return str([self[i] for i in xrange(len(self))])
        def __repr__(self):
            return str(self)
    hist = _History()
    import rlcompleter
    readline.parse_and_bind("tab: complete")
    #readline.parse_and_bind("bind ^I rl_complete") # for Leopard
    del readline, rlcompleter, _History
