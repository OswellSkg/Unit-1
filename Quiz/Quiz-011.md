## 09.23.2022 #Quiz 011

#Header Comment: Create a function that shows the days of your birthday's month for the year 2022 in a calendar format.

#[Google Slides Link](Paste Link)


------------------------------------------------------------------------

Program:
```.py
def july():
    week =["Fr", "Sa", "Su", "Mo", "Tu", "We", "Th"]
    day = 0
    for i in range(1,32):
        print(week[day],i , end = ",")
        day += 1
        if day % 7 == 0:
            day = 0
        elif day % 7 == 2 or day == 2:
            print("\n")
        else:
            i += 1
july()
```

------------------------------------------------------------------------

Proof:
### Fig.1
Input: Enter | Output: July Calendar
<img width="1046" alt="Input: Enter | Output: July Calendar" src="https://user-images.githubusercontent.com/112055140/195967926-4ea61257-3412-4386-8813-ad8787a1fe97.png">

------------------------------------------------------------------------

### Flowchart:
![ComputerScience-Quiz-11](https://user-images.githubusercontent.com/112055140/195967943-e2c1e328-2b1a-4e79-a2c6-cc11aa15a809.jpg)
