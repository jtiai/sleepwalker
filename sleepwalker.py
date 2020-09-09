import random

from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

window.title = "Pong"
window.borderless = True
window.fullscreen = False
window.exit_button.visible = False
window.fps_counter.enabled = True

mouse.visible = False

sky = Sky()

ground_collision_mesh = Entity(
    model="landscape_lowpoly", position=(0, 0, 0), collider="mesh", visible=False
)

ground = Entity(
    model="landscape_hipoly",
    color=color.green,
    position=(0, 0, 0),
    texture="grass_baked",
)

for _ in range(100):
    x = random.randrange(-90, 90)
    z = random.randrange(-90, 90)
    rot_y = random.randrange(0, 90)

    magic_box = Entity(
        model="cube",
        color=color.red,
        position=(x, 0, z),
        origin=(0, -0.5, 0),
        scale=(0.2, 0.2, 0.2),
        rotation_y=rot_y,
        collider="box",
    )
    magic_box.pickable = True

player = FirstPersonController(x=0, y=1, z=0)
player.gun = None
player.rotation_y = 270


def input(key):
    if key == "left mouse down":
        for hitinfo in mouse.collisions:
            try:
                if hitinfo.distance < 2.0 and hitinfo.entity.pickable:
                    print("Picking up...")
                    destroy(hitinfo.entity)
            except AttributeError:
                pass


app.run()
