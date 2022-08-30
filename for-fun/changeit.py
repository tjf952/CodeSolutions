"""
content = []
print("Enter the content. Ctrl-D or Ctrl-Z to save it.")
while True:
	try:
		line = input()
	except EOFError:
		break
	content.append(line)
program = "\n".join(content)
"""
file = input("Enter the file that needs to change: ")
try:
    program = open(file, "r").read()
except:
    print("Invalid File. Exiting...")
    exit()
print(f"===PROGRAM===\n\n{program}\n\n===END===")
program = program.replace("\xa0", " ").encode("ascii", "ignore").decode("utf-8")
print(f"===NEW===\n\n{program}\n\n===END===")
open(file, "w").write(program)
