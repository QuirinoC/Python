'''As you might see now the pseudo
tutorial will be all written in Python
This way you could just copy the code
 and test yourself'''
#The most basic thing we learn to print in Python is
#The one and only, the world famous Hello world
print ("Hello world")
'''In python 3.something print works
 as a function. It takes one argument which
  can be a string like Hello world
or a variable as it could be'''
string_x = "Hello world"
print (string_x) #Prints Hello World
#[Note for Myself add a link to Basic types and their use]
'''As you can see im jumping from single
line comments to multi when its needed,
"...because i can"-Ken Bauer'''
#You can print to the screen more types like integers or floats
int_x = 10 #Prints 10
float_x = 20.0 #Prints 20.0
#NOTE we are not using the same x or something each something_x
#Its used only for names [Note for self, add tips on calling things]
print (int_x) #Prints the int_x value
print (float_x) #Prints the float_x value
'''Sometimes you want to print something
more than just the value of something
thats when concatenating comes useful'''
hello = "Hola"
world = "Mundo"
print (hello + world) #This is a bit problematic since it Prints
#HolaMundo together so we need
print (hello + " " + world )
'''If we would need to print a string
with a lots of variebles in itit would get
tedious over time to do variable + " " + variable +
" " + variable... and so on, in this cases
we could use string formatting'''
#Watch dis string boi
#Copy this code if you want and test string formatting yourself
#(I could use input() but well this is a output tutorial)
name = "Juan"
lastName = "Quirino"
ageInYears = 18
fingersInLeftHand = 5.1
gender = "Male"
'''So now we have 5 variables, i would
like to write a line of code that is reusable
and describes the user this is when string
formatting comes useful'''
#So we can have this
print ("Hello my name is %s %s, i am %s years old im a %s and i \
have %s fingers in my left hand") % \
(name,lastName,ageInYears,gender,fingersInLeftHand)
#Instead of this
#Plus we need to use str() to convert to string
print ("Hello my name is " + name + ", i am " + \
str(ageInYears) + " old im a " + gender + " and i have " + \
str(fingersInLeftHand) + " in my left hand")
#As you can see im using a \ in my print statement
# \ Serves to continue a statement on next line without
#Breaking the statement
