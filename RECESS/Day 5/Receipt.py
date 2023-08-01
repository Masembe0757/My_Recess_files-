import tkinter as tk
Landlord = input("Enter your name:")
Tenant = input("Enter tenant's name:")
amount = input("Enter amount payed:")
balance = input("Enter standing balance:")


window = tk.Tk()
window.title("Sendi's Rentals")
window.geometry("350x400+10+20")
lbl = tk.Label(window,
               text ="Payment Receipt",
               fg= "green",
               font=("Helvetica",15)
               ).place(x=112, y=20)
lbl = tk.Label(window,
               text ="Dear {} , this receipt serves as an \n acknowledgement  for your  payment of {} shillings \n which leaves  you with a balance  of {} \n shillings. We really appreciate your \n co-operation and  for you chosing to reside at \n our rentals .  Yours Landlord {}".format(Tenant,amount,balance,Landlord) ,
               fg= "grey",
               font=("Helvetica",11),
               justify="center"
               ).place(x=10, y=50)
window.mainloop()
