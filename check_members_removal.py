import pathlib

members_dir = pathlib.Path("./content")

for member in members_dir.glob('*.md'):
    print(member)
