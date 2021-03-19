class info:
    author="n0nuser"
    description = "Executes a user-defined command."
    function = "User-defined"
    parameters = [ "COMMAND" ]
    content="""\
DELAY 200
GUI
DELAY 50
STRING terminal
ENTER
DELAY 750
STRING COMMAND\nENTER\nDELAY 1000\n\
"""