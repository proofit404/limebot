from io import StringIO

from lxml.etree import parse
from lxml.etree import tostring
from lxml.etree import XML
from lxml.etree import XSLT
from xmlschema import etree_tostring
from xmlschema import XMLSchema


class Index:
    def __init__(self):
        self.title = "Lime"
        self.message = "Hello world."

    def render(self):
        transform = XSLT(XML(open("src/app/web/xsl/index.xsl").read()))
        schema = XMLSchema("src/app/web/xsd/index.xsd")
        data = {"title": self.title, "message": self.message}
        xml = etree_tostring(schema.encode(data))
        # @todo #111 Avoid encoding to string and decoding back to etree.
        html = tostring(transform(parse(StringIO(xml))))
        return html
