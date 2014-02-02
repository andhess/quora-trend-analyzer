class headerNode():
    """
    Object class to represent each column of data
    Attributes:
        string name, string type, bool restricted (/SENSITIVE)
    """

    def __init__( self, name, typ ):
        self.name = name
        splice = typ.find('/SENSITIVE')

        # case:  restricted
        if  splice >= 0:
            self.type = typ[:splice]
            self.restricted = True
        else:
            self.type = typ
            self.restricted = False
        
        self.data = None

    def __str__( self ):
        output = '\nName:\t\t' + self.name + '\n'
        output += 'Type:\t\t' + self.type + '\n'
        output += 'Restricted:\t' + str( self.restricted ) + '\n'
        if self.data:
            output += 'Data:\n\n' + self.data 

        return output