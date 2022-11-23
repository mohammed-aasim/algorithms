# Python program to determine the value of factorial for a given number 
# modifying the value keyed in will produce a different result

Number = int(input(" Enter the number for which factorial value to be determined : "))

factorial = 1

# to verify that the given number is greater than zero incase it is less than zero then the 
# message stated below will be printed

if Number < 0:
   print(" ! ! ! ! ! Factorial value cannot be intended for negative integers ! ! ! ! ! ")
# The default factorial value for zero is one and this is printed here
elif Number == 0:
   print(" ! ! ! ! 1 is the factorial value 0 ! ! ! ! ")
else:
# For loop to handle the factorial calculation
   for i in range(1,Number + 1):
       factorial = factorial*i
   print("The factorial value for the " , Number , "is" , factorial)