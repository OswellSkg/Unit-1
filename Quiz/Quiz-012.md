## 00.00.0000 Quiz #0

#Header Comment: Create a function that receives integer 2<N<10, and returns the multiplication table for the number up to 9.

#[Google Slides Link](Paste Link)


------------------------------------------------------------------------

Program:
```.py
def mulTable(n, multiplications=""):
   for i in range(1, 10):
      multiplications += f"{n} x {i} = {n * i}\n"
   return multiplications

out = mulTable(2)
print(out)
```

------------------------------------------------------------------------

Proof:
### Fig.1
Input: 2 | Output: 2 x 1 = 2, 2 x 2 = 4, 2 x 3 = 6, 2 x 4 = 8, 2 x 5 = 10, 2 x 6 = 12, 2 x 7 = 14, 2 x 8 = 16, 2 x 9 = 18
<img width="1047" alt="Screen Shot 2022-10-15 at 13 57 40" src="https://user-images.githubusercontent.com/112055140/195969519-5787ca9b-f850-45db-9b3d-fe26614e010c.png">

------------------------------------------------------------------------

### Flowchart:
![ComputerScience-Quiz#012](https://user-images.githubusercontent.com/112055140/195969642-5d44f557-bbca-40ef-b205-3ee200fcf73d.jpg)
