from shape import Shape

class Button:
    def _init_(self,bgColor,txt):
        self.backgroundcolor = bgColor
        self.text = txt
        self.shape = Shape()
    def click(self):
        print(f"Button{self.text}")
        
#create a button object
button1 = Button(0,"black")

#   because the attribute is not in the init ,we assign values,i believe
button1.shape.width = 100
button1.shape.height = 100

button1.click()



        
    