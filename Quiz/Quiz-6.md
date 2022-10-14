## 09.12.2022 Quiz #06

#Header Comment: Given a string, create a program that produces the sum of the characters in the string.

#[Google Slides Link](Paste Link)


------------------------------------------------------------------------

Program:
```.py
string = input("Enter string: ")
sum = 0

for i in string:
    sum += ord(i.lower()) - 96

print(f'the sum of your ascii = {sum}')
```

------------------------------------------------------------------------

Proof:
### Fig.1
Input: aaaa | Output: 4
<img width="1026" alt="Input: aaaa | Output: 4" src="https://user-images.githubusercontent.com/112055140/195841290-faa30dcd-2646-4321-8f0c-d4a6c9fa05cf.png">


### Fig.2
Input: bbbb | Output: 8
<img width="1027" alt="Input: bbbb | Output: 8" src="https://user-images.githubusercontent.com/112055140/195841299-0d33b9a6-18ed-47a2-a638-ae22678c077f.png">


------------------------------------------------------------------------

### Flowchart:
![ComputerScience-Quiz-6](https://user-images.githubusercontent.com/112055140/195841318-0abc51c4-176c-4352-ab30-9015dcbd3440.jpg)
