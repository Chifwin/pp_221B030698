import json


with open("sample-data.json", 'r', encoding="utf-8") as f:
    data = json.load(f)
print("Interface Status")
print("="*85)
mask = "{:<50} {:<20} {:<7} {:<5}"
print(mask.format("DN", "Description", "Speed", "MTU"))
print(mask.format("-"*50, '-'*20, '-'*7, '-'*5))

for i in sorted(data['imdata']):
    cur = i['l1PhysIf']['attributes']
    print(mask.format(cur['dn'], cur.get('description', '') , cur['speed'], cur['mtu']))