# Garterline
Creating beautiful colored lines for your CLI

```python
delimiter = GarterLine(' ]-[ ', 'red').tie()
line = GarterLine('Hello')
line.append('World', 'green')
line.append('!')
print(line.tie(delimiter))
```
>  Hello ]-[ World ]-[ !
