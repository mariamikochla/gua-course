from turtle import*

#we start drawing a house
speed(4)
#we start drawing a square
begin_fill()
color("orange")
width(4)
forward(150)
left(90)
forward(150)
left(90)
forward(150)
left(90)
forward(150)
end_fill()


#we start drawing a door
begin_fill()
left(90)
forward(55)
left(90)
color("brown")
forward(70)
right(90)
forward(40)
right(90)
forward(70)
end_fill()

#we finished drawing a door

#we start drawing a roof

penup()
goto(150 , 150)
pendown()
begin_fill()
color("brown")
left(210)
forward(150)
left(120)
forward(150)
end_fill()

#we finish drawing a roof

#we start drawing a window
penup()
goto(130,130)
pendown()
color("red")
right(60)
forward(30)
left(90)
forward(30)
left(90)
forward(30)
left(90)
forward(30)
left(90)
forward(15)
left(90)
forward(30)



penup()
goto(20,130)
pendown()
left(90)
forward(30)
right(90)
forward(30)
right(90)
forward(30)
right(90)
forward(30)
right(90)
forward(30)
left(180)
forward(15)
left(90)
forward(30)

#we finish drawing a window

#we finish drawing a house














































































exitonclick()














