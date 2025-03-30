# Application and Web Site Launcher


## ■ ダウンロード
### こちらのリンク先の最新の Latest から AppLauncher.exe をダウンロードしてください
https://github.com/Y0pp1r0k1/FavoriteLinks/releases

### ダウンロードできない場合
こちらのリンクをお試しください
[gofile.io](https://gofile.io/d/ff69ed5b-c6ad-4a93-b475-7ccd582d1738)


> [!WARNING]
このアプリはPyinstallerでアプリ化したため、Windows11 64-bitのみ使用可能になっています。ご了承ください


## ■ 作ったキッカケ
世の中には大量のアプリと大量のサイトがあります。これらの共通点としては、一つにまとめるという事ができないという事です。
もちろん、デスクトップ上にまとめたり、スタートメニューのフォルダにまとめることができます。しかし、これだとたくさんのアイコンであふれ帰ってしまい、分からなくなってしまいます。
そのため、アプリもサイトもまとめることができれば、とても便利だ！と気づき、作り始めました。


## ■ 用途
自分が好きなサイトやアプリをすべてこのアプリにまとめることができ、1クリックですべての管理が可能。


## ■ Wiki
過去の更新履歴とアプリの使い方をまとめています。初めて使う方はこちらを読むことをお勧めします。
https://github.com/Y0pp1r0k1/AppLauncher/wiki


## ■ 使用言語・ツール等一覧
> [!TIP]
これらの情報はアプリ内でも確認可能です


### 言語
<img src="https://img.shields.io/badge/Pythnon-3.12.4-3776AB.svg?logo=python&style=flat-square">


### 使用ツール

| Tool name | Version |
| ------------- | ------------- |
| Visual Studio Code | 1.98.2 |
| Pyinstaller  | 6.12.0  |
| PowerShell 7 | 7.4.5 |
| GitHub | ------ |
| Windows11 | 64bit 24H2 |


### 使用したライブラリ
| Package name | Version |
| ------------ | ---------------- |
| customtkinter | 5.2.2 |
| os | ---------------- |
| subprocess | ---------------- |
| sys | ---------------- |
| shutil | ---------------- |
| webbrowser | ---------------- |
| winshell | 0.6 |
| pandas | 2.2.3 |
| pathlib.path | ---------------- |
| pyinstaller | 6.11.1 |
| platform | ---------------- |
| pykakasi | 2.3.0 |
| pywin32 | 308 |


### 自作モジュール
| Package name | Explanation |
| ------------- | ------------ |
| allWidgetsMaker | For make all frames and links at startup app |
| CustomLinkDefs | For easy to write of links |
| CTkDefs | For easy to write of ctk commands |
| CSVReader | To read CSV content from some CSV files from data|
| gridSystem | To avoid having to think about grid numbers |
| startupShortcut | To add or delete the app on startup apps folder |
| linkManager | For management classes of links (add, delete or customize) |
| frameManager | All frame creation classes and some functions |


## ■ 機能一覧
**1. リンク機能**
  まとめておきたいサイト・アプリをほぼ無限（上限アリ）にまとめることができる

    これに関しては、現状、アプリのテキストのみのため、テキスト+アイコンという形にしたい。

**2. フォルダー機能 (制作中)**
  リンクを箇条書きでは抑えきれなくなる可能性があるため、フォルダーを作り、より多くのリンク先を置いておけるようにできる

    現状、CTkFrameに分けてまとめているが、CtkToplevelにして、個別のウィンドウで管理できるようにしたい。

**3. カスタム機能**
  リンク先の編集・追加・削除が可能

**4. 設定**
  ウィンドウのテーマ・ボタンの色など一般的な設定をする事が可能

  設定一覧

    ・外観の設定（appearance）

    ・アプリテーマの設定 (theme)

    ・リンクのフォントサイズ

    ・起動設定 (Windows スタートアップアプリに関するもの)

    ・アプリ情報 (使用したツール、パッケージ、開発環境などがアプリ内でも閲覧可能)

    ・その他 (今後追加予定。現在はお知らせウィンドウの表示切り替えのみ)

**~~5. ユーザー機能~~**
  ~~ユーザー機能により特別なことはありません。ただ作りたかっただけです！(・ω<) ﾃﾍﾍﾟﾛ~~

      ユーザー機能により、使用して得られるメリットがないため、削除しました。



## ■ フォルダ構成
ファイル管理苦手です。もっときれいに整理できるようになりたい。

> [!TIP]
一部のフォルダ・ファイルは gitignore により除外しています。

```
.
└── AppLauncher
    ├── data
    |   ├── icon.ico
    |   ├── custom.json
    |   ├── frame.csv
    |   ├── link.csv
    |   └── setting.csv
    ├──dist
    |   └── AppLauncher.exe
    ├── packages
    |   ├── CTkDefs.py
    |   ├── CustomLinkDefs.py
    |   ├── gridSystem.py
    |   ├── startupShortcut.py
    |   ├── frameManager.py
    |   ├── linkManager.py
    |   ├── allWidgetsMaker.py
    |   └── CSVReader.py
    ├── customizePackages
    |   ├── addFrame.py
    |   ├── deleteFrame.py
    |   ├── customFrame.py
    |   ├── addLink.py
    |   ├── deleteLink.py
    |   └── customLink.py
    ├── settings
    |   ├── Appearance.py
    |   ├── AutoStart.py
    |   ├── fontSize.py
    |   ├── information.py
    |   ├── etc.py
    |   └── Theme.py
    ├── Custom.py
    ├── AppLauncher.py
    ├── setting.py
    ├── Notes.py
    ├── AppLauncher.spec
    └── README.md
```

## ■ アプリ化について
アプリ化は AppLauncher.spec を使い、Pyinstallerで行っています。


## ■ 参考資料
これらの資料がなければこのアプリを作ることはできませんでした。
資料を作っていただいた方々に感謝します。

・[Python公式サイト](https://docs.python.org/ja/3.12/index.html)
・[CustomTkinter公式サイト](https://customtkinter.tomschimansky.com/documentation/)
・[Qiitaで参考にさせていただいた記事まとめ](https://qiita.com/Y0pp1r0k1/likes)
・[キカガクブログさんのPandas記事](https://www.kikagaku.co.jp/kikagaku-blog/pandas-dataframe/#i-3)
・[猩々博士さんが翻訳したCustomTkinterの入門](https://note.com/mega_gorilla/n/n6b9d7364c54e#74b06d35-285a-4be6-926b-650f69944ed1)
・[exeファイルのアイコンをカスタムする方法](https://various-python.hatenablog.com/entry/2021/07/11/003749)
・[おさだのホームページ よりtkinterの備忘録](https://ossa2019.stars.ne.jp/Remember/tkinter/tk1.html) \n
・その他AI (chatGPT, CodiumAI, etc...)

## ■ このアプリの今後
このアプリはゆくゆくWindowsのみではなく、Macにも対応させたいと思っています。また、今製作途中の設定・ユーザー機能（いらないかも）・リンクのカスタム機能が完成したら基本的には完成だと思っています。
上記の機能が完成したら、XなどのSNSにて公開し、より多くの方に知っていただき、利用して欲しいと思っています。
また、SNSへの公開により、フィードバックをいただき、よりよいアプリへと改善をしていきたいです。

## ■ 追記
なにかエラーや不自然な点、間違っている箇所がある場合は下記のX(twitter)よりDMにてご連絡ください。

## ■ 著作権について
**このアプリの自作発言、商法利用、二次配布を固く禁じます。**

## ■ 最終更新日
**2025/3/5**

## ■ 製作者
**Y0pp1r0k1** (X:[@Y0pp1r0k1](https://www.x.com/@y0pp1r0k1))
