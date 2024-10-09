from fasthtml.common import *

def get_search_bar_component():
    search_bar = [
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
    ]
    return Div(*search_bar, cls="searchbar_container")