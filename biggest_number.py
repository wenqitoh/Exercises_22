"""Biggest Number Exercise
two number values, compare, output highest value or equal. Loop till '0'
Wen-Qi Toh
4/2/22"""


num_1 = int(input("Please enter an integer number:"))

while num_1 != 0:
    num_2 = int(input("Please enter another integer number:"))

    if num_1 > num_2:
        print("{} is bigger than {}.".format(num_1, num_2))
    elif num_1 < num_2:
        print("{} is bigger than {}.".format(num_2, num_1))
    else:
        print("The numbers are equal.")

    num_1 = int(input("Please enter an integer number:"))

else:
    print("end of num test.")

