import pandas as pd
import customtkinter as CTK

import modules.CSVReader as CSVReader
from modules.gridSystem import gridSystem
from modules.CSVReader import settingCSVReader

def etcSetting(root) :

    gridSystem.resetGrid("row")
    gridSystem.resetGrid("column")

    gridSystem.addGrid("row")

    font = settingCSVReader("fontFamily")

    setting_csv_path = CSVReader.return_true_csv_path("setting")

    #checkbox
    checkbox1 = CTK.CTkCheckBox(root, text="<< 重要なお知らせ >>  を二度と表示しない", font=(font, 13), width=80)
    checkbox1.grid(row=gridSystem.getGrid("row"), column=0, padx=80, pady=30, sticky="e")
    checkbox1.bind("<Button-1>", lambda e:renewalCSV())

    #CSVファイルの書き換え
    def renewalCSV() :

        settingCSV = pd.read_csv(setting_csv_path, index_col=0, na_values=["NaN", "Na"])
        oldValue = settingCSV.loc["row_1", "notesShow"]

        if checkbox1.get() == 1 :

            settingCSV = settingCSV.replace({"notesShow" : {oldValue : "no"}})
            settingCSV.to_csv(setting_csv_path)

        else :

            settingCSV = settingCSV.replace({"notesShow" : {oldValue : "yes"}})
            settingCSV.to_csv(setting_csv_path)

    def checkCheckBox() :

        settingCSV = pd.read_csv(setting_csv_path, index_col=0, na_values=["NaN", "Na"])

        if settingCSV.loc["row_1", "notesShow"] == "yes" :

            checkbox1.deselect()

        else :

            checkbox1.select()


    checkCheckBox()