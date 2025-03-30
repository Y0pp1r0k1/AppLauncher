import customtkinter as CTK

import modules.CustomLinkDefs as CLD
from modules.CSVReader import settingCSVReader
from modules.gridSystem import gridSystem
from modules.allWidgetsMaker import allLinkMaker
from Notes import checkCSVFile
from setting import settings
from Custom import customWindow

#main
def main():

    #ウィンドウの設定
    root = CTK.CTk()
    root.title("Application and Website launcher")
    root.geometry("1366x768")
    root.geometry("+300+120")
    root.focus_set()

    #フォントfamilyの取得
    font = settingCSVReader("fontFamily")

    CTK.set_appearance_mode(settingCSVReader("appearance"))  #外観の色の設定
    CTK.set_default_color_theme(settingCSVReader("theme"))   #アプリテーマの設定

    #アイコンの設定
    root.iconbitmap(CLD.temp_path("data/icon.ico"))

    #すべてのフレームとリンクをまとめるframe
    linkFrame = CTK.CTkScrollableFrame(master=root, border_width=0, width=1150, height=750, fg_color=["gray92", "gray14"])
    linkFrame.grid(row=0, column=0, sticky="nsew", padx=0, pady=0)

    #リンクのカスタム機能
    custom = CTK.CTkButton(root, text="Custom link", font=(font, 10))
    custom.place(x=1200, y=660)
    custom.bind("<Button-1>", lambda e:customWindow())

    #設定
    setting = CTK.CTkButton(root, text="⚙ Setting", font=(font, 10))
    setting.place(x=1200, y=710)
    setting.bind("<Button-1>", lambda e:settings())

    #rowとcolumnをリセット
    gridSystem.resetGrid("row")
    gridSystem.resetGrid("column")

    allLinkMaker.make_all_main_widgets(root=linkFrame)

    #notesWindowを出すかの確認
    checkCSVFile()

    #ウィンドウの実行
    root.mainloop()


#main関数の呼び出し
main()

