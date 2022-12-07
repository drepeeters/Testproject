import pathlib
import os

members_dir = pathlib.Path("./contents")

current_members = []
for members in members_dir.glob('*.md'):
  print(str(members).split('/')[1])
  current_members.append(str(members).split('/')[1])
  print("Loaded all the members currently in contents")
  

previous_members = []
with open("day1.txt", 'r') as f:
    for line in f:
        previous_members.append(line.rstrip('\n'))
    print("Previous list of members is loaded")
 

print(current_members)
print(previous_members)

if set(previous_members).issubset(set(current_members)):
    print('Same List')
else:
    print('Not Same list')
