class info:
    author="n0nuser"
    description = "Executes a user-defined command without output."
    function = "User-defined"
    parameters = [ "COMMAND" ]
    content="""\
DELAY 200
GUI
DELAY 50
STRING terminal
ENTER
DELAY 500
CTRL s
STRING COMMAND\nENTER\nDELAY 1000\nCTRL q\n\
"""