## 09.30.2022 Quiz 013

#Header Comment: Create a function that receives one input and produces the output shown.

#[Google Slides Link](Paste Link)

------------------------------------------------------------------------

Program:
```.py
def mystery(A: int, B: int) -> int:
    out = ((A * B) - (abs(A - B)))
    return out

out = mystery(2, 6)
print(out)

out = mystery(4, 10)
print(out)

out = mystery(10, 10)
print(out)

out = mystery(70, 50)
print(out)
```

------------------------------------------------------------------------

Proof:
### Fig.1
Input: Enter | Output: 8,34,100,3480
<img width="1047" alt="Input: Enter | Output: 8,34,100,3480" src="https://user-images.githubusercontent.com/112055140/195968322-efabd72d-8e8e-49d6-8ebb-821a51906c8d.png">


------------------------------------------------------------------------

### Flowchart:
![ComputerScience-Quiz-013](https://user-images.githubusercontent.com/112055140/195968257-2a568a28-d25d-4f55-8116-506553ee8d3f.jpg)
