from xml.etree import ElementTree as ET

from numpy.typing import NDArray

from xdmf.attribs.attribute import (
    AttributeAttribs,
    Center,
    attribute_type_from_shape
)
from xdmf.create.base import add_child
from xdmf.create import data_item


def create(a: AttributeAttribs) -> ET.Element:
    attribs = {}
    attribs["AttributeType"] = a.attribute_type.name
    attribs["Center"] = a.center.name
    if a.name is not None:
        attribs["Name"] = a.name

    return ET.Element("Attribute", attribs)


def create_from_ndarray(
    arr: NDArray, name: str, center=Center.Node
) -> ET.Element:
    attribs = AttributeAttribs(
        attribute_type=attribute_type_from_shape(arr.shape),
        center=center,
        name=name,
    )
    attribute = create(attribs)
    e_data_item = data_item.uniform_from_ndarray(arr)
    add_child(attribute, e_data_item)
    return attribute


