"""
Created on Wed Dec  5 18:34:52 2018

@author: akash
"""

import mmh3
from bitarray import bitarray
from collections import Counter

# Set S
with open('listed_username_30.txt', 'r') as f:
    text = f.read()
    S = text.split('\n')
    
# Stream to test
with open('listed_username_365.txt', 'r') as f:
    text = f.read()
    Stream = text.split('\n')    
    
    
# m => len(S) => 316851
# n => Total number of bits in array => 4 * 316851 => 1267404
# k = n/m * ln(2) => 2.77
  
# Initializing parameters
n = 4 * len(S)
k = 3 # ~ 2.77

hashTable = Counter(S)

# Initializing bit array
bitArray = bitarray(n)
bitArray.setall(0)

# Populating bit vector
def addToBitArray(item):
    for i in range(k):
        bitIndex = mmh3.hash(item, i) % n
        bitArray[bitIndex] = 1

        
for i in S:
    addToBitArray(i)


# Testing the stream             
def testItem(item):
    for i in range(k):
        bitIndex = mmh3.hash(item, i) % n
        if (bitArray[bitIndex] == 0):
            return False
    return True

    
FPCount, TNCount = 0, 0
for elem in Stream:
    if (testItem(elem)):
        if (elem not in hashTable):
            FPCount += 1
    else:
        TNCount += 1


print("================================================================")
print("n (number of bits in an array) : ", n)
print("m (number of elements in the set) : ", len(S))
print("k (number of hash functions) : ", k)
print("False positive % : ", FPCount / (FPCount + TNCount) * 100, "%")
print("================================================================")


"""

Output:
    
    
================================================================
n (number of bits in an array) :  1267404
m (number of elements in the set) :  316851
k (number of hash functions) :  3
False positive % :  14.686090663986018 %
================================================================


"""