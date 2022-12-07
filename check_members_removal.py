import pathlib

members_dir = pathlib.Path("./content/images/theses")

for member in members_dir.glob('*.md'):
    print(member)
