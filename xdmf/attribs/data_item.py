from dataclasses import dataclass
from enum import Enum
from typing import Union

import numpy as np

from xdmf.shape import Shape


class ItemType(Enum):
    Uniform = 1
    Collection = 2
    Tree = 3
    HyperSlab = 4
    Coordinates = 5
    Function = 6


class Format(Enum):
    XML = 1
    HDF = 2
    # BINARY = 3


# class Endian(Enum):
#     """Applicable only to binary format"""
#     NATIVE = 1
#     BIG = 2
#     LITTLE = 3


class NumberType(Enum):
    Float = 1
    Int = 2
    UInt = 3
    Char = 4
    UChar = 5

    @staticmethod
    def from_numpy(dt: np.dtype) -> "NumberType":
        if dt.name.startswith("float"):
            return NumberType.Float
        elif dt.name.startswith("int"):
            return NumberType.Int
        elif dt.name.startswith("uint"):
            return NumberType.UInt
        elif dt.name.startswith("char"):
            return NumberType.Char
        elif dt.name.startswith("uchar"):
            return NumberType.UChar
        raise Exception("Invalid type")


class Precision(Enum):
    Byte = 1
    Half = 2
    Single = 4
    Double = 8

    @staticmethod
    def from_numpy(dt: np.dtype) -> "Precision":
        if dt.name.endswith("8"):
            return Precision.Byte
        elif dt.name.endswith("16"):
            return Precision.Half
        elif dt.name.endswith("32"):
            return Precision.Single
        elif dt.name.endswith("64"):
            return Precision.Double
        raise Exception("Invalid type")


@dataclass
class DataItemAttribs:
    """Represents an XDMF DataItem

    Fields
    ------
    dimensions : str
        The dimensions of the data separated by spaces name (str | None,
        optional): The name of the DataItem. Defaults to None
    item_type : ItemType
        The type of the item.
    number_type : NumberType
        The number type.
    precision : Precision
        The number precision.
    format : Format
        The format of the data.
    """
    dimensions: Shape
    name: Union[str, None] = None
    item_type: ItemType = ItemType.Uniform
    number_type: NumberType = NumberType.Float
    precision: Precision = Precision.Single
    format: Format = Format.XML
