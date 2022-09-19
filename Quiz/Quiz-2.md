## 09.01.2022 Quiz 002
#Header Comment: Given 2 numbers, A and B, output TRUE if one of them is 20 or if their sum is 20.

#https://docs.google.com/presentation/d/1-OQ_8RiP4aocDOHyJCb4n9fQbw9uuG8ynlidZTXRoUQ/edit#slide=id.g146fa78211f_0_0

------------------------------------------------------------------------
Program:
```.py
numberA = int(input("Please enter a number: "))
numberB = int(input("Please enter a number: "))
#print a message to the user to confirm the inputs are correct
print(f"You entered {numberA} and {numberB}.")

output = False
if numberA == 20 or numberB == 20 or numberA + numberB == 20:
  output = True

print(f"Your answer to the quiz is {output}")
```
------------------------------------------------------------------------
Proof:
### Fig.1
Input: 20,20 | Output: True
<img width="1026" alt="Input: 20,20 | Output: True" src="https://user-images.githubusercontent.com/112055140/191015799-3f4e1cc0-e82a-44a7-a2b1-e7f400009360.png">

### Fig.2
Input: 20,100 | Output: True
<img width="1026" alt="Input: 20,100 | Output: True" src="https://user-images.githubusercontent.com/112055140/191015824-054ec3a3-9d2e-4ea8-8137-287913647a12.png">

### Fig.3
Input: 100,20 | Output: True
<img width="1026" alt="Input: 100,20 | Output: True" src="https://user-images.githubusercontent.com/112055140/191015839-0fbc3a09-b7c9-4c71-b6bb-c721caa1ba07.png">

### Fig.4
Input: 100,100 | Output: False
<img width="1026" alt="Input: 100,100 | Output: False" src="https://user-images.githubusercontent.com/112055140/191015864-34e4aa49-2ff8-4675-836e-df55a2dbadd9.png">

