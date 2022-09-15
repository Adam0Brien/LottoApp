import os
from tkinter import *
from xml.etree import ElementTree

#import requests

# setup
window = Tk()  # instance of a window
window.geometry("400x400")
window.title("F1 Requests")
window.config(background="grey")
window.resizable(False, False)

fileName = 'f1Data.xml'
fullFile = os.path.abspath(os.path.join('data', fileName))
print(fullFile)

dom = ElementTree.parse(fullFile)
print(dom)

table = dom.findall('./Race')
print(table)


# functions#
def pullInfo():
    # if yearBox.get == range(1970, 2022) and roundBox.get == range(0, 11):  # work on this
    year = str(yearBox.get())
    round = str(roundBox.get())

    print("Your details were correct good job")

 #   r = requests.get("http://ergast.com/api/f1/" + year + "/" + round)
    # r = requests.get("http://ergast.com/api/f1/2021/1") # test
    f = open('data/f1Data.xml', 'a')

    f.truncate(0)
   # f.write(r.text)

    textField.delete(1.0, "end")
    # textField.insert(1.0,fullFile)


def displayInfo():
    for c in table:
        # date = c.find('Date').text
        print('\n')
        print(c.text)
        RaceName = c.find('RaceName')
        CircuitName = c.find('Circuit/CircuitName')
        Country = c.find('Circuit/Location/Country')
        Date = c.find('Date')

        textField.insert(1.0, RaceName.text + '\n')
        textField.insert(2.0, CircuitName.text + '\n')
        textField.insert(3.0, Country.text + '\n')
        textField.insert(4.0, Date.text)

def submit():
    pullInfo()
    displayInfo()


def deleteAll():
    yearBox.delete(0, END)
    roundBox.delete(0, END)
    textField.delete(1.0, "end")


# ============== tkinter ==============#

yearLabel = Label(window, text="Enter a year"
                  , fg='green'
                  , bg='black'
                  , relief=RAISED,
                  bd=10
                  , padx=10
                  , pady=10
                  )

roundLabel = Label(window, text="Enter a round"
                   , fg='green'
                   , bg='black'
                   , relief=RAISED,
                   bd=10
                   , padx=10
                   , pady=10
                   )

yearBox = Entry(window, font='italics'
                , fg='green'
                , bg='black'
                , relief=RAISED
                , bd=10
                )

roundBox = Entry(window, font='italics'
                 , fg='green'
                 , bg='black'
                 , relief=RAISED
                 , bd=10
                 )

yearBox.insert(0, '')  # default text

submitButton = Button(window, text="Enter",
                      command=submit,
                      fg='green',
                      bg='black',
                      relief=RAISED,
                      activebackground='black',
                      activeforeground='green',
                      bd=10)

deleteButton = Button(window, text="Delete TextFields",
                      command=deleteAll,
                      fg='green',
                      bg='black',
                      activebackground='black',
                      activeforeground='green',
                      relief=RAISED,
                      bd=10
                      )

textField = Text(window,
                 height=200,
                 width=100,
                 fg='green',
                 bg='black',
                 bd=10
                 )

yearLabel.pack()
yearBox.pack()
roundLabel.pack()
roundBox.pack()
textField.place(x=0, y=250)
submitButton.place(x=100, y=200)
deleteButton.place(x=190, y=200)

# ============== tkinter end ==============#


###original code###

#####################
# year = input("What year?: ")
# round = input("What round?: ")
# r = requests.get("http://ergast.com/api/f1/"+year+"/"+round)
# f = open('f1Data.xml', 'a')
#
# f.truncate(0)
# f.write(r.text)
#
# x = etree.parse('f1Data.xml')
# print(etree.tostring(x, pretty_print=True))
#########################


window.mainloop()  # makes the window and listen for events

if __name__ == '__main__':
    print()