class LessonOneProblems:
    PI: float = 3.141692

    def problem_one():
        """
        Create a Hello World
        """
        print("Hello World")

    def problem_two(first_value: int, second_value: int):
        """
        Create a calculator

        Args:
            first_value (int): first value to operate
            second_value (int): second value to operate
        """
        result_sum: int = first_value + second_value
        result_deduction: int = first_value - second_value
        result_multiplication: int = first_value * second_value
        result_division: float = first_value / second_value
        result_remainder: int = first_value % second_value
        print(f"resultados {result_sum}, {result_deduction}, {result_multiplication}, {result_division}, {result_remainder}.")

    def problem_three() -> None:
        """
        Ask for a number (radius) to user and calculate the circle area
        """
        radius = float(input("Write a radius measure..."))
        result_area: float = LessonOneProblems.PI * (radius ** 2)
        print(f"the result area of the circle is {result_area}")

if __name__ == "__main__":
    # LessonOneProblems.problem_one()
    # LessonOneProblems.problem_two(4, 6)

    LessonOneProblems.problem_three()