import turtle
jimmy = turtle.Turtle()
print(jimmy)
jimmy.fillcolor("coral")
jimmy.forward(100)
jimmy.shape("turtle")
my_screen = turtle.Screen()
print(my_screen.canvheight)
my_screen.exitonclick()


from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name",["Pikachu","Squirtle","Charmender"])
table.add_column("Type",["Electric","Water","Fire"])
print(table)
table.align = "l"
print(table)