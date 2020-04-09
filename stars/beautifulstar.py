import json

with open('stars_all.json') as f:
    data = json.load(f)

stars = data["JSON"]["edges"]
print("~~~Have Given {} stars~~~".format(len(stars)))

for i, star in enumerate(stars): 
    dsp = star["node"]
    print("No.{:04d}: {}".format(i+1, dsp["nameWithOwner"]))
    print(dsp["description"])
    print(dsp["url"])
    print()
