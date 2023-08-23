import xml.etree.ElementTree as ET
from .data_item import DataItem
from .attribute import Attribute
from .domain import Domain
from .xdmf import Xdmf
from .geometry import Geometry
from .grid import Grid, GridType, CollectionType, Section
from .time import Time, TimeType
from .topology import Topology, TopologyType
from typing import Iterable

def add_text(elt: ET.Element, s: str):
    """Add the string `s` inside the XML element `elt`
    """
    elt.text = s

def add_data_item(elt: ET.Element, d: DataItem):
    """Add the data item `d` as a sub element of `elt`
    """
    attribs = {
        "Dimensions": d.dimensions,
        "ItemType": d.item_type.name,
        "NumberType": d.number_type.name,
        "Precision": str(d.precision.value),
        "Format": d.format.name
    }

    if d.name is not None:
        attribs["Name"] = d.name

    data_item = ET.SubElement(elt, "DataItem", attribs)
    return data_item

def add_attribute(elt: ET.Element, a: Attribute):
    """Add the attribute `a` as a sub element of `elt`
    """
    attribs = {
        "AttributeType": a.attribute_type.name,
        "Center": a.center.name
    }

    if a.name is not None:
        attribs["Name"] = a.name

    attribute = ET.SubElement(elt, "Attribute", attribs)
    return attribute

def add_domain(elt: ET.Element, d: Domain):
    """Add the domain `d` as a sub element of `elt`
    """
    attribs: dict[str, str] = {}

    if d.name is not None:
        attribs["Name"] = d.name

    domain = ET.SubElement(elt, "Domain", attribs)
    return domain

def create_xdmf(x: Xdmf = Xdmf()):
    """Create an xdmf wrapper element
    """
    attribs: dict[str, str] = {}

    if x.version is not None:
        attribs["Version"] = x.version

    xdmf = ET.Element("Xdmf", attribs)
    return xdmf

def add_geometry(elt: ET.Element, g: Geometry):
    """Add the geometry `g` as a sub element of `elt`
    """
    attribs = {
        "GeometryType": g.geometry_type.name
    }

    geometry = ET.SubElement(elt, "Geometry", attribs)
    return geometry

def add_grid(elt: ET.Element, g: Grid):
    """Add the grid `g` as a sub element of `elt`
    """
    attribs = {
        "GridType": g.grid_type.name
    }

    if g.name is not None:
        attribs["Name"] = g.name

    if g.grid_type == GridType.Collection:
        assert(isinstance(g.collection_type, CollectionType))
        attribs["CollectionType"] = g.collection_type.name

    if g.grid_type == GridType.Subset:
        assert(isinstance(g.section, Section))
        attribs["Section"] = g.section.name

    grid = ET.SubElement(elt, "Grid", attribs)
    return grid

def add_topology(elt: ET.Element, t: Topology):
    """Add the topology `t` as a sub element of `elt`
    """
    attribs: dict[str, str] = {
        "TopologyType": t.topology_type.name,
        "NumberOfElements": str(t.number_of_elements)   
    }
    
    if t.name is not None:
        attribs["Name"] = t.name

    types = [
        TopologyType.Polyvertex,
        TopologyType.Polygon,
        TopologyType.Polyline
    ]
    if t.topology_type in types:
        assert(t.nodes_per_element is not None)
        attribs["NodesPerElement"] = str(t.nodes_per_element)

    if t.order is not None:
        attribs["Order"] = t.order
    
    topology = ET.SubElement(elt, "Topology", attribs)
    return topology


def add_time(elt: ET.Element, t: Time):
    """Add the topology `t` as a sub element of `elt`
    """
    attribs = {"TimeType": t.time_type.name}

    if t.time_type == TimeType.Single:
        assert(t.value is not None)
        attribs["Value"] = str(t.value)

    time = ET.SubElement(elt, "Time", attribs)
    return time

def write_tree(root: ET.Element, filename: str):
    """Write `root` and all its children to an XML file given by
    `filename`
    """
    tree = ET.ElementTree(root)
    tree.write(filename)

def array_string(a: Iterable):
    """Returns the elements of `a` in a string separated by spaces
    """
    return " ".join(map(str, a))