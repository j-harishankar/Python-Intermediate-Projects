from gettext import textdomain

from breezypythongui import EasyFrame
class Rectangle(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self,title="rectangle area")
        self.areaField = self.addTextField(text="", row=3, column=0, columnspan=2,state='readonly')
        self.addLabel(text="Width", row=0, column=0, sticky="nsew")
        self.width = self.addIntegerField(value=0, row=0, column=1)

        self.addLabel(text="Length", row=1, column=0, sticky="nsew")
        self.length = self.addIntegerField(value=0, row=1, column=1)

        self.addButton(text="Compute Area", row=2, column=0, columnspan=2, command=self.computearea)
    def computearea(self):
        w = self.width.getNumber()
        l = self.length.getNumber()
        area = w * l
        self.areaField.setText(str(area))

def main():
    Rectangle().mainloop()
if __name__=="__main__":
    main()