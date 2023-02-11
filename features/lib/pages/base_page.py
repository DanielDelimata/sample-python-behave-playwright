class BasePage(object):
    """
    Base class that all page models can inherit from
    """

    def __init__(self, context):
        self.context = context

    def find_element(self, locator):
        return self.context.page.locator(locator)
