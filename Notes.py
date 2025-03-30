import customtkinter as CTK
import pandas as pd

import modules.CustomLinkDefs as CLD
import modules.CTkDefs as defs
import modules.CSVReader as CSVReader
from modules.gridSystem import gridSystem
from modules.CSVReader import settingCSVReader as setting


#フォントサイズ・フォントファミリーの取得+変数への代入
font = setting("fontFamily")
lFontSize = setting("linkFontSize")

setting_csv_path = CSVReader.return_true_csv_path("setting")


def NotesWindow() :

    #ウィンドウの制作
    NotesWindow = CTK.CTkToplevel()
    NotesWindow.title("お知らせ")
    NotesWindow.geometry("700x500")
    NotesWindow.geometry("+750+280")
    NotesWindow.focus_force()
    NotesWindow.attributes("-topmost", True)

    gridSystem.resetGrid("row")
    gridSystem.resetGrid("column")

    #注意事項のテキストたち
    defs.labelDef("label", NotesWindow, "重要なお知らせ", "w", 25, 10, 10)

    defs.labelDef("label", NotesWindow, "この度は当アプリをご利用いただきありがとうございます。突然ですが、お知らせになります。", "w", 15, 20, 5)

    defs.labelDef("label", NotesWindow, "現在、このアプリは一時的に完成した状態であるため、今後以下の機能を実装しようと思っています。", "w", 15, 20, 5)

    defs.labelDef("label", NotesWindow, "○ 実装予定の機能一覧", "w", 15, 30, 5)

    defs.labelDef("label", NotesWindow, "● アイコン機能（アプリ・Webサイトのアイコンを文字と一緒に表示させる機能）", "w", 15, 50, 5)

    defs.labelDef("label", NotesWindow, "● 解像度機能 （画面の最大サイズに応じたこのアプリの解像度設定機能）", "w", 15, 50, 5)

    defs.labelDef("label", NotesWindow, "その他よさそうな機能を思いついたら気分で実装していきます", "w", 15, 50, 5)

    defs.labelDef("label", NotesWindow, "更新情報や使い方などは以下のリンクから確認可能です。ぜひご覧ください。", "w", 15, 20, 5)

    CLD.linkContent(NotesWindow, "label", "GitHub : https://github.com/Y0pp1r0k1/AppLauncher", "https://github.com/Y0pp1r0k1/AppLauncher")

    defs.labelDef("label", NotesWindow, "アプリバージョン Release 1.0 : 最終アップデート日 2025/3/14", "w", 15, 30, 5)

    defs.labelDef("label", NotesWindow, "このウィンドウの表示は下記の二度と表示しないボタン、または 設定 → その他 から変更可能です", "w", 11, 50, 5)

    #checkbox
    checkbox1 = CTK.CTkCheckBox(NotesWindow, text="二度と表示しない", font=(font, 13), width=80)
    checkbox1.grid(row=gridSystem.getGrid("row"), column=0, padx=(0, 200), pady=30, sticky="e")
    checkbox1.bind("<Button-1>", lambda e:renewalCSV())

    #閉じるボタン
    Button = CTK.CTkButton(NotesWindow, text="agree")
    Button.grid(row=gridSystem.getGrid("row"), column=0, padx=(0, 40), pady=30, sticky="e")
    Button.bind("<Button-1>", lambda e:defs.close(NotesWindow))

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

    #checkBoxにチェックを入れるかどうか
    def checkCheckBox() :

        settingCSV = pd.read_csv(setting_csv_path, index_col=0, na_values=["NaN", "Na"])

        if settingCSV.loc["row_1", "notesShow"] == "yes" :

            checkbox1.deselect()

        else :

            checkbox1.select()


    checkCheckBox()

#csvファイルから読み取ってこのウィンドウを起動するかしないかの確認関数
def checkCSVFile() :

    settingCSV = pd.read_csv(setting_csv_path, index_col=0, na_values=["NaN", "Na"])

    if settingCSV.loc["row_1", "notesShow"] == "yes" :

        NotesWindow()

    else :

        print("csv file is 'NO'")



