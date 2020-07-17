Appendix A:
Marching Cube Algorithm

In programming, firstly, a MR image is input and converted into digital binary matrixes using “os”
and “Nibabel” module. The Library and Cube Index are set up to achieve the database exchange.
The Cube Index then matches the data that are extracted from the library to find the edge
intersection. “Data_path” is a complete file path. Then the data is read through Nibabel module
into a 3D array (in this case 64*64*64) named “data_mri” in from of a digital binary array.
Then the read data is rotated and “squeeze” function is used to remove single-dimensional
entries from the shape of the array.
“aiCubeEdgeFlags” is a table that the algorithm uses to indicate the edge intersections and how
a surface cuts through each cube in a 3D data set, to make the programming convenient and the
performance fast.

Whether a vertex value is inside or outside the isosurface is determined by the 8-bit Cube Index.
If say vertex 0 and 3 are below the isosurface. Cube-index will then be 0000 1001 == 9. The 9th
entry into the egdeTable is 905hex == 1001 0000 0101 which means edge 11,8,2, and 0 are cut
and so we work out the vertices of the intersection of the isosurface with those edges.

Next, 9 in the triTable is 0, 11, 2, 8, 11, 0. This corresponds to 2 triangular facets, one between
the intersection of edge 0 11 and 2. The other between the intersections along edges 8 11 and 0.
This part of algorithm determines how the Edge Configuration and the Triangulated Cube
Configuration are generated, and then moves to the next cube until the whole object is marched
through to create the 3D model.
“Edge_vertex_address” is defined as a dictionary that its keys are the edges of cubes and the
values are vertices related to each edge. Also, “normalize” function calculates the normal vector
for each face.

The first methods that runs (display method for OpenGL) in the program is the “test1” method.
The class “cube” draws the cubes in the environment to create the grids.
In this class each cube is an object with its edges, vertices and cube index (the cube-index
indicated which vertex is equal to one and which is equal to zero). In this program edge-size is 
define equal to (0.3) in a global variable. Each consists of 12 edges that each edge is defined with
its starting and ending vertices.

(i, j, k) indicates the 0th vertex of the cube and the cube is drawn by adding the edges. Self.edges
defines the edges between each vertices. Index of the cube is initially set to zero (all eight vertices
are set to zero initially).

Since the images are 64 * 64 8 64 we have defined a matrix (named “cube_shap”) with the same
dimension. So we need 63 cubes in each direction to marching through in the algorithm.
We also use a nested for loop to traverse each vertex of a each cube in the cube-list and create
the addresses dictionary. This dictionary is created to check the relation between each cube index
vertex number of that to the image data.

The cubes are generated first by drawing one column along y-axis (until it reaches to j=63) and
then the second column along y-axis starts from bottom to top, and so on. Then when we get a
complete list of cubes in x-y plane it shifts one unit along the z-axis to complete the second round
of cube generation (each created cube is appended to a list named “cube_list”). The sequence of
marching the cubes is exactly the same as the sequence of generating them.

“segment_shape” has the same size of segmented part. Here we have considered the whole
image data as the segmented part data, but the pixel numbers of segmented area can be entered
to just reconstruct the surface for the region of interest. “obj” is defined as a zero matrix which
has the same size of “segment-shape”. We use “obj” list to put all the related data to segmented
part in that list. “shift” is the variable defined to move the “obj” in the grid, but by inserting the
whole image data the value of shift will become equal to zero. The threshold for pixel values is
set to 1561 and at the end of each nested for loop (after checking all 8 vertices of each cube) it
checks if the pixel values are over 1561, if so, all those pixel values should be set to zero. Since
we need to use the pixel values for look up table and binary numbers are read from right to left,
we need to reverse them.

We create “edited_cube_list” to remove unnecessary cubes to increase the efficiency of the
code. These cubes are the ones that all their vertices are either equal to zero or one (because in
this part we just need to create the surface), in this case the length of cubes’ list decreases
significantly and increases the code’s efficiency. 

There is also a method named “surface_sketcher” takes the number of the cube (i.number) and
returns the coordinates of triangles in that cube. This function creates a list of edges with vertices
related to each edge. The “init” function is used to define the light position. 