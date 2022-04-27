# plot9img
versatile visualization of images and labels (eg boxes, text, masks) by re-using the grammar of graphics interface.

This is a utility that lets you "plot" your labeled images using a grammar of graphics interface (plotnine).
It is currently implemented as a small wrapper around the plotnine interface with defaults for showing 
 images (which can be hard to remember every time). 

Plotnine itself is a a grammar of graphics interface implemented on top of matplotlib. Unlike using matplotib directly,
you can leave a lot of details (eg how is data mapped to colors, etc) to the library. 

Plotnine already includes standard ways to plot boxes, points, lines, polygons, text, etc, refer to their documentation
about how to map your data to those shapes.

Plot9img helps plot any image data you have around, as long as you provide your labels as a python dataframe.
Coordinates are assumed to be absolute (pixels) with 0,0 at the top left of the image.

# examples:
see notebook in [examples/boxes.ipynb](examples/boxes.ipynb)

# trying it out:
`pip install git+https://github.com/orm011/plot9img.git@v0.1.0-alpha`
