## 10.15.2022 Quiz #009

#Header Comment: Create a function that receives as input a string and returns the string ciphered with shift 13.

#[Google Slides Link](Paste Link)


------------------------------------------------------------------------

Program:
```.py
encoded = input("Please enter a sentence to encode:")
for i in range(len(encoded)):
    split = ord(encoded[i])
    if split >109:
        a = split-13
        b = chr(a)
        print(b, end = "")
    else:
        a = split+13
        b = chr(a)
        print(b, end = "")
```

------------------------------------------------------------------------

Proof:
### Fig.1
Input: aaaa | Output: nnnn
<img width="1048" alt="Input: aaaa | Output: nnnn" src="https://user-images.githubusercontent.com/112055140/195890906-6a06f8d4-313f-4310-ad16-8f5d22aba8ba.png">


### Fig.2
Input: nnnn | Output: aaaa
<img width="1046" alt="Input: nnnn | Output: aaaa" src="https://user-images.githubusercontent.com/112055140/195890923-097522ad-5fb4-4f68-8340-45d61a7678c6.png">


------------------------------------------------------------------------

### Flowchart:
![ComputerScience-Quiz-9](https://user-images.githubusercontent.com/112055140/195891180-8b12acb1-4eeb-442b-872d-0818f0d07fb4.jpg)
