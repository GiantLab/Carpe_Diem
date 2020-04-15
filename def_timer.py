import datetime,time

x=datetime.datetime.now()
z=x.ctime()
print(z)
var=x.year
while True:
            if var==2040:
                break
            else:
                var+=1
                y=x.replace(year=var)
                z=y.ctime()
                print(z)
                time.sleep(2)
print("You are dead")
    

