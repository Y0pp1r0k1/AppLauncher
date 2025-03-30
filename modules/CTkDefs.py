import customtkinter as ctk
import sys
import subprocess
import time

import modules.CSVReader as CSVReader
from modules.gridSystem import gridSystem

#フォントサイズ・フォントファミリーの取得+変数への代入
font = CSVReader.settingCSVReader("fontFamily")

lFontSize = CSVReader.settingCSVReader("linkFontSize")

#CustomTkinterを書きやすくするための関数たち

#Label
def labelDef(name, root, text, sticky, fontSize, padx, pady) :

    name = ctk.CTkLabel(root, text=text, font=(font, fontSize))
    name.grid(row=gridSystem.getGrid("row"), column=gridSystem.getGrid("column"), sticky=sticky, padx=padx, pady=pady)
    gridSystem.addGrid("row")

#Button
def buttonDef(name, root, text, row, column, padx, pady, Def) :

    name = ctk.CTkButton(root, text=text)
    name.grid(row=row, column=column, padx=padx, pady=pady)
    name.bind("<Button-1>", lambda e:Def)

#Entry
def entryDef(name, root, width, row, column, padx, pady) :

    name = ctk.CTkEntry(root, width=width, border_width=0)
    name.grid(row=row, column=column, padx=padx, pady=pady)

#close
def close(root) :

    root.destroy()

#アプリの再起動関数
def reStart(root) :

    name = ctk.CTkToplevel()
    name.geometry("520x300")
    name.geometry("+600+400")
    name.title("お知らせ")
    name.focus_set()
    name.wm_attributes("-topmost", True)

    gridSystem.resetGrid("row")
    gridSystem.resetGrid("column")

    labelDef("label", name, "データの更新を確認しました。", "w", 15, 30, 20)
    labelDef("label", name, "更新のため、アプリを再起動してください。", "w", 15, 30, 20)

    labelDef("label", name, "編集を続ける場合は、続行ボタンを押してください。", "w", 15, 30, 20)

    button = ctk.CTkButton(name, text="アプリを終了 ", font=(font, 12))
    button.grid(row=gridSystem.getGrid("row"), column=gridSystem.getGrid("column"), padx=200, pady=30, sticky="e")
    button.bind(delAttributes(root=root))
    button.bind("<Button-1>", lambda e:sys.exit())

    button = ctk.CTkButton(name, text="続行 ", font=(font, 12))
    button.grid(row=gridSystem.getGrid("row"), column=gridSystem.getGrid("column"), padx=50, pady=30, sticky="e")
    button.bind(delAttributes(root=root))
    button.bind("<Button-1>", lambda e:close(name))

def delAttributes(root) :

    root.wm_attributes("-topmost", False)




