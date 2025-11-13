"""modules imported for basic factorial and test factorial limits"""
from factorial import factorial

print(factorial(4) == 24)
print(factorial(18) == 6402373705728000)
print(factorial(45) == 119622220865480194561963161495657715064383733760000000000)
# Test how high of a number your program can calculate. Can you push it further?
# Test to make sure function only accepted integers
print(factorial("banana") == "TypeError : Not a positive integer")
