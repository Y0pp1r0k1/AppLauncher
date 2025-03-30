# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['AppLauncher.py'],
    pathex=[],
    binaries=[],
    datas=[
        ("data", "data"),
        ("data/icon.ico", "data"),
        ("data/setting.csv", "data"),
        ("data/frame.csv", "data"),
        ("data/link.csv", "data"),
        ("data/custom.json", "data"),
        ("dist", "dist"),
        ("dist/AppLauncher.exe", "dist")
    ],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=True,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [('v', None, 'OPTION')],
    name='AppLauncher',
    debug=True,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['data\\icon.ico'],
)
