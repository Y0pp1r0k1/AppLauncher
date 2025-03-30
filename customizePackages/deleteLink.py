import customtkinter as CTK
import pandas as pd

from modules.CTkDefs import labelDef as label
from modules.gridSystem import gridSystem
from modules.CSVReader import settingCSVReader as setting
from modules.linkManager import etcDefs
from modules.linkManager import deleteLink
import modules.CTkDefs as defs

def deleteLinkWindow() :

    font = setting("fontFamily")

    gridSystem.resetGrid("row")
    gridSystem.resetGrid("column")

    deleteLinkWindow = CTK.CTkToplevel()
    deleteLinkWindow.title("リンクの削除")
    deleteLinkWindow.geometry("850x450")
    deleteLinkWindow.geometry("+400+300")
    deleteLinkWindow.focus_force()
    deleteLinkWindow.attributes("-topmost", True)


    label("label", deleteLinkWindow, "リンクの削除", "w", 15, 20, 20)

    label("label", deleteLinkWindow, "削除するリンクのフレームを選択してください", "w", 12, 40, 20)

    #OptionMenu
    pulldownMenu1 = CTK.CTkOptionMenu(deleteLinkWindow, values=etcDefs.returnFrameNamelist(), font=(font, 12))
    pulldownMenu1.grid(row=gridSystem.getGrid("row"), column=gridSystem.getGrid("column"), sticky="w", padx=60, pady=20)
    gridSystem.addGrid("column")

    #chooseButton
    button1 = CTK.CTkButton(deleteLinkWindow, text="選択", font=(font, 12), width=60)
    button1.grid(row=gridSystem.getGrid("row"), column=gridSystem.getGrid("column"), sticky="w", padx=60, pady=20)

    gridSystem.addGrid("row")
    gridSystem.reduceGrid("column")

    label("label", deleteLinkWindow, "削除するリンクを選択してください", "w", 12, 40, 20)

    #select link OptionMenu
    pulldownMenu2 = CTK.CTkOptionMenu(deleteLinkWindow, values=["select the frame"], state="disabled", font=(font, 12))
    pulldownMenu2.grid(row=gridSystem.getGrid("row"), column=gridSystem.getGrid("column"), sticky="w", padx=60, pady=20)

    button1.bind("<Button-1>", lambda e:returnLinkValues(pulldownMenu1, pulldownMenu2))

    gridSystem.addGrid("row")
    gridSystem.addGrid("column")

    #deleteButton
    button2 = CTK.CTkButton(deleteLinkWindow, text="リンクを削除", font=(font, 12))
    button2.grid(row=gridSystem.getGrid("row"), column=gridSystem.getGrid("column"), sticky="e", padx=180, pady=20)
    button2.bind("<Button-1>", lambda e:deleteLink.delete_from_csv(pulldownMenu2))
    button2.bind("<Button-1>", lambda e:defs.reStart(deleteLinkWindow))

    #closeButton
    button3 = CTK.CTkButton(deleteLinkWindow, text="close", font=(font, 12))
    button3.grid(row=gridSystem.getGrid("row"), column=gridSystem.getGrid("column"), sticky="e", padx=20, pady=20)
    button3.bind("<Button-1>", lambda e:defs.close(deleteLinkWindow))

    gridSystem.reduceGrid("row")
    gridSystem.reduceGrid("column")

    #選択されたフレームに存在するリンクをリンクのオプションメニューに追加する関数
    def returnLinkValues(frameOptionMenu, linkOptionMenu) :

        #選択されたフレームにあるリンクの名前を取得
        values = etcDefs.returnOptionMenuValues(frameOptionMenu)

        #try文でオプションメニューのバリューを更新
        try :
            linkOptionMenu.configure(state="normal", values=values)
            linkOptionMenu.set(values[0])
        except IndexError : #リンクが存在しない場合、選択不可にし、分かりやすいように警告
            values = ["リンクが存在しません"] + values
            linkOptionMenu.configure(state="disabled", values=values)
            linkOptionMenu.set(values[0])
