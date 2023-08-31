from dataclasses import dataclass
from enum import Enum
from typing import Tuple, Union
from xml.etree import ElementTree as ET

import h5py
import numpy as np
from numpy.typing import NDArray

from . import utils


Shape = Tuple[int, ...]


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
    text: str = ""

    def get_xml_element(self) -> ET.Element:
        attribs = {
            "Dimensions": self.dimensions,
            "ItemType": self.item_type.name,
            "NumberType": self.number_type.name,
            "Precision": str(self.precision.value),
            "Format": self.format.name
        }
        if self.name is not None:
            attribs["Name"] = self.name
        data_item = ET.Element("DataItem", attribs)
        if self.text != "":
            data_item.text = self.text

        return data_item

@dataclass
class Uniform:
    data_item: DataItem

    @staticmethod
    def from_hdf5_dataset(data: h5py.Dataset) -> "Uniform":
        data_item = DataItem(
            dimensions=utils.array_string(data.shape),
            name=data.name,
            item_type=ItemType.Uniform,
            number_type=NumberType.from_numpy(data.dtype),
            precision=Precision.from_numpy(data.dtype),
            format=Format.HDF,
            text=data.file.filename
        )
        return Uniform(data_item)

    @staticmethod
    def from_numpy_array(data: NDArray, *, name=None) -> "Uniform":
        data_item = DataItem(
            dimensions=utils.array_string(data.shape),
            name=name,
            item_type=ItemType.Uniform,
            number_type=NumberType.from_numpy(data.dtype),
            precision=Precision.from_numpy(data.dtype),
            format=Format.XML,
            text=utils.array_string(data.flatten())
        )
        return Uniform(data_item)

    def get_xml_element(self) -> ET.Element:
        return self.data_item.get_xml_element()

@dataclass
class Hyperslab:
    hyperslab: DataItem
    descriptor: Uniform
    data_item: Uniform

    @staticmethod
    def from_hdf5_dataset(
        data: h5py.Dataset, *,  start: Shape, stride: Shape, count: Shape
    ) -> "Hyperslab":
        hyperslab = DataItem(
            dimensions=utils.array_string(count),
            item_type=ItemType.HyperSlab,
            number_type=NumberType.from_numpy(data.dtype),
            precision=Precision.from_numpy(data.dtype),
            format=Format.XML,
        )

        descriptor_array = np.array((start, stride, count))
        descriptor = Uniform.from_numpy_array(descriptor_array)

        data_item = Uniform.from_hdf5_dataset(data)

        return Hyperslab(hyperslab, descriptor, data_item)

    @staticmethod
    def from_numpy_array(
        data: NDArray, *,  start: Shape, stride: Shape, count: Shape
    ) -> "Hyperslab":
        hyperslab = DataItem(
            dimensions=utils.array_string(count),
            item_type=ItemType.HyperSlab,
            number_type=NumberType.from_numpy(data.dtype),
            precision=Precision.from_numpy(data.dtype),
            format=Format.XML,
        )

        descriptor_array = np.array((start, stride, count))
        descriptor = Uniform.from_numpy_array(descriptor_array)

        data_item = Uniform.from_numpy_array(data)

        return Hyperslab(hyperslab, descriptor, data_item)

    def get_xml_element(self) -> ET.Element:
        e_hyperslab = self.hyperslab.get_xml_element()
        e_descriptor = self.descriptor.get_xml_element()
        e_data_item = self.data_item.get_xml_element()

        e_hyperslab.append(e_descriptor)
        e_hyperslab.append(e_data_item)

        return e_hyperslab
