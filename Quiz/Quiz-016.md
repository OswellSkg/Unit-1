## 10.07.2022 Quiz 016

#Header Comment: Create a function that produces the output given the input shown.

| Input given:str     | Output:str          |
|---------------------|---------------------|
| "hello world"       | "11121 12131"       |
| "aaaaAABB"          | "12345612"          |
| "abABabAB"          | "11223344"          |
| "Create a Function" | "111112 2 11122111" |

#[Google Slides Link](Paste Link)


------------------------------------------------------------------------

Program:
```.py
def blackboxThree(given:str)->str:
    given = list(given.lower())
    output = ""
    for i in range(len(given)):
        if given[i] == " ":
            output += " "
        else:
            letters = 0
            for j in range(i+1):
                if given[i] == given[j]:
                    letters += 1
            output += str(letters)
    print(output)


for i in ["Hello World","aaaaAABB","abABabAB","Create a Function"]:
    print(i)
    blackboxThree(i)
    print("\n")
```

------------------------------------------------------------------------

Proof:
### Fig.1
Input: ["Hello World","aaaaAABB","abABabAB","Create a Function"] | Output: ["11121 12131,"12345612","11223344","111112 2 11122112"]
<img width="1047" alt="Si" src="https://user-images.githubusercontent.com/112055140/194457242-b105b49b-bb5d-4240-af77-1a386142dabc.png">
