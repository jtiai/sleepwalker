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

ground_collision_mesh = Entity(model="landscape_lowpoly", position=(0, 0, 0), collider="mesh")
ground_collision_mesh.visible = False

ground = Entity(model="landscape_hipoly", color=color.green, position=(0, 0, 0), texture="grass_baked")

player = FirstPersonController(x=0, y=1, z=0)
player.gun = None

app.run()
