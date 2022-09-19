#08.25.2022 Quiz #1
#Header Comment: Create a program that counds the number of letters of a word except the first and last letters.
#Print the first letter, the number of letters without the first and last letters, and the last letter.
#The counter should count each words individually and not the whole sentence.

![Quiz001-1](https://user-images.githubusercontent.com/112055140/186579273-91972721-a52b-4d5e-9bee-540f544670e8.jpg)


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
