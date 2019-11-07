import turtle
wn = turtle.Screen()
wn.title("Benims Pong")
wn.bgcolor("red")
wn.setup(width=800, height=600)
wn.tracer(0)

#Racket 1
racket_a = turtle.Turtle()
racket_a.speed(0)
racket_a.shape("circle")
racket_a.color("magenta")
racket_a.shapesize(stretch_wid=5, stretch_len=1)
racket_a.penup()
racket_a.goto(-350,0)

#Racket 2
racket_b = turtle.Turtle()
racket_b.speed(0)
racket_b.shape("circle")
racket_b.color("blue")
racket_b.shapesize(stretch_wid=5, stretch_len=1)
racket_b.penup()
racket_b.goto(350,0)

#Boll
boll = turtle.Turtle()
boll.speed(0)
boll.shape("circle")
boll.color("yellow")
boll.penup()
boll.goto(0, 0)
boll.dx = 2
boll.dy = -2

#Rörligheter
def racket_a_up():
    y = racket_a.ycor()
    y += 20
    racket_a.sety(y)

def racket_a_down():
    y = racket_a.ycor()
    y -= 20
    racket_a.sety(y)

def racket_b_up():
    y = racket_b.ycor()
    y += 20
    racket_b.sety(y)

def racket_b_down():
    y = racket_b.ycor()
    y -= 20
    racket_b.sety(y)

#Styra
wn.listen()
wn.onkeypress(racket_a_up, "w")
wn.onkeypress(racket_a_down, "s")
wn.onkeypress(racket_b_up, "Up")
wn.onkeypress(racket_b_down, "Down")

while True:
    wn.update()

    #bollrörelser
    boll.setx(boll.xcor() + (boll.dx / 5))
    boll.sety(boll.ycor() + (boll.dy / 5))

    #väggar
    if boll.ycor() > 290:
        boll.sety(290)
        boll.dy *= -1
    
    if boll.ycor() < -290:
        boll.sety(-290)
        boll.dy *= -1
    
    if boll.xcor() > 390:
        boll.goto(0, 0)
        boll.dx *= -1
    
    if boll.xcor() < -390:
        boll.goto(0, 0)
        boll.dx *= -1

    #Racket träff
    if (boll.xcor() > 340 and boll.xcor() < 350) and (boll.ycor() < racket_b.ycor() + 40 and boll.ycor() > racket_b.ycor() -40):
        boll.dx *= -1
        boll.setx(340)

    if (boll.xcor() < -340 and boll.xcor() > -350) and (boll.ycor() < racket_a.ycor() + 40 and boll.ycor() > racket_a.ycor() -40):
        boll.dx *= -1
        boll.setx(-340)