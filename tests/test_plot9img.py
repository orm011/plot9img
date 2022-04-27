from plot9img import __version__, ggimg, ggimg_toImage
import PIL.Image
from pathlib import Path
from plotnine import geom_rect, aes, geom_text
import pandas as pd


def test_version():
    assert __version__ == "0.1.0"


def test_PIL_render():
    """basic check that annotated image has same size as original (ie no extraneous space from matplotlib)"""
    test_dir = Path(__file__).parent
    im = PIL.Image.open(f"{test_dir}/vine_med.jpeg")

    annotations_df = pd.DataFrame(
        [{"x1": 100, "x2": 225, "y1": 100, "y2": 300, "label": "a box"}]
    )
    gimg = (
        ggimg(image=im, data=annotations_df)
        + geom_rect(
            aes(xmin="x1", xmax="x2", ymin="y1", ymax="y2", color="label"), fill=None
        )
        + geom_text(aes(label="label", x="x1", y="y1", color="label"))
    )

    annotated_im = ggimg_toImage(gimg)
    assert annotated_im.size == im.size
