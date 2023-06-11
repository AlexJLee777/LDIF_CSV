validChangeTypes = ["add", "delete", "modify"]
ignoredAttrs = []

# Handle LDIF file
class LDIF:
    def __init__(self): # Constructor
        pass

    def _handle(self, dn, entry): # handle a record
        pass

    def _stripLineSep(self, s): # remove all unnecessary characters from string
        pass

    def _unfoldedLine(self): # unfold all lines of a attribute
        pass

    def _parseAttrAndVal(self): # parse Attribute and Value of a record
        pass

    def _parse(self): # parse whole ldif file.
        pass

