import json
back = json.load(open("results.json", encoding="utf-8"))
print(f"读到了 {len(back)} 个文件的统计")
