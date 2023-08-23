from dataclasses import dataclass
from enum import Enum
from typing import Union

class TopologyType(Enum):
    Polyvertex = 1
    Polyline = 2
    Polygon = 3
    Triangle = 4
    Quadrilateral = 5
    Tetrahedron = 6
    Pyramid = 7
    Wedge = 8
    Hexahedron = 9
    Edge_3 = 10
    Triangle_6 = 11
    Quadrilateral_8 = 12
    Tetrahedron_10 = 13
    Pyramid_13 = 14
    Wedge_15 = 15
    Hexahedron_20 = 16
    Mixed = 17
    _2DSMesh = 18 
    _2DRectMesh = 19
    _2DCoRectMesh = 20
    _3DSMesh = 21
    _3DRectMesh = 22
    _3DCoRectMesh = 23

@dataclass
class Topology:
    """Represents an XDMF Topology

    Fields:
        topology_type (TopologyType): The type of topology
        number_of_elements (int): The number of elements
        name (str | None, optional): The name of the topology. Defaults 
            to None
        nodes_per_element (int | None, optional): The number of nodes 
            per element. Only meaningful when topology_type is 
            Polyvertex, Polygon, or Polyline. Defaults to None
        order (?): ?
    """
    topology_type: TopologyType
    number_of_elements: int
    name: Union[str, None] = None
    nodes_per_element: Union[int, None] = None 
    order: None = None