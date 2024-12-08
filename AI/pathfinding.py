import pgzrun
import itertools
import random

WIDTH, HEIGHT = 600,600

POSITIONS = [(550,50), (550,550), (50,550), (50,50)]
cycle = itertools.cycle(POSITIONS)
target = Actor('target')
spaceship = Actor("spaceship")
spaceship.center = (50,50)
print(cycle)

def move_target():
    animate(target, "bounce_end", duration = 1, pos = next(cycle))

clock.schedule_interval(move_target, 2)

def update():
    pass
    
    

def draw():
    screen.clear()
    screen.fill((40,40,40))
    target.draw()
    spaceship.draw()


pgzrun.go()
