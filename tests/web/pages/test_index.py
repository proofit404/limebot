from app.web.pages.index import Index


def test_index_render():
    """The `render` method of the `Index` class should return HTML."""
    index = Index()
    html = index.render()
    assert html.startswith(b"<html")
