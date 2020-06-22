import turtle
import random
import time


def turtle1():

    text = turtle.Turtle()
    text.penup()

    for i in range(8):
        for i in range(9):
            colors = ["red", "white", "blue", "red", "white", "blue", "red", "white", "blue"]
            screen = turtle.Screen()
            screen.bgcolor("black")
            text.color(colors[i])
            text.shape("blank")
            screen.delay(75)
            text.write("." * i, align="center", font=("Arial", 100))
            i += 1
        screen.reset()

    text = turtle.Turtle()
    text.penup()
    screen = turtle.Screen()
    screen.bgcolor("black")
    text.shape("blank")
    text.color("white")
    text.setpos(0, -100)
    text.write("?", align="center", font=("Arial", 200))

    screen.exitonclick()


def turtle2():

    screen = turtle.Screen()
    screen.bgcolor("green")
    time.sleep(0)

    fence = turtle.Turtle()
    fence.penup()
    fence.pensize(5)
    fence.shape("blank")
    fence.pencolor("white")
    fence.setpos(-50, -200)
    fence.left(180)
    fence.pendown()
    fence.forward(200)
    fence.right(90)
    fence.forward(400)
    fence.right(90)
    fence.forward(500)
    fence.right(90)
    fence.forward(400)
    fence.right(90)
    fence.forward(200)
    fence.penup()

    bush = turtle.Turtle()
    bush.shape("circle")
    bush.color("black")

    xpos = -220
    ypos = -180
    for i in range(1, 10, 2):
        xpos += i * 10
        ypos += i * 10
        for j in range(5):
            bush.penup()
            bush.setpos(xpos, ypos)
            bush.pendown()
            bush.stamp()
            bush.setpos(xpos - 10, ypos)
            bush.stamp()
            bush.setpos(xpos , ypos + 12)
            bush.stamp()
            ypos += 65
        xpos = -220
        ypos = -180

    xpos = -95
    ypos = -180
    for i in range(1, 10, 2):
        xpos += i * 10
        ypos += i * 10
        for j in range(5):
            bush.penup()
            bush.setpos(xpos, ypos)
            bush.pendown()
            bush.stamp()
            bush.setpos(xpos - 10, ypos)
            bush.stamp()
            bush.setpos(xpos , ypos + 12)
            bush.stamp()
            ypos += 65
        xpos = -95
        ypos = -180

    xpos = 55
    ypos = -180
    for i in range(1, 10, 2):
        xpos += i * 10
        ypos += i * 10
        for j in range(5):
            bush.penup()
            bush.setpos(xpos, ypos)
            bush.pendown()
            bush.stamp()
            bush.setpos(xpos - 10, ypos)
            bush.stamp()
            bush.setpos(xpos , ypos + 12)
            bush.stamp()
            ypos += 65
        xpos = 55
        ypos = -180

    bush = turtle.Turtle()
    bush.shape("circle")
    bush.color("darkgreen")

    xpos = -200
    ypos = -180
    for i in range(1, 10, 2):
        xpos += i * 10
        ypos += i * 10
        for j in range(5):
            bush.penup()
            bush.setpos(xpos, ypos)
            bush.pendown()
            bush.stamp()
            bush.setpos(xpos - 10, ypos)
            bush.stamp()
            bush.setpos(xpos , ypos + 12)
            bush.stamp()
            ypos += 65
        xpos = -200
        ypos = -180

    xpos = -75
    ypos = -180
    for i in range(1, 10, 2):
        xpos += i * 10
        ypos += i * 10
        for j in range(5):
            bush.penup()
            bush.setpos(xpos, ypos)
            bush.pendown()
            bush.stamp()
            bush.setpos(xpos - 10, ypos)
            bush.stamp()
            bush.setpos(xpos , ypos + 12)
            bush.stamp()
            ypos += 65
        xpos = -75
        ypos = -180

    xpos = 75
    ypos = -180
    for i in range(1, 10, 2):
        xpos += i * 10
        ypos += i * 10
        for j in range(5):
            bush.penup()
            bush.setpos(xpos, ypos)
            bush.pendown()
            bush.stamp()
            bush.setpos(xpos - 10, ypos)
            bush.stamp()
            bush.setpos(xpos , ypos + 12)
            bush.stamp()
            ypos += 65
        xpos = 75
        ypos = -180

    text = turtle.Turtle()
    text.speed(5)
    text.penup()
    text.shape("blank")
    text.color("white")
    text.setpos(0, 0)
    time.sleep(1)

    bush = turtle.Turtle()
    bush.shape("circle")
    bush.color("limegreen")

    xpos = -180
    ypos = -180
    for i in range(1, 10, 2):
        xpos += i * 10
        ypos += i * 10
        for j in range(5):
            bush.penup()
            bush.setpos(xpos, ypos)
            bush.pendown()
            bush.stamp()
            bush.setpos(xpos - 10, ypos)
            bush.stamp()
            bush.setpos(xpos , ypos + 12)
            bush.stamp()
            ypos += 65
        xpos = -180
        ypos = -180

    xpos = -55
    ypos = -180
    for i in range(1, 10, 2):
        xpos += i * 10
        ypos += i * 10
        for j in range(5):
            bush.penup()
            bush.setpos(xpos, ypos)
            bush.pendown()
            bush.stamp()
            bush.setpos(xpos - 10, ypos)
            bush.stamp()
            bush.setpos(xpos , ypos + 12)
            bush.stamp()
            ypos += 65
        xpos = -55
        ypos = -180

    xpos = 95
    ypos = -180
    for i in range(1, 10, 2):
        xpos += i * 10
        ypos += i * 10
        for j in range(5):
            bush.penup()
            bush.setpos(xpos, ypos)
            bush.pendown()
            bush.stamp()
            bush.setpos(xpos - 10, ypos)
            bush.stamp()
            bush.setpos(xpos , ypos + 12)
            bush.stamp()
            ypos += 65
        xpos = 95
        ypos = -180

    bush = turtle.Turtle()
    bush.shape("circle")
    bush.color("white")

    xpos = -160
    ypos = -180
    for i in range(1, 10, 2):
        xpos += i * 10
        ypos += i * 10
        for j in range(5):
            bush.penup()
            bush.setpos(xpos, ypos)
            bush.pendown()
            bush.stamp()
            bush.setpos(xpos - 10, ypos)
            bush.stamp()
            bush.setpos(xpos , ypos + 12)
            bush.stamp()
            ypos += 65
        xpos = -160
        ypos = -180

    xpos = -35
    ypos = -180
    for i in range(1, 10, 2):
        xpos += i * 10
        ypos += i * 10
        for j in range(5):
            bush.penup()
            bush.setpos(xpos, ypos)
            bush.pendown()
            bush.stamp()
            bush.setpos(xpos - 10, ypos)
            bush.stamp()
            bush.setpos(xpos , ypos + 12)
            bush.stamp()
            ypos += 65
        xpos = -35
        ypos = -180

    xpos = 115
    ypos = -180
    for i in range(1, 10, 2):
        xpos += i * 10
        ypos += i * 10
        for j in range(5):
            bush.penup()
            bush.setpos(xpos, ypos)
            bush.pendown()
            bush.stamp()
            bush.setpos(xpos - 10, ypos)
            bush.stamp()
            bush.setpos(xpos , ypos + 12)
            bush.stamp()
            ypos += 65
        xpos = 115
        ypos = -180



    screen.exitonclick()


