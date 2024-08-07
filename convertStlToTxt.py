import numpy as np
from stl import mesh

def convert_stl_to_txt(stl_file, txt_file):
  # Load the STL file
  mesh_data = mesh.Mesh.from_file(stl_file)

  # Extract the vertices from the mesh
  vertices = mesh_data.vectors.reshape(-1, 3)

  # Save the vertices to a TXT file
  np.savetxt(txt_file, vertices, delimiter=' ')

# Specify the input STL file path
stl_file = 'full_head.stl'

# Specify the output TXT file path
txt_file = 'output.txt'

# Convert the STL file to TXT
convert_stl_to_txt(stl_file, txt_file)