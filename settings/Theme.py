import customtkinter as CTK
import pandas as pd
import sys
import os

import CTkDefs as defs
import CustomLinkDefs as CLD

def wTheme() :

    #ウィンドウの設定
    wThemeWindow = CTK.CTkToplevel()
    wThemeWindow.title("ウィンドウテーマの変更")
    wThemeWindow.geometry("500x500")
    wThemeWindow.geometry("+750+280")
    wThemeWindow.focus_force()
    wThemeWindow.attributes("-topmost", True)

    #label
    defs.labelDef("label", wThemeWindow, "ウィンドウのテーマを変更", 0, 0, CTK.W, "游ゴシック", 20, 20, 20)

    defs.labelDef("label", wThemeWindow, "※チェックボックスをクリックすると、テーマを更新するため、アプリが再起動します。", 1, 0, CTK.W, "游ゴシック", 10, 20, 20)

    #checkboxes 
    #blue(default)
    checkbox1 = CTK.CTkCheckBox(wThemeWindow, text="blue mode (default)", border_width=2, font=("游ゴシック", 15), corner_radius=100)
    checkbox1.grid(row=2, column=0, padx=50, pady=20, sticky=CTK.W)
    checkbox1.bind("<Button-1>", lambda e:renewalCSV("blue"))
    checkbox1.bind("<Button-1>", lambda e:blueMode(), "+")



    #dark-blue
    checkbox2 = CTK.CTkCheckBox(wThemeWindow, text="dark blue mode", border_width=2, font=("游ゴシック", 15), corner_radius=100)
    checkbox2.grid(row=3, column=0, padx=50, pady=20, sticky=CTK.W)
    checkbox2.bind("<Button-1>", lambda e:renewalCSV("dark-blue"))
    checkbox2.bind("<Button-1>", lambda e:darkBlueMode(), "+")


    #green
    checkbox3 = CTK.CTkCheckBox(wThemeWindow, text="green mode", border_width=2, font=("游ゴシック", 15), corner_radius=100)
    checkbox3.grid(row=4, column=0, padx=50, pady=20, sticky=CTK.W)
    checkbox3.bind("<Button-1>", lambda e:renewalCSV("green"), "+")
    checkbox3.bind("<Button-1>", lambda e:greenMode(), "+")

    #custom
    checkbox4 = CTK.CTkCheckBox(wThemeWindow, text="custom mode", border_width=2, font=("游ゴシック", 15), corner_radius=100)
    checkbox4.grid(row=5, column=0, padx=50, pady=20, sticky=CTK.W)
    checkbox4.bind("<Button-1>", lambda e:customMode(), "+")

    #closeButton
    closeButton = CTK.CTkButton(wThemeWindow, text="close", font=("游ゴシック", 13))
    closeButton.grid(row=6, column=0, padx=(300, 0), pady=20)
    closeButton.bind("<Button-1>", lambda e:defs.close(wThemeWindow))


    #チェックボックスがクリックされたらCSVファイルの書き換え
    def renewalCSV(theme) :


        #csvファイルの読み込み+現在のテーマの取得
        df = pd.read_csv("./data/data.csv", sep=",", index_col=0)
        oldMode = df.loc["row_1", "theme"]

        #csvファイルのmodeを新旧で入れ替える+csvファイルを更新
        reCSV = df.replace(oldMode, theme)
        reCSV.to_csv("./data/data.csv")
        

        #新しいmodeを取得
        newMode = reCSV.loc["row_1", "theme"]
        print(newMode)



    #ウィドウカラーテーマの設定
    #blue (default) 
    def blueMode() :

        if checkbox1.get() == 1 :

            CTK.set_default_color_theme("blue")

            reStart()

            checkbox2.deselect()
            checkbox3.deselect()
            checkbox4.deselect()

    #dark-blue
    def darkBlueMode() :

        if checkbox2.get() == 1 :

            CTK.set_default_color_theme("dark-blue")

            reStart()

            checkbox1.deselect()
            checkbox3.deselect()
            checkbox4.deselect()

    #green
    def greenMode() :

        if checkbox3.get() == 1 :

            CTK.set_default_color_theme("green")

            reStart() 

            checkbox1.deselect()
            checkbox2.deselect()
            checkbox4.deselect()

    #custom
    def customMode() :

        if checkbox4.get() == 1 :

            #CTK.set_default_color_theme("blue")

            reStart() 

            checkbox1.deselect()
            checkbox2.deselect()
            checkbox3.deselect()


    #ウィンドウを起動したらCSVを参考に自動でcheckboxにチェックを入れる
    def setSelect() :

        df = pd.read_csv("./data/data.csv", index_col=0, sep=",")
        theme = df.loc["row_1", "theme"]

        if theme == "blue" :

            checkbox1.select()
        
        elif theme == "dark-blue" :

            checkbox2.select() 
 
        elif theme == "green" :

            checkbox3.select()

        elif theme == "custom" :

            checkbox4.select()
    
    """
        アプリの再起動関数を作る！！！！！！！！！
        
    """

    #アプリの再起動関数
    def reStart() :

        python = sys.executable
        os.execl(python, python, *sys.argv)



    setSelect()




