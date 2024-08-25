from compas_ifc.model import Model
from compas.geometry import Box
from compas.geometry import Frame


# ==============================================================================
# Setup minimal spatial hierarchy
# ==============================================================================
model = Model()

# Create a default project
project = model.create_default_project()

model.unit = "m"

# Create a site and a building
site = model.create("IfcSite", name="MySite", parent=project)
building = model.create("IfcBuilding", name="MyBuilding", parent=site)

# Create 3 storeys
model.create("IfcBuildingStorey", name="Storey 1", parent=building)
model.create("IfcBuildingStorey", name="Storey 2", parent=building)
model.create("IfcBuildingStorey", name="Storey 3", parent=building)


# ==============================================================================
# Using the template method
# ==============================================================================
# model = Model.template(building_count=1, storey_count=3, unit="m")


# ==============================================================================
# Inserting floor geometries to the storeys
# ==============================================================================
height = 0

for storey in model.building_storeys:
    geometry = Box(10, 10, 0.1).to_mesh()
    model.create("IfcSlab", name="MyFloor", parent=storey, geometry=geometry, frame=Frame([0, 0, height]))
    height += 3

model.show()

# ==============================================================================
# Save the model
# ==============================================================================
model.save("data/ifc_from_scratch.ifc")