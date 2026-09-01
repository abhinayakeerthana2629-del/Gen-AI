Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Pattern programs using for loop
>>> for i in range(5):
...     print(i,end =' ')
... 
...     
0 1 2 3 4 
>>> for i in range(5,0,-1):
...     print(i,end =' ')
... 
...     
5 4 3 2 1 
>>> #Right angle triangle
>>> for i in range(0,5):
...     for j in range(0,i):
...         print(i, end = ' ')
...     print()
... 
...     

1 
2 2 
3 3 3 
4 4 4 4 
>>> for i in range(1,6):
    for j in range(0,i):
        print(i+64, end = ' ')
    print()

    
65 
66 66 
67 67 67 
68 68 68 68 
69 69 69 69 69 
for i in range(1,6):
    for j in range(0,i):
        print(chr(i+64), end = ' ')
    print()

    
A 
B B 
C C C 
D D D D 
E E E E E 
for i in range(1,6):
    for j in range(0,i):
        print(chr(j+65), end = ' ')
    print()

    
A 
A B 
A B C 
A B C D 
A B C D E 
for i in range(1,6):
    for j in range(0,i):
        print(chr(i+64+32), end = ' ')
    print()

    
a 
b b 
c c c 
d d d d 
e e e e e 
