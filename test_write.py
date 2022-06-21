import json

datas = {
    "format_version": "v1",
    "name": "test",
    "id": "test",
    "desp": "测试包管理器",
    "author": ["SteveUbuntu"],
    "system": "Windows",
    "system_versionlimits": ["8.1", "10"],
    "machine": "AMD64",
    "need": []
}

with open("info.json", "w") as f:
    a = json.dumps(datas, indent=4)
    f.write(a)
    f.close()