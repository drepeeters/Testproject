import pathlib

members_dir = pathlib.Path("./contents")

members_list = []
for members in members_dir.glob('*.md'):
  print(str(members).split('/')[1])
  members_list.append(str(members).split('/')[1])
  
print(members_list)
