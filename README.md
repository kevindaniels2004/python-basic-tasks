# Basic Python Tasks - Module 2

This repository contains two Python programs created as part of **Module 2: Basic Python Concepts**.

## 🔹 Task 1: Perform Basic Mathematical Operations

**Objective:**  
This program performs basic arithmetic operations between two numbers entered by the user.

### ✔ Functionality:
- Takes two integer inputs from the user.
- Performs:
  - Addition
  - Subtraction
  - Multiplication
  - Division
- Prints the result of each operation.

**Note:**  
Division is performed without error handling, so users should avoid entering 0 as the second number to prevent runtime errors.

---

## 🔹 Task 2: Personalized Greeting

**Objective:**  
This program creates a greeting message using the user’s full name.

### ✔ Functionality:
- Takes the user's first and last name as input.
- Concatenates them into a full name.
- Prints a personalized greeting message using `f-string`.

---

## 💻 How to Run

1. Open the folder containing your Python files.
2. Run the script using any Python interpreter:
   ```bash
   python your_script_name.py


# Python Tasks - Module 3: Control Structures

This repository contains two Python programs created as part of **Module 3: Control Structures in Python**.

---

## 🔹 Task 3: Check if a Number is Even or Odd

**Objective:**  
This program checks whether a given number is even or odd using an `if-else` condition.

### ✔ Functionality:
- Takes an integer input from the user.
- Uses an `if-else` statement to determine if the number is even or odd.
- Prints the result.

### 🧪 Sample Output:
Enter a number: 6

6 is a even number 


Enter a number 7

7 is a odd number 




---

## 🔹 Task 4: Sum of Integers from 1 to 50 Using a Loop

**Objective:**  
This program calculates the sum of integers from 1 to 50 using a `for` loop.

### ✔ Functionality:
- Iterates from 1 to 50 using a `for` loop.
- Adds all numbers in the range.
- Prints the final sum.

### 🧪 Sample Output:

The sum of numbers from 1 to 50 is: 1275






---

## 💻 How to Run

1. Open the folder containing your Python files.
2. Run the scripts using any Python interpreter:

   ```bash
   python task3_oddeven.py
   python task4_forloop.py


📌 Task 5: Calculate Factorial Using a Function
Problem Statement

Write a Python program that:

Defines a function named factorial that takes a number as an argument.

Calculates its factorial using recursion.

Returns the calculated factorial.

Calls the function with a sample number and prints the output.

Code Example
def fact(n):
    if n < 2:
        return 1
    else:
        return n * fact(n-1)
    
n=int(input("enter a  number "))    
result =  fact(n)
print(f"factorial of {n} is ",result)


Expected Output
enter a number 5
factorial of 5 is: 120

📌 Task 2: Using the Math Module for Calculations
Problem Statement

Write a Python program that:

Asks the user for a number as input.

Uses the math module to calculate:

The square root of the number

The natural logarithm (log base e) of the number

The sine of the number (in radians)

Displays the calculated results.

Code Example
import math 
n = int(input("enter a number"))
print("square root :", math.sqrt(n))
print("logarithm:", math.log(n))
print("sine :", math.sin(n))

example
enter a number  25
square root : 5.0
logarithm: 3.2188758248682006
sine : -0.13235175009777303
🚀 How to Run

Save the code in a .py file (e.g., task5.py or task6.py).

Open a terminal and navigate to the file’s directory.

Run the program with:

python task5.py
python task6.py


