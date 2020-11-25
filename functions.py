def hello(name='Persona'):
    print('Hello '+name)

hello('Xavier')
hello('Arturo')
hello('Esmeralda')
hello()

def add(n1,n2):
    return n1 + n2

print(add(10,32))
print(add(10,320))

agg =lambda x1,y1: x1*y1
print(agg(10,2))
