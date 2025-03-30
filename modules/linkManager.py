import pandas as pd
from tkinter import filedialog

import modules.CustomLinkDefs as CLD
import modules.CSVReader as CSVReader

"""リンクの追加クラス"""
class addLink :

    #フォントファミリー + リンクのフォントサイズの取得
    font = CSVReader.settingCSVReader("fontFamily")
    lFontSize = CSVReader.settingCSVReader("linkFontSize")

    link_csv_path = CSVReader.return_true_csv_path("link")
    linkCSV = pd.read_csv(link_csv_path, sep=",", index_col=0, na_values=["NaN", "Na"])

    #csvファイルへの追加関数
    @classmethod
    def add_to_csv(cls, entry1, entry2, pulldownMenu) :

        #新しいリンクの要素生成+代入
        newLink = addLink.getTexts(entry1=entry1, entry2=entry2, pulldownMenu=pulldownMenu)

        #新しい行(row)の辞書データ
        NewLinkData = {

            "root" : newLink[0],
            "name" : CLD.convertKana(newLink[1]),
            "linkText" : newLink[1],
            "padx" : 50,
            "url" : newLink[2],
            "def" : addLink.returnDefText(newLink[2])

        }

        #DataFrameに変換
        newLinkCSV = pd.concat([cls.linkCSV, pd.DataFrame([NewLinkData])], ignore_index=True)

        #CSVに出力（追記）
        newLinkCSV.to_csv(cls.link_csv_path, sep=",", encoding="utf-8")

        #フレーム別に並び替え+CSVに出力
        newCSV = pd.read_csv(cls.link_csv_path, index_col=0, na_values=["NaN", "Na"])
        newCSV = newCSV.sort_values(by=["root", "name"])
        newCSV.to_csv(cls.link_csv_path, sep=",", encoding="utf-8")

        #indexの再生成
        CSVReader.resetIndex("link")

        print(f"<< {NewLinkData["linkText"]} >>が正常に追加されました")

    #リンクの url が アプリかリンクかの判別
    @classmethod
    def returnDefText(cls, defText) :

            #リンクかアプリかの判別+最後のdefの追加
            if "https" in defText or "http" in defText :

                return "linkContent"

            elif ".exe" in defText :

                return "AppContent"

            else :
                return "NaN"

    #新しいリンクに必要なテキストたちのget関数
    @classmethod
    def getTexts(cls, entry1, entry2, pulldownMenu) :

        linkTitle = entry1.get()            #リンクの名前
        linkURL = entry2.get()              #リンクのURL
        frame = pulldownMenu.get()          #リンクを追加するフレーム
        list = [frame, linkTitle, linkURL]  #リスト化

        return list



"""リンクの削除クラス"""
class deleteLink :

    link_csv_path = CSVReader.return_true_csv_path("link")
    linkCSV = pd.read_csv(link_csv_path, index_col=0, na_values=["NaN", "Na"])

    #リンクの削除（CSVファイルから削除）をする関数
    @classmethod
    def delete_from_csv(cls, optionMenu) :

        #削除するリンクの名前を取得
        delLinkName = optionMenu.get()

        #削除するために必要な変数
        target_column = "linkText"      #検索する列名
        target_value = delLinkName      #検索するテキスト

        #削除する行のindex番号の取得
        delLinkIndex = cls.linkCSV[cls.linkCSV[target_column] == target_value].index

        #リンクの削除
        linkCSV = cls.linkCSV.drop(index=delLinkIndex)
        linkCSV.to_csv(cls.link_csv_path)

        #indexの再生成
        CSVReader.resetIndex("link")

        print(f"<< {delLinkName} >>が正常に削除されました")



