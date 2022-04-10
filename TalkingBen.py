import random
import time
print("Talking Ben on Python 3")
time.sleep(0.8)
print("ring...ring...")
time.sleep(1)
print("Ben...")
text=input()
ben=random.randint(1, 4)
if ben == 1:
	print("yes")
if ben == 2:
	print("no")
if ben == 3:
	print("hohoho")
if ben == 4:
	print("ugh")