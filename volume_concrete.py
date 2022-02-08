"""Volume of Concrete Exercise
Calculate concrete volume needed, and total volume needed for all jobs needed
on a particular day
Wen-Qi Toh
8/2/22"""

volume_list = []
total_sum = 0

building = input("Do you have a residential or commercial building? ")

building = ''
while building != 'X':
    # 3 inputs: building type, length, width
    length = int(input("What is your concrete length in metres? "))
    width = int(input("What is your concrete width in metres? "))
    depth = int(input("What is your concrete depth in metres? "))

    volume = length * width * depth
    volume_list.append(volume)

    print("The volume of concrete required for a slab with a length of {} and"
          " width of {} and a depth of {} is {} cubic metres.".format(length,
                                                                      width,
                                                                      depth,
                                                                      volume))
    # building type
    building = input("Do you have a residential or commercial building? ")


for vol in volume_list:
    total_sum += vol

print("total amount of concrete needed for the day:{}".format(total_sum))
