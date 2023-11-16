from pycad.visualization import STLVisualizer

path_to_stl = ['assets/mandible.stl', 'assets/maxilla.stl']
path_to_stl_file = 'assets/maxilla.stl'
visualizer = STLVisualizer(path_to_stl)
visualizer.visualize()