"""リンクの更新クラス"""
class updateLink :

    link_csv_path = CSVReader.return_true_csv_path("link")
    linkCSV = pd.read_csv(link_csv_path, index_col=0, na_values=["NaN", "Na"])

    #リンクの更新（CSVファイルの更新）をする関数
    @classmethod
    def customize_link(cls, linkIndex, frameOptionMenu, linkTextEntry, URLEntry) :

        #新しいリンクの情報を取得
        newFrame = frameOptionMenu.get()    #フレーム
        newLinkText = linkTextEntry.get()   #リンクのテキスト
        newURL = URLEntry.get()             #URL

        #リンクの更新
        cls.linkCSV.loc[linkIndex, ["root", "name", "linkText", "url", "def"]] = [newFrame, newLinkText, newLinkText, newURL, updateLink.returnDefText(newURL)]
        cls.linkCSV.to_csv(cls.link_csv_path, sep=",", encoding="utf-8")

        #フレーム別に並び替え+CSVに出力
        cls.linkCSV = pd.read_csv(cls.link_csv_path, index_col=0, na_values=["NaN", "Na"])
        cls.linkCSV = cls.linkCSV.sort_values(by=["root", "name"])
        cls.linkCSV.to_csv(cls.link_csv_path, sep=",", encoding="utf-8")

        #indexの再生成
        CSVReader.resetIndex("link")

        print(f"<< {newLinkText} >>が正常に更新されました")


    #更新するリンクのindex番号を取得またはlinkTextを取得する関数
    @classmethod
    def get_Link_Index(cls, type, linkOptionMenu) :

        if type == "index":

            target_link_name = linkOptionMenu.get()            #選択されたリンクの名前を取得
            search_column = "linkText"                          #検索する列名

            #検索した列名からヒットした行の取得
            linkData = cls.linkCSV[cls.linkCSV[search_column] == target_link_name].index
            return linkData

        elif type == "name" :

            #選択されたリンクの名前を取得
            target_link_name = linkOptionMenu.get()
            return target_link_name

    #選択されたリンクデータの挿入
    @classmethod
    def set_Link_Data(cls, linkOptionMenu, frameOptionMenu, linkTextEntry, URLEntry) :

        target_link_name = linkOptionMenu.get()            #選択されたリンクの名前を取得
        search_column = "linkText"                          #検索する列名

        #検索した列名からヒットした行の取得
        linkData = cls.linkCSV[cls.linkCSV[search_column] == target_link_name].to_dict(orient="records")

        #データの挿入
        frameOptionMenu.set(linkData[0]["root"])                 #フレーム
        linkTextEntry.insert(0, linkData[0]["linkText"])         #リンクのテキスト
        URLEntry.insert(0, linkData[0]["url"])                   #URL

    #リンクのURLのdefを返す関数
    @classmethod
    def returnDefText(cls, url) :

        if "https" in url or "http" in url :

            return "linkContent"

        elif ".exe" in url :

            return "AppContent"
        else :
            return "NaN"


"""リンクに関する関数をまとめたクラス"""
class etcDefs :

    #リンクの情報を適応する場所からすべて削除する関数
    @classmethod
    def delete_all_link_data(cls, frameOptionMenu, urlEntry, linkTextEntry) :

        #frameOptionMenuのすべての値を取得
        frameOptionMenuValue = frameOptionMenu.cget("values")

        #元のリストに値 none を追加
        allValues = ["None"] + frameOptionMenuValue

        frameOptionMenu.configure(values=allValues)       #OptionMenuのテキストを更新
        frameOptionMenu.set(allValues[0])                 #set
        urlEntry.delete(0, 'end')                         #URLEntryのテキストを削除
        linkTextEntry.delete(0, 'end')                    #LinkTextEntryのテキストを削除

    #エクスプローラーから.exeファイルを選択する関数
    @classmethod
    def open_file(cls, root, entry):
        file_path = filedialog.askopenfilename(title="open file", filetypes=[("exeファイル", "*.exe")], parent=root)
        if file_path :

            entry.delete(0, "end")
            entry.insert("end", file_path)

    #選択されたフレームから、オプションメニューのValueの作成
    @classmethod
    def returnOptionMenuValues(cls, optionMenu) :

        #CSVファイルの読み込み
        link_csv_path = CSVReader.return_true_csv_path("link")
        linkCSV = pd.read_csv(link_csv_path, sep=",", index_col=0)

        #選択したフレームの情報を取得
        frame = optionMenu.get()

        #選択したフレームに存在するリンクをリストに変換するための変数
        target_string = frame           #選択されたフレーム
        column_to_search = "root"       #検索する列名
        column_to_extract = "linkText"  #取得する列名

        #選択されたフレームに存在するリンクをリストに保存
        frameLinks = linkCSV[linkCSV[column_to_search].str.contains(target_string, na=False)][column_to_extract].tolist()

        return  frameLinks

    @classmethod
    def returnFrameNamelist(cls) :

        #optionMenuValue
        frame_csv_path = CSVReader.return_true_csv_path("frame")
        csv = pd.read_csv(frame_csv_path, sep=",", index_col=0, na_values=["NaN", "Na"])        #CSVファイルの読み込み
        row_indices = csv.index.tolist()                                                        #行番号(index)を取得
        frameNames = csv.loc[row_indices, "frameName"].tolist()                                 #frameNameをリスト形式にして保存

        return frameNames