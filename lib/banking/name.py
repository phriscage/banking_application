"""
    name class
"""
#pylint: disable=R0903

class Name(object):
    """ the name class includes """

    def __init__(self, name):
        """ instantiate the class
        Args:
            name (str): name of a customer with a comma
        """
        self.first = None
        self.last = None
        self._format_name(name)

    def _format_name(self, name):
        """ format the name into first ane last
        Args:
            name (str): name of a customer with a comma
        """
        name_parts = (part.strip() for part in str(name).split(','))
        self.last = name_parts.next()
        self.first = name_parts.next()
