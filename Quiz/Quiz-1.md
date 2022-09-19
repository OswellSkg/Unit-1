## 08.25.2022 Quiz #1
#Header Comment: Create a program that counds the number of letters of a word except the first and last letters.

#Print the first letter, the number of letters without the first and last letters, and the last letter.

#The counter should count each words individually and not the whole sentence.

#[https://docs.google.com/presentation/d/1AdYQ_ch5KAz-V7YcOctjIEK-Uyp_hBH6OoateH34Z_s/](https://docs.google.com/presentation/d/1AdYQ_ch5KAz-V7YcOctjIEK-Uyp_hBH6OoateH34Z_s/)


------------------------------------------------------------------------

The procedure to generate the outputs below are:

| input                        | output          |
|------------------------------|-----------------|
| international                | i11l            |
| (cats) + (dogs) = (troubles) | (4) + (4) = (8) |

1. Get Input.
2. Separate the input by words.
3. For each word: 

  a. Calculate the number of the characters.(nc)

  b. If the nc>2, first letter+(nc-2)+last letter. 

  c. If not, then just print the word.

------------------------------------------------------------------------

Program:
```.py
#08.25.2022 Quiz #1
#Header Comment: Create a program that counds the number of letters of a word except the first and last letters.
#Print the first letter, the number of letters without the first and last letters, and the last letter.
#The counter should count each words individually and not the whole sentence.


input = input("Input: ") #User inputs whatever alphabet or letter
words = input.split(' ') #Split the input by spaces
x = 0 #Loop counter
while x < len(words): #len(words) counts how many words there are, and x counts up to how many words. (Counts all the words) #x keeps adding up by 1, so the while loop continues until the x reaches the number of words in the input
   if len(words[x]) > 2: #If the number of letters in the word is greater than 2, then it will print the first letter, the number of letters in the word, and the last letter. If it is smaller than 2, it will just print it out.
       print(words[x][0] + str(len(words[x])-2) + words[x][-1])
       x = x + 1
   else:
       print(words[x])
       x = x + 1
```

------------------------------------------------------------------------

Proof:
### Fig.1
Input: International | Output: I11l
<img width="1026" alt="Input: International | Output: I11l" src="https://user-images.githubusercontent.com/112055140/191014532-cc4156e7-2aee-45fe-a384-8905027e1a4b.png">

### Fig.2
Input: (cats) + (dogs) = (troubles) | Output:(4) + (4) = (8)
<img width="1026" alt="Input: (cats) + (dogs) = (troubles) | Output:(4) + (4) = (8)" src="https://user-images.githubusercontent.com/112055140/191014541-15e0396a-a260-47f8-926e-c730f78b601d.png">

