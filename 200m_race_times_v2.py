"""Mr Baker's quiz
Modify this second version so that users can enter times for either the 100m,
the 200m, or the 400m races. The user should also be allowed to select an event
and see all the times entered, as well as the fastest and average times for
that event. There should also be a command to clear all saved times.
Wen-Qi Toh
13/2/22"""


# functions
def remove(list):
    try:
        list.remove(-1)
    except ValueError:
        return


def average_fast(list):
    average = sum(list) / len(list)
    print(f"Average time for event is: {average.__round__(2)} seconds")
    fastest = min(list)
    print(f"Fastest time for event is: {fastest} seconds")


def list_add(list):
    valid_num = False
    while not valid_num:
        finish_time = float(input("What are the finishing times of the race "
                                  "in seconds? Enter one by one, pressing <enter> "
                                  "after each entry. Enter '-1' to stop: "))
        if finish_time != -1:
            list.append(finish_time)
        else:
            valid_num = True
            print("*Program Has Stopped Entering Finish Times*")
            break


# main program
valid = False

oh_times = []
th_times = []
fh_times = []

finish_time = ""

while not valid:
    event = int(input("Is your event 100m, 200m, or 400m? Please enter either "
                      "'100', '200', or '400' as your answer: "))

    # while finish_time != -1:
    if event == 100:
        list_add(oh_times)
    elif event == 200:
        list_add(th_times)
    elif event == 400:
        list_add(fh_times)

    see_results = int(input("Would you like to see the results? Enter '1' for 100m, '2' for "
                            "200m or '4' for 400m: "))
    if see_results == 1:
        print("100m results:")
        print(*oh_times, sep=", ")
        average_fast(oh_times)
    elif see_results == 2:
        print("200m results:")
        print(*th_times, sep=", ")
        average_fast(th_times)
    elif see_results == 4:
        print("400m results:")
        print(*fh_times, sep=", ")
        average_fast(fh_times)

    exit_cont = input("To clear all saved data, enter 'C' + <enter> To exit "
                      "the program, enter 'X' + <enter>. To continue the"
                      " program, press any other key + <enter>.").capitalize()
    if exit_cont == "X":
        valid = True
        print("Goodbye")
    elif exit_cont == "C":
        oh_times.clear()
        th_times.clear()
        fh_times.clear()
        print("*All Data Cleared*")





