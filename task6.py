"""
Create a file named task6.py and write the Python code that matches
this pseudo-code:

function check {
  luck = produce random number
  if luck < 0.5 then print "Sorry"
  else print "Congratulations"
}
check()
Hint: you may import the module random to produce the random number,
but don't put it inside the function.

Then check the style with flake8. If it produces any errors,
fix them and run it again until it produces no error.
"""

# Solution
import random


def check():
    luck = random.random()  # Generate a random number between 0 and 1
    if luck < 0.5:
        print("Sorry")
    else:
        print("Congratulations")


check()
