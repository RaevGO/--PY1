from pprint import pprint

list_ = [{'bin' : bin(x), 'dec' : x, 'hex' : hex(x), 'oct' : oct(x)} for x in range(16)]

pprint(list_)
