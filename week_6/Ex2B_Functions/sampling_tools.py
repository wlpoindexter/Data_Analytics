import random

products = ['Laptop', 'Monitor', 'Keyboard', 'Mouse', 'Webcam',
'Headset', 'Docking Station', 'USB Hub', 'Desk Lamp', 'Surge Protector']

print(random.choice(products))

print(random.sample(products,3))

random.shuffle(products)

print(products)

rint = random.randint(50,300)
print(rint)
