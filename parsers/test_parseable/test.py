#!/usr/bin/env python

import example_json
import sys

#def f_parse_constant(o):
#    raise BaseException

def parse_file(path):

    with open(path, 'r') as f:
    
        data = f.read()

        try:
            o = example_json.JSONElement.parse(data).value
            return o
            #o = json.loads(data, parse_constant=f_parse_constant)
            #print(o)
            #if o == None:
            #    sys.exit(1)

        except Exception as e:
            #print("--1")
            #print(e)
            #print("--2")
            sys.exit(1)
    
    """
    s = o.encode('utf-8')
    with open('/Users/nst/Desktop/p.txt', 'wb') as f:
        f.write(s)
    """

def parse_interactive(path):
    with open(path, 'r') as f:
        data = f.read()
        return example_json.JSONElement.parse(data).value

    
if __name__ == "__main__":

    path = sys.argv[1]
    parse_file(path)

    sys.exit(0)
