import pandas as pd

import modules.CSVReader as CSVReader

class gridSystem :

    setting_csv_path = CSVReader.return_true_csv_path("setting")

    #row, column の現在の値の取得
    @classmethod
    def getGrid(cls, type) : #clsはこのgridSystemクラスが持つ、グローバル変数全てのこと。（ここでは csv のこと）

        #CSVファイルのパス
        csv = pd.read_csv(cls.setting_csv_path, index_col=0, na_values=["NaN", "Na"])

        if type == "row" :

            #rowの取得
            Row = csv.loc["row_1", "row"]

            return Row

        elif type == "column" :

            #columnの取得

            Column = csv.loc["row_1", "column"]

            return Column

        else :

            print("error")



    #row, column を+1する関数
    @classmethod
    def addGrid(cls, type) :

        #CSVファイルのパス
        csv = pd.read_csv(cls.setting_csv_path, index_col=0, na_values=["NaN", "Na"])

        if type == "row" :

            #csvファイルから読み込み
            row = csv.loc["row_1", "row"]
            addRow = row + 1

            #csvファイルの書き換え
            updateRow = csv.replace({"row" : {row : addRow}})
            updateRow.to_csv(cls.setting_csv_path)

        elif type == "column" :

            #csvファイルから読み込み
            column = csv.loc["row_1", "column"]
            addColumn = column + 1

            #csvファイルの書き換え
            updateColumn = csv.replace({"column" : {column : addColumn}})
            updateColumn.to_csv(cls.setting_csv_path)

        else :

            print("error")


    #setting.csvのrow, column を0に設定する関数
    @classmethod
    def resetGrid(cls, type) :

        csv = pd.read_csv(cls.setting_csv_path, index_col=0, na_values=["NaN", "Na"])

        default = 0

        if type == "row" :

            #CSVのrowを読み込み
            Row = csv.loc["row_1", "row"]

            #書き換え+更新
            resetRow = csv.replace({"row" : {Row : default}})
            resetRow.to_csv(cls.setting_csv_path)

        elif type == "column" :

            #CSVのcolumnを読み込み
            Column = csv.loc["row_1", "column"]

            #書き換え+更新
            resetColumn = csv.replace({"column" : {Column : default}})
            resetColumn.to_csv(cls.setting_csv_path)

        else :

            print("error")


    #row, column を―1する関数
    @classmethod
    def reduceGrid(cls, type) :

        csv = pd.read_csv(cls.setting_csv_path, index_col=0, na_values=["NaN", "Na"])

        if type == "row" :

            #csvファイルの読み込み
            row = csv.loc["row_1", "row"]
            reduceRow = row - 1

            #書き換え+更新
            updateRow = csv.replace({"row" : {row : reduceRow}})
            updateRow.to_csv(cls.setting_csv_path)

        elif type == "column" :

            #csvファイルの読み込み
            column = csv.loc["row_1", "column"]
            reduceColumn = column - 1

            #書き換え+更新
            updateColumn = csv.replace({"column" : {column : reduceColumn}})
            updateColumn.to_csv(cls.setting_csv_path)

        else :

            print("error")