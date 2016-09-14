num = int(input("Give me a number: "))
if num % 4 == 0:
    print ("This is multiple of 4")
elif num % 2 == 0:
    print ("This is an even number")
check = int(input("Give me another number: "))
if num % check == 0:
    print ("{} is evenly divisible by {}".format(num,check))
