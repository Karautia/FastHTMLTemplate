from fasthtml.common import *
from .components.image_gallery import ImageGallery
from package_name.utils import get_image_paths
import os



public_path = os.path.join(os.path.abspath(os.path.join(__file__, os.pardir, "public")))
data_path = os.path.join(public_path, "data")

######## fastHTML app #########
app, rt = fast_app(static_path=public_path)

# Strip the paths to keep only "/data/..." part
stripped_image_paths = [os.path.relpath(path, public_path) for path in get_image_paths(data_path)]

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
                Div("FRAME FINDER", cls="logo"),  # Replace logo with plain text
                Button("Action!", cls="button"),
                cls="navbar"  # Main navbar div
            ),
            # content window
            ImageGallery(stripped_image_paths),
            # search bar
            Div(
                Input(type="text", placeholder="Search...", cls="input-field"),
                Button(
                    Div(
                        Img(src="auto-fix.svg", alt="Search", id="search-icon"),
                        cls="search-icon-container"
                    ),
                    id="search-button", cls="button"
                ),
                cls="searchbar"
            ),

        ),
    )