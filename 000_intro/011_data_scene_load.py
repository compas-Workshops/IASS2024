import pathlib

import compas
from compas.scene import Scene

session = compas.json_load(pathlib.Path(__file__).parent / "scenesession.json")

scene: Scene = session["scene"]

scene.clear_context()
scene.draw()
