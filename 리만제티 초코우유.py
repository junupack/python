import turtle
import mpmath

screen = turtle.Screen()
screen.bgcolor("white")
screen.setup(800, 800)
screen.tracer(0)  # 자동 갱신 끔

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.pensize(1)
t.pencolor("black")

scale = 50
sigma = 0.5
step = 0.05
t_val = 0
first = True
running = True

def stop_drawing():
    global running
    running = False


screen.listen()

def draw_step():
    global t_val, first, running

    if not running:
        return

    s = complex(sigma, t_val)
    try:
        z = mpmath.zeta(s)
        x = float(mpmath.re(z)) * scale
        y = float(mpmath.im(z)) * scale

        if first:
            t.penup()
            t.goto(x, y)
            t.pendown()
            first = False
        else:
            t.goto(x, y)
    except:
        pass

    t_val += step

    # 매 5 점마다 화면 갱신해서 움직임 보이도록 조절
    if int(t_val / step) % 5 == 0:
        screen.update()

    screen.ontimer(draw_step, 1)

draw_step()
screen.mainloop()