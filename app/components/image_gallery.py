from fasthtml.common import *

#imgs.append(Img(src=pth, alt=fnm, style="width: 100px; height: auto; margin: 5px;"))

def ImageGallery(image_paths: List[str]):

    return Div(*[Img(src=pth, style="width: 100px; height: auto; margin: 5px;") for pth in image_paths], id="gallery")