from datetime import datetime
from datetime import timedelta


# Simple Pomodoro Timer
# Work loop still needs a bit of work: Short breaks should stop happening after
# 4 work intervals.


def work_interval_timer():
    """Time the 25 minute work intervals."""
    print("Time to get to work!\n")
    work_interval = datetime.now() + timedelta(minutes=25)
    while datetime.now() < work_interval:
        pass
    else:
        print("Work interval complete.")


def short_break():
    """Time short breaks."""
    print("Time for a short break.\n")
    short_break_timer = datetime.now() + timedelta(minutes=5)
    while datetime.now() < short_break_timer:
        pass
    else:
        print("Break time is up.\n")


def long_break():
    """Time long breaks."""
    print("Fourth work interval completed.\nTime for a long break.\n"
          "You've earned it!\n")
    long_break_timer = datetime.now() + timedelta(minutes=15)
    while datetime.now() < long_break_timer:
        pass
    else:
        print("Your long break is over.")


instructions = input("Welcome to a Pomodoro Timer!\n"
                     "This application will enhance your productivity\n"
                     "by timing your work periods and break times.\n"
                     "Please enter [c]ontinue to start or e[x]it to quit\n>")

counter = 0

if instructions == 'c':
    pomodoro = True
    while pomodoro:
        work_interval_timer()
        counter += 1
        short_break()
        start_working = input("Please enter [c]ontinue to start or e[x]it to "
                              "quit\n>")
        if start_working == 'c':
            pass
        elif start_working == 'x':
            pomodoro = False
        if counter == 4:
            long_break()
            start_again = input("If you would like to start over, enter "
                                "[c]ontinue to start or e[x]it to quit\n>")
            if start_again == 'c':
                counter = 0
            elif start_again == 'x':
                pomodoro = False
