# DocString to document its purpose.
'''
This is a DocString.
This class can be used to generate triangle Objects
with arguments
base and height
'''

# UpperCamelCase ClassName
# Starts with LETTER
class Triangle():
    
    # Constructor
    # Starts with double underscore -> Dunder Method -> MANDATORY !
    def __init__(self, heightArg, baseArg, colorArg='black'):
        '''summary'''
        self.height = heightArg
        self.base = baseArg
        self.area = round((self.base * self.height))/2
        self.color = colorArg
   
    
    #Method
    
    # def getArea(self):
    #     # Next keeps value inside (LOCAL) function
    #     self.area = round((self.base * self.height))/2
    #     # Now value is distributed outside (GLOBAL) function.
    #     # return round(self.width * self.height)
    #     # 
    #     return self.area

    # def getColor(self):
    #     return self.color