from dataclasses import dataclass
from enum import Enum, auto

class GeometryType(Enum):
    XYZ = 1
    XY = 2
    X_Y_Z = 3
    VxVyVz = 4
    Origin_DxDyDz = 5
    Origin_DxDy = 6

@dataclass
class Geometry:
    """Represents an XDMF Geometry

    Fields:
        geometry_type (GeometryType, optional): The layout of the 
            geometry data given. Defaults to GeometryType.XYZ
    """
    geometry_type: GeometryType = GeometryType.XYZ