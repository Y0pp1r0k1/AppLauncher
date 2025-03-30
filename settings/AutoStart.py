import customtkinter as CTK
import os
import pandas as pd

import modules.CTkDefs as defs
import modules.CSVReader as CSVReader
import modules.startupShortcut as startupShortcut

from modules.gridSystem import gridSystem
from modules.CSVReader import settingCSVReader as setting


#フォントサイズ・フォントファミリーの取得+変数への代入
font = setting("fontFamily")
lFontSize = setting("linkFontSize")

setting_csv_path = CSVReader.return_true_csv_path("setting")

def autoStart(root) :

    settingCSV = pd.read_csv(setting_csv_path, index_col=0, na_values=["NaN", "Na"])

    gridSystem.resetGrid("row")
    gridSystem.resetGrid("column")

    gridSystem.addGrid("row")
    #label
    defs.labelDef("label", root, "PC起動時にこのアプリも起動", "w", 15, 40, 20)

    #switch
    switch = CTK.CTkSwitch(root, font=(font, 15), text=" ", switch_height=30, switch_width=50)
    switch.grid(row=gridSystem.getGrid("row"), column=gridSystem.getGrid("column"), padx=80, pady=20)
    switch.bind("<Button-1>", lambda e:changeText(switch))
    switch.bind("<Button-1>", lambda e:check_exist_app(switch))

    #switchテキストの書き換え
    def changeText(name) :

        if name.get() == 1 :

            name.configure(text="on")

        elif name.get() == 0 :

            name.configure(text="off")

    #スタートアップアプリの状態の確認
    def check_startup_status() :

        startup = settingCSV.loc["row_1", "startup"]

        if startup == "on" :

            switch.select()
            switch.configure(text="on")

        elif startup == "off" :

            switch.deselect()
            switch.configure(text="off")

        else :

            print("error")


    #スタートアップアプリにこのアプリがあるかの確認
    def check_exist_app(name) :

        userName = os.getlogin()

        #スタートアップアプリの設定
        shortcut_path = rf"c:\users\{userName}\appdata\roaming\microsoft\windows\Start Menu\programs\startup\AppLauncher.lnk"
        app_path = startupShortcut.get_app_path()

        #アプリが存在して、スイッチも on だったらコンソールに表示
        if os.path.exists(shortcut_path) == True and name.get() == 1 :

            print("exist an app")
            renewalCSV("on")

        #アプリが存在せず、スイッチが on だったらスタートアップアプリに追加 + その他もろもろ
        elif os.path.exists(shortcut_path) == False and name.get() == 1 :

            startupShortcut.add_app_to_startup_apps(app_path)
            renewalCSV("on")

        #アプリが存在して、スイッチが off だったらスタートアップアプリから削除 + その他もろもろ
        elif os.path.exists(shortcut_path) == True and name.get() == 0 :

            startupShortcut.delete_app_from_startup_apps()
            renewalCSV("off")

        #アプリが存在せず、スイッチも off だったら、コンソールに表示
        else :
            print("not exist an app")

    # setting.csv の startup を書き換える関数
    def renewalCSV(type) :

        startUp = settingCSV.loc["row_1", "startup"]

        if type == "on" :

            reCSV = settingCSV.replace({"startup" : {startUp : "on"}})
            reCSV.to_csv(setting_csv_path)

        elif type == "off" :

            reCSV = settingCSV.replace({"startup" : {startUp : "off"}})
            reCSV.to_csv(setting_csv_path)

    check_startup_status()


