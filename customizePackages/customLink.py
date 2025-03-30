import customtkinter as CTK
import pandas as pd

from modules.CTkDefs import labelDef as label
from modules.CSVReader import settingCSVReader as setting
from modules.gridSystem import gridSystem
from modules.frameManager import updateFrame
from modules.linkManager import updateLink
from modules.linkManager import etcDefs
import modules.CTkDefs as defs


class customizeLink :

    font = setting("fontFamily")

    #編集するリンクを選ぶウィンドウ
    @classmethod
    def selectCustomLinkWindow(cls) :

        #Gridの初期化
        gridSystem.resetGrid("row")
        gridSystem.resetGrid("column")

        #ウィンドウの初期設定
        selectCustomLinkWindow = CTK.CTkToplevel()
        selectCustomLinkWindow.title("編集するリンクの選択")
        selectCustomLinkWindow.geometry("850x420")
        selectCustomLinkWindow.geometry("+400+300")
        selectCustomLinkWindow.focus_force()
        selectCustomLinkWindow.wm_attributes("-topmost", True)

        selectCustomLinkFrame = CTK.CTkFrame(master=selectCustomLinkWindow, border_width=0)
        selectCustomLinkFrame.grid(row=0, column=0, sticky="nsew", padx=0, pady=0)

        label("label", selectCustomLinkFrame, "編集するリンクの選択", "w", 15, 20 ,20)

        label("label", selectCustomLinkFrame, "編集するリンクのフレームを選択してください", "w", 12, 40, 20)
        #select frame optionMenu
        pulldownMenu1 = CTK.CTkOptionMenu(selectCustomLinkFrame, values=etcDefs.returnFrameNamelist(), font=(cls.font, 12))
        pulldownMenu1.grid(row=gridSystem.getGrid("row"), column=gridSystem.getGrid("column"), sticky="w", padx=60, pady=20)
        gridSystem.addGrid("column")

        #chooseButton
        button1 = CTK.CTkButton(selectCustomLinkFrame, text="フレームを選択", font=(cls.font, 12), width=60)
        button1.grid(row=gridSystem.getGrid("row"), column=gridSystem.getGrid("column"), sticky="w", padx=60, pady=20)

        gridSystem.addGrid("row")
        gridSystem.reduceGrid("column")

        label("label", selectCustomLinkFrame, "編集するリンクを選択してください", "w", 12, 40, 20)

        #select link OptionMenu
        pulldownMenu2 = CTK.CTkOptionMenu(selectCustomLinkFrame, values=["select the frame"], font=(cls.font, 12) ,state="disabled")
        pulldownMenu2.grid(row=gridSystem.getGrid("row"), column=gridSystem.getGrid("column"), sticky="w", padx=60, pady=20)

        #bindされた時に、pulldownMenu2のvaluesを対応するリンクたちに変更する
        button1.bind("<Button-1>", lambda e:customizeLink.returnLinkValues(pulldownMenu1, pulldownMenu2))


        gridSystem.addGrid("row")
        gridSystem.addGrid("column")

        #nextButton
        button2 = CTK.CTkButton(selectCustomLinkFrame, text="次へ進む", font=(cls.font, 12))
        button2.grid(row=gridSystem.getGrid("row"), column=gridSystem.getGrid("column"), sticky="w", padx=(150, 20), pady=25)
        button2.bind("<Button-1>", lambda e:customizeLink.customizeLinkWindow(selectCustomLinkWindow,pulldownMenu2))
        button2.bind("<Button-1>", lambda e:defs.delAttributes(selectCustomLinkWindow))

        #cancelButton
        button3 = CTK.CTkButton(selectCustomLinkFrame, text="キャンセル", font=(cls.font, 12))
        button3.grid(row=gridSystem.getGrid("row"), column=gridSystem.getGrid("column"), sticky="w", padx=(300, 80), pady=25)
        button3.bind("<Button-1>", lambda e:defs.close(selectCustomLinkWindow))

    #選択されたフレームに存在するリンクをリンクのオプションメニューに追加する関数
    def returnLinkValues(frameOptionMenu, linkOptionMenu) :

        #選択されたフレームにあるリンクの名前を取得
        values = etcDefs.returnOptionMenuValues(frameOptionMenu)

        #try文でオプションメニューのバリューを更新
        try :
            linkOptionMenu.configure(state="normal", values=values)
            linkOptionMenu.set(values[0])
        except IndexError : #リンクが存在しない場合、選択不可にし、分かりやすいように警告
            values = ["リンクが存在しません"] + values
            linkOptionMenu.configure(state="disabled", values=values)
            linkOptionMenu.set(values[0])

    #リンクを編集するウィンドウ
    @classmethod
    def customizeLinkWindow(cls, root, linkOptionMenu) :

        #gridの初期化
        gridSystem.resetGrid("row")
        gridSystem.resetGrid("column")

        customizeLinkFrame = CTK.CTkFrame(master=root, border_width=0)
        customizeLinkFrame.grid(row=0, column=0, sticky="nsew", padx=0, pady=0)


        #ウィジェットたち
        label("label", customizeLinkFrame, f"{updateLink.get_Link_Index(type="name", linkOptionMenu=linkOptionMenu)} を編集中", "w", 15, 20, 20)

        label("label", customizeLinkFrame, "リンクが所属するのフレームの選択", "w", 12, 40, 20)

        gridSystem.reduceGrid("row")
        gridSystem.addGrid("column")

        #フレーム選択のoptionMenu
        optionMenu1 = CTK.CTkOptionMenu(customizeLinkFrame, values=etcDefs.returnFrameNamelist(), font=(cls.font, 12))
        optionMenu1.grid(row=gridSystem.getGrid("row"), column=gridSystem.getGrid("column"), sticky="w", padx=20, pady=20)

        gridSystem.reduceGrid("column")
        gridSystem.addGrid("row")

        #リンクの名前のエントリー
        label("label", customizeLinkFrame, "表示されるリンクの名前", "w", 12, 40, 20)

        gridSystem.reduceGrid("row")
        gridSystem.addGrid("column")

        entry1 = CTK.CTkEntry(customizeLinkFrame, border_width=0, placeholder_text="Enter the link name", width=300, font=(cls.font, 12))
        entry1.grid(row=gridSystem.getGrid("row"), column=gridSystem.getGrid("column"), sticky="w", padx=20, pady=20)

        gridSystem.reduceGrid("column")
        gridSystem.addGrid("row")

        #リンクのパスorURLのエントリ－
        label("label", customizeLinkFrame, "リンク先のURL又はアプリパス", "w", 12, 40, 20)

        gridSystem.reduceGrid("row")
        gridSystem.addGrid("column")

        entry2 = CTK.CTkEntry(customizeLinkFrame, border_width=0, placeholder_text="Enter the URL or app path of the link", width=300, font=(cls.font, 12))
        entry2.grid(row=gridSystem.getGrid("row"), column=gridSystem.getGrid("column"), sticky="w", padx=20, pady=20)

        button1 = CTK.CTkButton(customizeLinkFrame, text="参照", font=(cls.font, 12), width=80)
        button1.grid(row=gridSystem.getGrid("row"), column=gridSystem.getGrid("column"), sticky="e", padx=0, pady=20)
        button1.bind("<Button-1>", lambda e:etcDefs.open_file(root=root, entry=entry2))
        button1.bind("<Button-1>", lambda e:defs.delAttributes(root=root))

        gridSystem.addGrid("row")

        #customizeButton
        button1 = CTK.CTkButton(customizeLinkFrame, text="決定", width=70, font=(cls.font, 12))
        button1.grid(row=gridSystem.getGrid("row"), column=gridSystem.getGrid("column"), sticky="e", padx=180, pady=20)
        button1.bind("<Button-1>", lambda e:updateLink.customize_link(linkIndex=index, frameOptionMenu=optionMenu1, linkTextEntry=entry1, URLEntry=entry2))
        button1.bind("<Button-1>", lambda e:defs.reStart(root=root))

        #allClearButton
        button2 = CTK.CTkButton(customizeLinkFrame, text="全て削除", width=70, font=(cls.font, 12))
        button2.grid(row=gridSystem.getGrid("row"), column=gridSystem.getGrid("column"), sticky="e", padx=100, pady=20)
        button2.bind("<Button-1>", lambda e:etcDefs.delete_all_link_data(frameOptionMenu=optionMenu1, linkTextEntry=entry1, urlEntry=entry2))

        #cancelButton
        button3 = CTK.CTkButton(customizeLinkFrame, text="キャンセル", width=70, font=(cls.font, 12))
        button3.grid(row=gridSystem.getGrid("row"), column=gridSystem.getGrid("column"), sticky="e", padx=20, pady=20)
        button3.bind("<Button-1>", lambda e:defs.close(root))

        #選択されたリンクのindex番号の取得
        index = updateLink.get_Link_Index(type="index", linkOptionMenu=linkOptionMenu)

        #Entry・OptionMenuに選択されたリンクのデータ挿入する
        updateLink.set_Link_Data(linkOptionMenu=linkOptionMenu, frameOptionMenu=optionMenu1, linkTextEntry=entry1, URLEntry=entry2)
