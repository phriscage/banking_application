"""
    name class
"""

class Name(object):
    """ the name class includes """

    def __init__(self, name):
        """ instantiate the class """
        self.first = None
        self.last = None
        self._format_name(name)

    def _format_name(self, name):
        """ format the name into first ane last """
        name_parts = (part.strip() for part in str(name).split(','))
        self.last = name_parts.next()
        self.first = name_parts.next()