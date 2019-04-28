import json


with open("src.json", "r") as f:
    src = f.read()
file = json.loads(src)
keyWord = input("input a KeyWord\n")
for f in file['objects']:
    if keyWord in f['lyric']:
        print(f'{keyWord} found in {f["title"]}')

print("_____")




