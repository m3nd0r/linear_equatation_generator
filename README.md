# Linear Equation Generator and Solver

## Overview
This project has been created to help my daughter learn and practice math, providing a hands-on tool for exploring linear equations. It offers a Python implementation for generating and solving linear equations, including functionality for creating equations with configurable complexity and solving them using symbolic computation. The project is designed to filter generated equations to identify those with integer or simple rational solutions, making it an ideal educational resource for students, educators, or anyone looking to enhance their understanding of simple mathematics.

## Features
- Linear Equation Generation: Create random linear equations with variable coefficients and numbers, with the ability to exclude specific values from being used as coefficients.
- Solution Filtering: Identify equations that have integer or simple rational solutions, making them "easy" to solve from an educational standpoint.
- Symbolic Solving: Utilize symbolic computation to solve generated equations, providing exact solutions where possible.

## Requirements
- Python 3.11+
- SymPy: Used for symbolic mathematics and solving equations.

## Installation
1. Clone the Repository:
```bash
git clone https://github.com/m3nd0r/linear_equatation_generator.git
cd linear_equatation_generator
```

2. Set Up a Virtual Environment (Optional):
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

3. Install Dependencies:
```bash
pip install -r requirements.txt
```

## Usage
The project is structured into two main classes: LinearEquationGenerator and LinearEquationSolver. Here's a quick guide on using these classes:

### Generating Linear Equations
```python
from linear_equation_generator_solver import LinearEquationGenerator

generator = LinearEquationGenerator(amount=5, range_=(-10, 10), exclude=(0,))
equations = generator.generate_random_linear_equations()
for equation in equations:
    print(equation)
```

### Solving Linear Equations
```python
from linear_equation_generator_solver import LinearEquationSolver

solver = LinearEquationSolver(equations)
solutions = solver.solve_equations()
for equation, solution in solutions.items():
    print(f"{equation} => {solution}")
```

## Contributing
Contributions to the project are welcome! Please feel free to fork the repository, make your changes, and submit a pull request.
