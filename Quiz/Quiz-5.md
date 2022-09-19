#09-02-2022 Quiz 05.a


```.py
number = input("Input number: ")
counter = 1
sum = 0

while counter < int(number):
    if int(number) % int(counter) == 0:
        sum = sum + 1
        print(counter)
        counter += 1
    else:
        counter += 1

if number == sum:
    print("Perfect number")
else:
    print("Not a perfect number")
```

![Screen Shot 2022-09-19 at 18 37 33](https://user-images.githubusercontent.com/112055140/190990188-041a9850-ca44-4ae5-a91c-99a52db47530.png)
