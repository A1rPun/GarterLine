from garterline import GarterLine

def example1():
    line = GarterLine()
    line.color("red")
    line.text("Hello")
    line.color("blue")
    line.text("World")
    return line

def example2():
    percentReady90 = ["In", "other", "words", "it's", "almost", "completed"]
    line = GarterLine()
    line.color("blue", "green")
    line.text(" ░ ".join(percentReady90))
    return line

def example3():
    line = GarterLine()
    line.color("black", "blue")
    line.text("SyntaxError")
    line.color(background="lightblue")
    line.text("(unicode error) 'unicodeescape'")
    line.color(background="cyan")
    line.text("codec can't decode bytes in position 0-1")
    line.color(background="lightcyan")
    line.text("truncated \\uXXXX escape")
    return line

def clear(msg=""):
    return GarterLine().text(msg).color()

#"Lisää viinaa silmät liikkuu :)"
print(clear("GarterLine examples"))
print(example1())
print(example2())
print(example3())
print(clear())
