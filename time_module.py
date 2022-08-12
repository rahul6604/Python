import time

from numpy import double

# calculating time for 'while loop'
initial = time.time()
i=0
while(i<45):
    print(i,end="  ")
    # time.sleep(2)
    i = i+1
print("While Loop ran in ", time.time() -initial)

# calculating time for 'for loop'
initial2 = time.time()
for i in range(45):
    print(i,end="  ")
print("For loop ran in ", time.time() - initial2)

# Note:- time.time() = it tells us the time in seconds that have passed since 1 January 1970.
# time.sleep(2)  delays the execution of further commands for given specific seconds.

localtime = time.asctime(time.localtime())
print(localtime)

# time.localtime() = return (given time + 1 Jan 1970)
# time.time() = return Time from 1 Jan 1970 in sec
# time.asctime() = used to format time

  