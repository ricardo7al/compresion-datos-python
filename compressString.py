
text = b'zyx zyx zyx zyx zyx zyx zyx zyx zyx'

import sys, zlib 

print ("Text:", text)
print ("Size in bytes:", sys.getsizeof(text))
print ()

compressed = zlib.compress(text)

print("Text compressed:", compressed)
print("size in bytes:", sys.getsizeof(compressed))