def turtle3():
    colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
    screen = turtle.Screen()
    screen.bgcolor("black")
    time.sleep(4.0)

    circles = turtle.Turtle()
    circles.shape("circle")
    circles.penup()

    for h in range(6):
        xpos = -700
        ypos = -200
        if h >= 1:
            xpos = xpos + (h*160)
        else:
            continue
        for i in range(6):
            for color in colors:
                circles.color(color)
                circles.setpos(xpos, ypos)
                circles.pendown()
                circles.left(90)
                for j in range(1):
                    for color in colors:
                        circles.color(color)
                        circles.forward(13)
                        circles.left(13)
                circles.penup()
                xpos += 0
                ypos += 10
        circles.shape("blank")
        circles.right(45)

    screen.exitonclick()



def turtle4():

    for i in range(10):
        screen = turtle.getscreen()
        screen.bgcolor("black")
        screen.delay(75)
        red = turtle.Turtle()
        red.pen(10)
        red.color("red")
        red.shape("circle")
        green = turtle.Turtle()
        green.color("limegreen")
        green.pen(10)
        green.shape("circle")
        blue = turtle.Turtle()
        blue.color("blue")
        blue.pen(10)
        blue.shape("circle")
        orange = turtle.Turtle()
        orange.color("orangered")
        orange.pen(10)
        orange.shape("circle")
        red.penup()
        red.setpos(-250,200)
        red.stamp()
        green.penup()
        green.setpos(-100,200)
        green.stamp()
        blue.penup()
        blue.setpos(50, 200)
        blue.stamp()
        orange.penup()
        orange.setpos(200, 200)
        orange.stamp()
        red.penup()
        red.setpos(-250,100)
        red.stamp()
        green.penup()
        green.setpos(-100,100)
        green.stamp()
        blue.penup()
        blue.setpos(50, 100)
        blue.stamp()
        orange.penup()
        orange.setpos(200, 100)
        orange.stamp()
        red.penup()
        red.setpos(-250,0)
        red.stamp()
        green.penup()
        green.setpos(-100,0)
        green.stamp()
        blue.penup()
        blue.setpos(50, 0)
        blue.stamp()
        orange.penup()
        orange.setpos(200, 0)
        orange.stamp()
        red.penup()
        red.setpos(-250,-100)
        red.stamp()
        green.penup()
        green.setpos(-100,-100)
        green.stamp()
        blue.penup()
        blue.setpos(50, -100)
        blue.stamp()
        orange.penup()
        orange.setpos(200, -100)
        orange.stamp()
        red.penup()
        red.setpos(-250, -200)
        red.stamp()
        green.penup()
        green.setpos(-100, -200)
        green.stamp()
        blue.penup()
        blue.setpos(50, -200)
        blue.stamp()
        orange.penup()
        orange.setpos(200, -200)
        orange.stamp()
        screen.reset()


    screen.exitonclick()


