import itertools
import random
from typing import List, Tuple, Dict

from sympy import symbols, Eq, parse_expr, solve, Integer, Rational


class LinearEquationGenerator:
    """
    A class to generate linear equations with variable coefficients and numbers.
    """

    def __init__(
        self,
        amount: int = 10,
        range_: Tuple[int, int] = (-10, 10),
        exclude: Tuple[int, int] = (0, 1),
    ):
        """
        Initializes the LinearEquationGenerator class.

        Args:
            amount (int): The number of linear equations to generate.
            range_ (Tuple[int, int]): The range of coefficients to generate.
            exclude (Tuple[int, int]): The values to exclude from the coefficients.
        """
        self.amount = amount
        self.range_ = range_
        self.exclude = exclude
        self.good_equations = {}

    def generate_number(self) -> int:
        """
        Generates a random coefficient for the linear equation, excluding specified values.

        Returns:
            int: A random coefficient.
        """
        valid_coefficients = [
            i for i in range(self.range_[0], self.range_[1] + 1) if i not in self.exclude
        ]
        return random.choice(valid_coefficients)

    @staticmethod
    def format_number(number: int) -> str:
        """
        Formats the number to be properly displayed within an equation.

        Args:
            number (int): The number to format.

        Returns:
            str: The formatted number, enclosed in parentheses if negative.
        """
        return f"{number}" if number >= 0 else f"({number})"

    @staticmethod
    def generate_random_sign() -> str:
        """
        Generates a random sign for the linear equation.

        Returns:
            str: A random sign.
        """
        return random.choice(["+", "-"])

    def generate_random_equation(self) -> str:
        """
        Generates a random linear equation.

        Returns:
            str: A random linear equation in string format.
        """
        part = (
            lambda: f"{self.generate_number()}*({self.generate_number()}*x {self.generate_random_sign()} {self.format_number(self.generate_number())})"
        )
        return f"{part()} = {part()}"

    def generate_random_linear_equations(self) -> List[str]:
        """
        Generates a list of random linear equations.

        Returns:
            List[str]: A list of random linear equations in string format.
        """
        return [self.generate_random_equation() for _ in range(self.amount)]

    def generate_easy_linear_equations(self) -> Dict[str, List]:
        """
        Generates and filters linear equations to find those with integer solutions.

        Returns:
            Dict[str, List]: A dictionary of easy (integer solution) linear equations.
        """

        while len(self.good_equations) < self.amount:
            # Solve the linear equations and sort them
            solved_equations = LinearEquationSolver(
                self.generate_random_linear_equations()
            ).solve_equations()
            equation_sorter = LinearEquationSorter(solved_equations)
            self.good_equations.update(equation_sorter.sort_equations())
            # Break the loop if the number of good equations exceeds the specified amount
            if len(self.good_equations) > self.amount:
                self.good_equations = dict(
                    itertools.islice(self.good_equations.items(), self.amount)
                )
                break

        return self.good_equations


class LinearEquationSolver:
    """
    A class to solve linear equations.
    """

    def __init__(self, equations: List[str]) -> None:
        self.equations = equations

    @staticmethod
    def solve_equation(equation: str) -> List:
        """
        Solves a single linear equation.

        Args:
            equation (str): The linear equation to solve.

        Returns:
            List: The solution(s) of the linear equation.
        """
        x = symbols("x")
        left, right = equation.split("=")
        equation = Eq(parse_expr(left), parse_expr(right))
        return solve(equation, x)

    def solve_equations(self) -> Dict[str, List]:
        """
        Solves multiple linear equations.

        Returns:
            Dict[str, List]: A dictionary with the equations as keys and their solutions as values.
        """
        return {equation: self.solve_equation(equation) for equation in self.equations}


class LinearEquationSorter:
    """
    A class to filter and sort linear equations based on their solutions.
    """

    def __init__(self, equations: Dict[str, List]):
        self.equations = equations
        self.good = {}

    @staticmethod
    def is_good_equation(solution: List) -> bool:
        """
        Determines if an equation has an integer solution.

        Returns:
            bool: True if the equation has an integer solution, False otherwise.
        """
        try:
            return any(
                [
                    isinstance(solution[0], Integer),
                    isinstance(solution[0], Rational)
                    and len(str(solution[0])) <= 3
                    and solution[0].p < solution[0].q,
                ]
            )
        except IndexError:
            return False

    @staticmethod
    def clean_good_equations(equations: dict) -> Dict[str, List]:
        """
        Cleans the good equations by removing the coefficient of x from the equation.

        Returns:
            Dict[str, List]: A dictionary of cleaned equations.
        """
        return {equation.replace("*", ""): solution for equation, solution in equations.items()}

    def sort_equations(self) -> Dict[str, List]:
        """
        Filters the equations to retain only those with integer solutions.

        Returns:
            Dict[str, List]: A dictionary of equations with integer solutions.
        """
        for equation, solution in self.equations.items():
            if self.is_good_equation(solution):
                self.good[equation] = solution

        return self.clean_good_equations(self.good)
