# Opdracht 1 lists
# Naam student:
# Groep:

mylist = []
dict_1 = {"id": 0, "voornaam": "", "achternaam": ""}
dict_2 = {"id": 0, "voornaam": "", "achternaam": ""}
dict_3 = {"id": 0, "voornaam": "", "achternaam": ""}
dict_4 = {"id": 0, "voornaam": "", "achternaam": ""}

mylist.append(dict_1)

mylist.append({"id": 1, "voornaam": "Henk", "achternaam": "Jan"})
mylist.append({"id": 2, "voornaam": "Truus", "achternaam": "Bakker"})
mylist.append({"id": 3, "voornaam": "Geert", "achternaam": "Molenaar"})
mylist.append({"id": 4, "voornaam": "Tinus", "achternaam": "Smit"})


#dict_1 = { "id": 1, "voornaam": "Henk", "achternaam": "Jan" }
#dict_2 = { "id": 2, "voornaam": "Truus", "achternaam": "Bakker" }
##dict_3 = { "id": 3, "voornaam": "Geert", "achternaam": "Molenaar" }
#dict_4 = { "id": 4, "voornaam": "Tinus", "achternaam": "Smit" }
#print (mylist[1]["voornaam"]) 
#print (mylist[1]["achternaam"])

Full_name = mylist[2]["voornaam"] + " " +  mylist[2]["achternaam"]
print (Full_name)


