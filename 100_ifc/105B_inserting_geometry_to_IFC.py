from compas_ifc.model import Model
from compas.geometry import Box
from compas.geometry import Frame

model = Model("data/Duplex_A_20110907.ifc")

last_storey = model.building_storeys[-1]

# ==============================================================================
# Prepare geometry and properties for the roof
# ==============================================================================
geometry = Box(10, 10, 0.1).to_mesh() 
# This can be any COMPAS geometry

frame = Frame([5, 5, 6])

custom_properties = {
    "Pset_RoofCommon": {"IsExternal": True, "AcousticRating": "40 dB", "FireRating": "F120"},
    "CustomPset": {"CustomProperty1": "Value1", "CustomProperty2": "Value2"},   
}


# ==============================================================================
# Insert the roof to the model
# ==============================================================================
model.create(
    "IfcRoof", 
    name="MyRoof", 
    description="A Custom roof made with COMPAS", 
    parent=last_storey, 
    geometry=geometry, 
    frame=frame, 
    properties=custom_properties
)

model.show()

# ==============================================================================
# Save the updated model
# ==============================================================================
model.save("data/Duplex_A_20110907_with_roof.ifc")
