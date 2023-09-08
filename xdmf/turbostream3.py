import h5py
from typing import List

def get_node_array_names(f: h5py.File) -> List[str]:
    array_names: list[str] = list(f)
    node_array_names = [n for n in array_names 
                        if n.startswith("node_array")]
    return node_array_names


def write_xdmf(f: h5py.File):
    pass

with h5py.File("input.hdf5", "r") as f:
    write_xdmf(f)

