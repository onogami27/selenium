import PySimpleGUI as sg
import sqlite3
import test_img

conn = sqlite3.connect("img.db")
c = conn.cursor()
c.execute("select file_name from img_t")
table_name = c.fetchall()


lay = [
    [sg.Table(values=table_name, key="table")],
    [sg.Button("追加する", key="insert"),sg.Button("書き込み", key="white"),sg.Button("削除", key="del")]
]

window = sg.Window("test", lay,size=(500,300))

while True:

    event, values = window.read()
    if event in (None,"",[],"Cancel"):
        break
    
    try:
        if event == "insert":
            test_img.file_insert()
            c.execute("select file_name from img_t")
            table_name = c.fetchall()
            window["table"].update(values=table_name)     
    except:
        continue
    
    try:
        if event == "white":
            get_table = window["table"].get()
            get_value = values["table"]
            file_name = get_table[get_value[0]][0]
            test_img.real(file_name,get_value[0])
    except:
        continue

    try:
        if event == "del":
            get_table = window["table"].get()
            get_value = values["table"]
            file_name = get_table[get_value[0]][0]
            test_img.delete(file_name)
            c.execute("select file_name from img_t")
            table_name = c.fetchall()
            window["table"].update(values=table_name)   

    except:
        continue