# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['control.py', 'CRLF_KNN.py', 'CRLF_Logistic.py', 'feature_extract_url.py', 'featurepossess.py', 'GUI.py', 'main.py', 'Normal_KNN.py', 'Normal_Logistic.py', 'Sql_KNN.py', 'Sql_Logistic.py', 'test.py', 'train.py', 'Traversal_KNN.py', 'Traversal_Logistic.py', 'user_test.py', 'Xss_KNN.py', 'Xss_Logistic.py'],
             pathex=['H:\\QT_python\\try1'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='control',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False )
