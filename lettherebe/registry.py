from .utils import extract_arguments


class HandlerRegistry(object):
    """
    Base container class to hold groups of handlers
    """

    def __init__(self):
        self.members = {}

    def __call__(self, identifier):
        """
        This is provided so that registry instances can be used
        as decorators.
        """

        def wrapper(function):
            arguments = extract_arguments(function)
            self.members[identifier] = {'function': function, 'arguments': arguments}
        return wrapper


repository_host = HandlerRegistry()
package_language = HandlerRegistry()
documentation_host = HandlerRegistry()
continuous_integration_host = HandlerRegistry()
