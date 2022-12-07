import pathlib

members_dir = pathlib.Path("./contents")

members_list = []
for members in members_dir.glob('*.md'):
  print(members)
  members_list.append(members)
  
print(members_list)
 
  
f = open("day1.txt", "r")

print(f.read())
