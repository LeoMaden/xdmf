# Create data item from numpy arrays

def data_item_uniform_from_numpy(arr: NDArray) -> ET.Element

def data_item_hyperslab_from_numpy(
    arr: NDArray, start: Shape, stride: Shape, count: Shape
) -> ET.Element

...

# Create data item from h5py datasets

def data_item_uniform_from_dataset(data: h5py.Dataset) -> ET.Element

def data_item_hyperslab_from_dataset(
    data: h5py.Dataset, start: Shape, stride: Shape, count: Shape
) -> ET.Element

def topology_from_dataset(
    data: h5py.Dataset, topology_type: TopologyType
) -> ET.Element

...

# Create grids

def grid_collection(
    uniform_grids: list[ET.Element], grid_type: GridType
) -> ET.Element


