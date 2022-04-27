from plotnine import (
    ggplot,
    scale_y_reverse,
    xlim,
    theme,
    element_blank,
)
from plotnine import scale_color_discrete
import matplotlib.pyplot as plt
import io
import PIL.Image
import plotnine
import pandas
import matplotlib.pyplot as plt


def _theme_image(w: int, h: int, dpi=80) -> plotnine.theme:
    """a theme with plotnine defaults for showing images without coordinates"""
    return theme(
        axis_line=element_blank(),
        axis_text_x=element_blank(),
        axis_text_y=element_blank(),
        axis_ticks=element_blank(),
        axis_ticks_length=0,
        axis_ticks_pad=0,
        axis_title_x=element_blank(),
        axis_title_y=element_blank(),
        legend_box=element_blank(),
        legend_position=None,
        plot_margin=0,
        panel_grid=element_blank(),
        plot_background=element_blank(),
        panel_background=element_blank(),
        panel_border=element_blank(),
        panel_grid_major=element_blank(),
        panel_grid_minor=element_blank(),
        figure_size=(w / dpi, h / dpi),
        dpi=dpi,
    )


def ggimg(
    image: PIL.Image.Image,
    mapping: plotnine.aes = None,
    data: pandas.DataFrame = None,
    dpi=80,
) -> plotnine.ggplot:
    w, h = image.size
    return (
        ggplot(mapping=mapping, data=data)
        + scale_y_reverse(limits=(0, h))
        + xlim(0, w)
        + scale_color_discrete(guide=False)  # removes legend for line color
        + _theme_image(w, h, dpi=dpi)
    )


def _add_image(f, im):
    w, h = im.size
    for ax in f.get_axes():
        ax.imshow(im, origin="lower", extent=(0, w, 0, -h))
        ax.set_xlim(0, w)
        ax.set_ylim(-h, 0)
    return f


def ggimg_draw(ggim: plotnine.ggplot) -> plt.Figure:
    """draws image object to figure."""
    f = ggim.draw()
    f = _add_image(f, ggim.environment.eval("image"))
    return f


def ggimg_toImage(gimg: plotnine.ggplot) -> PIL.Image.Image:
    """renders to PIL.Image"""
    plt.ioff()
    try:
        buf = io.BytesIO()
        f = ggimg_draw(gimg)
        f.savefig(buf, format="png")
        plt.close(f)
        buf.seek(0)
        im = PIL.Image.open(buf)
    finally:
        plt.ion()

    return im
