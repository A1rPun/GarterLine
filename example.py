from garterline import Ansi, GarterLine

delimiter = GarterLine(" ]-[ ", "red").tie()
line = GarterLine("Hello", "yellow", delimiter=delimiter)
line.append("World", "green")
line.append("!")
example1 = GarterLine("[ ", "red", delimiter=line.tie()).append(" ]")
print(example1.tie())

blend = GarterLine(" ░ ", "black").tie()
percentReady90 = ["In", "other", "words", "it's", "almost", "completed"]
example2 = GarterLine(percentReady90, "blue", "green", delimiter=blend)
print(example2.tie())

print(Ansi.attribute("all")["reset"] + ":)")
