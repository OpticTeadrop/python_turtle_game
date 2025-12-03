# tymoteusz walczak - astronomia, fizyka

import turtle
import random
import time

def turtul_is_null() :
    screen = turtle.Screen()
    t_special = turtle.Turtle()
    t_special.teleport(-300, 0)
    t_special.write("what are you starin' at?")
    t_special.teleport(0, 0)
    t_special.write("you chose nothin', you get nothin'")
    t_special.teleport(300, 0)
    t_special.write("that's all. get lost")
    t_special.hideturtle()
    screen.mainloop()
    exit()
    
def turtul_is_lonely() :
    screen = turtle.Screen()
    t_if_1 = turtle.Turtle()
    t_if_1.shape('turtle')
    t_if_1.write("yes, I've won!")
    t_if_1.teleport(-100, -50)
    t_if_1.write('kinda obvious, since I was the only one participating...')
    t_if_1.teleport(-200, -100)
    t_if_1.write('hey, could you invite some of my friends to race me next time? I would be very glad. walking a race by yourself is preatty boring...')
    t_if_1.teleport(370, -150)
    t_if_1.goto(370, -101)
    t_if_1.goto(365, -115)
    t_if_1.teleport(370, -101)
    t_if_1.goto(375, -115)
    t_if_1.teleport(350, -170)
    t_if_1.write('intentional')
    screen.mainloop()
    exit()
    
def make_turtuls(turt_num) :
    turtuls = []
    
    for i in range(turt_num) :
        t = turtle.Turtle()
        t.speed(1)
        t.pensize(5)
        t.shape('turtle')
        t.color(colours[i])
        t.teleport(-300, -25 * i)
        t.write(i + 1)
        turtuls.append(t)
    
    return turtuls

def turtul_make_finish() :
    t_start = turtle.Turtle()
    t_start.teleport(300, 50)

    for i in range(2) :
        t_start.fd(10)
        t_start.rt(90)
        t_start.fd(200)
        t_start.rt(90)

    t_start.pensize(10)

    for i in range(3) :
        t_start.teleport(300, -55 * i)
        t_start.fd(10)
    
    t_start.hideturtle()
    
def countdown() :
    screen = turtle.Screen()
    
    for colour in robots :
        screen.bgcolor(colour)
        screen.update()
        if want_sound == 'y' :
            if robots.index(colour) == 2 :
                sd.play(sq2)
            else :
                sd.play(sq1)
        time.sleep(1)

    screen.bgcolor('skyblue')
    screen.update()

def turtul_race(turt_num, turtuls, play_music) :
    if play_music == 1 :
        thread.start()
        play_music = 0
    
    turtul_win_num = 0
    win = 0
    global is_race_finished
    
    while win != 1 :
        for i in range(turt_num) :
            turtuls[i].fd(random.randint(0, 10))
    
        for turtle in turtuls :
            if turtle.xcor() >= 300 :
                win = 1
                turtul_win_num = turtuls.index(turtle) + 1
                is_race_finished = 1
    
    return turtul_win_num

def turtul_too_much() :
    screen = turtle.Screen()
    turtul_text = turtle.Turtle()
    turtul_text.teleport(100, 0)
    turtul_text.write("too many!")
    turtul_text.hideturtle()
    
    x_change = 0
    y_change = 10
    
    for i in range(1, 1000) :
        t = turtle.Turtle()
        t.shape('turtle')
        t.teleport(-400 + x_change, 400 - y_change)
        if i % 100 == 0 :
            x_change = x_change + 100
            y_change = 10
            
        y_change = y_change + 10
    
    screen.mainloop()
    exit()

want_sound = input('enable sound? [y, n] (choose n if numpy or sounddevice is unavailable) : ')

