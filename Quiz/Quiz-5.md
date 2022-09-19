## 09-02-2022 Quiz 05.a

#Given a number, create a program that produces the output factors.

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

###Fig.1

![Screen Shot 2022-09-19 at 19 11 35](https://user-images.githubusercontent.com/112055140/190995780-a086693b-816e-4ede-8d36-56033fddda86.png)
