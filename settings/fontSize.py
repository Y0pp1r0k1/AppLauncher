import customtkinter as CTK
import pandas as pd

import modules.CSVReader as CSVReader
from modules.CTkDefs import labelDef as label
from modules.gridSystem import gridSystem
from modules.CSVReader import settingCSVReader as setting
from modules.CTkDefs import reStart

#フォントサイズ・フォントファミリーの取得+変数への代入
fontFamily = setting("fontFamily")
lFontSize = setting("linkFontSize")
gFontSize = setting("groupFontSize")

setting_csv_path = CSVReader.return_true_csv_path("setting")


def font(root) :

    gridSystem.resetGrid("column")
    gridSystem.resetGrid("row")

    gridSystem.addGrid("row")

    #label
    label("label", root, "フォントサイズを変更", "w", 15, 40, 20)

    #groupFontSize Label
    label("groupFontSize", root, "フレームタイトルのフォントサイズ", "w", 15, 60, 20)

    #groupFontSize Entry
    entry1 = CTK.CTkEntry(root, border_width=0, width=200, height=30, placeholder_text=f"now is {gFontSize}(px)", font=(fontFamily, 15))
    entry1.grid(row=gridSystem.getGrid("row"), column=gridSystem.getGrid("column"), padx=80, pady=(10, 20))

    gridSystem.reduceGrid("row")
    gridSystem.addGrid("column")

    #linkFontSize Label
    label("linkFontSize", root, "リンクのフォントサイズ", "w", 15, 40, 20)

    #LinkFontSize Entry
    entry2 = CTK.CTkEntry(root, border_width=0, width=200, height=30, placeholder_text=f"now is {lFontSize}(px)", font=(fontFamily, 15))
    entry2.grid(row=gridSystem.getGrid("row"), column=gridSystem.getGrid("column"), padx=60, pady=(10, 20))

    gridSystem.addGrid("row")

    #fontFamily label
    label("fontFamily", root, "使用するフォントファミリー", "w", 15, 40, 20)

    #fontFamily entry
    entry3 = CTK.CTkEntry(root, border_width=0, width=200, height=30, placeholder_text=f"now is {fontFamily}", font=(fontFamily, 15))
    entry3.grid(row=gridSystem.getGrid("row"), column=gridSystem.getGrid("column"), padx=80, pady=(10, 20))

    gridSystem.addGrid("column")
    gridSystem.reduceGrid("row")

    #cancelButton
    button = CTK.CTkButton(root, text="cancel", width=80, font=(fontFamily, 12))
    button.grid(row=gridSystem.getGrid("row"), column=gridSystem.getGrid("column"), padx=20, pady=(10, 20))
    button.bind("<Button-1>", lambda e:delEntryText())
    button.bind("<Button-1>", lambda e:setPlaceholderText())

    gridSystem.addGrid("row")

    #updateButton
    button2 = CTK.CTkButton(root, text="update", width=80, font=(fontFamily, 12))
    button2.grid(row=gridSystem.getGrid("row"), column=gridSystem.getGrid("column"),  padx=20, pady=(10, 20))
    button2.bind("<Button-1>", lambda e:renewalCSV("groupFontSize", entry1))
    button2.bind("<Button-1>", lambda e:renewalCSV("linkFontSize", entry2))
    button2.bind("<Button-1>", lambda e:renewalCSV("fontFamily", entry3))
    button2.bind("<Button-1>", lambda e:reStart(root=root))

    #entryの内容を削除+placeholder_textを設定
    def delEntryText() :

        entry1.delete(0, "end")
        entry2.delete(0, "end")
        entry3.delete(0, "end")

    def setPlaceholderText() :

        entry1.configure(placeholder_text=f"now is {gFontSize}(px)")
        entry2.configure(placeholder_text=f"now is {lFontSize}(px)")
        entry3.configure(placeholder_text=f"now is {fontFamily}")

    #csvファイルの書き換え
    def renewalCSV(type, entry):
        settingCSV = pd.read_csv(setting_csv_path, index_col=0, na_values=["NaN", "Na"])

        if type == "groupFontSize":

            newGroupFontSize = entry.get()

            if newGroupFontSize != "" :

                # 直接値を更新する
                settingCSV.loc["row_1", "groupFontSize"] = newGroupFontSize
                settingCSV.to_csv(setting_csv_path)

                print("正常にgroupFontSizeが更新されました")

            else:
                print("text not found")

        elif type == "linkFontSize":

            newLinkFontSize = entry.get()

            if newLinkFontSize != "" :

                settingCSV.loc["row_1", "linkFontSize"] = newLinkFontSize
                settingCSV.to_csv(setting_csv_path)

                print("正常にlinkFontSizeが更新されました")

            else:
                print("text not found")

        elif type == "fontFamily" :

            fontFamily = entry.get()

            if fontFamily != "" :

                settingCSV.loc["row_1", "fontFamily"] = fontFamily
                settingCSV.to_csv(setting_csv_path)

                print("正常にfontFamilyが更新されました")

            else:
                print("text not found")
