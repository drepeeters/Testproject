import pathlib

members_dir = pathlib.Path("./contents")

with open('members.txt', 'w') as fp:
    for member in members_dir.glob('*.md'):
        fp.write(str(member))
        fp.write('\n')
