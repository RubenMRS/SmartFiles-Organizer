Set shell = CreateObject("WScript.Shell")
userProfile = shell.ExpandEnvironmentStrings("%USERPROFILE%")
pythonPath = userProfile & "\Desktop\SmartFiles\venv\Scripts\pythonw.exe"
scriptPath = userProfile & "\Desktop\SmartFiles\organizer.py"

' O comando final entre aspas para lidar com espaços e acentos
command = """" & pythonPath & """ """ & scriptPath & """"

shell.Run command, 0, False