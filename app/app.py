from fasthtml.common import *
from .components.image_gallery import ImageGallery
from package_name.main import get_image_paths
import os



public_path = os.path.join(os.path.abspath(os.path.join(__file__, os.pardir, "public")))
data_path = os.path.abspath("/workspaces/FastHTMLTemplate/data")

######## fastHTML app #########
app, rt = fast_app(static_path=public_path)

image_paths = get_image_paths(data_path)
print(image_paths)
# frontend
@rt('/')
def get():
    return Html(
        Head(
            Link(rel="stylesheet", href="styles.css")
        ),
        Body(
            # Navbar container
            Div(
                # Left-aligned logo (now replaced with plain text)
                Div("FRAME FINDER", id="logo"),  # Replace logo with plain text
                Button("Action!", id="button"),
                id="navbar"  # Main navbar div
            ),
            # content window
            ImageGallery(image_paths),
            # search bar
            Div(
                Div(
                    Input(type="text", placeholder="Search...", id="input-field"),
                    Button(
                        Img(src="auto-fix.svg", id="search-icon"),
                        id="search-button"),
                    ),
                id="searchbar"),
        ),
    )