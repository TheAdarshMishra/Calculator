#Taking User's Input
n1 = input("Enter the first number: ")
n2 = input("Enter the second number: ")

#Converting the string to integer
n1 = int(n1)
n2 = int(n2)

#Selecting the operator
o = input("Enter the operator: ")

#Performing the operation 

if o == "+":
  print(n1+n2)
elif o == "-":
  print(n1-n2)  
elif o == "*":
  print(n1*n2)
elif o == "/":
  print(n1/n2)
else:
  print("Please Select a Valid Operator")
