import turtle

def draw_pythagoras_tree(t, length, level):
    if level == 0:
        return

    t.forward(length)
    pos = t.position()
    heading = t.heading()

    t.left(45)
    draw_pythagoras_tree(t, length * 0.7, level - 1)

    t.setposition(pos)
    t.setheading(heading)

    t.right(45)
    draw_pythagoras_tree(t, length * 0.7, level - 1)

    t.setposition(pos)
    t.setheading(heading)

def init(level, size=200):
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(0, -window.window_height() // 2 + 20)
    t.left(90)
    t.pendown()

    draw_pythagoras_tree(t, size, level)

    window.mainloop()

def main():
    user_input = input("Рівень рекурсії: ")

    if not user_input:
        level = 10
    else:
        level = int(user_input)

    init(level)

if __name__ == "__main__":
    main()
