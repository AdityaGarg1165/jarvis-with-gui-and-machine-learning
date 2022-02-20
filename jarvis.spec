# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['C:/Users/pc/Documents/python/JARVIS/jarvis.py'],
             pathex=[],
             binaries=[],
             datas=[('C:/Users/pc/Documents/python/JARVIS/model', 'model/'), ('C:/Users/pc/Documents/python/JARVIS/modules', 'modules/'), ('C:/Users/pc/Documents/python/JARVIS/files', 'files/')],
             hiddenimports=[],
             hookspath=[],
             hooksconfig={},
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
          name='jarvis',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None )
