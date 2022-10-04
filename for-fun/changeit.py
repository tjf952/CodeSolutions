"""
Correct the file output of a TEAMS python file
"""

choice = None
while choice not in ("1", "2"):
    choice = input('Enter "1" for manual input or "2" for file input: ')

if choice == "1":
    content = []
    print("Enter the content. Ctrl-D or Ctrl-Z to save it.")
    while True:
        try:
            line = input()
        except EOFError:
            break
        content.append(line)
    program = "\n".join(content)
    file = "output-tmp.py"
elif choice == "2":
    file = input("Enter the file that needs to change: ")
    try:
        program = open(file, "r").read()
    except:
        print("Invalid File. Exiting...")
        exit()

program = program.replace("\xa0", " ").encode("ascii", "ignore").decode("utf-8")
open(file, "w").write(program)
print("[+] Done")
