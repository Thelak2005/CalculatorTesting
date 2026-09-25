print("===== SIMPLE CALCULATOR =====")

while True:
    try:
        result = float(input("\nEnter first number: "))

        while True:
            operator = input("Enter operator (+, -, *, /) or = to finish: ")

            if operator == "=":
                print("Final Result:", result)
                break

            if operator not in ["+", "-", "*", "/"]:
                print("Invalid operator. Please use +, -, *, or /.")
                continue

            num = float(input("Enter next number: "))

            if operator == "+":
                result = result + num

            elif operator == "-":
                result = result - num

            elif operator == "*":
                result = result * num

            elif operator == "/":
                if num == 0:
                    print("Error: Cannot divide by zero.")
                    continue
                result = result / num

            print("Current Result:", result)

        choice = input("\nDo you want to calculate again? (yes/no): ")

        if choice.lower() == "no":
            print("Calculator closed.")
            break

    except ValueError:
        print("Invalid input. Please enter a number.")