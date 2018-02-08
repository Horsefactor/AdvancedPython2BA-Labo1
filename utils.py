# utils.py
# Math library
# Author: Sébastien Combéfis
# Version: February 8, 2018

def fact(n):
    """Computes the factorial of a natural number.
    
    Pre: -
    Post: Returns the factorial of 'n'.
    Throws: ValueError if n < 0
    """
    try:
        fact = 1
        if n > 0 :
            while n > 0:
                fact = fact*n
                n -= 1
            return fact
        
        if n == 0 :
            return fact

    except :
        pass

    

def roots(a, b, c):
    """Computes the roots of the ax^2 + bx + x = 0 polynomial.
    
    Pre: -
    Post: Returns a tuple with zero, one or two elements corresponding
          to the roots of the ax^2 + bx + c polynomial.
    """
    delta = b**2 - 4*a*c

    if delta > 0 :
        root = (-b + sqrt(delta))/(2*a),(-b - sqrt(delta))/(2*a)
        return root

    if delta == 0 :
        root = (-b/(2*a))

    if delta < 0 :
        return ()
    
def ff(x):
    return (x**2 - 1)

def integrate(function, lower, upper):


    m = (lower+upper)/2
    fa = function(lower)
    fb = function(upper)
    fm = function(m)

    return ((upper - lower)/6)*(fa + 4*fm+fb)


    """Approximates the integral of a fonction between two bounds
    
    Pre: 'function' is a valid Python expression with x as a variable,
         'lower' <= 'upper',
         'function' continuous and integrable between 'lower‘ and 'upper'.
    Post: Returns an approximation of the integral from 'lower' to 'upper'
          of the specified 'function'.
    """


    pass

if __name__ == '__main__':
    print(fact(5))
    print(roots(1, 0, 1))
    print(integrate(ff, 0, 5))
