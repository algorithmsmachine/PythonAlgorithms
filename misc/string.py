import string
import re

str = "Hello World"
j = 0
srr = ""

for i in str:
    print(str[i])
    srr[j] = i #'str' object does not support item assignment 
    j = j + 1
print (srr)

