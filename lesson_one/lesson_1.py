############################
# Programming lessons. Nº 1
# Author: xxxxx xxxx xxxx
# Reviewed by: Daniel Saiz Azor
# Date: 16/11/24
# Language: Python
# License: MIT License
############################

class LessonOne:
    # Python has not typed variables

    # Exadecimal
    # 0x01 = 1
    # 0x09 = 9
    # 0x0a = 10
    # 0x0f = 15
    # 0x10 = 16
    # 0xf14e5a10f14e5a10 -> 14


    x: int  # Define
    x = 0   # Initialize


    # General variables
    # Should represent something that let you remember what the variable represents
    x = 0                           # Define any variable
    y: int = 0                      # Let you define any naturl number variables
    z: float = 0.055                # Let you define floating point variables
    your_name: str = "Carlota"      # Let you define character's names
    do_you_have_a_dog: bool = False  # Let define you boolean variables (True or False)

    # 2º level variables
    ## Lists
    your_friends: list[str] = ["David", "Marta", "Sergio"]
    years_you_have_already_passed_longer: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]  # ...
    years_you_have_already_passed_shorter: list[int] = list(range(1, 29, 1))  # The same as above but shorter

    wrong_list = [1, "dfs", 0.00]  # Esto es una mierda


    ## Tuples 
    tupla: tuple = (your_name, your_friends, do_you_have_a_dog)  # Nobody use this


    ## Dicts
    numbers_that_make_me_feel_in_the_same_way: dict[int, int] = {
        1: 17,
        2: 80,
        3: 7
    }

    multiple_numbers_that_make_me_feel_in_the_same_way: dict[int, list[int]] = {
        1: [17, 77, 11, 31],
        2: [80, 60, 90],
        3: [7, 5, 55]
    }


    # Uses of complex variables
    ## Lists and tuples
    years_you_have_already_passed_longer[0] == 1    # True
    years_you_have_already_passed_longer[-1] == 15  # True
    years_you_have_already_passed_longer[-2] == 14  # True
    years_you_have_already_passed_longer[len(years_you_have_already_passed_longer) - 1] == 15  # True

    ## Dicts
    numbers_that_make_me_feel_in_the_same_way[1] = 90      # Overwrite
    numbers_that_make_me_feel_in_the_same_way.get(2) == 80 # True. Its a comparison
    # numbers_that_make_me_feel_in_the_same_way.get(1) = 17  # You cannot do this. .get() only returns the value, does not let you modify it
    multiple_numbers_that_make_me_feel_in_the_same_way.get(1)[0] == 17  # True

    # Ways to show info to the user
    print("ola k ase")
    print(f"Mi name is {your_name}")
    print("My friends are {}".format(your_friends))

    # Operator
    result_sum: int = 5 + 6             # 11
    result_deduction: int = 9 - 7       # 2
    result_multiplication: int = 5 * 7  # 35
    result_division: float = 9 / 5      # 1.8
    result_division: int = int(9 / 5)   # 1
    result_remainder: int = 9 % 5       # 4
    result_exponential: int = 2 ** 3    # 8