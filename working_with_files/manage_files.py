import os

print(f"your actual directorie: {os.getcwd()}")
print("listing files on archives folder: ")

archives_list = os.listdir("archives")

for archive in archives_list:
    print(archive)

# Automation file to your extension folder
for archive in archives_list:
    if ".bat" in archive:
        os.rename(f"archives/{archive}", f"archives/bat/{archive}")

    if ".txt" in archive:
        os.rename(f"archives/{archive}", f"archives/txt/{archive}")

print("\nDone!, files moved to their respective folders: ")
