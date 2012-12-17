# Basic map, filter & reduce

def sqr(n):
  return n * n

map(sqr, range(10))
map(lambda n: n * n, range(10))

def positive(n):
  return n > 0

filter(positive, range(-5, 5))
filter(lambda n: n > 0, range(-5, 5))

reduce(lambda a, b: a + b, range(10))

# Combinators

def splat(fn):
  def splatmap(l):
    return map(fn, l)
  return splatmap

mapsqr = splat(sqr)
mapsqr(range(10))

# Partial application

def add(*ns):
  return reduce(lambda a, b: a + b, ns)

add(1,2,3,4,5)

def partial(fn, *args):
  def newfn(*moar_args):
    return fn(*(args + moar_args))
  return newfn

inc2 = partial(add, 2)
inc2(2)
inc2(1,2,3,4,5)

# Referential opaqueness

counter = 0
def count():
  global counter
  counter = counter + 1
  return counter
