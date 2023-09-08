from xml.etree import ElementTree as ET

import h5py
import numpy as np
from numpy.typing import NDArray

from xdmf.attribs.data_item import (
    DataItemAttribs,
    Format,
    ItemType,
    NumberType,
    Precision,
)
from xdmf.convert import array_to_string
from xdmf.create.base import add_children
from xdmf.shape import Shape


def create(d: DataItemAttribs) -> ET.Element:
    attribs: dict[str, str] = {}
    attribs["Dimensions"] = array_to_string(d.dimensions)
    attribs["ItemType"] = d.item_type.name
    attribs["NumberType"] = d.number_type.name
    attribs["Precision"] = str(d.precision.value)
    attribs["Format"] = d.format.name
    if d.name is not None:
        attribs["Name"] = d.name

    return ET.Element("DataItem", attribs)


def uniform_from_ndarray(arr: NDArray) -> ET.Element:
    attribs = DataItemAttribs(
        dimensions=arr.shape,
        format=Format.XML,
        item_type=ItemType.Uniform,
        number_type=NumberType.from_numpy(arr.dtype),
        precision=Precision.from_numpy(arr.dtype),
    )
    data_item = create(attribs)
    data_item.text = array_to_string(arr)
    return data_item


def uniform_from_dataset(data: h5py.Dataset) -> ET.Element:
    attribs = DataItemAttribs(
        dimensions=data.shape,
        format=Format.HDF,
        item_type=ItemType.Uniform,
        number_type=NumberType.from_numpy(data.dtype),
        precision=Precision.from_numpy(data.dtype),
    )
    data_item = create(attribs)
    data_item.text = data.file.filename
    return data_item


# NOTE: Doesn't really make sense to use hyperslab if data is being stored
# directly in the XDMF
# def hyperslab_from_ndarray(
    # arr: NDArray, start: Shape, stride: Shape, count: Shape
# ) -> ET.Element:
    # descriptor_array = np.array((start, stride, count))
    # descriptor = uniform_from_ndarray(descriptor_array)
    # data_item = uniform_from_ndarray(arr)
    # attribs = DataItemAttribs(
        # dimensions=count,
        # format=Format.XML,
        # item_type=ItemType.HyperSlab,
        # number_type=NumberType.from_numpy(arr.dtype),
        # precision=Precision.from_numpy(arr.dtype),
    # )
    # hyperslab = create(attribs)
    # add_children(hyperslab, descriptor, data_item)
    # return hyperslab


def hyperslab_from_dataset(
    data: h5py.Dataset, start: Shape, stride: Shape, count: Shape
) -> ET.Element:
    descriptor_array = np.array((start, stride, count))
    descriptor = uniform_from_ndarray(descriptor_array)
    data_item = uniform_from_dataset(data)
    attribs = DataItemAttribs(
        dimensions=count,
        format=Format.XML,
        item_type=ItemType.HyperSlab,
        number_type=NumberType.from_numpy(data.dtype),
        precision=Precision.from_numpy(data.dtype),
    )
    hyperslab = create(attribs)
    add_children(hyperslab, descriptor, data_item)
    return hyperslab
