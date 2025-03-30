import os
import sys
import shutil

from win32com.client import Dispatch

#正しいアプリ（exeファイル）のパスを取得する関数
def get_app_path() :

    #ファイル名の定義
    file_name = "AppLauncher.exe"

    if hasattr(sys, '_MEIPASS'): #実行環境の識別 (exeファイルの場合)

        user_dist_dir = os.path.join(os.environ["APPDATA"], "AppLauncher", "dist")  #ユーザーのAppDataフォルダ
        os.makedirs(user_dist_dir, exist_ok=True)                                   #フォルダがなければ作成

        #MEIPASSとAppDataのパスを定義
        original_app_path = os.path.join(sys._MEIPASS, "dist", file_name)
        user_app_path = os.path.join(user_dist_dir, file_name)

        if not os.path.exists(user_app_path) : #AppDataに存在しない場合、コピー

            shutil.copy(original_app_path, user_app_path)

        return user_app_path #AppDataのパスを返す

    else: #通常の実行環境の場合
        return os.path.join(os.path.abspath("."), "dist", file_name)


#スタートアップにアプリを追加する関数
def add_app_to_startup_apps(app_path) :

    #必要なパスの情報を取得
    userName = os.getlogin()
    startup_path = rf"c:\users\{userName}\appdata\roaming\microsoft\windows\Start Menu\programs\startup"
    shortcut_path = os.path.join(startup_path, "AppLauncher.lnk")

    #アプリショートカットを作成
    shell = Dispatch("WScript.Shell")
    shortcut = shell.CreateShortCut(shortcut_path)
    shortcut.TargetPath = app_path
    shortcut.WorkingDirectory = os.path.dirname(app_path)
    shortcut.Save()

    print(f"added AppLauncher for startup apps")


#スタートアップからアプリを削除する関数
def delete_app_from_startup_apps() :

    #必要なパスの情報を取得
    userName = os.getlogin()

    startup_path = rf"c:\users\{userName}\appdata\roaming\microsoft\windows\Start Menu\programs\startup"
    shortcut_path = os.path.join(startup_path, "AppLauncher.lnk")

    #スタートアップからショートカットを削除
    if os.path.exists(shortcut_path):

        os.remove(shortcut_path)

        print("removed AppLauncher at startup apps")

    else:
        print("AppLauncher is not exist in startup apps")