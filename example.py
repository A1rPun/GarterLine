from garterline import GarterLine

def example1():
    line = GarterLine("Hello", "yellow")
    line.append("World", "green")
    line.append("!")
    result = GarterLine("[ ", "red").append(" ]")
    delimiter = GarterLine(" ]-[ ", "red")
    return result.tie(line.tie(delimiter))

def example2():
    percentReady90 = ["In", "other", "words", "it's", "almost", "completed"]
    result = GarterLine(percentReady90, "blue", "green")
    dlmtr = GarterLine(" ░ ", "black", "green")
    return result.tie(dlmtr)

def example3():
    result = GarterLine("SyntaxError:", "black", "blue")
    result.append("(unicode error) 'unicodeescape'", background="lightblue", attribute="underlined")
    result.append("codec can't decode bytes in position 0-1:", background="cyan")
    result.append("truncated \\uXXXX escape", background="lightcyan")
    return result.tie("▶", True)

def clear(msg=""):
    return GarterLine(msg, attribute="reset").tie()

#"Lisää viinaa silmät liikkuu :)"
print(clear("GarterLine examples"))
print(example1())
print(example2())
print(example3())
print(clear())
