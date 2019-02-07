from Object import Object
from Domain import Domain
from Logic import Logic

def testeAdaugare(logic):
	# Testeaza functionalitatea de adaugare
	newObj = Object(1, "test1", "desc1", 3.5, "loc1")
	logic.addObject(newObj)
	objects = logic.domain.getObjects()
	assert len(objects) == 1
	assert objects[0].getNume() == newObj.getNume()
	newObj2 = Object(2, "test2", "desc2", 2.6, "loc2")
	logic.addObject(newObj2)
	objects = logic.domain.getObjects()
	assert len(objects) == 2
	assert objects[0].getNume() == newObj.getNume()
	assert objects[0].getNume() != newObj2.getNume()
	assert objects[1].getNume() == newObj2.getNume()
	
def testeStergere(logic):
	# Testeaza functionalitatea de stergere
	objects = logic.domain.getObjects()
	assert len(objects) == 2
	logic.removeObject(1)
	objects = logic.domain.getObjects()
	assert len(objects) == 1

def testeModificare(logic):
	# Testeaza functionalitatea de modificare
	objects = logic.domain.getObjects()
	obj = Object(objects[0].getId(), objects[0].getNume(), objects[0].getDescriere(), objects[0].getPret(), objects[0].getLocatie())
	obj.setNume("testModify")
	assert objects[0] != obj
	logic.modifyObject(obj.getId(), obj)
	objects = logic.domain.getObjects()
	assert objects[0].getNume() == obj.getNume()

def testeMutare(logic):
	# Testeaza functionalitatea de mutare
	objects = logic.domain.getObjects()
	newObj = Object(3, "test", "desc", 3, "loc3")
	logic.addObject(newObj)
	newObj = Object(4, "test", "desc", 4, "loc3")
	logic.addObject(newObj)
	newObj = Object(5, "test", "desc", 2.6, "loc5")
	logic.addObject(newObj)
	nrloc3 = 0
	nrloc4 = 0
	for obj in logic.domain.getObjects():
		if obj.getLocatie() == "loc3":
			nrloc3 = nrloc3 + 1
		if obj.getLocatie() == "loc4":
			nrloc4 = nrloc4 + 1
	assert nrloc3 == 2
	assert nrloc4 == 0
	logic.moveObjects("loc3", "loc4")
	nrloc3 = 0
	nrloc4 = 0
	for obj in logic.domain.getObjects():
		if obj.getLocatie() == "loc3":
			nrloc3 = nrloc3 + 1
		if obj.getLocatie() == "loc4":
			nrloc4 = nrloc4 + 1
	assert nrloc3 == 0
	assert nrloc4 == 2

def testeConcatenare(logic):
	# Testeaza functionalitatea de concatenare
	nrModif = 0
	for obj in logic.domain.getObjects():
		if "new string added" in obj.getDescriere():
			nrModif = nrModif + 1
	assert nrModif == 0
	logic.concatDescription("new string added", 3)
	nrModif = 0
	for obj in logic.domain.getObjects():
		if "new string added" in obj.getDescriere():
			nrModif = nrModif + 1
	assert nrModif == 2

def testeRaportMaxim(logic):
	# Testeaza functionalitatea de raport maxim
	raport = logic.raportPrices()
	assert raport["loc4"] == 4
	assert raport["loc2"] == 2.6
	assert raport["loc5"] == 2.6

def testeRaportSuma(logic):
	# Testeaza functionalitatea de raport suma
	raport = logic.raportSumPrices()
	assert raport["loc4"] == 7
	assert raport["loc2"] == 2.6
	assert raport["loc5"] == 2.6

def testeRaportSort(logic):
	# Testeaza functionalitatea de sortare
	sort = logic.sortedObjects()
	assert sort[0].getPret() == 2.6
	assert sort[1].getPret() == 2.6
	assert sort[-1].getPret() == 4

