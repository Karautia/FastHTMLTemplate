from fasthtml.common import *
from .components import HelloWorldComponent

app, rt = fast_app()

@rt('/')
def get(): return Div(HelloWorldComponent(), hx_get="/change")

@rt('/change')
def get(): return P('Nice to be here!')

