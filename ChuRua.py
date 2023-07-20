#!/usr/bin/env python
# coding: utf-8

# In[1]:


import turtle
import random
import time

# Khai báo biến global
win_width = 800
win_height = 400
start_line = -win_width/2 + 20
finish_line = win_width/2 - 20
colors = ['red', 'blue', 'green', 'orange', 'purple', 'yellow']
racers = []
race_started = False

# Hàm để bắt đầu cuộc đua
def start_race():
    global race_started
    if not race_started:
        race_started = True
        for racer in racers:
            racer.speed(1)
            racer.forward(random.randint(1, 20))

# Hàm kiểm tra và thông báo người chiến thắng
def check_winner():
    global racers
    for racer in racers:
        if racer.xcor() >= finish_line:
            race_started = False
            winner = racer.color()[0]
            print("Rùa", winner, "thắng cuộc!")
            return True
    return False

# Hàm chạy đua
def race():
    global race_started
    while race_started:
        for racer in racers:
            racer.forward(random.randint(1, 20))
            if check_winner():
                race_started = False
                break

# Hàm tạo màn hình và các rùa
def setup():
    global racers
    turtle.setup(win_width, win_height)
    turtle.title("Rùa chạy đua - Phần hai")
    turtle.bgcolor('white')

    for i in range(len(colors)):
        new_racer = turtle.Turtle()
        new_racer.shape('turtle')
        new_racer.color(colors[i])
        new_racer.penup()
        new_racer.setpos(start_line, -80 + i*40)
        racers.append(new_racer)

    turtle.hideturtle()

    # Bắt đầu cuộc đua khi nhấn phím "Enter"
    turtle.onkeypress(start_race, 'Return')
    turtle.listen()

# Hàm tính thời gian chạy của rùa
def display_time_elapsed(start_time):
    elapsed_time = time.time() - start_time
    print("Thời gian chạy của rùa:", round(elapsed_time, 2), "giây")

# Hàm main
def main():
    setup()
    global race_started

    # Bắt đầu đếm thời gian khi cuộc đua bắt đầu
    start_time = time.time()

    # Thực hiện cuộc đua
    race()

    # Hiển thị thời gian chạy của rùa khi cuộc đua kết thúc
    display_time_elapsed(start_time)

    turtle.mainloop()

if __name__ == "__main__":
    main()

