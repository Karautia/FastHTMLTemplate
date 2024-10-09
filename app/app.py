from fasthtml.common import *
from .components.image_gallery import ImageGallery
from .components.head_component import get_head_component
from .components.search_bar import get_search_bar_component
from .components.navbar import get_navbar_component
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
        # head  
        get_head_component(),
        # body
        Body(
            # Navbar container
            get_navbar_component(),
            # content window
            ImageGallery(stripped_image_paths),
            # search bar
            get_search_bar_component(),
        ),
        # footer
        # get_footer_component(),
    )
