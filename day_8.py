import math
# greeting function
def greeting(name,location,c):
    print(f"hello {name}")
    print(f"how is {location}")
    print(f"yo {c}")
# giving input using split function
def greeting_using_split(a):
    x=a.split(",")[0]
    y=a.split(",")[1]
    z=a.split(",")[2]
    print(f"hello {x}")
    print(f"yo {y}")
    print(f"yo {z}")
# paint calculator function
def paint_calc(height, width, coverage):
    area=height*width
    area_covered=math.ceil(area/coverage)
    print(f"total area= {area}")
    print(f"paint cans required= {area_covered}")
# prime checker function
def prime_checker(number):
    is_prime=True
    for i in range(2,number):
        if number%i==0:
            is_prime=False
    if is_prime:
        print("it is a prime number")
    else:
        print("it is not a prime number")
   
    
