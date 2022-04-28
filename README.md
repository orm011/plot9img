# plot9img
versatile visualization of images and labels (eg boxes, text, masks) by re-using the grammar of graphics interface.

Instead of learning to use each dataset's plotting tools (if they have any), use one standard tool with a flexible interface for all your plotting. 
Plot9img lets you view images and labels using a grammar of graphics interface [plotnine](https://plotnine.readthedocs.io/en/stable/)
Plot9img helps plot any image data you have around, as long as you provide your labels as a python dataframe. You do need to 
convert the annotations you want to view into this format.

Annotation coordinates are assumed to be absolute (pixels) with 0,0 at the top left of the image (though that can probably be changed using plotnine 
options)

This tool is a small wrapper around the plotnine interface with defaults (themes/scales) for showing images (which can be hard to remember every time).
Plotnine itself is a a grammar of graphics interface for general plotting implemented on top of matplotlib. Unlike using matplotib directly,
you can leave a lot of details (eg how is data mapped to colors, etc) to the library. 

Plotnine already includes standard ways to plot boxes, points, lines, polygons, text, etc, refer to their documentation
about how to map your data to those shapes. The notebook below shows you how to draw boxes.

Mostly meant for my use in my own projects.

# examples:
see notebook in [examples/boxes.ipynb](examples/boxes.ipynb)

# trying it out:
`pip install git+https://github.com/orm011/plot9img.git@v0.1.0-alpha`
