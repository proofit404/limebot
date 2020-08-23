from attr import attrib
from attr import attrs
from generics import private


@private
@attrs(frozen=True)
class IndexPage:

    engine = attrib()

    def render(self):
        return self.engine.process(
            "index.xsl", "index.xsd", {"title": "Lime", "message": "Hello world."}
        )
