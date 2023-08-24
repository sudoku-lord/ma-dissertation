import os
num_lines = {}
for filename in os.listdir("concordances"):
    if ".txt" in filename:
        with open(os.path.join("concordances", filename), 'r') as f:
            line_count = len(f.readlines())
            name = filename.split(".")[0]
            num_lines[name] = line_count
sorted_lines = dict(sorted(num_lines.items(), key=lambda item: item[1]))
for entry in sorted_lines:
    print(f"num_lines[{entry}] = {num_lines[entry]}")