if want_sound == 'y' :
    import numpy as np
    import sounddevice as sd
    from threading import Thread
    
    def sine_tone(hz, s, a, sr) :
        n_samples = int(sr * s)
        time_points = np.linspace(0, s, n_samples, False)
        sine = np.sin(2 * np.pi * hz * time_points)
        sine = sine * a
        return sine
    
    def white_noise(s, a, sr) :
        n_samples = int(s * sr)
        noise = np.random.uniform(-1, 1, n_samples)
        noise = noise * a
        return noise
    
    def envelope(sound, adsr, sr) :
        attack_samples = int(adsr[0] * sr)
        decay_samples = int(adsr[1] * sr)
        release_samples = int(adsr[3] * sr)
        sustain_samples = len(sound) - (attack_samples + decay_samples + release_samples)
        sound[:attack_samples] *= np.linspace(0, 1, attack_samples)
        sound[attack_samples:attack_samples + decay_samples] *= np.linspace(0, adsr[2], decay_samples)
        sound[attack_samples + decay_samples:attack_samples + decay_samples + sustain_samples] *= adsr[2]
        sound[attack_samples + decay_samples + sustain_samples:] *= np.linspace(adsr[2], 0, release_samples)
        return sound
        
    def drumbeat() :
        nois1 = white_noise(0.15, 0.5, 48000)
        nois1 = envelope(nois1, [0, 0.1, 0.5, 0.01], 48000)
        nois2 = white_noise(0.15, 0.5, 48000)
        
        drums = [nois1, nois2]
        
        global is_race_finished
        
        while True :
            sd.play(nois1)
            sd.wait()
            sd.play(nois1)
            sd.wait()
            sd.play(nois2)
            sd.wait()
            sd.play(random.choice(drums))
            sd.wait()
            if is_race_finished == 1 :
                break
    
    square1 = [sine_tone(200 * i, 1.0, 0.5 / i, 48000) for i in range(1, 65, 2)]
    square2 = [sine_tone(300 * i, 1.0, 0.5 / i, 48000) for i in range(1, 65, 2)]
    
    square_c5 = [sine_tone(523 * i, 0.5, 0.5 / i, 48000) for i in range(1, 65, 2)]
    square_b5 = [sine_tone(988 * i, 0.5, 0.5 / i, 48000) for i in range(1, 65, 2)]
    square_e5 = [sine_tone(659 * i, 0.5, 0.5 / i, 48000) for i in range(1, 65, 2)]
    square_g5 = [sine_tone(784 * i, 0.5, 0.5 / i, 48000) for i in range(1, 65, 2)]
    
    square_d5_sharp = [sine_tone(622 * i, 0.5, 0.5 / i, 48000) for i in range(1, 65, 2)]
    square_g5_sharp = [sine_tone(831 * i, 0.5, 0.5 / i, 48000) for i in range(1, 65, 2)]
    
    sq1 = sum(square1)
    sq2 = sum(square2)
    
    sq3 = sum(square_c5)
    sq4 = sum(square_b5)
    sq5 = sum(square_e5)
    sq6 = sum(square_g5)
    
    sq7 = sum(square_d5_sharp)
    sq8 = sum(square_g5_sharp)
    
    final_melody = [sq3, sq4, sq5, sq6, sq7, sq8]
    
    for i in final_melody :
        i = envelope(i, [0, 0, 1, 0.5], 48000)
    
    nois1 = white_noise(0.15, 0.5, 48000)
    nois1 = envelope(nois1, [0, 0.1, 0.5, 0.01], 48000)
    nois2 = white_noise(0.15, 0.5, 48000)
    
    play_music = 1
    
    thread = Thread(target=drumbeat)

colours = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

robots = ['red3', 'gold', 'green3']

print('turtle race!')

turt_num = int(input('input the number of turtles you want to see race! [2-6] : '))

if turt_num == 0 :
    turtul_is_null()

if turt_num == 1 :
    turtul_is_lonely()

if turt_num > 6 :
    turtul_too_much()

turtul_bet = int(input("which turtle do you think'll win? : "))

turtuls = make_turtuls(turt_num)

turtul_make_finish()

countdown()

is_race_finished = 0
    
turtul_win_num = turtul_race(turt_num, turtuls, play_music)

print('turtle', turtul_win_num, 'has won!')

if turtul_bet == turtul_win_num : 
    print("you've won the bet!")
    
    time.sleep(2)
    
    for i in range(2) :
        sd.play(sq3)
        time.sleep(0.35)
        sd.play(sq4)
        time.sleep(0.15)
        sd.play(sq5)
        time.sleep(0.2)
        sd.play(sq6)
        time.sleep(0.25)
    
else :
    print("you've lost the bet!")
    
    time.sleep(2)
    
    for i in range(2) :
        sd.play(sq3)
        time.sleep(0.35)
        sd.play(sq8)
        time.sleep(0.15)
        sd.play(sq7)
        time.sleep(0.2)
        sd.play(sq6)
        time.sleep(0.25)

screen = turtle.Screen()
screen.mainloop()