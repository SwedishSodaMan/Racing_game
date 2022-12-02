from ursina import*
import random

def update():
    global offset, run

    if run:
        offset += time.dt*1
        setattr(road, "texture_offset", (0, offset))

        car.x += held_keys['d']*time.dt * .5
        car.x -= held_keys['a']*time.dt * .5

        if car.x>= 0.24:
            car.x= 0.24
        if car.x<= -0.28:
            car.x= -0.28

app = Ursina()

window.color = color.pink

road = Entity(model = "cube", color = color.pink, scale = (10, 0.5, 60), position = (0,0,0),
    texture = "Assets/road.png")
car = Entity(parent = road, model = "cube", texture = "Assets/car.png", scale = (.17, .0001, .06), 
    position = (-.07, 1, -.12,), collider = "box")

offset = 0
run = True


camera.position = (0, 8, -26)
camera.rotation_x = 20

app.run()
