from dataclasses import dataclass
from enum import Enum
from typing import Union

from xdmf.shape import Shape


class AttributeType(Enum):
    Scalar = 1
    Vector = 2
    Tensor = 3
    Tensor6 = 4
    Matrix = 5
    GlobalID = 6


def attribute_type_from_shape(s: Shape) -> AttributeType:
    if len(s) == 1:
        return AttributeType.Scalar
    elif len(s) == 2:
        return AttributeType.Vector
    elif (len(s) == 3 and s[1:2] == (3, 3)):
        return AttributeType.Tensor
    elif len(s) == 3:
        return AttributeType.Matrix
    else:
        raise NotImplementedError("Tensor6 and GlobalID not implemented")


class Center(Enum):
    Node = 1
    Cell = 2
    Grid = 3
    Face = 4
    Edge = 5
    Other = 6


@dataclass
class AttributeAttribs:
    """Describes an XDMF attribute

    Fields
    ------
    name : str | None
        The name of the attribute.
        Defaults to None
    attribute_type : AttributeType
        Type of attribute. Defaults to AttributeType.Scalar.
    center : Center
        Defines where attribute data are centered. Defaults to Center.Node.
    """
    name: Union[str, None] = None
    attribute_type: AttributeType = AttributeType.Scalar
    center: Center = Center.Node

