import pathlib

members_dir = pathlib.Path("./content")

with open('members.txt', 'w') as fp:
    for member in members_dir.glob('*.md'):
        fp.write(member)
        fp.write('\n')
