from random import randint
import turtle


number_of_turtles = 50
steps_of_time_number = 100


pool = [turtle.Turtle(shape='circle') for i in range(number_of_turtles)]
for unit in pool:
    unit.penup()
    unit.speed(50)
    unit.shapesize(0.4, 0.4, 1)


x = [randint(-190, 190) for unit in pool]
y = [randint(-210, 210) for unit in pool]
vx = [randint(-10, 10) for unit in pool]
vy = [randint(-10, 10) for unit in pool]
dt = 1

def step(k):
  x[k] += vx[k]*dt
  y[k] += vy[k]*dt


def y_def(k):
  if y[k] > y_max: 
    y[n] = y_max
  else: 
    y[n] = y_min

y_max = 210
y_min = -210
x_max = 190
x_min = -190



for i in range(steps_of_time_number):
    for unit in pool:
        n=pool.index(unit)
        if (abs(x[n]) <= x_max ) and (abs(y[n]) <= y_max):
            unit.goto(x[n], y[n])
            step(n)
        elif (abs(x[n])<=x_max ) and (abs(y[n])> y_max):
            y_def(n)
            unit.goto(x[n],y[n])
            vy[n] = - vy[n]
            step(n)
        elif (abs(x[n]) > x_max) and (abs(y[n]) <= y_max):
            if x[n] > x_max:
               x[n] = x_max
            else: x[n] = x_min
            unit.goto(x[n], y[n])
            vx[n] = - vx[n]
            step(n)
        else:
            y_def(n)
            if x[n] > x_max: 
              x[n] = x_max
            else: 
              x[n] = x_min
            unit.goto(x[n], y[n])
            vx[n] = - vx[n]
            vy[n] = - vy[n]
            step(n)