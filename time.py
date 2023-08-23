from dataclasses import dataclass
from enum import Enum
from typing import Union

class TimeType(Enum):
    Single = 1
    HyperSlab = 2
    List = 3
    Range = 4

@dataclass
class Time:
    """Represents an XDMF Time
    
    Fields:
        time_type (TimeType, optional): The type of time data. Defaults
            to TimeType.Single
        value (float | None, optional): The time value. Only meaningful 
            when time_type is Single. Defaults to None
    """
    time_type: TimeType = TimeType.Single
    value: Union[float, None] = None