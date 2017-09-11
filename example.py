from garterline import Ansi, GarterLine

line = GarterLine("Hello", "yellow")
line.append("World", "green")
line.append("!")
example1 = GarterLine("[ ", "red").append(" ]")
delimiter = GarterLine(" ]-[ ", "red")
print(example1.tie(line.tie(delimiter)))

percentReady90 = ["In", "other", "words", "it's", "almost", "completed"]
example2 = GarterLine(percentReady90, "blue", "green")
dlmtr = GarterLine(" ░ ", "black")
print(example2.tie(dlmtr))

blend = GarterLine("▶")
coolStats = ["3000kg"]
example3 = GarterLine(coolStats, "black", "blue")
example3.append("6.000.000!!!", background="lightblue")
example3.append("more cool stats", background="cyan")
example3.append("one more cool stat", background="lightcyan")
print(example3.tie(blend, true))

print(Ansi.attribute("all")["reset"] + ":)")
