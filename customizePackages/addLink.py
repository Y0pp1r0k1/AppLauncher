import customtkinter as CTK
import pandas as pd

from modules.CTkDefs import labelDef as label
from modules.gridSystem import gridSystem
from modules.CSVReader import settingCSVReader as setting
from modules.linkManager import addLink
from modules.linkManager import etcDefs
import modules.CTkDefs as defs

def addLinkWindow() :

    #フォントfamilyの取得
    font = setting("fontFamily")

    gridSystem.resetGrid("row")
    gridSystem.resetGrid("column")

    #ウィンドウの初期設定
    addLinkWindow = CTK.CTkToplevel()
    addLinkWindow.title("リンクの追加")
    addLinkWindow.geometry("1000x500")
    addLinkWindow.geometry("+400+300")
    addLinkWindow.focus_force()
    addLinkWindow.attributes("-topmost", True)

    label("label", addLinkWindow, "リンクの追加", "w", 15, 20, 20)

    label("label", addLinkWindow, "表示するリンクの名前を入力してください", "w", 12, 40, 20)

    gridSystem.reduceGrid("row")
    gridSystem.addGrid("column")

    #リンクのテキスト
    entry1 = CTK.CTkEntry(addLinkWindow, border_width=0, placeholder_text="enter the link name (example : Youtube)", width=400, font=(font, 12))
    entry1.grid(row=gridSystem.getGrid("row"), column=gridSystem.getGrid("column"), sticky="w", padx=20, pady=20)
    gridSystem.addGrid("row")
    gridSystem.reduceGrid("column")

    label("label", addLinkWindow, "追加するリンクのパス, 又はURLを入力してください", "w", 12, 40, 20)

    gridSystem.reduceGrid("row")
    gridSystem.addGrid("column")

    entry2 = CTK.CTkEntry(addLinkWindow, border_width=0, placeholder_text="enter the link URL or app path (example : https://www.youtube.com)", width=400, font=(font, 12))
    entry2.grid(row=gridSystem.getGrid("row"), column=gridSystem.getGrid("column"), sticky="w", padx=20, pady=20)

    gridSystem.addGrid("column")

    button1 = CTK.CTkButton(addLinkWindow, text="参照", font=(font, 12), width=80)
    button1.grid(row=gridSystem.getGrid("row"), column=gridSystem.getGrid("column"), sticky="w", padx=0, pady=20)
    button1.bind("<Button-1>", lambda e:defs.delAttributes(addLinkWindow))
    button1.bind("<Button-1>", lambda e:etcDefs.open_file(root=addLinkWindow, entry=entry2))

    gridSystem.addGrid("row")
    gridSystem.reduceGrid("column")
    gridSystem.reduceGrid("column")

    label("label", addLinkWindow, "追加するフレームを選択してください", "w", 13, 40, 20)

    pulldownMenu = CTK.CTkOptionMenu(addLinkWindow, values=etcDefs.returnFrameNamelist(), font=(font, 12))
    pulldownMenu.grid(row=gridSystem.getGrid("row"), column=gridSystem.getGrid("column"), sticky="w", padx=60, pady=20)

    gridSystem.addGrid("row")
    gridSystem.addGrid("column")

    #addButton
    button2 = CTK.CTkButton(addLinkWindow, text="リンクを追加", font=(font, 12))
    button2.grid(row=gridSystem.getGrid("row"), column=gridSystem.getGrid("column"), sticky="e", padx=180, pady=20)
    button2.bind("<Button-1>", lambda e:addLink.add_to_csv(entry1=entry1, entry2=entry2, pulldownMenu=pulldownMenu))
    button2.bind("<Button-1>", lambda e:defs.reStart(addLinkWindow))

    #closeButton
    button3 = CTK.CTkButton(addLinkWindow, text="close", font=(font, 12))
    button3.grid(row=gridSystem.getGrid("row"), column=gridSystem.getGrid("column"), sticky="e", padx=20, pady=20)
    button3.bind("<Button-1>", lambda e:defs.close(addLinkWindow))