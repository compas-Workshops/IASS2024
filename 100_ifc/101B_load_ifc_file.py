from compas_ifc.model import Model

# ==============================================================================
# Load IFC file
# ==============================================================================
model = Model("data/Duplex_A_20110907.ifc")


# ==============================================================================
# Print summary of the model
# ==============================================================================
model.print_summary()


# ==============================================================================
# Print spatial hierarchy of the model
# ==============================================================================
model.print_spatial_hierarchy(max_depth=3)


# ==============================================================================
# Visualize the model
# ==============================================================================
model.show()
