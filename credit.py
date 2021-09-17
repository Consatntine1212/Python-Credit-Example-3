from cs50 import get_string

import re


while (True):
    number = get_string("Please insert your credit card number : ")
    sting = number.isnumeric()
    if sting == True:
        break
    else:
        print("Please incert an integer")

length = len(number)
if length == 15 or length == 13 or length == 16:
    omega = 0
else:
    print("INVALID")
    quit()

temp = 0
summ1 = 0
summ2 = 0
digits_array = [ 0 ,2 , 4 , 6, 8 , 1 , 3 , 5 , 7 , 9 ]
for i in range(length):
    temp = int(number[length - 1 -i])
    if (i + 1) % 2 == 0: # if i mod 2 = 0 aka i is even
        summ2 = summ2 + digits_array[temp]
    else:
        summ1 = summ1 + temp
    summ = summ1 + summ2


if summ % 10 != 0:
    print("INVALID")
    quit()

temp1 = int(number[0])
temp2 = int(number[1])
if length == 15 :
    #American Express
    if temp1 == 3 and (temp2 == 4 or temp2 ==7):
        print("AMEX")
        quit()
    else:
        print("INVALID")
        quit()
    # visa
elif length == 13:
    if temp1 == 4 :
        print("VISA")
        quit()
    else:
        print("INVALID")
        quit()
    # visa or Mastercard
elif length == 16:
    if temp1 == 4 :
        print("VISA")
        quit()
    elif temp1 == 5 and (temp2 == 1 or temp2 == 2 or temp2 == 3 or temp2 == 4 or temp2 == 5 ):
        print("MASTERCARD")
        quit()
    else:
        print("INVALID")
        quit()
else :
    print("IINVALID")
    quit()

