# Double precision Calculator and Numerical Calculus methods for approximation program

#Description
This program utilizes a few methods for approximating formulas with a given tolerance.
-Converts any given double precision binary string to its full 64 bit form
-Solves this 64 bit string to its floating point number using the struct import
-Both rounds and chops this floating point number to the given digit(s)
-Solves alternating series with a given set number of terms and required tolerance
-Solves a hardcoded equation using both the bisection and newton-raphson method

#Dependencies
-The program uses the struct library to properly bring the binary string to its floating point number form
-This means no third party libraries are required, so the requirements.txt isn’t really needed, but the following line can be used to install the requirements from the requirements.txt if the program is ever changed.

pip install -r requirements.txt

#How to Run the program
-The bash script to run the program is python main.py
-The first input is the desired double precision string you want to solve, this does not need to be the full 64 bits but is required to be at least the full sign, exponent, and any value that contains a 1 in the mantissa. 
-The program will then output the exact number, the rounded 3 DIGIT, the chopped 3 DIGIT, and the error with the rounded 3 digit
-The program then ask for the desired tolerance for Alternating series
-The program will output the required number for terms for the Alternating series
-The program then ask the desired tolerance for the bisection method, along with the a and b values(note the equation asked in the assignment is hardcoded into the program, but this can be changed for any given equation)
-The number of iterations required is then output
-The required tolerance for the Newton Raphson method is then asked, along with your initial guess and max number of iterations(the max number of iterations isn’t asked in the assignment 1, but is required for solving this method properly.)
-The number of Iterations needed for this method(assuming you input enough for it to solve to desired tolerance) is given.

#Contributors
-This program was written by Andrew Chambers
-The program does use a code derived from the code in the posted slides of Dr Khanh Vu

#License
-The program is licensed under the MIT License
