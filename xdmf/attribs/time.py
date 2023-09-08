from dataclasses import dataclass
from enum import Enum
from typing import Union


class TimeType(Enum):
    Single = 1
    HyperSlab = 2
    List = 3
    Range = 4


@dataclass
class TimeAttribs:
    """Represents an XDMF Time

    Fields
    ------
    time_type : TimeType
        The type of time data.
    value : float | None
        The time value. Only meaningful when time_type is Single.
    """
    time_type: TimeType = TimeType.Single
    value: Union[float, None] = None
