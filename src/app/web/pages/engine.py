from attr import attrib
from attr import attrs
from attr import Factory
from generics import private
from lxml.etree import Element
from lxml.etree import tostring
from lxml.etree import XML
from lxml.etree import XSLT
from xmlschema import XMLSchema


@private
@attrs(frozen=True)
class Engine:

    # @todo #130 Don't load style and schema on the method level. We
    #  should implement two dict-like classes which will load XSL and
    #  XSD documents as necessary. Path to directories should not be
    #  hardcoded as well. This will gave us a necessary level of the
    #  flexibility to change this logic. Path to the directory should
    #  be passed through the implementations module.
    schemes = attrib(default=Factory(dict))
    styles = attrib(default=Factory(dict))

    def process(self, style, schema, data):
        if style not in self.styles:
            # @todo #130 Do not accept arbitrary relative paths. We
            #  should know the path of directories we relies on. Join
            #  base path of the file with directory constant.
            self.styles[style] = XSLT(XML(open(style).read()))
        if schema not in self.schemes:
            # @todo #130 Protect against malformed files. We should
            #  accept only XSD documents for the schema argument and
            #  XSL document for the style argument.
            self.schemes[schema] = XMLSchema(schema)
        xml = self.schemes[schema].encode(data, etree_element_class=Element)
        html = tostring(self.styles[style](xml))
        return html
