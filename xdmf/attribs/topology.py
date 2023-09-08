from dataclasses import dataclass
from enum import Enum
from typing import Union

from xdmf.shape import Shape


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
class TopologyAttribs:
    """Represents an XDMF Topology

    Fields
    ------
    topology_type : TopologyType
        The type of topology.
    dimensions : Shape
        The dimensions of the topology
    name : str | None
        The name of the topology.
    nodes_per_element : int | None
        The number of nodes per element. Only meaningful when topology_type is
        Polyvertex, Polygon, or Polyline.
    order (?): ?
    """
    topology_type: TopologyType
    dimensions: Shape
    name: Union[str, None] = None
    nodes_per_element: Union[int, None] = None
    order: None = None
