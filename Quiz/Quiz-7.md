#09-15-22 Quiz #7
#Header Comment: Create a program that creates 10 random password with digits and letters of length 20.

```.py
import random
end_code = "\033[00m"
green = "\033[0;32m"

length_pass = 20


for i in range(10):
    password = ""  # empty string
    for n in range(length_pass):
        rand_num = random.randint(48, 122) #range that includes lower case digits and upper case
        while 65>rand_num>57 or 97>rand_num>90:
            rand_num = random.randint(48, 122)

        #convert number to letter using ascii table
        rand_letter = chr(rand_num)
        password += rand_letter
    print(f"{green}Your password is: {password}{end_code}")
```

![Screen Shot 2022-09-19 at 18 39 12](https://user-images.githubusercontent.com/112055140/190990446-86d92564-f0f9-4dc5-8ebe-a1ac6486d75a.png)
