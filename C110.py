#num = input('Enter the name:')
#print(num)

import time
print(dir(time))
seconds=input('enter the seconds:')
def timer(seconds):
   while seconds>0:
    mins = int(seconds / 60)
    secs = int(seconds % 60)
    timer = f'{mins}:{secs}'
    print(timer)
    time.sleep(1) 
    seconds-=1
timer(int(seconds))  
