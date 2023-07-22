import threading
import time

# Explanation:
# This code demonstrates the use of threads in Python. It defines two functions 'fuc' and 'fuct',
# and creates two threads 'x' and 'y' to execute these functions concurrently. The 'fuc' function
# prints 'run', sleeps for 0.83 seconds, and then prints 'done'. The 'fuct' function prints
# 'review passed'. Both threads 'x' and 'y' start concurrently, and their output may be
# interleaved depending on the scheduler.

def fuc():
    print('run')
    time.sleep(0.83)
    print('done')

def fuct():
    print('review passed')

x = threading.Thread(target=fuc)
y = threading.Thread(target=fuct)

x.start()
y.start()

# The 'threading.active_count()' function returns the number of active threads in the program.
# Here, we print the count of active threads, which will be at least 2 (for threads 'x' and 'y').
print(threading.active_count())

ls = []

# The 'count1' function appends numbers from 1 to 'n' to the list 'ls', with a sleep of 0.5 seconds
# between each append.
def count1(n):
    for i in range(1, n+1):
        ls.append(i)
        time.sleep(0.5)

# The 'count2' function appends numbers from 1 to 'n' to the same list 'ls', with a sleep of 0.5 seconds
# between each append.
def count2(n):
    for i in range(1, n+1):
        ls.append(i)
        time.sleep(0.5)

# Create two threads 'first' and 'second' to execute the 'count1' and 'count2' functions respectively.
first = threading.Thread(target=count1, args=(5,))
first.start()

second = threading.Thread(target=count2, args=(5,))
second.start()

# Wait for both threads 'first' and 'second' to complete before printing the 'ls' list.
first.join()
second.join()

# Print the 'ls' list, which will contain numbers from 1 to 10 appended by both threads.
print(ls)
