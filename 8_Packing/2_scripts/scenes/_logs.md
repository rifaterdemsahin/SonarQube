Warning: PowerShell detected that you might be using a screen reader and has disabled PSReadLine for compatibility purposes. If you want to re-enable it, run 'Import-Module PSReadLine'.

PS C:\projects\SonarQube> python C:\projects\SonarQube\8_Packing\2_scripts\scenes\generate_scenes.py
Traceback (most recent call last):
  File "C:\projects\SonarQube\8_Packing\2_scripts\scenes\generate_scenes.py", line 4, in <module>
    import yaml
ModuleNotFoundError: No module named 'yaml'
PS C:\projects\SonarQube> pip install pyyaml
Defaulting to user installation because normal site-packages is not writeable
Collecting pyyaml
  Downloading pyyaml-6.0.2.tar.gz (130 kB)
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Preparing metadata (pyproject.toml) ... done
Building wheels for collected packages: pyyaml
  Building wheel for pyyaml (pyproject.toml) ... done
  Created wheel for pyyaml: filename=pyyaml-6.0.2-cp314-cp314-win_amd64.whl size=45184 sha256=c45375c792969e6256209128e394a3743008f9b294a657dc2c40a8c16e5a5ae3
  Stored in directory: c:\users\pexabo\appdata\local\pip\cache\wheels\16\d3\3b\1f603c475e2c00f8749b9c112c874a87093b6fc1ef4a11ce07
Successfully built pyyaml
Installing collected packages: pyyaml
Successfully installed pyyaml-6.0.2

[notice] A new release of pip is available: 25.0.1 -> 25.1.1
[notice] To update, run: python.exe