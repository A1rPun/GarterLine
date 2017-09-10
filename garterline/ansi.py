class Ansi(object):
    @staticmethod
    def attribute(attr):
        return Attributes[attr or 'none']
    @staticmethod
    def background(color):
        return BackgroundColor[color or 'none']
    @staticmethod
    def foreground(color):
        return ForegroundColor[color or 'none']

Attributes = {
    "none": {},
    "all": { "apply": "\e[1m\e[2m\e[4m\e[5m\e[7m\e[8m", "reset": "\e[0m" },
    "blink": { "apply": "\e[5m", "reset": "\e[25m" },
    "bold": { "apply": "\e[1m", "reset": "\e[21m" },
    "dim": { "apply": "\e[2m", "reset": "\e[22m" },
    "hidden": { "apply": "\e[8m", "reset": "\e[28m" },
    "reverse": { "apply": "\e[7m", "reset": "\e[27m" },
    "underlined": { "apply": "\e[4m", "reset": "\e[24m" },
}

ForegroundColor = {
    "none": "",    
    "default": "\e[39m",
    "black": "\e[30m",
    "red": "\e[31m",
    "green": "\e[32m",
    "yellow": "\e[33m",
    "blue": "\e[34m",
    "magenta": "\e[35m",
    "cyan": "\e[36m",
    "lightgray": "\e[37m",
    "darkgray": "\e[90m",
    "lightred": "\e[91m",
    "lightgreen": "\e[92m",
    "lightyellow": "\e[93m",
    "lightblue": "\e[94m",
    "lightmagenta": "\e[95m",
    "lightcyan": "\e[96m",
    "white": "\e[97m",
}

BackgroundColor = {
    "none": "",
    "default": "\e[49m",
    "black": "\e[40m",
    "red": "\e[41m",
    "green": "\e[42m",
    "yellow": "\e[43m",
    "blue": "\e[44m",
    "magenta": "\e[45m",
    "cyan": "\e[46m",
    "lightgray": "\e[47m",
    "darkgray": "\e[100m",
    "lightred": "\e[101m",
    "lightgreen": "\e[102m",
    "lightyellow": "\e[103m",
    "lightblue": "\e[104m",
    "lightmagenta": "\e[105m",
    "lightcyan": "\e[106m",
    "white": "\e[107m",
}
