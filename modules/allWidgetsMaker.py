import pandas as pd
import customtkinter as CTK
import os
import re

import modules.CSVReader as CSVReader
import modules.CustomLinkDefs as CLD
from modules.gridSystem import gridSystem


"""すべてのリンクの作成を作るクラス"""
class allLinkMaker :

    link_csv_path = CSVReader.return_true_csv_path("link")
    frame_csv_path = CSVReader.return_true_csv_path("frame")

    linkCSV = pd.read_csv(link_csv_path, sep=",", index_col=0, na_values=["NaN", "NA"], encoding="utf-8")
    frameCSV = pd.read_csv(frame_csv_path, sep=",", index_col=0, na_values=["NaN", "NA"], encoding="utf-8")

    fontSize = CSVReader.settingCSVReader("linkFontSize")
    font = CSVReader.settingCSVReader("fontFamily")

    @classmethod
    def make_all_main_widgets(cls, root) :

        #データの取得に必要なリストの定義
        #リンク
        frame = []
        name = []
        text = []
        url = []
        truePath = []
        define = []

        #フレーム
        frameNameList = []
        frameTitleList = []
        row = []
        column = []

        #フレームのデータを格納
        for frameNumber in range(len(cls.frameCSV)) :

            #フレームデータの取得
            frameNameList.append(cls.frameCSV.loc[frameNumber, "frameName"])       #フレームの名前
            frameTitleList.append(cls.frameCSV.loc[frameNumber, "frameTitle"])     #タイトル
            row.append(int(cls.frameCSV.loc[frameNumber, "row"]))                  #row
            column.append(int(cls.frameCSV.loc[frameNumber, "column"]))            #column

        #リンクのデータを格納
        for linkNumber in range(len(cls.linkCSV)) :

            #リンクデータの取得
            frame.append(cls.linkCSV.loc[linkNumber, "root"])                      #フレーム
            name.append(cls.linkCSV.loc[linkNumber, "name"])                       #リンクの名前
            text.append(cls.linkCSV.loc[linkNumber, "linkText"])                   #リンクのテキスト
            url.append(cls.linkCSV.loc[linkNumber, "url"])                         #URL
            truePath.append(allLinkMaker.returnUserName(url[linkNumber]))          #アプリパス
            define.append(cls.linkCSV.loc[linkNumber, "def"])                      #def

        #リンク,フレームの作成
        for frameNumber in range(len(cls.frameCSV)) :

            #フレームの作成
            frameNameList[frameNumber] = CTK.CTkFrame(root, border_width=0)
            frameNameList[frameNumber].grid(row=row[frameNumber], column=column[frameNumber], padx=(20,0), pady=(10,5), sticky="nsew")

            #フレームタイトルの追加
            CLD.TitleContent(frameNameList[frameNumber], frameTitleList[frameNumber], frameTitleList[frameNumber])

            #gridSystem.addGrid("row")

            #同じフレームの名前の列のindexの取得
            frameName = cls.frameCSV.loc[frameNumber, "frameName"]
            frameLinks = cls.linkCSV[cls.linkCSV["root"] == frameName].index

            for linkNumber in frameLinks :

                #範囲外エラーを防ぐもの
                if linkNumber + 1 < len(cls.linkCSV) :

                    next_frame = cls.linkCSV.loc[linkNumber + 1, "root"]

                else:
                    next_frame = None  # 最後の要素の場合

                #リンクの作成
                #Webサイトの場合
                if define[linkNumber] == "linkContent" :

                    CLD.linkContent(root=frameNameList[frameNumber], name=name[linkNumber], text=text[linkNumber], url=url[linkNumber])

                #アプリの場合
                elif define[linkNumber] == "AppContent" :

                    CLD.AppContent(root=frameNameList[frameNumber], name=name[linkNumber], text=text[linkNumber], exeUrl=truePath[linkNumber])

                else :  #その他
                    print(f"define error : {name[linkNumber]} >> {define[linkNumber]}")

                #gridの初期化
                if next_frame is not None and next_frame is not frame[linkNumber] :

                        gridSystem.resetGrid("row")
                        gridSystem.resetGrid("column")

                else :
                    print("also frame")
            else :
                print(f"made {frameName}'s links")
        else :
            print("end make links")

    #URLの{userName}をユーザー名に変換
    @classmethod
    def returnUserName(cls, text) :

        #ユーザー名の取得
        userName = os.getlogin()

        if r"{UserName}" in text :

            #URLの{UserName}をユーザー名に変換
            truePath = re.sub(r"{UserName}", userName, text)

            return truePath

        else :
            return text