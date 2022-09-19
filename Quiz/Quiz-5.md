## 09-02-2022 Quiz 05

#Given a number, create a program that produces the output factors.

#[https://docs.google.com/presentation/d/1yhMenGxwHqeOgw2MP8ozuCJq6pF3D38Ajv8KllHAnLQ/](https://docs.google.com/presentation/d/1yhMenGxwHqeOgw2MP8ozuCJq6pF3D38Ajv8KllHAnLQ/)

------------------------------------------------------------------------

Program:
```.py
number = int(input("Input number: "))
counter = 1
sum = 0

while counter < number:
    if number % counter == 0:
        sum = sum + 1
        print(counter)
        counter += 1
    else:
        counter += 1
```

------------------------------------------------------------------------

Proof:
### Fig.1
Input: 999 | Output: 1,3,9,27,37,111,333
<img width="1026" alt="Input: 999 | Output: 1,3,9,27,37,111,333" src="https://user-images.githubusercontent.com/112055140/191017618-0617b2b7-6df8-4827-a240-0eb2bbd5757d.png">
