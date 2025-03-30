import pandas as pd
import customtkinter as CTK

from modules.gridSystem import gridSystem
from modules.frameManager import makeFrame
from modules.CTkDefs import labelDef
import modules.CSVReader as CSVReader
import modules.CTkDefs as defs

#フレームを追加するウィンドウ
def addFrameWindow() :

    #フォントfamilyの取得
    font = CSVReader.settingCSVReader("fontFamily")

    gridSystem.resetGrid("row")
    gridSystem.resetGrid("column")

    #ウィンドウの初期設定
    addFrameWindow = CTK.CTkToplevel()
    addFrameWindow.title("フレームの追加")
    addFrameWindow.geometry("500x300")
    addFrameWindow.geometry("+600+400")
    addFrameWindow.focus_force()
    addFrameWindow.attributes("-topmost", True)


    #ウィジェットたち
    labelDef("label", addFrameWindow, "フレームの追加", "w", 15, 20, 20)

    labelDef("label", addFrameWindow, "追加するフレームの名前を入力してください", "w", 15, 40, 20)

    entry1 = CTK.CTkEntry(addFrameWindow, border_width=0, width=200, height=30, placeholder_text="Enter the new frame name", font=(font, 13))
    entry1.grid(row=gridSystem.getGrid("row"), column=gridSystem.getGrid("column"), padx=60, pady=20, sticky="w")

    gridSystem.addGrid("row")

    #addButton
    button1 = CTK.CTkButton(addFrameWindow, text="追加", font=(font, 12), width=80)
    button1.grid(row=gridSystem.getGrid("row"), column=gridSystem.getGrid("column"), padx=(0, 120), pady=20, sticky="e")
    button1.bind("<Button-1>", lambda e:makeFrame.add_frame(frameNameEntry=entry1))
    button1.bind("<Button-1>", lambda e:defs.reStart(addFrameWindow))

    #closeButton
    button3 = CTK.CTkButton(addFrameWindow, text="Close", font=(font, 12), width=80)
    button3.grid(row=gridSystem.getGrid("row"), column=gridSystem.getGrid("column"), padx=(0, 20), pady=20, sticky="e")
    button3.bind("<Button-1>", lambda e:defs.close(addFrameWindow))
