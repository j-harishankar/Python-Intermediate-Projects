from breezypythongui import EasyFrame
class TextDemo(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self,title="text field demo")
        self.addLabel(text="Input",row=0,column=0)
        self.InputField = self.addTextField(text="enter the string",row=0,column=1)
        self.addLabel(text="Output",row=1,column=0)
        self.OutputField = self.addTextField(text=" ",row=1,column=1,state = "readonly")
        self.addButton(text="convert",row=2,column=0,columnspan=2,command=self.convert,)
    def convert(self):
        text = self.InputField.getText()
        result = text.upper()
        self.OutputField.setText(result)
TextDemo().mainloop()