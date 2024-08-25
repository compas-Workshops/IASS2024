#! python3

import compas
import compas_fd
import compas_ifc


def check_version(package, version):
    return f"{version} => {package.__version__}  {'OK' if package.__version__ == version else 'ERROR'}"


print(f"compas     : {check_version(compas, '2.4.1')}")
print(f"compas_fd  : {check_version(compas_fd, '0.5.1')}")
print(f"compas_ifc : {check_version(compas_ifc, '0.5.1')}")
