from tkinter import * 
class Calculator:

    def _init_(self, master):
        
        self.master = master
        master.title("My Calculator")

        self.equation = Entry(master, width=64, borderwidth=10)
        self.equation.grid(row=0, column=0, columnspan=4, padx=20, pady=20)
        self.createButton()


    def createButton(self):
        
        b0 = self.addButton(0)
        b1 = self.addButton(1)
        b2 = self.addButton(2)
        b3 = self.addButton(3)
        b4 = self.addButton(4)
        b5 = self.addButton(5)
        b6 = self.addButton(6)
        b7 = self.addButton(7)
        b8 = self.addButton(8)
        b9 = self.addButton(9)
        b_add = self.addButton("+")
        b_sub = self.addButton("-")
        b_mult = self.addButton("*")
        b_div = self.addButton("/")
        b_clear = self.addButton("c")
        b_equal = self.addButton("=")
    
        row1 = [b1, b2, b3, b_clear]
        row2 = [b4, b5, b6, b_add]
        row3 = [b7, b8, b9, b_sub]
        row4 = [b0, b_div, b_mult, b_equal]

        r = 1
        for row in [row1, row2, row3, row4]:
            c = 0
            for buttn in row:
                buttn.grid(row=r, column=c, columnspan=1)
                c += 1
            r += 1


    def addButton(self, value):
            return Button(
            self.master,
            text=value,
            width=9,
            command=lambda: self.clickButton(str(value)),
        )


    def clickButton(self, value):

        current_equation = str(self.equation.get())

        if value == "c":
            self.equation.delete(-1, END)

        elif value == "=":
            answer = str(eval(current_equation))
            self.equation.delete(-1, END)
            self.equation.insert(0, answer)

        else:
            self.equation.delete(0, END)
            self.equation.insert(-1, current_equation + value)

if __name__ == "_main_":

    root = Tk()
    root.configure(background="red")
    my_gui = Calculator(root)
    root.mainloop()
