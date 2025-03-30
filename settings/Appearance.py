import customtkinter as CTK
import pandas as pd

import modules.CTkDefs as defs
import modules.CSVReader as CSVReader
from modules.gridSystem import gridSystem
from modules.CSVReader import settingCSVReader as setting

#フォントサイズ・フォントファミリーの取得+変数への代入
font = setting("fontFamily")
lFontSize = setting("linkFontSize")

setting_csv_path = CSVReader.return_true_csv_path("setting")

def wColor(root) :

    settingCSV = pd.read_csv(setting_csv_path, index_col=0, na_values=["NaN", "Na"])

    gridSystem.resetGrid("row")
    gridSystem.resetGrid("column")

    gridSystem.addGrid("row")

    defs.labelDef("label", root, "アプリの外観を変更", "w", 15, 40, 20)

    #checkboxes
    #dark
    checkbox1 = CTK.CTkCheckBox(root, text="dark mode", border_width=2, font=(font, 15), corner_radius=100)
    checkbox1.grid(row=gridSystem.getGrid("row"), column=gridSystem.getGrid("column"), padx=80, pady=20)
    checkbox1.bind("<Button-1>", lambda e:DarkMode())
    checkbox1.bind("<Button-1>", lambda e:renewalCSV("dark"), "+")
    checkbox1.bind("<Button-1>", lambda e:root.focus_force())
    gridSystem.addGrid("row")

    #light
    checkbox2 = CTK.CTkCheckBox(root, text="light mode", border_width=2, font=(font, 15), corner_radius=100)
    checkbox2.grid(row=gridSystem.getGrid("row"), column=gridSystem.getGrid("column"), padx=80, pady=20)
    checkbox2.bind("<Button-1>", lambda e:LightMode())
    checkbox2.bind("<Button-1>", lambda e:renewalCSV("light"), "+")
    checkbox2.bind("<Button-1>", lambda e:root.focus_force())
    gridSystem.addGrid("row")

    #system
    checkbox3 = CTK.CTkCheckBox(root, text="system", border_width=2, font=(font, 15), corner_radius=100)
    checkbox3.grid(row=gridSystem.getGrid("row"), column=gridSystem.getGrid("column"), padx=80, pady=20)
    checkbox3.bind("<Button-1>", lambda e:SystemMode())
    checkbox3.bind("<Button-1>", lambda e:renewalCSV("system"), "+")
    checkbox3.bind("<Button-1>", lambda e:root.focus_force())
    gridSystem.addGrid("row")



    #チェックボックスがクリックされたらCSVファイルの書き換え
    def renewalCSV(mode) :


        #csvファイルの読み込み+現在のモードの取得
        oldMode = settingCSV.loc["row_1", "appearance"]

        #csvファイルのmodeを新旧で入れ替える+csvファイルを更新
        reCSV = settingCSV.replace(oldMode, mode)
        reCSV.to_csv(setting_csv_path)


        #新しいmodeを取得
        newMode = reCSV.loc["row_1", "appearance"]
        print(f"new appearance mode : {newMode}")



    #ウィンドウの外観の設定
    #dark
    def DarkMode() :

        if checkbox1.get() == 1:

            CTK.set_appearance_mode("dark")

            checkbox2.deselect()
            checkbox3.deselect()


    #light
    def LightMode() :

        if checkbox2.get() == 1:

            CTK.set_appearance_mode("light")

            checkbox1.deselect()
            checkbox3.deselect()


    #system
    def SystemMode() :

        if checkbox3.get() == 1:

            CTK.set_appearance_mode("system")

            checkbox1.deselect()
            checkbox2.deselect()

    #setting.csvに保存されたテキストからウィンドウ起動時にcheckboxにチェックをつける
    def setSelect() :

        mode = settingCSV.loc["row_1", "appearance"]

        if mode == "dark" :

            checkbox1.select()

        elif mode == "light" :

            checkbox2.select()

        elif mode == "system" :

            checkbox3.select()

        else :

            print("error")

    setSelect()


