import pathlib

members_dir = pathlib.Path("./contents")

members_list = []
for members in members_dir.glob('*.md'):
  print(str(members).split('/')[1])
  members_list.append(str(members).split('/')[1])
  
print(members_list)

with open('members_cache.txt', 'w') as f:
    for member in members_list:
        f.write("%s\n" % member)
