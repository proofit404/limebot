from attr import attrib
from attr import attrs
from generics import private
from lxml.etree import Element
from lxml.etree import tostring
from lxml.etree import XML
from lxml.etree import XSLT
from xmlschema import XMLSchema


@private
@attrs(frozen=True)
class Engine:

    schemes = attrib()
    styles = attrib()

    def process(self, style, schema, data):
        xsd = self.schemes.get(schema)
        xslt = self.styles.get(style)
        xml = xsd.encode(data, etree_element_class=Element)
        html = tostring(xslt(xml))
        return html


@private
@attrs(frozen=True)
class Registry:

    function = attrib()
    directory = attrib()
    data = attrib()

    def get(self, key):
        # @todo #130 Do not accept arbitrary relative paths. We
        #  should know the path of directories we relies on. Join
        #  base path of the file with directory constant.
        if key not in self.data:
            self.data[key] = self.function(self.directory / key)
        return self.data[key]


# @todo #130 Protect against malformed files. We should
#  accept only XSD documents for the schema argument and
#  XSL document for the style argument.


def read_xsd(path):
    with path.open() as f:
        return XMLSchema(f)


def read_xslt(path):
    return XSLT(XML(path.read_text()))
