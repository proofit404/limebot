"""Implementations."""
from pathlib import Path

from dependencies import Injector
from dependencies import Package

current = Package("app.implementations")
pages = Package("app.web.pages")


class IndexPage(Injector):
    render = pages.IndexPage.render
    engine = current.Engine.engine


class Engine(Injector):
    engine = pages.Engine
    schemes = current.XSD.registry
    styles = current.XSLT.registry


class XSD(Injector):
    registry = pages.Registry
    function = pages.read_xsd
    directory = Path("src/app/web/xsd")
    data = {}


class XSLT(Injector):
    registry = pages.Registry
    function = pages.read_xslt
    directory = Path("src/app/web/xsl")
    data = {}
