## 09-02-2022 Quiz 03

#Header Comment: Create a program that translate the proteins in the DNA chain.

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
<img width="1025" alt="Input: A | Output: T" src="https://user-images.githubusercontent.com/112055140/191013837-8ef1cb12-856a-47a9-aa26-ee0e002519bd.png">
<img width="1025" alt="Input: T | Output: A" src="https://user-images.githubusercontent.com/112055140/191013850-1395341f-6733-499f-93a6-4e0e38990327.png">
<img width="1026" alt="Input: C | Output: G" src="https://user-images.githubusercontent.com/112055140/191013860-fe2d058a-71e3-433f-813d-93cfb1078142.png">
<img width="1027" alt="Input: G | Output: C" src="https://user-images.githubusercontent.com/112055140/191013868-214512cb-6d93-4184-b1c4-95df2be313c7.png">
