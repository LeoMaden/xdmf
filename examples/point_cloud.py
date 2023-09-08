import numpy as np
import xdmf
from xdmf.attribs.time import TimeAttribs
from xdmf.create import create_topology

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
    e_domain = xdmf.create_domain()
    xdmf.add_child(e_xdmf, e_domain)
    e_grid = xdmf.create_grid(xdmf.GridAttribs())
    xdmf.add_child(e_domain, e_grid)

    # Add time
    e_time = xdmf.create_time(TimeAttribs(value=t))
    xdmf.add_child(e_grid, e_time)

    # Add topology
    topology_attribs = xdmf.TopologyAttribs(
        topology_type=xdmf.TopologyType.Polyvertex,
        dimensions=(npoints,),
        nodes_per_element=1,
    )
    e_topology = create_topology(topology_attribs)
    xdmf.add_child(e_grid, e_topology)

    # Add geometry
    e_geometry = xdmf.create_geometry(xdmf.GeometryAttribs())
    xdmf.add_child(e_grid, e_geometry)


    xyz_dims = xdmf.array_string(xyz.shape)
    geom_data_item = xdmf.DataItem(dimensions=xyz_dims)
    e_geom_data = xdmf.add_data_item(e_geometry, geom_data_item)

    geom_data = xdmf.array_string(xyz.flatten())
    xdmf.add_text(e_geom_data, geom_data)

    # Write to file
    xdmf.write_tree(e_xdmf, f"{base_name}_{i}.xdmf")

