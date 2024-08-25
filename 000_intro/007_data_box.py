from compas.geometry import Box

box = Box(1)

print(box)

print(box.xsize)
print(box.ysize)
print(box.zsize)
print(box.frame)
print(box.guid)
print(box.name)

print(box.to_jsonstring(pretty=True))
print(box.to_json("box.json"))
