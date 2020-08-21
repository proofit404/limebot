"""Implementations."""
from dependencies import Injector
from dependencies import Package


current = Package("app.implementations")
pages = Package("app.web.pages")


class IndexPage(Injector):
    render = pages.IndexPage.render
    engine = current.Engine.engine


class Engine(Injector):
    engine = pages.Engine
    # @todo #130 Cache opened schemes and styles.
