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
seeworm = '#00FF33'
haoworm = 'yellow'
kuy = '#FF0033'
turtle.color('black', seeworm )
turtle.begin_fill()
turtle.shape('turtle')
turtle.pensize(5)
turtle.speed(2)


turtle.penup()
turtle.forward(-20)
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
turtle.end_fill()

turtle.forward(45)
turtle.left(90)
turtle.forward(15)
turtle.right(90)
turtle.pendown()
turtle.color('black', haoworm)
turtle.begin_fill()
turtle.circle(15)
turtle.penup()
turtle.end_fill()

turtle.right(90)
turtle.forward(15)
turtle.left(90)
turtle.backward(a)
turtle.left(90)
turtle.forward(60)
turtle.pendown()
turtle.color('black', haoworm)
turtle.begin_fill()
turtle.circle(c)
turtle.end_fill()



turtle.penup()
turtle.right(90)
turtle.backward(30)
turtle.left(90)
turtle.forward(30)
turtle.pendown()
turtle.right(45)
turtle.forward(45)
turtle.color('black', kuy)
turtle.begin_fill()
turtle.circle(-6)
turtle.end_fill()
turtle.backward(45)
turtle.left(90)
turtle.forward(45)
turtle.color('black', kuy)
turtle.begin_fill()
turtle.circle(6)
turtle.end_fill()
turtle.backward(45)
turtle.penup()
turtle.forward(222)





turtle.mainloop()