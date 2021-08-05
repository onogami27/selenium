import PySimpleGUI as sg
import sqlite3


conn = sqlite3.connect("img.db")
c = conn.cursor()
c.execute("select file_name from img_t")
table_name = c.fetchall()


lay = [
    [sg.Table(values=table_name)]
]

window = sg.Window("test", lay,size=(500,500))

while True:

    event, values = window.read()
    if event == None:
        break