import turtle
import time

print("Making Ghadi for you")
screen = turtle.Screen()  # turtle screen
screen.bgcolor("white")  # background of the screen
screen.setup(width=600, height=600)  # geometry of the GUI
screen.title("Ghadi")  # title of the GUI
screen.tracer(0)  # tracer for the GUI

Aadii = turtle.Turtle()  # the turtle
Aadii.hideturtle()  # make the turtle invisible
Aadii.speed(0)  # setting the speed to 0
Aadii.pensize(3)  # setting the pensize to 3


def ghadi_bana(ghantaa, minutee, secondd, kalam):  # function with 4 parameters

    Aadii.up()  # not ready to draw
    Aadii.goto(0, 210)  # positioning the turtle
    Aadii.setheading(180)  # setting the heading to 180
    Aadii.color("BLack")  # setting the color of the pen to red
    Aadii.pendown()  # starting to draw
    Aadii.circle(210)  # a circle with the radius 210

    Aadii.up()  # not ready to draw
    Aadii.goto(0, 0)  # positioning the turtle
    Aadii.setheading(90)  # same as seth(90) in newer version

    for z in range(12):  # loop
        Aadii.fd(190)  # moving forward at 190 units
        Aadii.pendown()  # starting to draw
        Aadii.fd(20)  # forward at 20
        Aadii.penup()  # not ready to draw
        Aadii.goto(0, 0)  # positioning the turtle
        Aadii.rt(30)  # right at an angle of 30 degrees

    hands = [("black", 80, 12), ("black", 150, 60), ("black", 110, 60)]  # the color and the hands set
    time_set = (ghantaa, minutee, secondd)  # setting the time

    for hand in hands:  # loop
        time_part = time_set[hands.index(hand)]  # time part in the hand index in hands of time_Set
        angle = (time_part / hand[2]) * 360  # setting the angle for the clock
        Aadii.penup()  # not ready to draw
        Aadii.goto(0, 0)  # positioning the turtle
        Aadii.color(hand[0])  # setting the color of the hand
        Aadii.setheading(90)  # same as seth(90)
        Aadii.rt(angle)  # right at an angle of "right"
        Aadii.pendown()  # ready to draw
        Aadii.fd(hand[1])  # forward at a unit of 1st index of the hand var


while True:
    ghantaa = int(time.strftime("%I"))  # setting the hour from the time module
    minutee = int(time.strftime("%M"))  # setting the minute from the time module
    secondd = int(time.strftime("%S"))  # setting the second as above

    ghadi_bana(ghantaa, minutee, secondd, Aadii)  # calling the ghanta_bana() function with the given parameters
    screen.update()  # updating the scren
    time.sleep(1)  # making the code sleep for a second with the time module
    Aadii.clear()  # clearing the pen
