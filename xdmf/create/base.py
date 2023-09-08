from typing import Union
from xml.etree import ElementTree as ET

from xdmf.attribs.data_item import DataItemAttribs
from xdmf.attribs.attribute import AttributeAttribs
from xdmf.attribs.geometry import GeometryAttribs
from xdmf.attribs.grid import GridAttribs
from xdmf.attribs.time import TimeAttribs
from xdmf.attribs.topology import TopologyAttribs
from xdmf.convert import array_to_string


def create_xdmf(version: Union[str, None] = None) -> ET.Element:
    attribs: dict[str, str] = {}
    if version is not None:
        attribs["Version"] = version

    return ET.Element("Xdmf", attribs)


def create_domain(name: Union[str, None] = None) -> ET.Element:
    attribs: dict[str, str] = {}
    if name is not None:
        attribs["Name"] = name

    return ET.Element("Domain", attribs)


def create_geometry(g: GeometryAttribs) -> ET.Element:
    attribs: dict[str, str] = {}
    attribs["GeometryType"] = g.geometry_type.name

    return ET.Element("Geometry", attribs)


def create_grid(g: GridAttribs) -> ET.Element:
    attribs: dict[str, str] = {}
    attribs["GridType"] = g.grid_type.name
    if g.name is not None:
        attribs["Name"] = g.name
    if g.collection_type is not None:
        attribs["CollectionType"] = g.collection_type.name
    if g.section is not None:
        attribs["Section"] = g.section.name

    return ET.Element("Grid", attribs)


def create_time(t: TimeAttribs) -> ET.Element:
    attribs = {"TimeType": t.time_type.name}
    if t.value is not None:
        attribs["Value"] = str(t.value)

    return ET.Element("Time", attribs)


def create_topology(t: TopologyAttribs) -> ET.Element:
    attribs: dict[str, str] = {}
    attribs["TopologyType"] = t.topology_type.name
    attribs["Dimensions"] = array_to_string(t.dimensions)
    if t.name is not None:
        attribs["Name"] = t.name
    if t.nodes_per_element is not None:
        attribs["NodesPerElement"] = str(t.nodes_per_element)
    if t.order is not None:
        attribs["Order"] = t.order

    return ET.Element("Topology", attribs)


def add_child(parent: ET.Element, child: ET.Element) -> None:
    parent.append(child)


def add_children(parent: ET.Element, *children: ET.Element) -> None:
    for c in children:
        parent.append(c)


def set_text(elt: ET.Element, txt: str) -> None:
    elt.text = txt
