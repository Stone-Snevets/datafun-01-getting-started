"""
Purpose: Illustrate basic expressions and operators in Python.

Author: Solomon Stevens

This file name is:   basic_expressions.py
This module name is: basic_expressions

Expressions

Data analytics is all about getting value out of data.
Expressions are the building blocks of data analytics.

Rather like math expressions, or Excel expressions, Python expressions
are a combination of values, variables, operators, and function calls.

Expressions are made of operands and operators.

- Operators are symbols like +, -, *, /, and =.
- Operands can be values or variables, 
  and can include function calls like len() and str().

Writing expressions in Python is like writing formulas in Excel.
 
"""

# ----------------- INSTRUCTOR GENERATED CODE -----------------

# Use this handy logger to document your work automatically

# import setup_logger function from instructor-generated module
from util_logger import setup_logger

# setup the logger using the current file name (a built-in variable)
logger, logname = setup_logger(__file__)

# ----------------- END INSTRUCTOR GENERATED CODE -----------------

# Declare  Variables
rectangle_base = 15
rectangle_height = 8
num1 = 34
num2 = 6
float_num1 = 1.2
float_num2 = 2.3
float_num3 = 3.4

# Basic Arithmetic Operations
rectangle_area = rectangle_base * rectangle_height
triangle_area = rectangle_area / 2
total_sum = float_num1 + float_num2 + float_num3
difference = num1 - num2

# Log Information
logger.info(
    f"Given base = {rectangle_base} and height = {rectangle_height}, rectangle_area = {rectangle_area}"
)
logger.info(
    f"Given rectangle_area = {rectangle_area}, triangle_area = {triangle_area}"
)
logger.info(
    f"Given float_num1 = {float_num1}, float_num2 = {float_num2}, and float_num3 = {float_num3}, sum = {total_sum}"
)
logger.info(f"Given num1 = {num1} and num2 = {num2}, the difference = {difference}")
