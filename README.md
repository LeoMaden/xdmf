# Xdmf: Python package to help write XDMF files

This Python package defines a number of data classes, enums, and functions to help write XML files using the XDMF model and format.

## Examples

### Time Varying Polygon Point Cloud

Write a sequence of XDMFs to describe the position of vertices of a regular polygon that rotate about the $x$ axis over time

```python

import numpy as np
import xdmf.construct as xdmf

base_name = "points"
radius = 2
npoints = 12

tend = 5
nsteps = 20

times = np.linspace(0, tend, nsteps)

for i, t in enumerate(times):
    # Define point positions at time t
    angles = np.linspace(0, 360, npoints+1)[:-1]
    angles += 360 * (t / tend)
    
    x = np.zeros_like(angles)
    y = radius * np.cos(np.deg2rad(angles))
    z = radius * np.sin(np.deg2rad(angles))

    xyz = np.column_stack((x, y, z))

    # Create XDMF structure and grid
    e_xdmf = xdmf.create_xdmf()
    e_domain = xdmf.add_domain(e_xdmf, xdmf.Domain())
    e_grid = xdmf.add_grid(e_domain, xdmf.Grid())

    # Add time
    e_time = xdmf.add_time(e_grid, xdmf.Time(value=t))

    # Add topology
    topology = xdmf.Topology(
        topology_type=xdmf.TopologyType.Polyvertex, 
        number_of_elements=npoints,
        nodes_per_element=1
    )
    e_topology = xdmf.add_topology(e_grid, topology)

    # Add geometry
    e_geometry = xdmf.add_geometry(e_grid, xdmf.Geometry())

    xyz_dims = xdmf.array_string(xyz.shape)
    geom_data_item = xdmf.DataItem(dimensions=xyz_dims)
    e_geom_data = xdmf.add_data_item(e_geometry, geom_data_item)

    geom_data = xdmf.array_string(xyz.flatten())
    xdmf.add_text(e_geom_data, geom_data)

    # Write to file
    xdmf.write_tree(e_xdmf, f"{base_name}_{i}.xdmf")

```

## FAQs

### How do I use data from a HDF5 file?

To reference data that lives in a HDF5 file, use a `DataItem` with `format = Format.HDF` and then set its text to `name.hdf5:/array_name` using `add_text`. To see what arrays are inside a HDF5 file, you can use `h5ls name.hdf5`.

## Learn More

XDMF3 Model and Format Specification: https://www.xdmf.org/index.php/XDMF_Model_and_Format