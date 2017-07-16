import math

fib = [0,1,1,2,3,5,8,13,21,34,55]
result = filter(lambda x: x % 2, fib)
print result

fib = [0,1,1,2,3,5,8,13,21,34,55]
result = filter(lambda x: x % 2 == 0, fib)
print result

f = lambda a,b: a if (a>b) else b
reduce(f, [47, 11, 42, 13]) 

reduce(lambda x, y: x+y, range(1, 101))

max = lambda a,b: a if (a>b) else b
print reduce(max, [47, 11, 42, 13])

min = lambda a,b: a if (a<b) else b
print reduce(min, [47, 11, 42, 13])

print "!!!!!!!!!!!!!!!!!!!!!", map(lambda x: x*x, [47, 11, 42, 13])

def square(values):
	return map(lambda x: x*x, values)
	
def square_root(values):
	return map(lambda x: math.sqrt(x), values)
	
print square_root([2209, 121, 1764, 169])

Celsius = [39.2, 36.5, 37.3, 37.8]
Fahrenheit = [ ((float(9)/5)*x + 32) for x in Celsius ]
print Fahrenheit

triplets = []
for x in range(1,30):
	for y in range(x, 30):
		for z in range(y, 30):
			if x**2 + y**2 == z**2:
				triplets.append((x,y,z))
				
print triplets

#choice = input("What number to fib: \n")

def fibonacci(n):
    """Fibonacci numbers generator, first n"""
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n): return
        yield a
        a, b = b, a + b
        counter += 1
f = fibonacci(1)
for x in f:
    print x,
print


def pyth(n):

	for x in range(1,n):
		for y in range(x, n):
			for z in range(y, n):
				if x**2 + y**2 == z**2:
					yield(x,y,z)

choice = input("What number to pyth: \n")

pyth = pyth(choice)

for value in pyth:
	print value