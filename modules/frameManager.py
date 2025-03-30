import pandas as pd

import modules.CustomLinkDefs as CLD
import modules.CSVReader as CSVReader


"""フレームを追加するクラス"""
class makeFrame :

    frame_csv_path = CSVReader.return_true_csv_path("frame")
    frameCSV = pd.read_csv(frame_csv_path, sep=",", index_col=0, na_values=["NaN", "Na"])

    #フレームの追加関数
    @classmethod
    def add_frame(cls, frameNameEntry) :

        frameName = frameNameEntry.get()

        newFrameData = {
            "frameTitle" : frameName,
            "frameName" : CLD.convertKana(frameName),
            "row" : makeFrame.returnGrid("row"),
            "column" : makeFrame.returnGrid("column"),
        }

        #DataFrameに変換
        cls.frameCSV = pd.concat([cls.frameCSV, pd.DataFrame([newFrameData])], ignore_index=True)
        cls.frameCSV.to_csv(cls.frame_csv_path)

        #indexの再生成
        CSVReader.resetIndex("frame")

        print(f"<< {frameName} >>が正常に追加されました")

    #gridの値を返す関数
    @classmethod
    def returnGrid(cls, type) :

        if type == "row" :

            lastRow = cls.frameCSV.loc[cls.frameCSV.index[-1], "row"]      #最後の行のrow
            alsoLastRow = cls.frameCSV[cls.frameCSV["row"] == lastRow]     #最後の行のrowと同じ値の列の取得

            if len(alsoLastRow) == 4 :

                return lastRow + 1

            else :
                return lastRow

        elif type == "column" :

            lastColumn = cls.frameCSV.loc[cls.frameCSV.index[-1], "column"]

            if lastColumn == 4 :

                return 0

            else :
                return lastColumn + 1


"""フレームを削除するクラス"""
class delFrame :

    #csvファイルパスの取得
    frame_csv_path = CSVReader.return_true_csv_path("frame")
    link_csv_path = CSVReader.return_true_csv_path("link")

    #csvファイルの読み込み
    frameCSV = pd.read_csv(frame_csv_path, sep=",", index_col=0, na_values=["NaN", "Na"])
    linkCSV = pd.read_csv(link_csv_path, sep=",", index_col=0, na_values=["NaN", "Na"])

    #フレームの削除関数
    @classmethod
    def delete_frame(cls, optionMenu) :

        targetText = optionMenu.get()       #削除するフレームの名前の取得
        targetFrameColumn = "frameName"     #検索対象の列(Frame)
        targetLinkColumn = "root"           #検索対象の列(Link)


        delFrameIndex = cls.frameCSV[cls.frameCSV[targetFrameColumn] == targetText].index        #削除する行のindex番号の取得
        delLinksIndex = cls.linkCSV[cls.linkCSV[targetLinkColumn] == targetText].index           #削除するフレームの中にあるリンクのindex番号の取得

        #フレームの削除
        cls.frameCSV = cls.frameCSV.drop(index=delFrameIndex)

        #リンクの削除
        for index in delLinksIndex :

            cls.linkCSV = cls.linkCSV.drop(index=index)

        else :
            print(f"<< {targetText} >> に属するリンクを全て削除しました")

        cls.frameCSV.to_csv(cls.frame_csv_path)
        cls.linkCSV.to_csv(cls.link_csv_path)

        #indexの再生成
        CSVReader.resetIndex("frame")
        CSVReader.resetIndex("link")

        delFrame.resetFrameGrid()

        print(f"<< {targetText} >>が正常に削除されました")

    #削除されたとき、frame.csvの row, columnを修正する関数
    @classmethod
    def resetFrameGrid(cls) :

        #最新のCSVの読み込み
        frameCSV = pd.read_csv(cls.frame_csv_path, sep=",", index_col=0, na_values=["NaN", "Na"])

        #情報を入れるリストの定義
        row = []
        column = []

        #値の定義
        reRow = 0
        reColumn = 0

        #情報の挿入
        for Number in range(len(frameCSV)) :

            row.append(int(frameCSV.loc[Number, "row"]))        #row
            column.append(int(frameCSV.loc[Number, "column"]))  #column

        #row, columnの修正
        for index in range(len(frameCSV)) :

            #値の書き換え
            frameCSV.loc[index, ["row", "column"]] = reRow, reColumn

            reColumn += 1   #reColumnを1増やす

            if reColumn == 5 :  #reColumnが5になったら

                reRow += 1      #reRowを1増やす
                reColumn = 0    #reColumnを0に戻す

        #CSVの更新
        frameCSV.to_csv(cls.frame_csv_path)

        print("正常にrow, columnが更新されました")


"""フレームを更新するクラス"""
class updateFrame :

    #csvファイルパスの取得
    link_csv_path = CSVReader.return_true_csv_path("link")
    frame_csv_path = CSVReader.return_true_csv_path("frame")

    #csvファイルの読み込み
    frameCSV = pd.read_csv(frame_csv_path, sep=",", index_col=0, na_values=["NaN", "Na"])
    linkCSV = pd.read_csv(link_csv_path, sep=",", index_col=0, na_values=["NaN", "Na"])

    #フレームの更新関数
    @classmethod
    def update_frame(cls, entry, optionMenu) :

        #必要な情報の取得
        oldFrameName = optionMenu.get()                                                     #更新前のフレーム名
        newFrameName = entry.get()                                                          #更新後のフレーム名
        frameNameIndex = cls.frameCSV[cls.frameCSV["frameName"] == oldFrameName].index      #更新前のフレームのindex
        frameNamesLinkIndex = cls.linkCSV[cls.linkCSV["root"] == oldFrameName].index        #更新前のフレームに属するリンクのindex

        #フレームの更新
        cls.frameCSV.loc[frameNameIndex, ["frameTitle", "frameName"]] = [newFrameName, CLD.convertKana(newFrameName)]
        cls.frameCSV.to_csv(cls.frame_csv_path)

        for index in frameNamesLinkIndex :

            #フレームに属するリンクの更新
            cls.linkCSV.loc[index, "root"] = newFrameName

        else :
            print(f"<< {oldFrameName} >> に属するリンクを全て更新しました")

        cls.linkCSV.to_csv(cls.link_csv_path)

        #indexの再生成
        CSVReader.resetIndex("frame")
        CSVReader.resetIndex("link")

        print(f"<< {oldFrameName} >>が正常に更新されました")

    #フレームにフレームの名前を挿入する関数
    @classmethod
    def setFrameName(cls, entry) :

        entryName = entry.get()

        return entryName
