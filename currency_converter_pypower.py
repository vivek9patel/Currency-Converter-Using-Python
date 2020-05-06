import tkinter as tk

# Create a GUI window 
root = tk.Tk() 

# create a global variables 
variable1 = tk.StringVar(root) 
variable2 = tk.StringVar(root) 

# initialise the variables 
variable1.set("currency") 
variable2.set("currency") 

def RealTimeCurrencyConversion(): 
    from forex_python.converter import CurrencyRates
    c=CurrencyRates()
    
    from_currency = variable1.get() 
    to_currency = variable2.get()
    
    new_amount = c.convert(from_currency,to_currency,float(Amount1_field.get()))
    # insert method inserting the 
    # value in the text entry box.
    new_value=str(new_amount)
    
    Amount2_field.insert(0, new_value )

def clear_all() : 
	Amount1_field.delete(0, tk.END) 
	Amount2_field.delete(0, tk.END)

if __name__ == "__main__" : 

	# Set the background colour of GUI window 
	root.configure(background = '#e6e5e5') 
	
	# Set the configuration of GUI window (WidthxHeight) 
	root.geometry("400x200") 
	
	# Create welcome to Real Time Currency Convertor label 
	headlabel = tk.Label(root, text = 'Pypower Currency Converter', bg= '#663300',fg='white') 

	# Create a "Amount :" label 
	label1 = tk.Label(root, text = "Amount", bg="orange",fg = "white",font=('arial', 10,'bold')) 
	
	# Create a "From Currency :" label 
	label2 = tk.Label(root, text = "From Currency", bg="orange",fg = "white",font=('arial', 10,'bold')) 
	
	# Create a "To Currency: " label 
	label3 = tk.Label(root, text = "To Currency", bg="orange",fg = "white",font=('arial', 10,'bold')) 

	# Create a "Converted Amount :" label 
	label4 = tk.Label(root, text = "Converted Amount",bg="orange",fg = "white",font=('arial', 10,'bold')) 

	# grid method is used for placing 
	# the widgets at respective positions 
	# in table like structure . 
	headlabel.grid(row = 0, column = 1) 
	label1.grid(row = 1, column = 0) 
	label2.grid(row = 2, column = 0) 
	label3.grid(row = 3, column = 0) 
	label4.grid(row = 5, column = 0) 
	
	# Create a text entry box 
	# for filling or typing the information. 
	Amount1_field = tk.Entry(root) 
	Amount2_field = tk.Entry(root) 
	
	# ipadx keyword argument set width of entry space. 
	Amount1_field.grid(row = 1, column = 1, ipadx ="25") 
	Amount2_field.grid(row = 5, column = 1, ipadx ="25") 

	# list of currency codes 
	CurrenyCode_list = ["INR", "USD", "CAD", "CNY", "DKK", "EUR"] 

	# create a drop down menu using OptionMenu function 
	# which takes window name, variable and choices as 
	# an argument. use * befor the name of the list, 
	# to unpack the values 
	FromCurrency_option = tk.OptionMenu(root, variable1, *CurrenyCode_list) 
	ToCurrency_option = tk.OptionMenu(root, variable2, *CurrenyCode_list) 
	
	FromCurrency_option.grid(row = 2, column = 1, ipadx = 10) 
	ToCurrency_option.grid(row = 3, column = 1, ipadx = 10) 
	
	# Create a Convert Button and attached 
	# with RealTimeCurrencyExchangeRate function 
	button1 = tk.Button(root, text = "Convert", bg = "Green", fg = "White",command=RealTimeCurrencyConversion) 
	
	button1.grid(row = 4, column = 1) 

	# Create a Clear Button and attached 
	# with delete function 
	button2 = tk.Button(root, text = "Clear", bg = "red",fg = "White", command = clear_all) 
	button2.grid(row = 6, column = 1) 
	
	# Start the GUI 
	root.mainloop()
