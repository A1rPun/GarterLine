from garterline import GarterLine

delimiter = GarterLine(' ]-[ ', 'red').tie()
line = GarterLine('Hello', delimiter=delimiter)
line.append('World', 'green')
line.append('!')
example1 = GarterLine('[ ', 'default', delimiter=line.tie()).append(' ]')
print(example1.tie())
