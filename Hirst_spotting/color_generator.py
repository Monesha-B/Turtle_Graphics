import colorgram

rgb_colors = []
# Extract 6 colors from an image.
colors = colorgram.extract('image.jpeg', 50)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    tup = (r, g, b)
    rgb_colors.append(tup)

print(rgb_colors)
