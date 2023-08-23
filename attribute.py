from dataclasses import dataclass
from enum import Enum
from typing import Union

class AttributeType(Enum):
    Scalar = 1
    Vector = 2
    Tensor = 3
    Tensor6 = 4
    Matrix = 5
    GlobalID = 6

class Center(Enum):
    Node = 1
    Cell = 2
    Grid = 3
    Face = 4
    Edge = 5
    Other = 6

@dataclass
class Attribute:
    """Describes an XDMF attribute

    Fields:
        name (str | None, optional): The name of the attribute. 
            Defaults to None
        attribute_type (AttributeType, optional): Type of attribute. 
            Defaults to AttributeType.Scalar
        center (Center, optional): Defines where attribute data are 
            centered. Defaults to Center.Node
    """
    name: Union[str, None] = None
    attribute_type: AttributeType = AttributeType.Scalar
    center: Center = Center.Node