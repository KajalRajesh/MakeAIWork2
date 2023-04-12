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
    
    #Method
    
    def getArea(self):
        # Next keeps value inside (LOCAL) function
        # self.area = round(self.width * self.height)
        # Now value is distributed outside (GLOBAL) function.
        # return round(self.width * self.height)
        # 
        return self.area

    def getColor(self):
        return self.color

# child class from parent rectangle using super()
class Box(Rectangle): 
    
    def __init__(self, widthArg, heightArg, depthArg):   
        super().__init__(widthArg, heightArg) 
        self.depthArg = depthArg 
        self.area = round(self.width * self.height * self.depthArg) 
        
    # def getArea1(self):
    #     # Next keeps value inside (LOCAL) function
    #     #self.area1 = round(self.width * self.height * self.depthArg)
    #     # Now value is distributed outside (GLOBAL) function.
    #     # return round(self.width * self.height)
    #     # 
    #     return self.area1
    
class Triangle(Rectangle):
    
    def __init__(self, heightArg, baseArg, colorArg='black'):
        super().__init__(heightArg, baseArg) 
        self.height = heightArg
        self.base = baseArg
        self.area = round((self.base * self.height)/2)
        
   
    
