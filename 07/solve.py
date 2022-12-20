lines = [x.strip() for x in open("07/xinput.txt").readlines()]

files = {
    "b": {
        "a":{
            "file": 23123
        },
        "b.txt": 1431840
    }
}

current_path = ['/', 'a'] # /a/e/
print("/".join(current_path))
# print(files.get("b a"))