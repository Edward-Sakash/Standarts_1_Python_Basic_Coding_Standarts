"""
Create a file named task5.py and define a function named
greet that will accept two keyword arguments first and last
with default values John and Doe. The function will print
"Hello, {first} {last}!".

If you prefer, you can change or copy the task4.py file.

After the function, call it using keyword arguments with
any two texts of your choice.

Then check the style with flake8. If it produces any errors,
fix them and run it again until it produces no error.
"""

# Solution


def greet(first="John", last="Dou"):
    print(f"Hello, {first} {last}!")


greet(first="Edward", last="Superhero")
greet(first="Elton", last="Presley")
