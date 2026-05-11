import math

x1, y1 = 1, 2
x2, y2 = 7, 10

distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

print(f"Distance between ({x1}, {y1}) and ({x2}, {y2}) is {format(distance, '.4f')}")