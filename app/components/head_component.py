from fasthtml.common import *

def get_head_component():
    header = Head(Link(rel="stylesheet", href="styles.css"))
    return header
