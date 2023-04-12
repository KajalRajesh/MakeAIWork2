# DocString to document its purpose.
'''
This is a DocString.
This class can be used to generate Rectangle Objects
with arguments
width and height
'''

# UpperCamelCase ClassName
# Starts with LETTER
class Rectangle:
    
    # Constructor
    # Starts with double underscore -> Dunder Method -> MANDATORY !
    def __init__(self, widthArg, heightArg, colorArg='black'):
        '''summary'''
        self.width = widthArg
        self.height = heightArg
        self.area = round(self.width * self.height)
        self.color = colorArg
        
    def getWidth (self):
        pass
    
    def setWidth (self, width):
        pass
    
    def getArea(self):
        # Next keeps value inside (LOCAL) function
        self.area = round(self.width * self.height)
        # Now value is distributed outside (GLOBAL) function.
        # return round(self.width * self.height)
        # 
        return self.area

    def getColor(self, color):
        self.color = color

        
