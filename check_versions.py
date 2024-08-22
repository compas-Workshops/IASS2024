import compas
import compas_occ
import compas_viewer
import compas_fd
import compas_ifc

def check_version(package, version):
    return f"{version} => {package.__version__}  {'OK' if package.__version__ == version else 'ERROR'}"


print(f"compas               : {check_version(compas, '2.4.0')}")
print(f"compas_occ           : {check_version(compas_occ, '1.2.1')}")
print(f"compas_viewer        : {check_version(compas_viewer, '1.3.0')}")
print(f"compas_fd            : {check_version(compas_fd, '0.5.1')}")
print(f"compas_ifc           : {check_version(compas_ifc, '1.2.4')}")
