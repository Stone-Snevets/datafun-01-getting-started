"""
Purpose: Calculate basic statistics on three numbers.

Author: Solomon Stevens

This scrip uses the built-in function round().

When we install Python, it comes with the Python standard library.
Nearly all scripts will import at least one module from the standard library.

We can install additional, third-party modules using pip.
We'll do that later. 

All scripts in this repository use only the standard library.

@ uses statistics module for descriptive stats

"""
# ----------------- INSTRUCTOR GENERATED CODE -----------------

# Use this handy logger to document your work automatically

# import setup_logger function from instructor-generated module
from util_logger import setup_logger

# setup the logger using the current file name (a built-in variable)
logger, logname = setup_logger(__file__)

# ----------------- END INSTRUCTOR GENERATED CODE -----------------

# Import statistics from Python Standard Library
import statistics

# Get three numbers from user from the user - input result is always a string
# Use \n to add a blank new line to the terminal before we ask for input
num1 = input("\nEnter the first number: ")
num2 = input("\nEnter the second number: ")
num3 = input("\nEnter the third number: ")

# Convert the inputs to a integer values
int_num1 = int(num1)
int_num2 = int(num2)
int_num3 = int(num3)
num_list = [int_num1, int_num2, int_num3]

# Calculate basic statistics on these three numbers
# -> sum
total_sum = int_num1 + int_num2 + int_num3

# -> average
average_value = statistics.mean(num_list)
# --> Round average to 2 decimal places
average_value = round(average_value, 2)

# -> product
total_product = int_num1 * int_num2 * int_num3

# -> min
lowest_value = min(int_num1, int_num2, int_num3)

# -> max
highest_value = max(int_num1, int_num2, int_num3)

# Log the results
logger.info(f"The numbers you selected were {int_num1}, {int_num2}, and {int_num3}.")
logger.info(f"1. The SUM of these numbers is {total_sum}")
logger.info(f"2. The AVERAGE of these numbers is {average_value}")
logger.info(f"3. The PRODUCT of these numbers is {total_product}")
logger.info(f"4. The MINIMUM of these numbers is {lowest_value}")
logger.info(f"5. The MAXIMUM of these numbers is {highest_value}")