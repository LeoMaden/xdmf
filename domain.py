from dataclasses import dataclass
from typing import Union

@dataclass
class Domain:
    """Represents an XDMF Domain.

    Fields:
        name (str | None, optional): The name of the domain. Defaults to
            None
    """
    name: Union[str, None] = None