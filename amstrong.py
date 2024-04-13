######********Check Armstrong Number**********
# 153 is armstrong cuz 1*1*1+5*5*5+3*3*3 =153 and 120 is not armstrong 1*1*1+2*2*2+0*0*0=9

# import math
# a = int(input())
# b = a//10    # 153 ==> 15
# c = b%10     # 5
# d = a%100    ##53
# e = d%10     #3
# f = b//10    #1


# x = pow(f,3)+pow(c,3)+pow(e,3)


# if a==x:
#     print("Armstrong Number")
# else:
#     print("Not an Armstrong Number")

def is_armstrong_number(num):
  original_num = num
  sum = 0
  number_of_digits = len(str(num))

  while num > 0:
    digit = num % 10
    sum += digit ** number_of_digits
    num //= 10

  return original_num == sum

# Check if 153 is Armstrong number
if is_armstrong_number(153):
  print(153, "is an Armstrong number.")
else:
  print(153, "is not an Armstrong number.")
