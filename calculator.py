import simplegui

Store = 7
Operand = 6

#event handler

def output():
    return Store 
    return Operand
    
def swap():
    global Store, Operand
    Store, Operand = Operand, Store
    output()
    
def add():
    global Store
    Store = Store + Operand
    output()
    
def subtract():
    global Store 
    Store = Store - Operand
    output() 
    
def mult():
    global Store 
    Store = Store * Operand 
    output()
    
def enter_store(t1):
    global Store
    Store = int(t1)
    output()
    
def enter_operand(t2):
    global Operand 
    Operand = int(t2)
    output()
    
def draw(canvas):
    canvas.draw_text("store =" + str(Store), (50,50), 42, "Aqua", "monospace")
    canvas.draw_text("operand =" + str(Operand), (50,100), 42, "Teal", "monospace")
    
                     
tikka = simplegui.create_frame("calculator",350,350)    

#registereventhandler
tikka.add_input("Store", enter_store, 100)
tikka.add_input("Operand", enter_operand, 100)
tikka.add_button("Print", output, 100)
tikka.add_button("Swap", swap, 100)
tikka.add_button("Add", add, 100)
tikka.add_button("subract", subtract, 100)
tikka.add_button("mult", mult, 100)
tikka.set_draw_handler(draw)

tikka.start()
    

    
