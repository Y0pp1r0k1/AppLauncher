import customtkinter as CTK
import CTkDefs as defs

def info() :

    #ウィンドウの設定
    infoWindow = CTK.CTkToplevel()
    infoWindow.title("アプリ情報")
    infoWindow.geometry("700x500")
    infoWindow.geometry("+750+280")
    infoWindow.focus_force()
    infoWindow.attributes("-topmost", True)

    #情報のLabel
    defs.labelDef("label", infoWindow, "アプリVer　                   :          Ver 3.2", 0, 0, CTK.W, "游ゴシック", 15, 30, 15)   

    defs.labelDef("label", infoWindow, "このVerの最終更新日    :    2024/10/18", 1, 0, CTK.W, "游ゴシック", 15, 30, 5)

    defs.labelDef("label", infoWindow, "使用した言語・ツール", 2, 0, CTK.W, "游ゴシック", 15, 30, 5)       

    defs.labelDef("label", infoWindow, "言語     :   Python (Ver 3.12.4)", 3, 0, CTK.W, "游ゴシック", 15, 50, 5)   

    defs.labelDef("label", infoWindow, "ツール :", 4, 0, CTK.W, "游ゴシック", 15, 50, 5)   

    defs.labelDef("label", infoWindow, "● Visual Studio Code (Ver 1.94.0)", 5, 0, CTK.W, "游ゴシック", 15, 60, 5)   

    defs.labelDef("label", infoWindow, "● PyInstaller (Ver 6.10.0)", 6, 0, CTK.W, "游ゴシック", 15, 60, 5)   

    defs.labelDef("label", infoWindow, "● Power Shell 7 (Ver 7.4.5)", 7, 0, CTK.W, "游ゴシック", 15, 60, 5)   

    defs.labelDef("label", infoWindow, "● Git(Ver 2.43.0)", 8, 0, CTK.W, "游ゴシック", 15, 60, 5)   

    defs.labelDef("label", infoWindow, "● Git Hub (https://github.com/Y0pp1r0k1/FavoriteLinks)", 9, 0, CTK.W, "游ゴシック", 15, 60, 5)   

    defs.labelDef("label", infoWindow, "開発環境 : Windows11 home 64bit" , 10, 0, CTK.W, "游ゴシック", 15, 30, 5)   

    #閉じるボタン
    Button = CTK.CTkButton(infoWindow, text="Close")
    Button.grid(row=11, column=1, padx=(30, 0), pady=(20, 0))
    Button.bind("<Button-1>", lambda e:defs.close(infoWindow))

