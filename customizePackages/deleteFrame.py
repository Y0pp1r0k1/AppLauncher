import pandas as pd
import customtkinter as CTK

from modules.gridSystem import gridSystem
from modules.frameManager import delFrame
from modules.linkManager import etcDefs
from modules.CTkDefs import labelDef
import modules.CSVReader as CSVReader
import modules.CTkDefs as defs

#フレームを削除するウィンドウ
def deleteFrameWindow() :

    #フォントfamilyの取得
    font = CSVReader.settingCSVReader("fontFamily")

    gridSystem.resetGrid("row")
    gridSystem.resetGrid("column")

    #ウィンドウの初期設定
    delFrameWindow = CTK.CTkToplevel()
    delFrameWindow.title("フレームの削除")
    delFrameWindow.geometry("500x300")
    delFrameWindow.geometry("+400+300")
    delFrameWindow.focus_force()
    delFrameWindow.attributes("-topmost", True)


    #ウィジェットたち
    labelDef("label", delFrameWindow, "フレームの削除", "w", 15, 20, 20)

    labelDef("label", delFrameWindow, "削除するフレームを選択してください", "w", 15, 40, 20)

    gridSystem.addGrid("row")

    #OptionMenu
    optionMenu1 = CTK.CTkOptionMenu(delFrameWindow, values=etcDefs.returnFrameNamelist(), height=30,  font=(font, 15))
    optionMenu1.grid(row=gridSystem.getGrid("row"), column=gridSystem.getGrid("column"), padx=60, pady=20, sticky="w")

    gridSystem.addGrid("row")

    #deleteButton
    button1 = CTK.CTkButton(delFrameWindow, text="削除", font=(font, 12))
    button1.grid(row=gridSystem.getGrid("row"), column=gridSystem.getGrid("column"), padx=180, pady=20, sticky="e")
    button1.bind("<Button-1>", lambda e:delFrame.delete_frame(optionMenu=optionMenu1))
    button1.bind("<Button-1>", lambda e:defs.reStart(root=delFrameWindow))

    #closeButton
    button1 = CTK.CTkButton(delFrameWindow, text="Close", font=(font, 12))
    button1.grid(row=gridSystem.getGrid("row"), column=gridSystem.getGrid("column"), padx=20, pady=20, sticky="e")
    button1.bind("<Button-1>", lambda e:defs.close(delFrameWindow))