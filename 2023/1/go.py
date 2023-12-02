f = open('input')
total = 0
for l in f:
    l = l.replace('one', 'o1ne')
    l = l.replace('two', 't2wo')
    l = l.replace('three', 't3hree')
    l = l.replace('four', 'f4our')
    l = l.replace('five', 'f5ive')
    l = l.replace('six', 's6ix')
    l = l.replace('seven', 's7even')
    l = l.replace('eight', 'e8ight')
    l = l.replace('nine', 'n9ine')
    for c in l:
        if c.isdigit():
            one = c
            break
    for c in l[::-1]:
        if c.isdigit():
            two = c
            break
    total += int(f"{one}{two}")
print(total)