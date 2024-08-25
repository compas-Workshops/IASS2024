from compas_ifc.model import Model
from pprint import pprint

model = Model("data/Duplex_A_20110907.ifc", use_occ=False)
window = model.get_entities_by_type("IfcWindow")[0]

# ==============================================================================
# Spatial Hierarchy
# ==============================================================================
window.print_spatial_hierarchy()

parent_element = window.parent

print(f"\nParent of {window}:")
print(parent_element)

print(f"\nChildren of {parent_element}:")
print(parent_element.children)


# ==============================================================================
# Attributes
# ==============================================================================
print("=" * 80 + "\nAttributes\n" + "=" * 80)

# Get the attributes dictionary of the window
pprint(window.attributes)

# Recursively extract all sub attributes of the window
# pprint(window.to_dict(recursive=True))

# Print the attributes as a tree
window.print_attributes(max_depth=2)


# ==============================================================================
# Geometry
# ==============================================================================
print("=" * 80 + "\nGeometry\n" + "=" * 80)

print(f"\nGeometry of {window}:")
print(window.geometry)

print(f"\nFrame of {window}:")
print(window.frame)
# window.geometry.to_step("window.stp")


# ==============================================================================
# Custom Properties
# ==============================================================================
print("=" * 80 + "\nCustom Properties\n" + "=" * 80)

print(f"\nCustom properties of {window}:")
print(window.properties)
window.print_properties(max_depth=1)