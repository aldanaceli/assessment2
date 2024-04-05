import subprocess
import setuptools

def run_tests():
    print("Running unit tests...")
    subprocess.run(["python", "-m", "unittest", "discover", "-v"])

def build_package():
    print("Building package...")
    setuptools.setup(
        name='devops_application',
        version='1.0',
        packages=[],  # Add your package name if you have one
        # Add other metadata as necessary
    )

def main():
    print("Welcome to my DevOps application!")
    num = input("Please enter a number: ")
    print("The number entered is " + num + "!")

    # Check for correct input
    if int(num) < 0:
        print("Invalid input")

    if 0 <= int(num) <= 5:
        print("Number is inserted successfully")
    else:
        print("Number is not in the range of 0 to 5")

    # Handle division by zero
    numerator = 10
    denominator = 0
    try:
        result = numerator / denominator
        print(result)
    except ZeroDivisionError:
        print("Cannot divide by zero")

    # Check if input is a string
    input_str = input("Enter a string: ")
    if isinstance(input_str, str):
        print("Valid input")
    else:
        print ("Invalid input")


    run_tests()
    build_package()

if_name == "_main_"
main()

