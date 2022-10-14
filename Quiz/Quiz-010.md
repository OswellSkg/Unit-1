## 09.22.2022 Quiz 010

#Header Comment: Create a function that produces the power of ten of pico(10^-12) to tera(10^15) for a number provided as an input.

#[Google Slides Link](Paste Link)

------------------------------------------------------------------------

Program:
```.py
import math

number = int(input("Enter a number: "))
x = -12


while -12<=x<=15:
    power = math.pow(10, x)
    print(f"{number} * 10^{x} = {number*power}")
    x += 1
```

------------------------------------------------------------------------

Proof:
### Fig.1
Input: 10 | Output: Power of -12 to 0
<img width="1047" alt="Input: 10 | Output: Power of -12 to 0" src="https://user-images.githubusercontent.com/112055140/195893595-69da2ca5-bbe2-4fe9-82e7-564ace3a3921.png">


### Fig.2
Input: 10 | Output: Power of 4 to 15
<img width="1047" alt="Input: 10 | Output: Power of 4 to 15" src="https://user-images.githubusercontent.com/112055140/195893603-8d87d703-3edd-4c20-b4af-ce6a4f7665a5.png">


------------------------------------------------------------------------

### Flowchart:
![ComputerScience-Quiz-10](https://user-images.githubusercontent.com/112055140/195893773-13351b62-c63b-4608-87ff-76a9802a76d4.jpg)