def testeUndo(logic):
	# Testeaza functionalitatea de undo
	# Undo adaugare
	lista = logic.domain.getObjects()
	newObj = Object(3, "test", "desc", 3, "loc3")
	logic.addObject(newObj)
	listaNoua = logic.domain.getObjects()
	matching = 0
	for obj in lista:
		for obj2 in listaNoua:
			if obj.getNume() == obj2.getNume() and obj.getDescriere() == obj2.getDescriere() and obj.getPret() == obj2.getPret() and obj.getLocatie() == obj2.getLocatie():
				matching = matching + 1
	assert matching != len(listaNoua)
	assert matching == len(lista)
	logic.doUndo()
	listaNoua = logic.domain.getObjects()
	matching = 0
	for obj in lista:
		for obj2 in listaNoua:
			if obj.getNume() == obj2.getNume() and obj.getDescriere() == obj2.getDescriere() and obj.getPret() == obj2.getPret() and obj.getLocatie() == obj2.getLocatie():
				matching = matching + 1
	assert matching == len(listaNoua)
	assert matching == len(lista)

	# Undo stergere
	lista = logic.domain.getObjects()
	logic.removeObject(2)
	listaNoua = logic.domain.getObjects()
	assert len(lista) != len(listaNoua)
	logic.doUndo()
	listaNoua = logic.domain.getObjects()
	assert len(lista) == len(listaNoua)

	# Undo modificare
	lista = logic.domain.getObjects()
	newObj = Object(lista[0].getId(), "test", "desc", 3, "loc3")
	assert lista[0].getNume() != newObj.getNume()
	logic.modifyObject(lista[0].getId(), newObj)
	lista = logic.domain.getObjects()
	assert lista[0].getNume() == newObj.getNume()
	logic.doUndo()
	lista = logic.domain.getObjects()
	assert lista[0].getNume() != newObj.getNume()

	# Undo mutare
	nrLoc4 = 0
	nrLoc6 = 0
	for obj in logic.domain.getObjects():
		if obj.getLocatie() == "loc4":
			nrLoc4 = nrLoc4 + 1
		if obj.getLocatie() == "loc6":
			nrLoc6 = nrLoc6 + 1
	assert nrLoc4 == 2
	assert nrLoc6 == 0
	logic.moveObjects("loc4", "loc6")
	nrLoc4 = 0
	nrLoc6 = 0
	for obj in logic.domain.getObjects():
		if obj.getLocatie() == "loc4":
			nrLoc4 = nrLoc4 + 1
		if obj.getLocatie() == "loc6":
			nrLoc6 = nrLoc6 + 1
	assert nrLoc4 == 0
	assert nrLoc6 == 2
	logic.doUndo()
	nrLoc4 = 0
	nrLoc6 = 0
	for obj in logic.domain.getObjects():
		if obj.getLocatie() == "loc4":
			nrLoc4 = nrLoc4 + 1
		if obj.getLocatie() == "loc6":
			nrLoc6 = nrLoc6 + 1
	assert nrLoc4 == 2
	assert nrLoc6 == 0

	# Undo concatenare
	nrModif = 0
	for obj in logic.domain.getObjects():
		if "test undo concat" in obj.getDescriere():
			nrModif = nrModif + 1
	assert nrModif == 0
	logic.concatDescription("test undo concat", 3)
	nrModif = 0
	for obj in logic.domain.getObjects():
		if "test undo concat" in obj.getDescriere():
			nrModif = nrModif + 1
	assert nrModif == 2
	logic.doUndo()
	nrModif = 0
	for obj in logic.domain.getObjects():
		if "test undo concat" in obj.getDescriere():
			nrModif = nrModif + 1
	assert nrModif == 0

def teste():
	# Apeleaza testele existente pe un domain de test
	db = "testFile.txt"
	file = open(db, "w")
	file.write("")
	file.close()
	repo = Domain(db)
	logic = Logic(repo)
	testeAdaugare(logic)
	print("Teste adaugare trecute")
	testeStergere(logic)
	print("Teste stergere trecute")
	testeModificare(logic)
	print("Teste modificare trecute")
	testeMutare(logic)
	print("Teste mutare trecute")
	testeConcatenare(logic)
	print("Teste concatenare trecute")
	testeRaportMaxim(logic)
	print("Teste raport maxim trecute")
	testeRaportSuma(logic)
	print("Teste raport suma trecute")
	testeRaportSort(logic)
	print("Teste sortare trecute")
	testeUndo(logic)
	print("Teste undo trecute")
	input("Apasati ENTER pentru a continua")
