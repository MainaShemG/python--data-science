def tri_recursion(k):
  if(k>0):
    result = k+tri_recursion(k-1)
    print(result)
  else:
    result = 0
  return result

#print("\n\nRecursion Example Results")
tri_recursion(6)

#short program
name = input("Enter your name please: ")
age = input("enter you age:")
print(f'you are {name} and {int(age)} years old')

myset={3,3,3,4,4,5,5,5,23,34,23,65,56,77}
print(myset)




