# THINK OF A NUMBER TRICK
#WHATEVER NUMBER U ENTER IT WILL ALWAYS RESULT IN ONE PROVIDED IT IS BETWEEN 1 AND 10
number = int(input('Enter a number between 1 and 10'))
originalnumber = number
number += 2
number *= 2
number -= 2
number /= 2
number = number - originalnumber
print(number)