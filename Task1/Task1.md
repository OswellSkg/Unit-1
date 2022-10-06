# Task 1: Programming Task

https://docs.google.com/document/d/1hg1WuwKhudukA3kbMVTUJQFguYmJyJ0VXhLZwf4l_1M/edit

The lockers are to be painted in four colors: red, white, yellow and blue, in order of locker numbers.

Task 1: Create a program and the flow diagram that shows the colors of all the lockers from 1 to 2400.

Task 2: Using the program above, create another program that allows the user to enter a number and the program outputs the color that should be used in the locker.


------------------------------------------------------------------------


## Task 1

### Program:
```.py
for ln in range(1,2401,1):
    if ln % 4 == 1:
        print(f"{ln}: Red")
    elif ln % 4 == 2:
        print(f"{ln}: White")
    elif ln % 4 == 3:
        print(f"{ln}: Yellow")
    elif ln % 4 == 0:
        print(f"{ln}: Blue")
```

### Flowchart:
![Task1_Flowchart](https://user-images.githubusercontent.com/112055140/194348635-65efec5e-3e18-4a5a-926b-c2640733f597.png)

### Proof:
[Input: Command+R | Output: 10th - 13th]
<img width="1048" alt="Input: Command+R | Output: 10th - 13th" src="https://user-images.githubusercontent.com/112055140/194220717-6d01a62f-a249-4797-9fca-cbdda52346b2.png">
[Input: Command+R | Output: 2390th - 2400th]
<img width="1046" alt="Input: Command+R | Output: 2390th - 2400th" src="https://user-images.githubusercontent.com/112055140/194220739-b08908d8-92b1-41bb-81a8-be9dd07d3dc9.png">


## Task 2

### Program:
```.py
def locker_color():
    ln = int(input("Enter the locker number: "))
    if ln % 4 == 1:
        print("Red")
    elif ln % 4 == 2:
        print("White")
    elif ln % 4 == 3:
        print("Yellow")
    elif ln % 4 == 0:
        print("Blue")

locker_color()
```

### Proof:
[Input: 1 | Output: Red]
<img width="1047" alt="Input: 1 | Output: Red" src="https://user-images.githubusercontent.com/112055140/194220874-3c087c3c-4bdc-4811-bd75-029b0251aa0a.png">
[Input: 2400 | Output: Blue]
<img width="1045" alt="Input: 2400 | Output: Blue" src="https://user-images.githubusercontent.com/112055140/194220889-1fe8f5aa-131c-4141-aadb-8570e691852f.png">
