#09.01.2022 Quiz 002
#Header Comment: Given 2 numbers, A and B, output TRUE if one of them is 20 or if their sum is 20.
#https://docs.google.com/presentation/d/1-OQ_8RiP4aocDOHyJCb4n9fQbw9uuG8ynlidZTXRoUQ/edit#slide=id.g146fa78211f_0_0

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

![Screen Shot 2022-09-19 at 18 32 28](https://user-images.githubusercontent.com/112055140/190989443-6825319b-8e88-440e-bb03-bd81876b1e2c.png)
