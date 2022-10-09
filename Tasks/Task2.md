# Task 2: Complete the program for the EV calculator

1. Average time per kWh
2. Total kWh used
3. Total charge time
4. Show all data

------------------------------------------------------------------------

### Program:
```.py
#09-20-2022 Task 2: Complete the program for the EV calculator

from my_library import validate_int_input

colors = ["\033[0;30m", "\033[0;31m", "\033[0;32m", "\033[0;33m", "\033[0;34m", "\033[0;35m", "\033[0;36m", "\033[0;37m",
          "\033[0;38m", "\033[0;39m", "\033[0;40m", "\033[0;41m", "\033[0;42m", "\033[0;43m", "\033[0;44m", "\033[0;45m",
          "\033[0;46m", "\033[0;47m", "\033[0;48m", "\033[0;49m", "\033[0;50m", "\033[0;51m", "\033[0;52m", "\033[0;53m",
          "\033[0;54m", "\033[0;55m", "\033[0;56m", "\033[0;57m", "\033[0;58m", "\033[0;59m", "\033[0;60m", "\033[0;61m",
          "\033[0;62m", "\033[0;63m", "\033[0;64m", "\033[0;65m", "\033[0;66m", "\033[0;67m", "\033[0;68m", "\033[0;69m",
          "\033[0;70m", "\033[0;71m", "\033[0;72m", "\033[0;73m", "\033[0;74m", "\033[0;75m", "\033[0;76m", "\033[0;77m",
          "\033[0;78m", "\033[0;79m", "\033[0;80m", "\033[0;81m", "\033[0;82m", "\033[0;83m", "\033[0;84m", "\033[0;85m",
          "\033[0;86m", "\033[0;87m", "\033[0;88m", "\033[0;89m", "\033[0;90m", "\033[0;91m", "\033[0;92m", "\033[0;93m",
          "\033[0;94m",]
end_code = "\033[00m"

def Main():
    intro_msg = f"{colors[2]} Welcome to EV Calculator {end_code}".center(100, "-")
    options = "Options".center(100)
    menu = """
    1. Average time per kWh
    2. Total kWh used
    3. Total charge time
    4. Show all data
    """

    #[0] The Menu Screen
    print(intro_msg)
    print(options + menu)

    option = validate_int_input("Enter an option[1-4]: ")
    while option > 4 or option < 1:
        option = validate_int_input(f"{option} is incorrect. Enter an option[1-4]: ")

    # this is how to read a file
    with open("20220920_charging-log.csv", "r") as file:
        ev_data = file.readlines()

    #[1]Average time per kWh
    if option == 1:
        total_time = 0
        total_kwh = 0.0
        i = 0

        for line in ev_data:
            if i > 0:
                data = line.split(",")
                charge = data[1]
                charge_cleaned = charge[:5]
                charge_float = float(charge_cleaned)
                total_kwh += charge_float

                temp_time = data[2]
                temp_time = temp_time.split(":")
                temp_time = int(temp_time[0]) * 60 + int(temp_time[1])
                total_time += temp_time

            i += 1

        print(f"{colors[5]}Average time per kWh: {int(total_time / total_kwh)} minutes{end_code}")

    #[2]Total kWh used
    if option == 2:
        total_charge = 0.0
        i = 0

        for line in ev_data:
            if i > 0:
                values = line.split(",")
                charge = values[1]
                charge_cleaned = charge[:5]
                charge_float = float(charge_cleaned)
                total_charge += charge_float
            i += 1
        print(f"{colors[1]}Total kWh used: {total_charge} kWh{end_code}")

    #[3]Total charge time
    if option == 3:
        total_time = 0
        i = 0

        for line in ev_data:
            if i > 0:
                data = line.split(",")
                temp_time = data[2]
                temp_time = temp_time.split(":")
                temp_time = int(temp_time[0]) * 60 + int(temp_time[1])
                total_time += temp_time
            i += 1
        print(f"{colors[3]}Total charge time: {total_time} minutes{end_code}")

    #[4]Show all data
    if option == 4:
        count = 0
        i = 0

        for line in ev_data:
            if i > 0:
                count += 1
                line = line.strip()
                print(f"Log No.{count}: {colors[2]}{line}{end_code}")
            i += 1

Main()
```

### CSV File Reference:
```.csv
date,charge,duration
12.9.22,8.878Kwh,12:32:36
15.9.22,3.533Kwh,5:02:23
17.9.22,6.828Kwh,9:41:46
81.9.22,5.425Kwh,7:43:35
```

### Proof:
[Input: 1 | Output: "Average time per kWh: 85 minutes"]
<img width="1052" alt="Screen Shot 2022-10-10 at 3 33 52" src="https://user-images.githubusercontent.com/112055140/194773679-6f02a248-339c-4813-8822-2d21c414babb.png">


[Input: 2 | Output: "Total kWh used: 24.664 kWh"]
<img width="1054" alt="Screen Shot 2022-10-10 at 3 34 04" src="https://user-images.githubusercontent.com/112055140/194773688-282ddbc5-8dba-419e-a1d6-bf4cfe5f748a.png">


[Input: 3 | Output: "Total charge time: 2098 minutes"]
<img width="1053" alt="Screen Shot 2022-10-10 at 3 34 17" src="https://user-images.githubusercontent.com/112055140/194773692-4afcd61b-137e-4e18-8a64-3a04fc9b88e5.png">


[Input: 4 | Output: All the datas]
<img width="1054" alt="Screen Shot 2022-10-10 at 3 34 27" src="https://user-images.githubusercontent.com/112055140/194773695-b45447d7-7ed3-4ae4-84a9-d6cb4161058a.png">
