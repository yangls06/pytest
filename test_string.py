#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@Time    :   2022/12/04 09:25:46
@Author  :   Linsan Yang 
@Desc    :   test string
"""

# string in multiple lines using ''' '''
str_multiple_lines = '''
line1,
line2,
line3
'''

print('str_multiple_lines: \n', str_multiple_lines)

# ==== output ====
# str_multiple_lines: 
 
# line1,
# line2,
# line3


# string in multiple lines using ()
str_multiple_lines = ('line1,'
'line2,'
'line3'
)
print('str_multiple_lines: \n', str_multiple_lines)
# ==== output ====
# str_multiple_lines: 
#  line1,line2,line3

# string argment in multiple lines
def myprint(str):
    print('myprint:\n', str)

myprint('line1,'
'line2,'
'line3'
)
# ==== output ====
# myprint:
#  line1,line2,line3