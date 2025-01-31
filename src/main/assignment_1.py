import struct
#Written by Andrew Chambers

#Pads the number to its full 64 bit double precision form
def pad(binary_number):
    cur_len = len(binary_number)
    binary_number = binary_number + (64 - cur_len) * '0'
    return binary_number

#Takes the 64 bits and transfers it into the actual number
def double_precision_calc(binary_str):
    int_value = int(binary_str, 2)
    float_value = struct.unpack('d', struct.pack('Q', int_value))[0]
    return float_value

#Takes the actual number and finds its 3 digit chopped value, this is done by putting it in decimal form and chopping it at the 3rd digit, then bringing it back to its actual number
def chop_to_three_digits(value):
    counter = 0
    if value < 100:
        while abs(value) < 100:
            value *= 10
            counter += 1
        value = int(value)
        value /= 10 ** counter
        return value
    
    while abs(value) > 1000:
        value /= 10
        counter += 1
    value = int(value)
    value *= 10 ** counter
    
    return value
    

#Takes the actual number and rounds it to 3 digits
def round_to_three_digits(value):
    counter = 0
    while abs(value) > 1:
        value /= 10
        counter += 1
        
    value = round(value,3)
    value *= 10 **counter
   
    return value

#Solves the absolute error and relative error
def compute_errors(exact_value, approx_value):
    absolute_error = abs(exact_value - approx_value)
    relative_error = absolute_error / abs(exact_value)
    return absolute_error, relative_error

#Hardcoded equation for the  Bisection Method
def f(x):
    return x**3 + 4*x**2 - 10
#Hardcoded equation for the newton Raphson Method
def f_prime(x):
    return 3*x**2 + 8*x

#Runs the Bisection method
def Bisection_method(a,b,tol):
    iterations = 0
    while abs(b-a) / 2 > tol:
        c = (a+b) / 2
        if f(c) == 0:
            break
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
        iterations += 1
    return iterations

#Runs the Newton Raphson method
def newton_Raphson(init_guess,tol,max_iterations):
    iterations= 1
    p_prev = init_guess
    while(iterations <= max_iterations):
     
        p_next = p_prev - (f(p_prev) / f_prime(p_prev))
        if abs(p_next - p_prev) < tol:
            return iterations
        p_prev = p_next
        iterations += 1
    print(f"Cannot be done in given iterations")
    return

#With the given alternating series, solves the minimum number of terms needed
def Alternating_series(tol):
    #this only works if the form fits alternating series
    n = 1
    while 1 / n**3 > tol:
        n+= 1
    return n 

# Main process
def main():
    # Get binary number input from the user as a string
    binary_number = input("What is the binary number you want to solve in double precision format?\n ")
    
    # Ensure the binary string is 64 bits long
    binary_number = str(binary_number)
    if len(binary_number) < 64:
        binary_number = pad(binary_number)

    print(f"Padded Binary = {binary_number}\n")
    
    # Convert binary string to double precision float
    exact_value = double_precision_calc(binary_number)
    
    # Three-digit chopping
    chopped_value = chop_to_three_digits(exact_value)
    
    # Three-digit rounding
    rounded_value = round_to_three_digits(exact_value)
    
    # Find error in rounded value
    rounded_absolute_error, rounded_relative_error = compute_errors(exact_value, rounded_value)
    
    # Print the results
    print(f"Exact Value = {exact_value:.5f}\n")
    print(f"Rounded Value = {rounded_value} \n")
    print(f"Chopped Value = {chopped_value}\n")
    print(f"Absolute Error = {rounded_absolute_error:.5f}\n")
    print(f"Relative Error = {rounded_relative_error:.5f}\n")

    #Alternating Series
    tol =float(input(f"What is the tolerence you want for the Alternating series?, give in decimal form\n"))
    Alternating = Alternating_series(tol)
    print(f"Required Number of terms = {Alternating}\n")

    #bisection method
    tol =float(input(f"What is the tolerence you want for the bisection method?, give in decimal form\n"))
    a =float(input("What is the a for the bisection method\n "))
    b =float (input ("What is the b for the bisection method\n "))
    bisection = Bisection_method(a,b,tol)
    print(f"Iterations needed for bisection = {bisection}\n")

    #Newton raphson method
    tol =float(input(f"What is the tolerence you want for the newton_raphson?, give in decimal form.\n"))
    init_guess =  float(input("What is your initial_guess for the newton_raphson method?\n "))
    max_iterations = int(input("What is the max number of iterations for the newton_raphson method?\n "))
    newton = newton_Raphson(init_guess,tol,max_iterations)
    print(f"Iterations needed  for newton raphson = {newton}")

    #Keeps the program open for testing/viewing results
    dont_end = input("")
    
if __name__ == "__main__":
    main()

