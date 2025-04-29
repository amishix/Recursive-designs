import turtle 
import random 


t = turtle.Turtle()
#run these lines in order to import python turtle and importing random to use random function

def setup():
    t.reset() 
    t.speed("fastest")
    t.color("darkbrown")
    # set up all the different functions so speed is fast and turtle color is changed 
    t.penup()
    t.right(90)
    t.forward(300)
    t.right(90)
    t.forward(400)
    t.right(90)
    t.pendown()
    t.pensize(6)
    t.screen.bgcolor("orange")
    

t.penup()
t.left(90)
t.forward(300)
t.right(90)
t.pendown()
t.right(90)#fix position of turtle to draw grass

#grass
t.color("limegreen")
t.begin_fill()
for i in range(2):
    t.forward(1380)
    t.right(90)
    t.forward(400)    
    t.right(90)

t.end_fill()
   

t.left(90)#fix position of turtle back to draw trees
t.color("brown")
t.right(90)
t.penup()
t.forward(300)
t.left(90)
t.pendown()



# values for variables and integrated randomisation 
dist = 300
depth = 6
angle = random.randint(40, 90)
sf = random.uniform(0.4,0.6) #defining the scale factor for the branches

def tree(depth, dist, angle=random.randint(40, 90), sf=random.uniform(0.4,0.6)):
    if depth <0:
        return 
    else:
        t.forward(dist)
        t.right(angle/2)
        tree(depth - 1, dist * random.uniform(0.4,0.6), angle=random.randint(40, 90))#randominisation function in play 
        t.left(angle)
        tree(depth - 1, dist * random.uniform(0.4,0.6), angle=random.randint(40, 90))
        t.right(angle/2)
        t.color("green" if depth < 2 else "#40292d") 
        t.backward(dist) #returns to starting position 

tree(depth, dist, angle=random.randint(40, 90), sf=random.uniform(0.4,0.6))

t.penup()
t.right(90)
t.forward(400)
t.left(90)
t.pendown()



def tree(depth, dist, angle=random.randint(40, 90), sf=random.uniform(0.4,0.6)):
    if depth ==0: 
        # drawing tree leaves in a bunch at the last nodes by using depth==0
        t.color("green")
        t.begin_fill()
        t.circle(20)
        t.end_fill()
        t.color("brown")
    else:
        t.forward(dist) 
        t.color("brown")
        t.left(angle/2)
        tree(depth - 1, dist * random.uniform(0.4,0.6), angle=random.randint(40, 90))
        t.right(angle)
        tree(depth - 1, dist * random.uniform(0.4,0.6), angle=random.randint(40, 90))
        t.left(angle/2)
        t.backward(dist)

tree(depth, dist, angle=random.randint(40, 90), sf=random.uniform(0.4,0.6))

t.penup()
t.right(90)
t.forward(500)
t.left(90)
t.pendown()

def appletree(depth, dist, angle=random.randint(40, 90), sf=random.uniform(0.5,0.8)):
    if depth <0:
        return 
    else:
        turtle.pensize(max(1, 6 - depth)) #changing the thickness of the lines drawn for the trees
        t.forward(dist) 
        t.color("#147327")
        t.begin_fill()
        t.circle(25)
        t.end_fill()
        t.color("#c91c1c")
        t.begin_fill()
        t.circle(8)
        t.end_fill()
        t.color("brown")
        t.left(angle/2)
        appletree(depth - 1, dist * random.uniform(0.5,0.8), angle=random.randint(40, 90))
        t.right(angle)
        appletree(depth - 1, dist * random.uniform(0.5,0.8), angle=random.randint(40, 90))
        t.left(angle/2)
        t.backward(dist)


appletree(depth, dist, angle=random.randint(40, 90), sf=random.uniform(0.5,0.8))

turtle.hideturtle()


