import pandas as pd
import customtkinter as CTK

from modules.gridSystem import gridSystem
from modules.frameManager import updateFrame
from modules.linkManager import etcDefs
from modules.CTkDefs import labelDef
import modules.CSVReader as CSVReader
import modules.CTkDefs as defs


class customFrameWindow :

    font = CSVReader.settingCSVReader("fontFamily")

    #編集するフレームを選択するフレーム
    @classmethod
    def selectFrameWindow(cls) :

        #ウィンドウの初期設定
        customizeFrameWindow = CTK.CTkToplevel()
        customizeFrameWindow.title("フレームの編集")
        customizeFrameWindow.geometry("500x300")
        customizeFrameWindow.geometry("+400+300")
        customizeFrameWindow.focus_set()
        customizeFrameWindow.wm_attributes("-topmost", True)

        gridSystem.resetGrid("row")
        gridSystem.resetGrid("column")

        selectCustomFrame = CTK.CTkFrame(master=customizeFrameWindow, border_width=0)
        selectCustomFrame.grid(row=0, column=0, sticky="nsew", padx=0, pady=0)

        #ウィジェットたち
        labelDef("label", selectCustomFrame, "フレームの編集", "w", 15, 20, 20)

        labelDef("label", selectCustomFrame, "編集するフレームのを選択してください", "w", 15, 40, 20)

        gridSystem.addGrid("row")

        #optionMenu
        optionMenu1 = CTK.CTkOptionMenu(selectCustomFrame, values=etcDefs.returnFrameNamelist(), font=(cls.font, 12))
        optionMenu1.grid(row=gridSystem.getGrid("row"), column=gridSystem.getGrid("column"), sticky="w", padx=60, pady=20)

        gridSystem.addGrid("row")

        #customButton
        button1 = CTK.CTkButton(selectCustomFrame, text="次へ進む", font=(cls.font, 12))
        button1.grid(row=gridSystem.getGrid("row"), column=gridSystem.getGrid("column"), padx=180,  pady=(20, 50), sticky="e")
        button1.bind("<Button-1>", lambda e:customFrameWindow.customFrame(root=customizeFrameWindow, optionMenu=optionMenu1))

        #closeButton
        button1 = CTK.CTkButton(selectCustomFrame, text="Close", font=(cls.font, 12))
        button1.grid(row=gridSystem.getGrid("row"), column=gridSystem.getGrid("column"), padx=20, pady=(20, 50), sticky="e")
        button1.bind("<Button-1>", lambda e:defs.close(customizeFrameWindow))

    #フレームを編集するフレーム
    @classmethod
    def customFrame(cls, root, optionMenu) :

        gridSystem.resetGrid("row")
        gridSystem.resetGrid("column")

        customizeFrame = CTK.CTkFrame(master=root, border_width=0)
        customizeFrame.grid(row=0, column=0, sticky="nsew", padx=0, pady=0)

        labelDef("label", customizeFrame, f"{updateFrame.setFrameName(entry=optionMenu)}の編集中", "w", 15, 20, 20)

        labelDef("label", customizeFrame, "新しいフレーム名を入力してください", "w", 15, 40, 10)

        gridSystem.addGrid("row")

        newFrameNameEntry = CTK.CTkEntry(master=customizeFrame, border_width=1, width=200, height=30, font=(cls.font, 15))
        newFrameNameEntry.grid(row=gridSystem.getGrid("row"), column=gridSystem.getGrid("column"), sticky="w", padx=60, pady=20)
        newFrameNameEntry.bind("<Button-1>", lambda e:newFrameNameEntry.configure(border_color="gray"))

        gridSystem.addGrid("row")

        #customButton
        button2 = CTK.CTkButton(customizeFrame, text="更新", font=(cls.font, 12))
        button2.grid(row=gridSystem.getGrid("row"), column=gridSystem.getGrid("column"), padx=180, pady=20, sticky="es")
        button2.bind("<Button-1>", lambda e:customFrameWindow.checkEmpty(root=root, entry=newFrameNameEntry, optionMenu=optionMenu))
        button2.bind("<Button-1>", lambda e:defs.reStart(root=root))

        #closeButton
        button3 = CTK.CTkButton(customizeFrame, text="Close", font=(cls.font, 12))
        button3.grid(row=gridSystem.getGrid("row"), column=gridSystem.getGrid("column"), padx=20, pady=20, sticky="es")
        button3.bind("<Button-1>", lambda e:defs.close(root=root))

    #エントリーなどが空白科の確認＋空白の時の処理
    @classmethod
    def checkEmpty(cls, root, entry, optionMenu) :

        if entry.get() == "" :

            customFrameWindow.alertToEntry(root=root, entry=entry)

        else :

            updateFrame.update_frame(entry=entry, optionMenu=optionMenu)

    #エントリーが空白の時、空白のエントリーをハイライト＋警告文の表示
    @classmethod
    def alertToEntry(cls, root, entry) :

        entry.configure(border_color="red")

        labelDef("label", root, f"次のエントリーに情報を入力してください : {entry}", "w", 12, 20, 20)

