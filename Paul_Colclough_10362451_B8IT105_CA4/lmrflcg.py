
add = lambda x,y: x+y
print add(1,1)

def fahrenheit(t):
    return ((float(9)/5)*t + 32)
def celsius(t):
    return (float(5)/9*(t - 32))
temp = (36.5, 37, 37.5, 39)

F = map(fahrenheit, temp)
print F
C = map(celsius, F)
print C


a = [1,2,3,4]
b = [17,12,11,10]
c = [-1, -4, 5, 9]
print map(lambda x,y:x+y, a,b)

print map(lambda x,y,z:x+y+z, a,b,c)

fib = [0,1,1,2,3,5,8,13,21,34,55]
print fib
result = filter(lambda x: x % 2, fib)
print result

result = filter(lambda x: x % 2 == 0, fib)
print result

print reduce(lambda x, y: x+y, [47, 11, 42, 13])

f = lambda a,b: a if (a>b) else b
print reduce(f, [47, 11, 42, 13]) 

f = lambda a,b: a if (a<b) else b
print reduce(f, [47, 11, 42, 13]) 

print reduce(lambda x, y: x+y, range(1, 101))

def sum(values):
    return reduce(lambda x, y: x+y, values)

def max(values):
    return reduce(lambda a,b: a if (a>b) else b, values) 

def min(values):
    return reduce(lambda a,b: a if (a<b) else b, values) 

def add(first, second):
    return map(lambda x, y: x+y, first, second)

def is_even(values):
    return filter(lambda x: x%2==0, values)

def greater_than_mean(values):
    mean = sum(values)/len(values)
    return filter(lambda x: x>mean, values)

def to_fahrenheit(values):
    return [ ((float(9)/5)*x + 32) for x in values ]
    
print sum([47, 11, 42, 13])
print max([47, 11, 42, 13])
print min([47, 11, 42, 13])
print add([47, 11, 42, 13], [37, 21, 22, 33])
print is_even([47, 11, 42, 13])
print greater_than_mean([47, 11, 42, 13])

Celsius = [39.2, 36.5, 37.3, 37.8]
Fahrenheit = [ ((float(9)/5)*x + 32) for x in Celsius ]
print Fahrenheit

Fahrenheit = to_fahrenheit(Celsius)
print Fahrenheit

n = 30
print [(x,y,z) for x in range(1,n)
        for y in range(x,n)
                for z in range(y,n)
                        if x**2 + y**2 == z**2]

values = []
for x in range(1,n):
    for y in range(x,n):
        for z in range(y,n):
            if x**2 + y**2 == z**2:
                values.append((x,y,z))
print values

colours = [ "red", "green", "yellow", "blue" ]
things = [ "house", "car", "tree" ]
coloured_things = [ (x,y) for x in colours for y in things ]
print coloured_things

coloured_things = [(x,y) for x in colours for y in things]

coloured_things = []
for x in colours:
    for y in things:
        coloured_things.append((x,y))

def city_generator():
    yield("Konstanz")
    yield("Zurich")
    yield("Schaffhausen")
    yield("Stuttgart")

x = city_generator()
print x.next()
print 'Hello'

print x.next()

print x.next()

print x.next()

def fibonacci(n):
    """Fibonacci numbers generator, first n"""
    a = 0
    b = 1
    counter = 0
    while True:
        if (counter >= n): return
		
        yield a
        c = a
        a = b
        b = c + b
        counter += 1
f = fibonacci(20)
for x in f:
    print x,
print

def pythagorean(n):
	for x in range(1,n):
		for y in range(x,n):
			for z in range(y,n):
				if x**2 + y**2 == z**2:
					yield (x,y,z)

pyt = pythagorean(3000)
for v in pyt:
    print v,