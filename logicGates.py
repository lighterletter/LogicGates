
"""
0 = false
1 = true


Not
a	result
----------
0	1
1	0

And (true if both are true)
a 	b 	result
--------------
0	0     0
0	1	  0
1	0	  0
1	1	  1

Or (true if either is true)
a 	b 	result
--------------
0	0	  0
0	1	  1
1	0 	  1
1	1     1

Nand (negation of 'and')
--------------
a	b	result
0	0	1
0	1	1
1	0	1
1	1	0

Nor (negation of 'or')
--------------
a	b	result
0	0	1
0	1	0
1	0	0
1	1 	0

Xor (true if only one is true)
--------------
a 	b 	result
0	0	0
0	1	1
1	0	1
1	1 	0
"""

from prettytable import PrettyTable
from blessings import Terminal
term = Terminal()

# derive everything from `nand()`
def nand(a, b):
	return not (a and b)

def test(f):
	pt = PrettyTable(["a", "b", "result"])
	pt.add_row([False, 	False, 	f(False, 	False)])
	pt.add_row([False, 	True, 	f(False, 	True)])
	pt.add_row([True, 	False, 	f(True, 	False)])
	pt.add_row([True, 	True, 	f(True, 	True)])
	print term.yellow(f.__name__)
	print pt

def not_(val):
	return nand(val, True)

def or_(a, b):
	v1 = nand(a, True)
	v2 = nand(b, True)
	return nand(v1, v2)
test(or_)

def or_another_way(a, b):
	v1 = nand(a, a)
	v2 = nand(b, b)
	return nand(v1, v2)
test(or_another_way)

def and_(a, b):
	#nand(a, a), nand(b, b) doesn't work...
	v1 = nand(a, b)
	v2 = nand(a, b)
	return nand(v1, v2)
test(and_)
