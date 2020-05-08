speed = float(input('What is the speed of the vehicle in MPH: ')) #40MPH
while speed < 0:
    print('Must enter a positive speed!')#input validation
    speed = float(input('What is the speed of the vehicle in MPH: ')) #40MPH
travel = int(input('How many hours has the vehicle traveled?: ')) #3hours
while travel < 1:
    print('Must enter travel time greater then 0!')#input validation
    travel = int(input('How many hours has the vehicle traveled?: ')) #3hours

print("Hour", "\tDistance Traveled")
print()


for currenthour in range(1, travel + 1): #trying to find current hour 1, current hour 2 etc
        #x      in range(1, however many TRAVEL hours you input + 1)
                       #(start 1, stop at travel hours, increment by 1)
    distance = speed * currenthour
#distance=  40   * current hour 1, current hour 2, current hour 3, 40*1=40, 40*2=80, 40*3=120, 40*4=160
    print(currenthour, "\t", distance)



