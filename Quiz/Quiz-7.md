## 09-15-22 Quiz #7

#Header Comment: Create a program that creates 10 random password with digits and letters of length 20.

#[Google Slides Link](https://docs.google.com/presentation/d/1lhqm8ulFAlmLRXsSdNC7klPUah0-i_gXCnA24iQ_YqY/)

------------------------------------------------------------------------

Program:
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


------------------------------------------------------------------------

Proof:
### Fig.1
Input: Command+R | Output: 10 random passwords of 20 letters
<img width="1027" alt="Input: Command+R | Output: 10 random passwords of 20 letters" src="https://user-images.githubusercontent.com/112055140/191018343-4efb3917-742f-4aec-a93d-19f24b18a37f.png">

### Fig.2
Input: Command+R | Output: 10 random passwords of 20 lettersv(Different from Fig.1 as the program generated new random passwords
<img width="1025" alt="Input: Command+R | Output: 10 random passwords of 20 lettersv(Different from Fig.1 as the program generated new random passwords)" src="https://user-images.githubusercontent.com/112055140/191018653-e38c29a1-9389-41b3-a4b3-008636010ad9.png">
