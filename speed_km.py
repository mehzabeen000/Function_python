#Function to check the speed of drivers ,if the speed is 70km then it is ok .If the speed is beyond 70 km then for every 5km =1 point will be counted .If the point reaches 12 the license is being suspended.

def speed_check(speed):
    speed_km=0
    point=0
    if speed<=70:
        print("Speed is OK")
    for i in range(71,speed+1):
        speed_km+=1
        if speed_km%5==0:
            point+=1
            if point>12:
                print("License suspended")
                break
    print("point =",point)
        
speed_check(80)




