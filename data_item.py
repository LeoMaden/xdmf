from dataclasses import dataclass
from enum import Enum
from typing import Union

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

class Precision(Enum):
    Byte = 1
    Half = 2
    Single = 4
    Double = 8

@dataclass
class DataItem:
    """Represents an XDMF DataItem

    Fields:
        dimensions (str): The dimensions of the data separated by spaces
        name (str | None, optional): The name of the DataItem. Defaults
            to None
        item_type (ItemType, optional): The type of the item. Defaults 
            to ItemType.Uniform
        number_type (NumberType, optional): The number type. Defaults to
            NumberType.Float
        precision (Precision, optional): The number precision. Defaults
            to Precision.Single
        format (Format, optional): The format of the data. Defaults to
            Format.XML
    """
    dimensions: str
    name: Union[str, None] = None
    item_type: ItemType = ItemType.Uniform
    number_type: NumberType = NumberType.Float 
    precision: Precision = Precision.Single
    format: Format = Format.XML
