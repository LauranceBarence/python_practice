import turtle


def draw_star(size):
    count = 1
    while count <= 5:
        turtle.forward(size)
        turtle.right(144)
        count += 1


def star_draw():
    turtle.pencolor('blue')
    turtle.pensize(2)
    stars = 1
    while stars <= 5:
        draw_star(50 * stars)
        stars += 1


def draw_tree(depth):
    if depth+1 >= 1:
        turtle.forward((depth+1)*10)
        turtle.right(20)
        draw_tree(depth-1)
        turtle.left(40)
        draw_tree(depth-1)
        turtle.right(20)
        turtle.backward((depth+1)*10)


def main():
    turtle.left(90)
    draw_tree(4)
    turtle.exitonclick()


if __name__ == '__main__':
    main()
