#Hashan - Grammer correction - Letters to Words

import numpy as np
import S2T1
import cv2

Ltr = S2T1.B()

'''# Python program to convert a list of character
def convert(s):

# initialization of string to ""
new = ""

# traverse in the string
for x in s:
new += x

# return string
return new
		
# driver code
print(convert(s))

The syntax is :
str = ""
str1 = ( "geeks", "for", "geeks" )
str.join(str1)
'''

# Python program to convert a list of character
def convert(s):

# initialization of string to ""
str1 = ""

# using join function join the list s by separating words by str1
return(str1.join(s))
	
# driver code
print(convert(s))
