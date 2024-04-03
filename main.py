from generator import LinearEquationGenerator


def main():
    generator = LinearEquationGenerator(amount=5, range_=(-10, 10), exclude=(0, 1))
    equations = generator.generate_easy_linear_equations()
    for equation, solutions in equations.items():
        print(f"{equation} => {solutions}")


if __name__ == "__main__":
    main()
