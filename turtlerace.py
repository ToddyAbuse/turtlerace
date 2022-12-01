import turtle as tu

#Velger fart og plassering for tegning
tu.speed(5)
tu.penup()
tu.goto(-140, 140)

#class turtle:
    #def __init__(self, color, pos):
        

#Tegner banen

for step in range(6):
    tu.write(step, align="center")
    tu.forward(20)
    tu.right(90)
    tu.forward(10)
    tu.pendown()
    tu.forward(150)
    tu.penup()
    tu.backward(160)
    tu.left(90)
    tu.forward(20)

#Skilpadder

bob = tu.Turtle()
bob.color("green")
bob.shape("turtle")

bob.penup()
bob.goto(-160,100)
bob.pendown

gerd = tu.Turtle()
gerd.color("red")
gerd.shape("turtle")

gerd.penup()
gerd.goto(-160,70)
gerd.pendown

derek = tu.Turtle()
derek.color("blue")
derek.shape("turtle")

derek.penup()
derek.goto(-160,40)
derek.pendown

ronny = tu.Turtle()
ronny.color("yellow")
ronny.shape("turtle")

ronny.penup()
ronny.goto(-160,10)
ronny.pendown

for turn in range(100):
    bob.forward(bob.randint(1,5))


