import numpy as np

a = np.array([0, 1, 2, 3])  # a vector
b = np.array([4, 5, 6, 7])  # another vector
c = np.array([
    [0, 1, 2, 3],  # a matrix
    [4, 5, 6, 7]
])

d = np.zeros((2, 4))
e = np.random.rand(2, 5)

print('a: ')
print(a)
print('b: ')
print(b)
print('c: ')
print(c)
print('d: ')
print(d)
print('e: ')
print(e)

print('-----division-----')

print('a * .1: ')
print(a * .1)
print('c * .2: ')
print(c * .2)
print('a * b: ')
print(a * b)
print('a * b * .2: ')
print(a * b * .2)
print('a * c: ')
print(a * c)
print('a * e: ')
# print(a * e) Exception

print('-----shape-----')

a = np.zeros((1, 4))
b = np.zeros((4, 3))

# скалярное произведение 2 массивов
c = a.dot(b)

print(c.shape)

# транспонирование
h = np.zeros((5, 3)).T
print(h)
