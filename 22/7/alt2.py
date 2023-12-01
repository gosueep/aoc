from collections import defaultdict

file = open('input.txt', 'r')
lines = file.readlines()


curr = ['/']
size = defaultdict(int)
subs = defaultdict(list)
dirs = {'/'}
i = 1
while i < len(lines):

    l = lines[i].split()
    path = '/' + '/'.join(curr[1:])
    dirs.add(path)

    if l[0] == '$':
        if l[1] == 'cd':
            if l[2] == '..':
                curr.pop()
            else:
                curr.append(l[2])

    elif l[0] == 'dir':
        if path == '/':
            subpath = path + l[1]
        else:
            subpath = path + '/' + l[1]
        subs[path].append(subpath)

    else:
        size[path] += int(l[0])

    i += 1


def getsize(dir):
    subdirSize = 0
    for subdir in subs[dir]:
        subdirSize += getsize(subdir)
    return size[dir] + subdirSize


avail = 70000000
needed = 30000000
used = getsize('/')
left = avail - used
needDel = needed - left

cands = []
for dir in dirs:
    s = getsize(dir)
    if s >= needDel:
        cands.append(s)

print(min(cands))
