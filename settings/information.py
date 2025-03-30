import customtkinter as CTK
import modules.CTkDefs as defs
from modules.gridSystem import gridSystem
from modules.CSVReader import settingCSVReader as setting

#フォントサイズ・フォントファミリーの取得+変数への代入
font = setting("fontFamily")

lFontSize = setting("linkFontSize")

def info() :

    #ウィンドウの設定
    infoWindow = CTK.CTkToplevel()
    infoWindow.title("アプリ情報")
    infoWindow.geometry("700x500")
    infoWindow.geometry("+750+280")
    infoWindow.focus_force()
    infoWindow.attributes("-topmost", True)

    gridSystem.resetGrid("row")
    gridSystem.resetGrid("column")

    #情報のLabel
    defs.labelDef("label", infoWindow, "アプリVer                     :          Release 1.0", "w", 15, 30, 15)

    defs.labelDef("label", infoWindow, "このVerの最終更新日    :    2025/3/14", "w", 15, 30, 5)

    defs.labelDef("label", infoWindow, "使用した言語・ツール", "w", 15, 30, 5)

    defs.labelDef("label", infoWindow, "言語     :   Python (Ver 3.12.4)", "w", 15, 50, 5)

    defs.labelDef("label", infoWindow, "ツール :", "w", 15, 50, 5)

    defs.labelDef("label", infoWindow, "● Visual Studio Code (Ver 1.98.2)", "w", 15, 60, 5)

    defs.labelDef("label", infoWindow, "● PyInstaller (Ver 6.10.0)", "w", 15, 60, 5)

    defs.labelDef("label", infoWindow, "● Power Shell 7 (Ver 7.4.5)", "w", 15, 60, 5)

    defs.labelDef("label", infoWindow, "● Git(Ver 2.43.0)", "w", 15, 60, 5)

    defs.labelDef("label", infoWindow, "● Git Hub (https://github.com/Y0pp1r0k1/AppLauncher)", "w", 15, 60, 5)

    defs.labelDef("label", infoWindow, "開発環境 : Windows11 home 64bit (24H2)", "w", 15, 30, 5)

    gridSystem.addGrid("column")

    #閉じるボタン
    Button = CTK.CTkButton(infoWindow, text="Close")
    Button.grid(row=gridSystem.getGrid("row"), column=gridSystem.getGrid("column"), padx=(30, 0), pady=(20, 0))
    Button.bind("<Button-1>", lambda e:defs.close(infoWindow))

