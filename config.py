import soco
import json
import sys

conf = json.loads(open("conf.json", "r").read())
accts = json.loads(open("playlists.json", "r").read())

#player = soco.discover()
i = 0
tmp = []
for p in soco.discover():
    print(str(i) + ": " + p.player_name)
    tmp.append(p)

inp = int(raw_input("int: "))
conf['sonos_id'] = tmp[inp].uid
player = tmp[inp]


lists = player.get_sonos_playlists()['item_list']
new = []

for acct in accts:
    print("Which one of these playlists belongs to the callback: " + acct['name'])


    i = 0
    for l in lists:
        print(str(i) + ": " + l.title)
        #print(lists[inp].item_id)
        i+=1

    inp = int(raw_input("int: "))
    acct['id'] = lists[inp].item_id

print(accts)

conf = open("conf.json", "w").write(json.dumps(conf, indent=4, separators=(',', ': ')))
accts = open("playlists.json", "w").write(json.dumps(accts, indent=4, separators=(',', ': ')))

print("Done")