def race():
    screen = turtle.Screen()
    screen.bgcolor("black")
    time.sleep(4.0)
    lines1 = turtle.Turtle()
    lines1.penup()
    lines1.shape("blank")
    lines1.color("white")
    lines1.setpos(20, -20)
    lines1.speed(10)
    lines2 = turtle.Turtle()
    lines2.penup()
    lines2.shape("blank")
    lines2.color("white")
    lines2.setpos(20, -70)
    lines2.speed(10)
    lines3 = turtle.Turtle()
    lines3.penup()
    lines3.shape("blank")
    lines3.color("white")
    lines3.setpos(20, -125)
    lines3.speed(10)
    lines4 = turtle.Turtle()
    lines4.penup()
    lines4.shape("blank")
    lines4.color("white")
    lines4.setpos(20, -180)
    lines4.speed(10)
    lines5 = turtle.Turtle()
    lines5.penup()
    lines5.shape("blank")
    lines5.color("white")
    lines5.setpos(20, -230)
    lines5.speed(10)
    for run in range(130):

        if run < 20:
            lines1.pendown()
            lines1_distance = 4
            lines1.forward(lines1_distance)
            lines1.stamp()
            lines1.penup()
            lines1.forward(lines1_distance / 2)
            lines2.pendown()
            lines2_distance = 4
            lines2.forward(lines2_distance)
            lines2.stamp()
            lines2.penup()
            lines2.forward(lines2_distance / 2)
            lines3.pendown()
            lines3_distance = 4
            lines3.forward(lines3_distance)
            lines3.stamp()
            lines3.penup()
            lines3.forward(lines3_distance / 2)
            lines4.pendown()
            lines4_distance = 4
            lines4.forward(lines4_distance)
            lines4.stamp()
            lines4.penup()
            lines4.forward(lines4_distance / 2)
            lines5.pendown()
            lines5_distance = 4
            lines5.forward(lines5_distance)
            lines5.stamp()
            lines5.penup()
            lines5.forward(lines5_distance / 2)

        elif run >= 20 and run < 38:
            lines1.pendown()
            lines1_distance = 10
            lines1.left(lines1_distance)
            lines1.forward(1)
            lines1.stamp()
            lines1.penup()
            lines1.forward(lines1_distance / 2)
            lines2.pendown()
            lines2_distance = 10
            lines2.left(lines2_distance)
            lines2.forward(1)
            lines2.forward(lines2_distance)
            lines2.stamp()
            lines2.penup()
            lines2.forward(lines2_distance / 2)
            lines3.pendown()
            lines3_distance = 10
            lines3.left(lines3_distance)
            lines3.forward(10)
            lines3.forward(lines3_distance)
            lines3.stamp()
            lines3.penup()
            lines3.forward(lines3_distance / 2)
            lines4.pendown()
            lines4_distance = 10
            lines4.left(lines4_distance)
            lines4.forward(20)
            lines4.forward(lines4_distance)
            lines4.stamp()
            lines4.penup()
            lines4.forward(lines4_distance / 2)
            lines5.pendown()
            lines5_distance = 10
            lines5.left(lines5_distance)
            lines5.forward(30)
            lines5.forward(lines5_distance)
            lines5.stamp()
            lines5.penup()
            lines5.forward(lines5_distance / 2)

        elif run >= 40 and run < 85:
            lines1.pendown()
            lines1_distance = 4
            lines1.forward(lines1_distance)
            lines1.stamp()
            lines1.penup()
            lines1.forward(lines1_distance / 2)
            lines2.pendown()
            lines2_distance = 4
            lines2.forward(lines2_distance)
            lines2.stamp()
            lines2.penup()
            lines2.forward(lines2_distance / 2)
            lines3.pendown()
            lines3_distance = 4
            lines3.forward(lines3_distance)
            lines3.stamp()
            lines3.penup()
            lines3.forward(lines3_distance / 2)
            lines4.pendown()
            lines4_distance = 4
            lines4.forward(lines4_distance)
            lines4.stamp()
            lines4.penup()
            lines4.forward(lines4_distance / 2)
            lines5.pendown()
            lines5_distance = 4
            lines5.forward(lines5_distance)
            lines5.stamp()
            lines5.penup()
            lines5.forward(lines5_distance / 2)

        elif run >= 85 and run < 103:
            lines1.pendown()
            lines1_distance = 10
            lines1.left(lines1_distance)
            lines1.forward(1)
            lines1.stamp()
            lines1.penup()
            lines1.forward(lines1_distance / 2)
            lines2.pendown()
            lines2_distance = 10
            lines2.left(lines2_distance)
            lines2.forward(1)
            lines2.forward(lines2_distance)
            lines2.stamp()
            lines2.penup()
            lines2.forward(lines2_distance / 2)
            lines3.pendown()
            lines3_distance = 10
            lines3.left(lines3_distance)
            lines3.forward(10)
            lines3.forward(lines3_distance)
            lines3.stamp()
            lines3.penup()
            lines3.forward(lines3_distance / 2)
            lines4.pendown()
            lines4_distance = 10
            lines4.left(lines4_distance)
            lines4.forward(20)
            lines4.forward(lines4_distance)
            lines4.stamp()
            lines4.penup()
            lines4.forward(lines4_distance / 2)
            lines5.pendown()
            lines5_distance = 10
            lines5.left(lines5_distance)
            lines5.forward(30)
            lines5.forward(lines5_distance)
            lines5.stamp()
            lines5.penup()
            lines5.forward(lines5_distance / 2)

        elif run >= 103 and run <= 130:
            lines1.pendown()
            lines1_distance = 4
            lines1.forward(lines1_distance)
            lines1.stamp()
            lines1.penup()
            lines1.forward(lines1_distance / 2)
            lines2.pendown()
            lines2_distance = 4
            lines2.forward(lines2_distance)
            lines2.stamp()
            lines2.penup()
            lines2.forward(lines2_distance / 2)
            lines3.pendown()
            lines3_distance = 4
            lines3.forward(lines3_distance)
            lines3.stamp()
            lines3.penup()
            lines3.forward(lines3_distance / 2)
            lines4.pendown()
            lines4_distance = 4
            lines4.forward(lines4_distance)
            lines4.stamp()
            lines4.penup()
            lines4.forward(lines4_distance / 2)
            lines5.pendown()
            lines5_distance = 4
            lines5.forward(lines5_distance)
            lines5.stamp()
            lines5.penup()
            lines5.forward(lines5_distance / 2)

    yellow = turtle.Turtle()
    yellow.shape("circle")
    yellow.pensize(5)
    yellow.color("yellow")
    yellow.pencolor("white")
    blue = turtle.Turtle()
    blue.penup()
    blue.shape("circle")
    blue.pensize(6)
    blue.color("blue")
    red = turtle.Turtle()
    red.penup()
    red.shape("circle")
    red.pensize(6)
    red.color("red")
    green = turtle.Turtle()
    green.penup()
    green.shape("circle")
    green.pensize(6)
    green.color("green")
    orange = turtle.Turtle()
    orange.penup()
    orange.shape("circle")
    orange.pensize(6)
    orange.color("orange")
    red_range = 0
    green_range = 0
    orange_range = 0
    blue_range = 0
    blue.setpos(-10, -50)
    blue.pendown()
    red.setpos(-10, -100)
    red.pendown()
    orange.setpos(-10, -200)
    orange.pendown()
    green.setpos(-10, -150)
    green.pendown()
    yellow.penup()
    yellow.left(90)
    yellow.setpos(20, -230)
    yellow.pendown()
    yellow.stamp()
    yellow.forward(210)

    start = turtle.Turtle()
    start.penup()
    start.shape("blank")
    start.color("white")
    start.setpos(0, 0)
    start.write("Ready", align="center", font=("Arial", 30))
    time.sleep(1)
    start.clear()
    start.write("Set", align="center", font=("Arial", 30))
    time.sleep(1)
    start.clear()
    start.write("Go!!!", align="center", font=("Arial", 30))
    time.sleep(.5)
    start.clear()

    for run in range(500):

        if red_range < 150:
            red_distance = 4
            red.forward(red_distance)
            red_range += red_distance
            green_distance = 4
            green.forward(green_distance)
            green_range += green_distance
            orange_distance = 4
            orange.forward(orange_distance)
            orange_range += orange_distance
            blue_distance = 4
            blue.forward(blue_distance)
            blue_range += blue_distance


        elif red_range >= 150 and red_range < 300:
            for turn in range(18):
                red_distance = 10
                red.left(red_distance)
                red.forward(red_distance)
                red.forward(10)
                red_range += red_distance
                green_distance = 10
                green.left(green_distance)
                green.forward(green_distance)
                green.forward(19)
                green_range += green_distance
                orange_distance = 10
                orange.left(orange_distance)
                orange.forward(orange_distance)
                orange.forward(29)
                orange_range += orange_distance
                blue_distance = 10
                blue.left(blue_distance)
                blue.forward(blue_distance)
                blue_range += blue_distance


        elif red_range >= 300 and red_range < 600:
            red_distance = 4
            red.forward(red_distance)
            red_range += red_distance
            green_distance = 4
            green.forward(green_distance)
            green_range += green_distance
            orange_distance = 4
            orange.forward(orange_distance)
            orange_range += orange_distance
            blue_distance = 4
            blue.forward(blue_distance)
            blue_range += blue_distance


        elif red_range >= 600 and red_range < 650:
            for turn in range(18):
                red_distance = 10
                red.left(red_distance)
                red.forward(red_distance)
                red.forward(10)
                red_range += red_distance
                green_distance = 10
                green.left(green_distance)
                green.forward(green_distance)
                green.forward(19)
                green_range += green_distance
                orange_distance = 10
                orange.left(orange_distance)
                orange.forward(orange_distance)
                orange.forward(29)
                orange_range += orange_distance
                blue_distance = 10
                blue.left(blue_distance)
                blue.forward(blue_distance)
                blue_range += blue_distance


        elif red_range >= 650 and red_range < 935:
            red_distance = round(random.random() * 3)
            red.forward(red_distance)
            red_range += red_distance
            green_distance = round(random.random() * 3)
            green.forward(green_distance)
            green_range += green_distance
            orange_distance = round(random.random() * 3)
            orange.forward(orange_distance)
            orange_range += orange_distance
            blue_distance = round(random.random() * 3)
            blue.forward(blue_distance)
            blue_range += blue_distance

    if red_range > green_range:
        if red_range > blue_range:
            if red_range > orange_range:
                screen.reset()
                screen.bgcolor("black")
                start.shape("blank")
                start.color("white")
                start.setpos(0, 0)
                start.write("Red Wins!", align="center", font=("Arial", 40))

    if green_range > red_range:
        if green_range > blue_range:
            if green_range > orange_range:
                screen.reset()
                screen.bgcolor("black")
                start.shape("blank")
                start.color("white")
                start.setpos(0, 0)
                start.write("Green doesn't get to win.", align="center", font=("Arial", 40))
                time.sleep(1)
                start.clear()
                start.write("Sorry Not Sorry!", align="center", font=("Arial", 40))

    if blue_range > green_range:
        if blue_range > red_range:
            if blue_range > orange_range:
                screen.reset()
                screen.bgcolor("black")
                start.shape("blank")
                start.color("white")
                start.setpos(0, 0)
                start.write("Blue Wins!", align="center", font=("Arial", 40))

    if orange_range > green_range:
        if orange_range > blue_range:
            if orange_range > red_range:
                screen.reset()
                screen.bgcolor("black")
                start.shape("blank")
                start.color("white")
                start.setpos(0, 0)
                start.write("Orange Wins!", align="center", font=("Arial", 40))

    screen.exitonclick()



def main():


    turtle1()
    #turtle2()
    #turtle3()
    #turtle4()
    #race()


if __name__ == "__main__":
    main()

