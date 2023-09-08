from dataclasses import dataclass
from enum import Enum
from typing import Union


class GridType(Enum):
    Uniform = 1
    Collection = 2
    Tree = 3
    Subset = 4


class CollectionType(Enum):
    Spacial = 1
    Temporal = 2


class Section(Enum):
    DataItem = 1
    All = 2


@dataclass
class GridAttribs:
    """Represents an XDMF Grid

    Fields
    ------
    grid_type : GridType
        The type of grid.
    name : str | None
        The name of the grid.
    collection_type : CollectionType | None
        The type of collection this grid represents. Only meaningful if
        grid_type is Collection.
    section : Section | None
        The section of data. Only meaningful if grid_type is Subset.
    """
    grid_type: GridType = GridType.Uniform
    name: Union[str, None] = None
    collection_type: Union[CollectionType, None] = None
    section: Union[Section, None] = None
