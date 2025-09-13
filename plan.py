from math import *

convert = 0
# entering your current time, firstly the hour, then the minutes
current_time = [int(input("Enter an hour: ")),
                int(input("Enter the minutes: "))]
# the end of your working day (hours in paretheses and minutes outside after plus)
minutes = (22 * 60) + 0
time = int(minutes - (current_time[0] * 60 + current_time[1]))
# total resting time calculation (denominator is a sum of both work and rest from their ratio(1:6 -> 1+6=7))
rest = time / 7
rest_minutes = round(rest % 60)
averall_rest = [int(floor(rest / 60)), int(rest_minutes)]
# 6 is work from the ratio 1:6
work = [int(6 * floor(rest / 60)), int(6 * rest_minutes)]
work0 = 120  # your single work period in minutes
rest0 = 20  # your single rest period in minutes

if work[1] > 60:
    work[0] = work[0] + floor(work[1] / 60)
    work[1] = round(work[1] % 60)
# if the ratio of rest in your plan is different, multiply both parts of the averall rest by the same rest fraction


def plan():
    print(f"Your working time is {work[0]} hours and {work[1]} minutes ")
    print(
        f"Your resting time is {str(averall_rest[0])} hours and {str(averall_rest[1])} minutes ")


def full_plan(time=time):
    print(f"Beginning at", end=" ")
    print(":".join(str(x) for x in current_time))

    while time > 0:
        # this part of loop is for work and rest time calculation in the beginning
        if time >= 140:  # in every part of the loop pick your own sum of single work+rest period
            current_time[0] += (work0 // 60)
            print("Work till", end=" ")
            print(current_time[0], end=":")
            if current_time[1] < 10:
                print(f"0{current_time[1]}", end=" ")
            else:
                print(current_time[1], end=" ")
            current_time[1] = current_time[1] + rest0
            if current_time[1] >= 60:
                current_time[0] += 1
                current_time[1] -= 60
            if current_time[1] < 10:

                print(
                    f"Rest till {str(current_time[0])}:0{str(current_time[1])}")
            else:
                print(
                    f"Rest till {str(current_time[0])}:{str(current_time[1])}")
        # this part of loop is for work and rest time calculationm when there aren't
        elif 120 < time <= 140:  # right value - max work+rest time when the rest is still possible, left value is max work - singe rest period
            current_time[0] += (floor(time // 60))
            print("Work till", end=" ")
            print(":".join(str(x) for x in current_time), end=" ")
            current_time[1] += time - work0
            if current_time[1] >= 60:
                current_time[0] += 1
                current_time[1] -= 60
            if current_time[1] < 10:
                print(
                    f"rest till {str(current_time[0])}:0{str(current_time[1])} \n End of the day")
            else:
                print(
                    f"rest till {str(current_time[0])}:{str(current_time[1])} \n End of the day")

        elif 0 <= time <= 120:  # when rest is not possible anymore
            current_time[0] += floor(time // 60)
            current_time[1] += floor(time % 60)
            if current_time[1] >= 60:
                current_time[0] += 1
                current_time[1] -= 60
            if current_time[1] < 10:
                print(
                    f"work till {str(current_time[0])}:0{str(current_time[1])} \n End of the day")
            else:
                print(
                    f"work till {str(current_time[0])}:{str(current_time[1])} \n End of the day")
        time -= (work0 + rest0)


plan()
full_plan()
