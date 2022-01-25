num = input("insert a number for a fun fact about it:")
num = int(num)
if num < 0:
    print("haha wow ur num is smaller than 0 my dude")

elif 0 <= num <= 10:
    print("wow the integer u gave me is within the range of [0,10]")

else:
    print("yep that number is greater than 10 for sure")
