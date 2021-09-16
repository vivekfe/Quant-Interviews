
What would be the output of the following script:

def f(x):
    x.append('one')
    x = x + ['two']
    x.append('three')
    return x

a = [c for c in 'abc']

b = f(a)

print(a)
print(b)
print(c)
