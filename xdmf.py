from dataclasses import dataclass
from typing import Union

@dataclass
class Xdmf:
    version: Union[str, None] = None