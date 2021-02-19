import json

witih open('148.json') as artfile:
art = json.load(artfile)
print(art['description'])