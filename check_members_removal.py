import pathlib
import os

members_dir = pathlib.Path("./contents")

members_list = []
for members in members_dir.glob('*.md'):
  print(str(members).split('/')[1])
  members_list.append(str(members).split('/')[1])
  print("Loaded all the members currently in contents")
  
print(members_list)

previous_members = []
with open("day1.txt", 'r') as f:
    for line in f:
        previous_members.append(line.rstrip('\n'))
    print("Previous list of members is loaded")
 

print(members_list)
print(previous_members)

