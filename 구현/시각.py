import time

n = int(input())

s = time.time()
sum = 0

for hour in range(n+1):
    if hour==3 or hour==13:
        sum+=60*60
    else:
        for minute in range(60):
            if '3' in list(str(minute)):
                sum+=60
            else:
                for sec in range(60):
                    if '3' in list(str(sec)):
                        sum += 1

e = time.time()
print(sum)
print(e-s)