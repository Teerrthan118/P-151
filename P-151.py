from tkinter import *
import random

root = Tk()

root.title("Display the Country and City`")
root.geometry("600x600")

month_tuple =  Label(root, font=("courier, 15"), fg="green", bg="yellow", padx ="10", pady="5")
profit_tuple =  Label(root, font=("courier, 15"), fg="green", bg="yellow", padx ="10", pady="5")
country_list = []
city_list = []



label_max_month =  Label(root, font=("courier, 15"), fg="green", bg="yellow", padx ="10", pady="5")

label_min_month =  Label(root, font=("courier, 15"), fg="green", bg="yellow", padx ="10", pady="5")

months = ('January',"February","March","April","May","June","July","August","September","October","November","December")
profits = (20000,45000,78000,97000,12000,456000,65000,54000,10000,30000,70000,90000)

month_tuple['text'] = "Months: " + str(months)
profit_tuple['text'] = "Profit: " + str(profits)

def findMax():
  max_profits = max(profits)
  index_max = profits.index(max_profits)
  month_max = months[index_max]
  label_max_month['text'] = str(month_max)
  
def findMin():
  min_profits = min(profits)
  index_min = profits.index(min_profits)
  month_min = months[index_min]
  label_min_month['text'] = str(month_min)

btn =  Button(root, text= "Display Country And City Name", command=findMax , font=("courier, 15"), bg="orange", padx ="15", pady="25")
btn2 =  Button(root, text= "Display Country And City Name Randomly", command=findMin , font=("courier, 15"), bg="orange", padx ="15", pady="25")


month_tuple.place(relx=0.5, rely=0.2, anchor=CENTER)
profit_tuple.place(relx=0.5, rely=0.3, anchor=CENTER)
btn.place(relx=0.5, rely=0.4, anchor=CENTER)
label_max_month.place(relx=0.5, rely=0.8, anchor=CENTER)
btn2.place(relx=0.5, rely=0.7, anchor=CENTER)
label_min_month.place(relx=0.5, rely=0.9, anchor=CENTER)
root.mainloop()
