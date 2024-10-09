from fasthtml.common import *

def get_navbar_component():
    navbar = [
        Div(
                # Left-aligned logo (now replaced with plain text)
                Div("FRAME FINDER", cls="logo"),  # Replace logo with plain text
                Button("Action!", cls="button"),
                cls="navbar"  # Main navbar div
            ),
    ]
        
    return Div(*navbar, cls="navbar_container")