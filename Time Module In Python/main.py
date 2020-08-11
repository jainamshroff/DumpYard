import time

loop = 0
initial = time.time()
print(initial)
# this gives us ticks which increase one per second

while(loop < 45):
    time.sleep(2)
    print("This Is Jainam Shroff")
    loop = loop + 1

# We subtracted current ticks with initial ticks thus given ticks used by while loop
print("While Loop Took: ", time.time() - initial)
initial1 = time.time()

for i in range(45):
    print("This Is Jainam Shroff")

# We subtracted current tick by the tick that was before for loop ran thus giving
# Time taken by the for loop.
print("For Loop Took: ", time.time() - initial1)

localtime = time.asctime(time.localtime(time.time()))
print(localtime)