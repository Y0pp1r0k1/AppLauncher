import customtkinter as CTK
import pandas as pd

from CTkDefs import labelDef as label
import CTkDefs as defs

def wColor() :

    #ウィンドウの設定
    wColorWindow = CTK.CTkToplevel()
    wColorWindow.title("アプリの外観の設定")
    wColorWindow.geometry("300x400")
    wColorWindow.geometry("+750+280")
    wColorWindow.focus_force()
    wColorWindow.attributes("-topmost", True)


    #label
    label("label", wColorWindow, "アプリの外観を変更", 0, 0, CTK.W, "游ゴシック", 20, 20, 20)


    #checkboxes
    #dark
    checkbox1 = CTK.CTkCheckBox(wColorWindow, text="dark mode", border_width=2, font=("游ゴシック", 15), corner_radius=100)
    checkbox1.grid(row=1, column=0, padx=40, pady=20)
    checkbox1.bind("<Button-1>", lambda e:DarkMode())
    checkbox1.bind("<Button-1>", lambda e:renewalCSV("dark"), "+")

    #light
    checkbox2 = CTK.CTkCheckBox(wColorWindow, text="light mode", border_width=2, font=("游ゴシック", 15), corner_radius=100)
    checkbox2.grid(row=2, column=0, padx=40, pady=20)
    checkbox2.bind("<Button-1>", lambda e:LightMode())
    checkbox2.bind("<Button-1>", lambda e:renewalCSV("light"), "+")

    #system
    checkbox3 = CTK.CTkCheckBox(wColorWindow, text="system", border_width=2, font=("游ゴシック", 15), corner_radius=100)
    checkbox3.grid(row=3, column=0, padx=40, pady=20)
    checkbox3.bind("<Button-1>", lambda e:SystemMode())
    checkbox3.bind("<Button-1>", lambda e:renewalCSV("system"), "+")


    #閉じるボタン
    closeButton = CTK.CTkButton(wColorWindow, text="close", font=("游ゴシック", 13))
    closeButton.grid(row=4, column=0, padx=(130, 0), pady=100)
    closeButton.bind("<Button-1>", lambda e:defs.close(wColorWindow))


    #チェックボックスがクリックされたらCSVファイルの書き換え
    def renewalCSV(mode) :


        #csvファイルの読み込み+現在のモードの取得
        df = pd.read_csv("./data/data.csv", sep=",", index_col=0)
        oldMode = df.loc["row_1", "appearance"]

        #csvファイルのmodeを新旧で入れ替える+csvファイルを更新
        reCSV = df.replace(oldMode, mode)
        reCSV.to_csv("./data/data.csv")
        

        #新しいmodeを取得
        newMode = reCSV.loc["row_1", "appearance"]
        print(newMode)
        


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

    #data.csvに保存されたテーマからウィンドウ起動時にcheckboxにチェックをつける
    def setSelect() :

        df = pd.read_csv("./data/data.csv", sep=",", index_col=0)
        mode = df.loc["row_1", "appearance"]

        if mode == "dark" :

            checkbox1.select()

        elif mode == "light" :

            checkbox2.select()

        elif mode == "system" :

            checkbox3.select()

        else :

            print("error")

    setSelect()
    
    
