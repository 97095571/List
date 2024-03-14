# Opdracht 2 lists
# Naam student:
# Groep:


rivier_info = {
    "rijn": ["nederland", "duitsland", "Frankrijk"],
    "maas": ["nederland", "belgië", "duitsland"],
    "nijl": ["egypte", "soedan", "oeganda"]
}

rivieren = list(rivier_info.keys())
# rivieren is nu een list met alleen de riviernamen: ['rijn', 'maas', 'nijl']

# Hier jouw code.....

#print (rivieren[0])
#print (rivier_info["rijn"][1])
#print (rivieren[1])
##print (rivier_info["maas"][1])
#print (rivieren[2])
#print (rivier_info["nijl"][1])


print (f"De rivier {rivieren[1].capitalize()} stroomt onder andere door {rivier_info['rijn'][1].capitalize()}")

print (f"De rivier {rivieren[1].capitalize()} stroomt onder andere door {rivier_info['maas'][0].capitalize()}")

print (f"De rivier {rivieren[2].capitalize()} stroomt onder andere door {rivier_info['nijl'][2].capitalize()}")