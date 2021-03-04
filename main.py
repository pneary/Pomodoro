# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from datetime import datetime
import time
import sys


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


def pomodoro():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")

    str = f'Welcome to Pomodoro! The time is {current_time}. What would you like to get done for the next 25 minutes?'
    task = input(str)

    print(f"Doing Task: {task}")
    #timer(25)
    time_25 = 25*60
    for i in range(time_25):
        print_percent_done(i, time_25)
        time.sleep(1)
    str = 'Great Job! How productive were you?'
    rating = input(str)
    print('Awesome! Enjoy your 5 min break!')
    timer(5)




#T is minutes
def timer(t):
    t = t * 60
    while t:
        mins = t // 60
        secs = t % 60
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")  # overwrite previous line
        time.sleep(1)
        t -= 1

def print_percent_done(index, total, bar_len=50):
    '''
    index is expected to be 0 based index.
    0 <= index < total
    '''
    percent_done = (index+1)/total*100
    percent_done = round(percent_done, 1)

    done = round(percent_done/(100/bar_len))
    togo = bar_len-done

    done_str = '█'*int(done)
    togo_str = '░'*int(togo)

    sys.stdout.write('\r' + f'\t⏳{total}: [{done_str}{togo_str}] {percent_done}% done')

    if round(percent_done) == 100:
        print('\t✅')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pomodoro()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

