import customtkinter as CTK

from modules.CTkDefs import labelDef as label
from modules.gridSystem import gridSystem
from modules.CSVReader import settingCSVReader as setting
from customizePackages.addLink import addLinkWindow
from customizePackages.deleteLink import deleteLinkWindow
from customizePackages.customLink import customizeLink
from customizePackages.addFrame import addFrameWindow
from customizePackages.deleteFrame import deleteFrameWindow
from customizePackages.customFrame import customFrameWindow
import modules.CTkDefs as defs

def customWindow() :

    font = setting("fontFamily")

    gridSystem.resetGrid("row")
    gridSystem.resetGrid("column")

    customWindow = CTK.CTkToplevel()
    customWindow.title("リンクのカスタム")
    customWindow.geometry("600x400")
    customWindow.geometry("+850+400")
    customWindow.focus_set()
    customWindow.wm_attributes("-topmost", True)

    label("label", customWindow, "リンク・フレームのカスタマイズ", "w", 15, 30, 20)

    button1 = CTK.CTkButton(customWindow, text="リンクを作成", font=(font, 12))
    button1.grid(row=gridSystem.getGrid("row"), column=gridSystem.getGrid("column"), padx=50, pady=30)
    button1.bind("<Button-1>", lambda e:addLinkWindow())
    button1.bind("<Button-1>", lambda e:defs.delAttributes(customWindow))

    gridSystem.addGrid("row")

    button2 = CTK.CTkButton(customWindow, text="リンクを削除", font=(font, 12))
    button2.grid(row=gridSystem.getGrid("row"), column=gridSystem.getGrid("column"), padx=50, pady=30)
    button2.bind("<Button-1>", lambda e:deleteLinkWindow())
    button2.bind("<Button-1>", lambda e:defs.delAttributes(customWindow))

    gridSystem.addGrid("row")

    button3 = CTK.CTkButton(customWindow, text="リンクの編集",font=(font, 12))
    button3.grid(row=gridSystem.getGrid("row"), column=gridSystem.getGrid("column"), padx=50, pady=30)
    button3.bind("<Button-1>", lambda e:customizeLink.selectCustomLinkWindow())
    button3.bind("<Button-1>", lambda e:defs.delAttributes(customWindow))

    gridSystem.resetGrid("row")
    gridSystem.addGrid("column")
    gridSystem.addGrid("row")

    button4 = CTK.CTkButton(customWindow, text="フレームの作成", font=(font, 12))
    button4.grid(row=gridSystem.getGrid("row"), column=gridSystem.getGrid("column"), padx=80, pady=30, sticky="w")
    button4.bind("<Button-1>", lambda e:addFrameWindow())
    button4.bind("<Button-1>", lambda e:defs.delAttributes(customWindow))

    gridSystem.addGrid("row")

    button5 = CTK.CTkButton(customWindow, text="フレームの削除", font=(font, 12))
    button5.grid(row=gridSystem.getGrid("row"), column=gridSystem.getGrid("column"), padx=80, pady=30, sticky="w")
    button5.bind("<Button-1>", lambda e:deleteFrameWindow())
    button5.bind("<Button-1>", lambda e:defs.delAttributes(customWindow))


    gridSystem.addGrid("row")

    button6 = CTK.CTkButton(customWindow, text="フレームの編集", font=(font, 12))
    button6.grid(row=gridSystem.getGrid("row"), column=gridSystem.getGrid("column"), padx=80, pady=30, sticky="e")
    button6.bind("<Button-1>", lambda e:customFrameWindow.selectFrameWindow())
    button6.bind("<Button-1>", lambda e:defs.delAttributes(customWindow))

    gridSystem.addGrid("row")

    #closeButton
    button7 = CTK.CTkButton(customWindow, text="close", font=(font, 12))
    button7.grid(row=gridSystem.getGrid("row"), column=gridSystem.getGrid("column"), padx=80, pady=30, sticky="e")
    button7.bind("<Button-1>", lambda e:defs.close(customWindow))
