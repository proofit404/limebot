from lxml.etree import fromstring
from lxml.etree import tostring
from lxml.etree import XML
from lxml.etree import XSLT
from xmlschema import etree_tostring
from xmlschema import XMLSchema


class Index:
    def render(self):
        transform = XSLT(XML(open("src/app/web/xsl/index.xsl").read()))
        schema = XMLSchema("src/app/web/xsd/index.xsd")
        data = {"title": "Lime", "message": "Hello world."}
        xml = schema.encode(data)
        html = tostring(transform(fromstring(etree_tostring(xml))))
        return html
