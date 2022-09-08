import PySimpleGUI as sg
import os
import subprocess

sg.theme("SystemDefault")

sg.set_options(font=("meiryo",8),use_ttk_buttons=True,dpi_awareness=True)

lay_img = sg.Tab("画像",[
    [sg.Text("検出する画像フォルダを選択"),sg.InputText(key="img_in",size=(30,1)),sg.FolderBrowse("選択")],
    [sg.Text("学習データを選択(.ptファイル)"),sg.InputText(key="img_pt",size=(30,1)),sg.FileBrowse("選択")],
    [sg.Text("許容値 [--conf]"),sg.InputText(default_text=0.4, size=(10,1),key="img_conf")],
    [sg.Button("START",key="START_IMG")],
])

lay_cap = sg.Tab("動画",[
    [sg.Text("")]
])

layout = [[sg.TabGroup([[lay_img,lay_cap]])]]

window = sg.Window("",layout=layout)
while True:
    event, value = window.read()
    
    if event == None:
        break

    if event == "START_IMG":
        subprocess.run("python detect.py --source {0} --weights {1} --conf {2}".format(value["img_in"],value["img_pt"],value["img_conf"]),shell=True)
        