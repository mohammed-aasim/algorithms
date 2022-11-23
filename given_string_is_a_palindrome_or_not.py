num = int( input ( " ENTER THE NUMBER: " ) )
 
temporary = num
rev = 0
 
# looping the given input and reversing the value  
while temporary != 0:
	rev = ( rev * 10 ) + ( temporary % 10 )
	temporary = temporary // 10
 
if num == rev:
	print( " number is palindrome " )
else:
	print( " number is not palindrome " )