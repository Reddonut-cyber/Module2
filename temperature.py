"""temperature_celsius = float(input("celsius:"))
fahrenheit = ((temperature_celsius * 9) / 5) + 32
kelvin = temperature_celsius + 273
rohmer = temperature_celsius * 0.8
print(temperature_celsius, fahrenheit, kelvin, rohmer, sep="\n") """

import turtle
c = 30
k = 20
f = c * 2
a = f * 5 + 10

turtle.pensize(5)
turtle.speed(5)


turtle.penup()
turtle.forward(20)
turtle.pendown()
turtle.circle(c)
turtle.right(45)
turtle.forward(k)
turtle.backward(k)
turtle.right(90)
turtle.forward(k)
turtle.backward(k)
turtle.left(135)
turtle.penup()

turtle.forward(f)
turtle.pendown()
turtle.circle(c)
turtle.right(45)
turtle.forward(k)
turtle.backward(k)
turtle.right(90)
turtle.forward(k)
turtle.backward(k)
turtle.left(135)
turtle.penup()

turtle.forward(f)
turtle.pendown()
turtle.circle(c)
turtle.right(45)
turtle.forward(k)
turtle.backward(k)
turtle.right(90)
turtle.forward(k)
turtle.backward(k)
turtle.left(135)
turtle.penup()

turtle.forward(f)
turtle.pendown()
turtle.circle(c)
turtle.right(45)
turtle.forward(k)
turtle.backward(k)
turtle.right(90)
turtle.forward(k)
turtle.backward(k)
turtle.left(135)
turtle.penup()

turtle.forward(f)
turtle.pendown()
turtle.circle(c)
turtle.right(45)
turtle.forward(k)
turtle.backward(k)
turtle.right(90)
turtle.forward(k)
turtle.backward(k)
turtle.left(135)
turtle.penup()

turtle.forward(45)
turtle.left(90)
turtle.forward(15)
turtle.right(90)
turtle.pendown()
turtle.circle(15)
turtle.penup()

turtle.right(90)
turtle.forward(15)
turtle.left(90)
turtle.backward(a)
turtle.left(90)
turtle.forward(60)
turtle.pendown()
turtle.circle(c)

turtle.penup()
turtle.right(90)
turtle.backward(30)
turtle.left(90)
turtle.forward(30)
turtle.pendown()
turtle.right(45)
turtle.forward(45)
turtle.circle(-6)
turtle.backward(45)
turtle.left(90)
turtle.forward(45)
turtle.circle(6)
turtle.backward(45)



turtle.mainloop()