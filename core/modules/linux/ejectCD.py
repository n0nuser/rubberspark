class info:
    author="n0nuser"
    description = "Ejects CD."
    function = "Troll"
    parameters = [ ]
    content="""\
DELAY 500
GUI
DELAY 50
STRING terminal
ENTER
DELAY 500
STRING nohup eject && exit
ENTER
DELAY 150