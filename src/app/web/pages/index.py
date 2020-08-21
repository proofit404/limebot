from attr import attrib
from attr import attrs
from generics import private


@private
@attrs(frozen=True)
class IndexPage:

    engine = attrib()

    def render(self):
        return self.engine.process(
            "src/app/web/xsl/index.xsl",
            "src/app/web/xsd/index.xsd",
            {"title": "Lime", "message": "Hello world."},
        )
