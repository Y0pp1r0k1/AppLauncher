import pandas as pd
import os
import sys
import shutil
import customtkinter as ctk

from typing import Literal

#CSVファイルのパスを場合によって違うパスを返す関数
def return_true_csv_path(type : Literal["setting", "frame", "link", "json"]) :

    #タイプの識別
    if type == "setting" :
        csv_file_name = "setting.csv"
    elif type == "frame" :
        csv_file_name = "frame.csv"
    elif type == "link" :
        csv_file_name = "link.csv"
    elif type == "json" :
        csv_file_name = "custom.json"
    else :
        print(f"Type error : doesn't exist {type}")

    #実行環境の識別
    if hasattr(sys, '_MEIPASS'):    #ビルド環境の場合

        user_data_dir = os.path.join(os.environ["APPDATA"], "AppLauncher", "data")  #ユーザーのAppDataフォルダ
        os.makedirs(user_data_dir, exist_ok=True)                                   #フォルダがなければ作成

        #MEIPASS から AppData に CSV をコピー（初回のみ）
        original_csv_path = os.path.join(sys._MEIPASS, "data", csv_file_name)
        user_csv_path = os.path.join(user_data_dir, csv_file_name)

        if not os.path.exists(user_csv_path):  #ファイルが存在しなければコピー
            shutil.copy(original_csv_path, user_csv_path)

        return user_csv_path  #コピー先のCSVを使う

    else: #通常の実行環境では、dataフォルダのCSVを使用
        return os.path.join(os.path.abspath("."), "data", csv_file_name)


#起動したときのウィンドウ外観の設定
def settingCSVReader(type) :

    csv_path = return_true_csv_path("setting")
    csv = pd.read_csv(csv_path, index_col=0, na_values=["NaN", "Na"])

    #csvファイルが存在すればそのファイルから mode を取り出してテーマに設定
    if os.path.exists(csv_path) == True  :

        #csvファイルの読み込み+その他設定
        mode = csv.loc["row_1", type]

        print(f">> {type} << を読み取り、settingCSVReaderが実行されました")

        if mode == "custom" :

            return return_true_csv_path("json")

        else :
            return mode

    #csvファイルが存在しなければ csvWriter() を実行
    else :

        settingCSVMaker(type)


#csvファイルを制作そしてファイルを読み取り+書き込み
def settingCSVMaker(type) :

    csv_path = return_true_csv_path("setting")

    #ファイルが存在しないとき、csvFile を制作
    if not os.path.exists(csv_path) == False :

        #データの内容を作成
        dict = {
            "appearance" : ["system"],
            "theme" : ["blue"],
            "row" : ["0"],
            "column" : ["0"],
            "startup" : ["off"],
            "fontFamily" : ["游ゴシック"],
            "groupFontSize" : ["13"],
            "linkFontSize" : ["11"],
            "notesShow" : ["yes"]
        }

        #dictを DataFrameに変換
        data = pd.DataFrame(dict)
        data.index = ["row_1"]

        #csvファイルに変換
        data.to_csv(csv_path)

        print("settingCSVMakerが実行されました")

        reStart()
        settingCSVReader(type=type)

    else :

        #CSVファイルが存在するためcsvReader()に戻る（まず実行されない）
        settingCSVReader(type=type)

    #アプリの再起動関数
    def reStart(root) :

        name = ctk.CTkToplevel()
        name.geometry("520x300")
        name.geometry("+600+400")
        name.title("お知らせ")
        name.focus_set()
        name.wm_attributes("-topmost", True)

        label = ctk.CTkLabel(name, text="データの更新を確認しました。", font=(settingCSVReader(type="fontFamily"), 15))
        label.grid(row=0, column=0, padx=15, pady=30, sticky="w")

        label2 = ctk.CTkLabel(name, text="更新のため、アプリを再起動してください。", font=(settingCSVReader(type="fontFamily"), 15))
        label2.grid(row=1, column=0, padx=15, pady=30, sticky="w")


        label3 = ctk.CTkLabel(name, text="編集を続ける場合は、続行ボタンを押してください。", font=(settingCSVReader(type="fontFamily"), 15))
        label3.grid(row=2, column=0, padx=15, pady=30, sticky="w")

        button = ctk.CTkButton(name, text="アプリを終了 ", font=(settingCSVReader(type="fontFamily"), 12))
        button.grid(row=3, column=0, padx=200, pady=30, sticky="e")
        button.bind("<Button-1>", lambda e:root.wm_attributes("-topmost", False))
        button.bind("<Button-1>", lambda e:sys.exit())

        button2 = ctk.CTkButton(name, text="続行 ", font=(settingCSVReader(type="fontFamily"), 12))
        button2.grid(row=4, column=0, padx=50, pady=30, sticky="e")
        button2.bind("<Button-1>", lambda e:root.wm_attributes("-topmost", False))
        button2.bind("<Button-1>", lambda e:name.destroy())


#link.csvのindexを再生成する関数
def resetIndex(type : Literal["link", "frame"]) :

    csv_path = return_true_csv_path(type=type)

    #link.csvを開き、indexを再生成
    CSV = pd.read_csv(csv_path, index_col=0)
    CSV = CSV.reset_index(drop=True)
    CSV.to_csv(csv_path, sep=",", encoding="utf-8")

    print(f"<< {type} >> のindexを再生成しました")
