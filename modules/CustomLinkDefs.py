import customtkinter as ctk
import webbrowser
import subprocess
import os
import sys
import pykakasi.kakasi as kks
import chardet

import modules.CTkDefs as defs
from modules.gridSystem import gridSystem
from modules.CSVReader import settingCSVReader as setting

#フォントサイズ・フォントファミリーの取得+変数への代入
font = setting("fontFamily")
lFontSize = setting("linkFontSize")
gFontSize = setting("groupFontSize")

#Applauncher.py用
#タイトルの追加を簡単に記述するための関数
def TitleContent(root, name, text) :

    name = ctk.CTkLabel(master=root, text=text, font=(font, gFontSize))
    name.grid(row=gridSystem.getGrid("row"), column=gridSystem.getGrid("column"), sticky="w", padx=20, pady=0)
    gridSystem.addGrid("row")


#リンク(Webサイト)を簡単に記述するための関数
def linkContent(root, name, text, url) :

    name = ctk.CTkLabel(root, text=text, font=(font, lFontSize), text_color="#0095d9")
    name.grid(row=gridSystem.getGrid("row"), column=gridSystem.getGrid("column"), padx=50, pady=0, sticky="w")
    name.bind("<Button-1>", lambda e:link_click(url))
    gridSystem.addGrid("row")


#アプリ(exeファイル)を簡単に記述するための関数
def AppContent(root, name, text, exeUrl) :

    name = ctk.CTkLabel(root, text=text, font=(font, lFontSize), text_color="#0095d9")
    name.grid(row=gridSystem.getGrid("row"), column=gridSystem.getGrid("column"), padx=50, pady=0, sticky="w")
    name.bind("<Button-1>", lambda e:app_click(exeUrl))
    gridSystem.addGrid("row")

#テキスト系のファイルを開くための関数
def TextContent(root, name, text, filepath) :

    name = ctk.CTkLabel(root, text=text, font=(font, lFontSize), text_color="#0095d9")
    name.grid(row=gridSystem.getGrid("row"), column=gridSystem.getGrid("column"), padx=50, pady=0, sticky="w")
    name.bind("<Button-1>", lambda e:text_click(filepath))
    gridSystem.addGrid("row")

#リンクがクリックされた時に実行される処理
def link_click(url) :

    webbrowser.open_new(url)

#テキストファイルのリンクがクリックされたときの処理関数
def text_click(filepath) :

    if os.path.exists(filepath) :

        subprocess.run(["start", filepath], shell=True)

    else :
        print("error")

#App版のリンクをクリックしたときに実行される処理
def app_click(exeUrl) :

    if os.path.isfile(exeUrl) == True and os.path.exists(exeUrl) == True :

        subprocess.Popen(exeUrl)

    else :
        errorWindow(exeUrl)


#アイコンの指定用関数
def temp_path(relative_path) :

    try:
        #アプリが起動されているパスの取得
        base_path = sys._MEIPASS
    except Exception:
        #アプリのパスに "." を追加
        base_path = os.path.abspath(".")

        #アプリのパス、 ".", "relative_path"(アイコンの画像) を結合
    return os.path.join(base_path, relative_path)

#アプリのパスが存在しないときに表示するウィンドウ
def errorWindow(exeURL) :

    #ウィンドウの設定
    errorWindow = ctk.CTkToplevel()
    errorWindow.title("エラーがが発生しました")
    errorWindow.geometry("950x350")
    errorWindow.geometry("+600+400")
    errorWindow.focus_force()
    errorWindow.attributes("-topmost", True)

    #label
    defs.labelDef("errorAlert", errorWindow, f"エラーが発生しました", "w", 20, 20, 20)

    defs.labelDef("errorAlert", errorWindow, f">> {exeURL} <<", "w", 15, 30, 20)

    defs.labelDef("errorAlert", errorWindow, f"上記のアプリが見つかりませんでした。", "w", 15, 30, 20)

    defs.labelDef("errorAlert", errorWindow, f"ファイルが存在しないか、違う場所にインストールされいる可能性があります。存在しているか確認してください。", "w", 15, 30, 20)

    closeButton = ctk.CTkButton(errorWindow, text="OK")
    closeButton.grid(row=gridSystem.getGrid("row"), column=gridSystem.getGrid("column"), sticky="e")
    closeButton.bind("<Button-1>", lambda e:defs.close(errorWindow))

#フレームの名前をローマ字に変換する関数
def convertKana(text) :

    aa = chardet.detect(text.encode())

    if aa["encoding"] in ['EUC-JP', 'Shift_JIS', 'ISO-2022-JP', 'UTF-8'] :

        a = kks()
        a.setMode("H", "a")
        a.setMode("K", "a")
        a.setMode("J", "a")
        conv = a.getConverter()

        return conv.do(text)

    else :
        return text