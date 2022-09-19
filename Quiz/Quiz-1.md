#08.25.2022 Quiz #1
#Header Comment: Create a program that counds the number of letters of a word except the first and last letters.

#Print the first letter, the number of letters without the first and last letters, and the last letter.

#The counter should count each words individually and not the whole sentence.

**Fig. 1** This is the solution to the black box


**Fig.1** Shows my solution to the quiz001. The procedure to generate the outputs below are:

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


The coded program solution:
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

Proof:
![Screen Shot 2022-09-19 at 20 58 23](https://user-images.githubusercontent.com/112055140/191012238-eb32ecc0-c6aa-489e-b9b5-2d39b4cf9775.png)
![Screen Shot 2022-09-19 at 20 58 38](https://user-images.githubusercontent.com/112055140/191012255-40c4add0-c08f-451a-a3da-b81f90106566.png)
