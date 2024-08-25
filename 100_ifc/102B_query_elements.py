from compas_ifc.model import Model
from pprint import pprint

model = Model("data/Duplex_A_20110907.ifc")

# ==============================================================================
# Direct access to entities
# ==============================================================================
print("=" * 80 + "\nDirect access to entities\n" + "=" * 80)

# Access to project
project = model.project
print(project)
pprint(project.attributes)
print()

# Access to sites
sites = model.sites
print("Number of sites:", len(sites))
print(sites[0])
pprint(sites[0].attributes)
print()

# Access to buildings
buildings = model.buildings
print("Number of buildings:", len(buildings))
print(buildings[0])
pprint(buildings[0].attributes)
print()

# Access to building storeys
building_storeys = model.building_storeys
print("Number of building storeys:", len(building_storeys))
print(building_storeys[0])
pprint(building_storeys[0].attributes)
print()

# Access to building elements
building_elements = model.building_elements
print("Number of building elements:", len(building_elements))
print(building_elements[0])
pprint(building_elements[0].attributes)
print()


# ==============================================================================
# Querying entities
# ==============================================================================
print("=" * 80 + "\nQuerying entities\n" + "=" * 80)

# Search by type
windows = model.get_entities_by_type("IfcWindow")
print("Number of windows:", len(windows))
print(windows[0])
pprint(windows[0].attributes)


# Search by name
entities = model.get_entities_by_name("M_Fixed:4835mm x 2420mm:4835mm x 2420mm:145788")
print("\nFound entities: ",entities)
for entity in entities:
    print(entity)
    pprint(entity.attributes)
    print()


# Search by GlobalId
window = model.get_entity_by_global_id("1hOSvn6df7F8_7GcBWlR72")
print("\nFound entity: ",window)
pprint(window.attributes)