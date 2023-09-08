from xml.etree import ElementTree as ET


def write_tree(root: ET.Element, filename: str):
    """Write `root` and all its children to an XML file given by `filename`
    """
    tree = ET.ElementTree(root)
    tree.write(filename)
