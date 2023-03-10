# Welcome to My Convex Optimization
***

## Task
This project implements optimization algorithm.

## Description
def print_a_function(f, values) -  the function takes an input function f to generate the y-values for the x-values generated from the minimum and maximum values in the input values list. It will then plot the function.

def find_root_bisection(f, min_val, max_val, tol=1e-6, max_iter=100) - this function takes a function f, a minimum value min_val, a maximum value max_val, a tolerance tol, and a maximum number of iterations max_iter as inputs. It finds the root of the function f within the range [min_val, max_val] using the bisection method. 

def find_root_newton_raphson(f, f_deriv, x_0, tol=1e-6, max_iter=1000) - This function takes a function f, its derivative f_deriv, an initial guess x_0, a tolerance tol, and a maximum number of iterations max_iter as inputs. It returns the root of the function f.

def gradient_descent(f, f_prime, start, learning_rate=0.1, eps=1e-6) - At each iteration, the gradient of the objective function at the current point is calculated using f_prime(x). The algorithm then updates the current point by subtracting the gradient multiplied by the learning rate: x_new = x - learning_rate * grad.

def solve_linear_problem(A, b, c) - use of linear programming

## Installation
This project does not need installation.

## Usage
This project implements optimization algorithm.
```
my_convex_optimization.ipynb
```

### The Core Team


<span><i>Made at <a href='https://qwasar.io'>Qwasar SV -- Software Engineering School</a></i></span>
<span><img alt='Qwasar SV -- Software Engineering School's Logo' src='https://storage.googleapis.com/qwasar-public/qwasar-logo_50x50.png' width='20px'></span>
