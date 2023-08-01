def Morning() :
    """
    OPERATORS
    
    Arithmatic operators
    -Division /
    -Whole number Division //
    -Subtraction -
    -Modulus %
    -Exponemtial **
    -Multiplicatino *
    
    Comparison operators
    -Equal to ==
    -Not equal to != or !==
    -Geater than >
    -less than <
    -Greater than or equal to >=
    -Less than or equal to <=
    
    Logical operators
    -and
    -or
    -not
    
    Assignment operators
    -Assignment =
    -Add and assign +=
    -Subtract and assign -=
    
    Membership operators
    -in => checks if value exists in a sequence
    -not in => checks if value does not exist in a sequence
    
    Identity operators
    -is => checks similarity
    -is not => checks for difference in values
    
    """
    #Arithmatic examples
    a = 5
    b= 10
    c=3
    print(a+b)
    print(a-b)
    print(b/c)
    print(b//c)
    print(b%c)
    print(a*c)
    print(c**c)
    
     #Comparison examples
    print(a>b) #false
    print(a<b) #true
    print(a>=c) #true
    print(a<=c) #false
    print(a==b) #false
    print(a!=b) #true
    
    #Logical operators
    k = True
    l = False
    
    print(k and k) #true
    print(k and l) #false
    print(not k) #false
    print(k or l) #true
    
    #Assignment operators
    
    #subtract and assign
    m = 34
    m -= 4
    print(m) # 30
    
    #add and assign
    o = 34
    o += 6
    print(o) # 40
    
    #integer divide and assign
    p = 32
    p //= 2
    print(p) # 16
    
    #integer divide and assign
    p /= 2
    print(p) # 8.0
    
    #modulus and assign
    q = 4
    q %= 3
    print(q) # 1
    
    #Membership operators
    phones =["Samsung","Iphone","Blackberry","Nokia"]
    print("Nokia" in phones) #true
    print("Samsung" in phones) #true
    print("OLG" in phones) #false
    print("Oppo" in phones) #false
    
    #Identity operators
    f = "boy"
    g = "girl"
    
    print( f is g) #false
    print( f is not g) #true
    
    #Bitwise Operators => perform operations on individual bits of binary numbers
    # and &
    # or ||
    #xor ^
    #nont ~
    #leftshift <<
    #rightshift >>
    
    
    
    #ASSIGNMENT BUILT A SIMPLE FUNCTIONING CALCULATOR WITH A GUI INTERFACE USING TKINTER (+,-,*,/)
    #Title > your name   
    
     
    import tkinter as tk
    #Defining click handlers
    def tap_button(number):
        current = entry.get()
        entry.delete(0, tk.END)
        entry.insert(tk.END, current + str(number))

    def clear_button():
        entry.delete(0, tk.END)

    def equals_button():
        expression = entry.get()
        try:
            result = eval(expression)
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except Exception:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Arithmetic error")
            
    #Supplying title to my program
            
    window = tk.Tk()
    window.title("Sendi Joseph")

    #Creating display window

    entry = tk.Entry(window, width=35, border= 4)
    entry.grid(row=0, column=0, columnspan=4)

    #Creating buttons

    button_add = tk.Button(window,border= 3, background="coral", text="+", padx=19, pady=20, command=lambda: tap_button("+"))
    button_subtract = tk.Button(window,border= 3, background="coral", text="-", padx=20, pady=20, command=lambda: tap_button("-"))
    button_multiply = tk.Button(window,border= 3, background="coral", text="*", padx=20, pady=20, command=lambda: tap_button("*"))
    button_divide = tk.Button(window,border= 3, background="coral", text="/", padx=20, pady=20, command=lambda: tap_button("/"))
    clear_button = tk.Button(window,border= 3, background="red", text="C", padx=20, pady=20, command=clear_button)
    equals_button = tk.Button(window,border= 3, background="green", text="=", padx=20, pady=20, command=equals_button)

    button_1 = tk.Button(window,border= 3, background="purple", text="1", padx=20, pady=20, command=lambda: tap_button(1))
    button_2 = tk.Button(window,border= 3, background="purple",text="2", padx=20, pady=20, command=lambda: tap_button(2))
    button_3 = tk.Button(window,border= 3, background="purple",text="3", padx=20, pady=20, command=lambda: tap_button(3))
    button_4 = tk.Button(window,border= 3, background="purple",text="4", padx=20, pady=20, command=lambda: tap_button(4))
    button_5 = tk.Button(window,border= 3, background="purple",text="5", padx=20, pady=20, command=lambda: tap_button(5))
    button_6 = tk.Button(window,border= 3, background="purple",text="6", padx=20, pady=20, command=lambda: tap_button(6))
    button_7 = tk.Button(window,border= 3, background="purple",text="7", padx=20, pady=20, command=lambda: tap_button(7))
    button_8 = tk.Button(window,border= 3, background="purple",text="8", padx=20, pady=20, command=lambda: tap_button(8))
    button_9 = tk.Button(window,border= 3, background="purple",text="9", padx=20, pady=20, command=lambda: tap_button(9))
    button_0 = tk.Button(window,border= 3, background="purple",text="0", padx=20, pady=20, command=lambda: tap_button(0))

    #Positioning

    button_1.grid(row=1, column=0)
    button_2.grid(row=1, column=1)
    button_3.grid(row=1, column=2)
    button_4.grid(row=2, column=0)
    button_5.grid(row=2, column=1)
    button_6.grid(row=2, column=2)
    button_7.grid(row=3, column=0)
    button_8.grid(row=3, column=1)
    button_9.grid(row=3, column=2)
    button_0.grid(row=4, column=1)
    button_add.grid(row=1, column=3)
    button_subtract.grid(row=2, column=3)
    button_multiply.grid(row=3, column=3)
    button_divide.grid(row=4, column=3)
    clear_button.grid(row=4, column=0)
    equals_button.grid(row=4, column=2)

    # Starting window loop
    window.mainloop()

Morning()

def Afternoon() :
    pass

