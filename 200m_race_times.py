"""Mr Baker's quiz
Write a program that asks for finishing times of a 200m race, until the user enters the number -1.
Once all the times have been entered, print out
- all the times that were entered
- the fastest time, and
- the average time
Wen-Qi Toh
11/2/22"""

times = []
finish_time = ""
while finish_time != -1:
    finish_time = float(input("What are the finishing times of the 200m race "
                              "in seconds? Enter one by one, pressing <enter> "
                              "after each entry. Enter '-1' to stop: "))
    times.append(finish_time)

if finish_time == -1:
    times.remove(finish_time)

    print(f"\nAll running times entered :")
    print(*times, sep=", ")
    print("Fastest time is:", min(times))
    average = sum(times) / len(times)
    print(f"Average time is: {average.__round__(2)}")
    print("All times measured in seconds.")


