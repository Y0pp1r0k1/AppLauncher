import customtkinter as ctk
import CustomTkinterMessagebox as messageBox
import webbrowser
import subprocess
import os
import sys
import pandas as pd


import CTkDefs as defs

#main.py用
#タイトルの追加を簡単に記述するための関数
def TitleContent(root, title, text, row, column,) :

    title = ctk.CTkLabel(root, text=text, font=("游ゴシック", 13))
    title.grid(row=row, column=column, sticky=ctk.W, padx=20, pady=0)


#リンク(Web版など)を簡単に記述するための関数
def linkContent(root, name, text, row, column, padx, pady, url) : 

    name = ctk.CTkLabel(root, text=text, font=("游ゴシック", 11), text_color="#0095d9")
    name.grid(row=row, column=column, padx=padx, pady=pady, sticky=ctk.W)
    name.bind("<Button-1>", lambda e:link_click(url))


#アプリ(App版など)を簡単に記述するための関数
def AppContent(root, name, text, row, column, padx, pady, exeUrl) :

    name = ctk.CTkLabel(root, text=text, font=("游ゴシック", 11), text_color="#0095d9")
    name.grid(row=row, column=column, padx=padx, pady=pady, sticky=ctk.W)
    name.bind("<Button-1>", lambda e:app_click(exeUrl))


#リンクがクリックされた時に実行される処理
def link_click(url) :

    webbrowser.open_new(url)


#App版のリンクをクリックしたときに実行される処理
def app_click(exeUrl) :

    if os.path.isfile(exeUrl) and os.path.exists(exeUrl) == True :

        subprocess.Popen(exeUrl)

    else :

        errorWindow(exeUrl)



#アイコンの指定用関数
def temp_path(relative_path) :

    try:
        #アプリのパスの取得
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
    errorWindow.geometry("950x200")
    errorWindow.geometry("+600+400")
    errorWindow.focus_force()
    errorWindow.attributes("-topmost", True)


    #label
    defs.labelDef("errorAlert", errorWindow, f"エラーが発生しました   >>>   {exeURL}   <<<   が見つかりません。", 0, 0, ctk.W, "游ゴシック", 15, 20, 20)

    defs.labelDef("errorAlert", errorWindow, f"ファイルが存在しないか、違う場所にインストールされいる可能性があります。存在しているかご確認ください", 1, 0, ctk.W, "游ゴシック", 15, 20, 20)

    closeButton = ctk.CTkButton(errorWindow, text="OK")
    closeButton.grid(row=2, column=0, sticky=ctk.E)
    closeButton.bind("<Button-1>", lambda e:defs.close(errorWindow))



#row, column を省略して書くもの
#row
def autoRowSetter() :

    df = pd.read_csv("./data/data.csv", sep=",", index_col=0)
    row = df.loc["row_1", "row"]
    addRow = row + 1

    reCSV = df.replace({"row" : {row : addRow}})
    reCSV.to_csv("./data/data.csv")

    reDf = pd.read_csv("./data/data.csv", sep=",", index_col=0)
    newRow = reDf.loc["row_1", "row"]

    return newRow
    

#column
def autoColumnSetter() :

    df = pd.read_csv("./data/data.csv", sep=",", index_col=0)
    column = df.loc["row_1", "column"]
    addColumn = column + 1

    reCSV = df.replace({"column" : {column : addColumn}})
    reCSV.to_csv("./data/data.csv")

    reDf = pd.read_csv("./data/data.csv", sep=",", index_col=0)
    newColumn = reDf.loc["row_1", "column"]

    return newColumn


#data.csvのrow, column を―1に設定する関数
#row
def resetRow() :

    #初期値の設定
    default = -1

    #CSVのrowを読み込み
    df = pd.read_csv("./data/data.csv", sep=",", index_col=0)
    Row = df.loc["row_1", "row"]

    #書き換え+出力
    resetRow = df.replace({"row" : {Row : default}})
    resetRow.to_csv("./data/data.csv")


    #確認用
    #df = pd.read_csv("./data/data.csv", sep=",", index_col=0)
    #print(df.loc["row_1", "row"])
    

#column
def resetColumn() :

    #初期値の設定
    default = -1

    #CSVのcolumnを読み込み
    df = pd.read_csv("./data/data.csv", sep=",", index_col=0)
    Column = df.loc["row_1", "column"]


    #書き換え+出力
    resetRow = df.replace({"column" : {Column : default}})
    resetRow.to_csv("./data/data.csv")


    #確認用
    #df = pd.read_csv("./data/data.csv", sep=",", index_col=0)
    #print(df.loc["row_1", "column"])



