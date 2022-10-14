## 09.16.2022 #Quiz 8

#Header Comment: A hotel has 10 floors and 10 rooms on each floor. Write a program that prints the names of all rooms in the following format:
 1-Room 1F01, 2-Room 1F02...., 100-Room 10F10

#[Google Slides Link](Paste Link)


------------------------------------------------------------------------

Program:
```.py
for f in range(10):
    for r in range(10):
        print(f"{f+1} - Room {f+1}F{r+1:02}")
```

------------------------------------------------------------------------

Proof:
### Fig.1
Input: Enter | Output: Room List
<img width="1040" alt="Input: Enter | Output: Room List" src="https://user-images.githubusercontent.com/112055140/195855764-212aa01d-b176-426d-ba8b-417ed8a917fd.png">

------------------------------------------------------------------------

### Flowchart:
![ComputerScience-Quiz-8](https://user-images.githubusercontent.com/112055140/195855862-485d3ac1-a553-4949-9fbd-3797d8ff9be0.jpg)
