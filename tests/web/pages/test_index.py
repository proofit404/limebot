from app.implementations import IndexPage


def test_index_render():
    """The `render` method of the `Index` class should return HTML."""
    html = IndexPage.render()
    assert html.startswith(b"<html")
