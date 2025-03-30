import customtkinter as CTK
import pandas as pd
import os
import platform
import webbrowser

import modules.CTkDefs as defs
import modules.CustomLinkDefs as CLD
import modules.CSVReader as CSVReader
from modules.gridSystem import gridSystem
from modules.CSVReader import settingCSVReader as setting

#フォントサイズ・フォントファミリーの取得+変数への代入
font = setting("fontFamily")
lFontSize = setting("linkFontSize")

setting_csv_path = CSVReader.return_true_csv_path("setting")

def wTheme(root, window) :

    settingCSV = pd.read_csv(setting_csv_path, index_col=0, na_values=["NaN", "Na"])

    gridSystem.resetGrid("row")
    gridSystem.resetGrid("column")

    gridSystem.addGrid("row")

    #label
    defs.labelDef("label", root, "ウィンドウのテーマを変更", "w", 15, 40, 20)

    defs.labelDef("label", root, "※チェックボックスをクリックすると、テーマを更新するため、アプリが再起動します。", "w", 13, 55, 20)

    #checkboxes
    #blue(default)
    checkbox1 = CTK.CTkCheckBox(root, text="blue mode (default)", border_width=2, font=(font, 15), corner_radius=100)
    checkbox1.grid(row=gridSystem.getGrid("row"), column=gridSystem.getGrid("column"), padx=80, pady=20, sticky="w")
    checkbox1.bind("<Button-1>", lambda e:blueMode(), "+")
    gridSystem.addGrid("row")


    #dark-blue
    checkbox2 = CTK.CTkCheckBox(root, text="dark blue mode", border_width=2, font=(font, 15), corner_radius=100)
    checkbox2.grid(row=gridSystem.getGrid("row"), column=gridSystem.getGrid("column"), padx=80, pady=20, sticky="w")
    checkbox2.bind("<Button-1>", lambda e:darkBlueMode(), "+")
    gridSystem.addGrid("row")


    #green
    checkbox3 = CTK.CTkCheckBox(root, text="green mode", border_width=2, font=(font, 15), corner_radius=100)
    checkbox3.grid(row=gridSystem.getGrid("row"), column=gridSystem.getGrid("column"), padx=80, pady=20, sticky="w")
    checkbox3.bind("<Button-1>", lambda e:greenMode(), "+")
    gridSystem.addGrid("row")

    #custom
    checkbox4 = CTK.CTkCheckBox(root, text="custom mode", border_width=2, font=(font, 15), corner_radius=100)
    checkbox4.grid(row=gridSystem.getGrid("row"), column=gridSystem.getGrid("column"), padx=80, pady=20, sticky="w")
    checkbox4.bind("<Button-1>", lambda e:customMode(root), "+")
    gridSystem.addGrid("row")
    gridSystem.addGrid("row")
    gridSystem.addGrid("row")


    #チェックボックスがクリックされたらCSVファイルの書き換え
    def renewalCSV(theme) :


        #csvファイルの読み込み+現在のテーマの取得
        oldMode = settingCSV.loc["row_1", "theme"]

        #csvファイルのmodeを新旧で入れ替える+csvファイルを更新
        reCSV = settingCSV.replace(oldMode, theme)
        reCSV.to_csv(setting_csv_path)


        #新しいmodeを取得
        newMode = reCSV.loc["row_1", "theme"]
        print(f"new theme mode : {newMode}")



    #ウィドウカラーテーマの設定
    #blue (default)
    def blueMode() :

        if checkbox1.get() == 1 :

            renewalCSV("blue")

            defs.reStart(root=window)


            checkbox2.deselect()
            checkbox3.deselect()
            checkbox4.deselect()

    #dark-blue
    def darkBlueMode() :

        if checkbox2.get() == 1 :

            renewalCSV("dark-blue")

            defs.reStart(root=window)

            checkbox1.deselect()
            checkbox3.deselect()
            checkbox4.deselect()

    #green
    def greenMode() :

        if checkbox3.get() == 1 :

            renewalCSV("green")

            defs.reStart(root=window)

            checkbox1.deselect()
            checkbox2.deselect()
            checkbox4.deselect()

    #custom
    def customMode(root) :

        if checkbox4.get() == 1 :

            """
                customをクリックしたとき、自作のjsonファイルを使えるようにする。

            """

            gridSystem.resetGrid("column")

            gridSystem.addGrid("row")
            gridSystem.addGrid("row")
            gridSystem.addGrid("row")
            gridSystem.addGrid("row")
            gridSystem.addGrid("row")
            gridSystem.addGrid("row")


            defs.labelDef("label", root, "After editing custom.json, be sure to save it!", "w",  12, 100, 10)

            defs.labelDef("label", root, "JSONファイルの書き方はこちら ↓ ([]の中身は、外観設定がdark Mode, Light Mode の時の色です。)", "w", 12, 100, 10)

            label = CTK.CTkLabel(master=root, text="https://github.com/TomSchimansky/CustomTkinter/blob/master/customtkinter/assets/themes/dark-blue.json", font=(font, 12),  text_color="#0095d9")
            label.grid(row=gridSystem.getGrid("row"), column=gridSystem.getGrid("column"), padx=120, pady=20)
            label.bind("<Button-1>", lambda e:webbrowser.open("https://github.com/TomSchimansky/CustomTkinter/blob/master/customtkinter/assets/themes/dark-blue.json"))
            label.bind("<Button-1>", lambda e:defs.delAttributes(root=window))

            gridSystem.addGrid("row")

            editJsonButton = CTK.CTkButton(root, font=(font, 13), text="edit custom.json", width=70)
            editJsonButton.grid(row=gridSystem.getGrid("row"), column=gridSystem.getGrid("column"), padx=(110, 10), pady=10, sticky="w")
            editJsonButton.bind("<Button-1>", lambda e:defs.delAttributes(root=window))
            editJsonButton.bind("<Button-1>", lambda e:openJson())

            #updateButton
            updateButton = CTK.CTkButton(root, font=(font, 13), text="update", width=50)
            updateButton.grid(row=gridSystem.getGrid("row"), column=gridSystem.getGrid("column"), padx=(240, 10), pady=10, sticky="w")
            updateButton.bind("<Button-1>", lambda e:renewalCSV("custom"))
            updateButton.bind("<Button-1>", lambda e:defs.reStart(root=window))

            checkbox1.deselect()
            checkbox2.deselect()
            checkbox3.deselect()

    #ウィンドウを起動したらCSVを参考に自動でcheckboxにチェックを入れる
    def setSelect() :

        theme = settingCSV.loc["row_1", "theme"]

        if theme == "blue" :

            checkbox1.select()

        elif theme == "dark-blue" :

            checkbox2.select()

        elif theme == "green" :

            checkbox3.select()

        elif theme == "custom" :

            checkbox4.select()

        else :

            print("error")


    #jsonファイルを開く関数
    def openJson() :

        file_path = CSVReader.return_true_csv_path("json")

        if os.path.isfile(file_path) and os.path.exists(file_path) == True :

            if platform.system() == "Windows" :

                os.system(f"notepad {file_path} &")

        else :

            CLD.errorWindow(file_path)


    setSelect()




