import git
import pymsteams
import os
from pathlib import Path
cwd = os.getcwd()
print(cwd)

content_path = Path(cwd)

repo = git.Repo(content_path)
# myTeamsMessage = pymsteams.connectorcard("https://radboudumc.webhook.office.com/webhookb2/97a88c45-447f-4147-9e80-5e7c013f7501@b208fe69-471e-48c4-8d87-025e9b9a157f/IncomingWebhook/91295428cf8449f6a4a10aa8dc2f2e82/533f880f-0558-4b1f-9c63-1b76a1b4a439")

# Gives a list of the differing objects
diff_list = repo.head.commit.diff("HEAD~1", R=True)

for diff in diff_list:
    if diff.change_type == "D":
        deleted_filename = diff.deleted_file
        if "contents/" in diff.a_path:
            print(diff.a_path)
            # myTeamsMessage.text(f"This is an automated message. {deleted_filename} is deleted from content/pages/members. "
            #                     f"Please contact any of the webteam members to make sure the deleted files are added back or confirm that the deletion is correct.")
            # myTeamsMessage.send()

    elif diff.change_type == "A":
        print("file is added")
        print(diff.new_file)

    elif diff.change_type == "M":
        print("file is modified")
        print(diff.a_path)
    elif diff.change_type == "R":
        print("file name is changed")
        print(diff.a_path)
        print(diff.b_path)
