import customtkinter as CTK

import modules.CTkDefs as defs
from modules.gridSystem import gridSystem
from modules.CSVReader import settingCSVReader as setting

from settings import Appearance
from settings import Theme
from settings import fontSize
from settings import AutoStart
from settings import information
from settings import etc

#フォントサイズ・フォントファミリーの取得+変数への代入
font = setting("fontFamily")

lFontSize = setting("linkFontSize")


def settings() :

    gridSystem.resetGrid("row")
    gridSystem.resetGrid("column")

    #ウィンドウの設定
    settingWindow = CTK.CTkToplevel()
    settingWindow.geometry("1280x720")
    settingWindow.geometry("+400+150")
    settingWindow.title("settings")
    settingWindow.attributes('-topmost', True)
    settingWindow.lift()
    settingWindow.focus_force()



    #項目Frame
    dateItemFrame = CTK.CTkFrame(settingWindow, border_width=0, height=660)
    dateItemFrame.grid_propagate(False)
    dateItemFrame.grid(row=0, column=0, sticky="ns", padx=(20, 0), pady=5)

    #設定名一覧のlabelたち
    defs.labelDef("appearance", dateItemFrame, "外観", "w", 15, 20, 10)

    defs.labelDef("theme", dateItemFrame, "アプリテーマ", "w", 15, 20, 10)

    defs.labelDef("fontSize", dateItemFrame, "フォントサイズ", "w", 15, 20, 10)

    defs.labelDef("autoStart", dateItemFrame, "起動設定", "w", 15, 20, 10)

    defs.labelDef("information", dateItemFrame, "アプリ情報", "w", 15, 20, 10)

    defs.labelDef("etc", dateItemFrame, "その他", "w", 15, 20, 10)



    #設定一覧Frame
    settingsFrame = CTK.CTkScrollableFrame(settingWindow, border_width=0, width=1000, height=660)
    settingsFrame.grid(row=0, column=1, sticky="ns", padx=(20, 20), pady=5)



    #appearanceFrame
    appearanceFrame = CTK.CTkFrame(settingsFrame, border_width=0, width=960)
    appearanceFrame.grid(row=0, column=0, sticky="ew", padx=20, pady=5)

    gridSystem.resetGrid("row")

    #appearanceLabel
    defs.labelDef("appearanceLabel", appearanceFrame, "外観", "w", 20, 10, 10)

    #appearance関数の挿入
    Appearance.wColor(appearanceFrame)



    #themeFrame
    themFrame = CTK.CTkFrame(settingsFrame, border_width=0, width=960)
    themFrame.grid(row=1, column=0, sticky="ew", padx=20, pady=5)

    gridSystem.resetGrid("row")

    #themeLabel
    defs.labelDef("themeLabel", themFrame, "アプリテーマ", "w",   20, 10, 10)

    #theme関数の挿入
    Theme.wTheme(themFrame, settingWindow)



    #fontSizeFrame
    fontSizeFrame = CTK.CTkFrame(settingsFrame, border_width=0, width=960)
    fontSizeFrame.grid(row=2, column=0, sticky="ew", padx=20, pady=5)

    gridSystem.resetGrid("row")

    #fontSizeLabel
    defs.labelDef("fontSizeLabel", fontSizeFrame, "フォントサイズ", "w", 20, 10, 10)

    #fontSize関数の挿入
    fontSize.font(fontSizeFrame)



    #autoStartFrame
    autoStartFrame = CTK.CTkFrame(settingsFrame, border_width=0, width=960 )
    autoStartFrame.grid(row=3, column=0, sticky="ew", padx=20, pady=5)

    gridSystem.resetGrid("row")
    gridSystem.resetGrid("column")

    #autoStartLabel
    defs.labelDef("autoStartLabel", autoStartFrame, "起動設定", "w", 20, 10, 10)

    #autoStart関数の挿入
    AutoStart.autoStart(autoStartFrame)



    #informationFrame
    informationFrame = CTK.CTkFrame(settingsFrame, border_width=0, width=960 )
    informationFrame.grid(row=4, column=0, sticky="ew", padx=20, pady=5)


    gridSystem.resetGrid("row")

    #informationLabel
    defs.labelDef("informationLabel", informationFrame, "アプリ情報", "w", 20, 10, 10)

    #informationButton
    infoButton = CTK.CTkButton(informationFrame, text="Show information")
    infoButton.grid(row=gridSystem.getGrid("row"), column=gridSystem.getGrid("column"), padx=80, pady=10)
    infoButton.bind("<Button-1>", lambda e:information.info())
    infoButton.bind("<Button-1>", lambda e:defs.delAttributes(settingWindow))


    #etcFrame
    etcFrame = CTK.CTkFrame(settingsFrame, border_width=0, width=960 )
    etcFrame.grid(row=5, column=0, sticky="ew", padx=20, pady=5)

    gridSystem.resetGrid("row")
    gridSystem.resetGrid("column")

    #etc...
    defs.labelDef("etc", etcFrame, "その他", "w", 20, 10, 10)

    #etcSetting関数の挿入
    etc.etcSetting(etcFrame)

    #closeButton
    closeButton = CTK.CTkButton(settingWindow, text="close")
    closeButton.grid(row=1, column=1, padx=20, pady=5, sticky="es")
    closeButton.bind("<Button-1>", lambda e:defs.close(settingWindow))