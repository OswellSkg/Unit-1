## 10.06.2022 Quiz 015

#Header Comment: There are N closed doors in a school and N students present. 
#The first student opens each door. The second student flips(open<>close) every second door.
#The third student flips every third door. The fourth student flips every fourth door. The fifth student flips every fifth door.

#[Google Slides Link](Paste Link)


------------------------------------------------------------------------

Program:
```.py
def open_door(N):
    doors = []
    for x in range(N):
        doors.append(False)

    for d in range(1,N+1):
        for stu in range(1,N+1):
            if d % stu == 0:
                doors[d-1] = not doors[d-1]
    print(doors)

open_door(N = 100)
```

------------------------------------------------------------------------

Proof:
### Fig.1
Input: Enter | Output: [True, False, False, True, False, False, False, False,...True]
<img width="1046" alt="Input: Enter | Output: [True, False, False, True, False, False, False, False,...True]" src="https://user-images.githubusercontent.com/112055140/195969255-f6610fbc-f1dc-4677-b8a2-d8629711306b.png">

------------------------------------------------------------------------

### Flowchart:
![ComputerScience-Quiz#015](https://user-images.githubusercontent.com/112055140/195969305-7a15af67-9536-46ce-aa7b-fd178449713e.jpg)
