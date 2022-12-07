import fileinput, re
"""
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
"""
filesystem = {"/": { "_dir_": "/" }}
filesystem["/"][".."] = filesystem
pwd = filesystem

for line in fileinput.input():
    if line.strip() == "": continue

    dirname = None
    if "$" in line:
        cmd, _, path = re.findall("\$ (cd|ls)( ([a-z\./]+))?", line)[0]
       
        if cmd == "cd":
            if path == "..":
                size = 0
                for k,v in pwd.items():
                    if k == "_dirname_" or k == "..": continue
                    if type(v) is dict:
                        size += v["_size_"]
                    if type(v) is int:
                        size += v
                pwd["_size_"] = size

            pwd = pwd[path]
        
    elif "dir" in line:
        dirname = re.findall("dir ([a-z]+)", line)[0]
        pwd[dirname] = { "..": pwd, "_dir_": dirname } # add new directory
    else:
        size, filename = re.findall("(\d+) ([a-z\.]+)", line)[0]
        pwd[filename] = int(size) # add new file with size


#
# ---------------- PART 1 ------------------
#

def find_dict_sizes(pwd):
    size = 0
    dicts = []

    for path, size_or_dict in pwd.items():
        if path == ".." or path == "_dir_" or path == "_size_":
            continue

        if type(size_or_dict) is dict:
            _dicts = find_dict_sizes(size_or_dict)
            dicts.extend(_dicts)
    
    meta = (pwd["_dir_"], pwd["_size_"])
    dicts.append(meta)

    return dicts 

dicts = find_dict_sizes(filesystem["/"])


sum_of_dicts_less_than_100_000_bytes = 0
for name,size in dicts:
    if size < 100000:
        print(name,size)
        sum_of_dicts_less_than_100_000_bytes += size



print(sum_of_dicts_less_than_100_000_bytes)


#import pprint
#pp = pprint.PrettyPrinter(indent=2)
#pp.pprint(filesystem)

#
# ------ PART 2 ---------
#
total_disk_space = 7 * 10**7
required_disk_space = 3 * 10**7
used_disk_space = filesystem['/']['_size_']
disk_space_to_be_deleted = required_disk_space - (total_disk_space - used_disk_space)

print("Running update....")
print(f"Total disk space: {total_disk_space: >20} bytes")
print(f"Required disk space: {required_disk_space: >20} bytes")
print(f"Used disk space: {used_disk_space: >20} bytes")
print(f"Deleting {disk_space_to_be_deleted: > 20} bytes...")

# Find directory which is closest to disk_space_to_be_deleted
min_name = None
min_size = 9999999999999999 
for name, size in dicts:
    if size >= disk_space_to_be_deleted:
        if size < min_size:
            min_size = size
            min_name = name

print(f"Deleting directory '{min_name}', with size {min_size} bytes")

