import math

length = 12
width = 10
tiles_per_box = 12

tiles_needed = length * width
tiles_with_buffer = math.ceil(tiles_needed * 1.10)
boxes_needed = math.ceil(tiles_with_buffer / tiles_per_box)

print(f"Room size: {length} x {width} = {tiles_needed} sq ft")
print(f"Tiles needed with 10% buffer: {tiles_with_buffer}")
print(f"Boxes to buy (at {tiles_per_box} tiles/box): {boxes_needed}")