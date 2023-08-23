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
class Grid:
    """Represents an XDMF Grid

    Fields:
        name (str | None, optional): The name of the grid. Defaults to
            None
        grid_type (GridType, optional): The type of grid. Defaults to
            GridType.Uniform
        collection_type (CollectionType, optional): The type of 
            collection this grid represents. Only meaningful if 
            grid_type is Collection. Defaults to None
        section (Section | None, optional): The section of data. Only 
            meaningful if grid_type is Subset. Defaults to None
    """
    name: Union[str, None] = None
    grid_type: GridType = GridType.Uniform
    collection_type: Union[CollectionType, None] = None
    section: Union[Section, None] = None

