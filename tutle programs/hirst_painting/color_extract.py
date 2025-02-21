import colorgram


def color_ext():
    rgb_colors = []
    color = colorgram.extract('image.jpg',50)
    for i in color:
        r = i.rgb.r
        g = i.rgb.g
        b = i.rgb.b
        new_color = (r,g,b)
        rgb_colors.append(new_color)
    return rgb_colors
c = color_ext()
print(c)