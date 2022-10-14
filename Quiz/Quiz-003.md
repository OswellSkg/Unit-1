## 09-02-2022 Quiz 003

#Header Comment: Create a program that translate the proteins in the DNA chain.

#[Google Slides Link](https://docs.google.com/presentation/d/1Uqg2Nmkv4x-jS_XNBVeVQyHhmbwMmoCo6So38QEoiBY/)

------------------------------------------------------------------------

Program:
```.py
in_protein = input("Input Protein: ")

if in_protein=="A":
    print("T")
elif in_protein=="T":
    print("A")
elif in_protein=="C":
    print("G")
elif in_protein=="G":
    print("C")
else:
    print("Error")
    exit()
```

------------------------------------------------------------------------

Proof:
### Fig.1
Input: A | Output: T
<img width="1025" alt="Input: A | Output: T" src="https://user-images.githubusercontent.com/112055140/191013837-8ef1cb12-856a-47a9-aa26-ee0e002519bd.png">

### Fig.2
Input: T | Output: A
<img width="1025" alt="Input: T | Output: A" src="https://user-images.githubusercontent.com/112055140/191013850-1395341f-6733-499f-93a6-4e0e38990327.png">

### Fig.3
Input: C | Output: G
<img width="1026" alt="Input: C | Output: G" src="https://user-images.githubusercontent.com/112055140/191013860-fe2d058a-71e3-433f-813d-93cfb1078142.png">

### Fig.4
Input: G | Output: C
<img width="1027" alt="Input: G | Output: C" src="https://user-images.githubusercontent.com/112055140/191013868-214512cb-6d93-4184-b1c4-95df2be313c7.png">

------------------------------------------------------------------------

### Flowchart:
![ComputerScience-Quiz-3](https://user-images.githubusercontent.com/112055140/195838963-e25bad20-bec5-40b5-a645-0a39d7ff2247.jpg)

