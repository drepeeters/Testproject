import pathlib
import os

members_dir = pathlib.Path("./contents")

members_list = []
for members in members_dir.glob('*.md'):
  print(str(members).split('/')[1])
  members_list.append(str(members).split('/')[1])
  
print(members_list)
print(members_dir.absolute())

with open(os.path.join(str(members_dir.absolute()).rsplit('/', 1)[0], 'members_cache.txt'), 'w') as f:
    for member in members_list:
        print(member)
        f.write("%s\n" % member)
