class Logic():
	"""
	Clasa de tip logic ce contine:
	domain - baza de date
	"""
	
	def __init__(self, domain):
		# constructor
		self.domain = domain
		self.undo = []
		
	def existingId(self, ide):
		# verifica daca idul ide exista in baza de date
		# date intrare: ide - int
		# date iesire: True daca ide exista, altfel False
		ids = self.domain.getIds()
		for ido in ids:
			if ide == ido:
				return True
		return False
		
	def getUnusedID(self):
		# returneaza un id inexistent in baza de date
		# date de iesire: ido - int
		ids = self.domain.getIds()
		for ido in range(1, len(ids)+2):
			if ido not in ids:
				return ido
				
	def addObject(self, obj):
		# adauga obiectul obj in baza de date
		# date de intrare: obj - de tip Object
		# date de iesire: True daca s-a creat obiectul, altfel False
		self.undo.append([self.domain.getObjects(), self.domain.getIds()])
		self.domain.add(obj)
		return True
		
	def removeObject(self, ido):
		# scoate obiectul cu idul ido din baza de date
		# date de intrare: ido - int
		# date de iesire: True daca s-a sters obiectul, altfel False
		self.undo.append([self.domain.getObjects(), self.domain.getIds()])
		objects = self.domain.getObjects()
		ids = self.domain.getIds()
		removeObj = None
		for obj in objects:
			if obj.getId() == ido:
				objects.remove(obj)
				ids.remove(ido)
				self.domain.setObjects(objects)
				self.domain.setIds(ids)
				return True
		return False
		
	def modifyObject(self, ido, modObj):
		# modifica obiectul cu idul ido cu valorile lui modObj
		# date de intrare: ido - int, modObj - Object
		# date de iesire: True daca obiectul a fost modificat, altfel False
		self.undo.append([self.domain.getObjects(), self.domain.getIds()])
		objects = self.domain.getObjects()
		modified = False
		for obj in objects:
			if obj.getId() == ido:
				obj.setNume(modObj.getNume())
				obj.setDescriere(modObj.getDescriere())
				obj.setPret(modObj.getPret())
				obj.setLocatie(modObj.getLocatie())
				modified = True
		self.domain.setObjects(objects)
		return modified

	def moveObjects(self, sala_inceput, sala_final):
		# modifica sala tuturor obiectelor ce au sala curenta egala
		# cu sala_inceput in sala_final
		# date de intrare: sala_inceput - string, sala_final - string
		# date de iesire: True daca a fost mutat vreun obiect, altfel False
		self.undo.append([self.domain.getObjects(), self.domain.getIds()])
		objects = self.domain.getObjects()
		moved = False
		for obj in objects:
			if obj.getLocatie() == sala_inceput:
				moved = True
				obj.setLocatie(sala_final)
		self.domain.setObjects(objects)
		return moved

	def concatDescription(self, concat, pret):
		# concateneaza descrierea tuturor obiectele mai scumpe decat pret
		# cu stringul din concat
		# date de intrare: concat - string, pret - float
		# date de iesire: True daca s-a concatenat vreun obiect, altfel False
		self.undo.append([self.domain.getObjects(), self.domain.getIds()])
		objects = self.domain.getObjects()
		modified = False
		for obj in objects:
			if obj.getPret() >= pret:
				modified = True
				obj.setDescriere(obj.getDescriere() + concat)
		self.domain.setObjects(objects)
		return modified

	def raportPrices(self):
		# returneaza un dictionar de locatii unde cheia este locatia
		# iar valoarea este cel mai mare pret din acea locatie
		# date de iesire: raport - dictionar de forma {locatie: pret}
		# unde locatie - string, pret - float
		objects = self.domain.getObjects()
		raport = {}
		for obj in objects:
			if obj.getLocatie() in raport:
				if obj.getPret() > raport[obj.getLocatie()]:
					raport[obj.getLocatie()] = obj.getPret()
			else:
				raport[obj.getLocatie()] = obj.getPret()
		return raport

	def sortedObjects(self):
		# returneaza lista de obiecte sortate dupa pret
		# date de iesire: objects - lista de obiecte
		objects = self.domain.getObjects()
		for i in range(0, len(objects)):
			for j in range(0, len(objects)):
				if objects[i].getPret() <= objects[j].getPret():
					objects[i], objects[j] = objects[j], objects[i]
		return objects
                
	def raportSumPrices(self):
		# returneaza un dictionar de locatii unde cheia este locatia
		# iar valoarea este suma preturilor din acea locatie
		# date de iesire: raport - dictionar de forma {locatie: pret}
		# unde locatie - string, pret - float
		objects = self.domain.getObjects()
		raport = {}
		for obj in objects:
			if obj.getLocatie() in raport:
				raport[obj.getLocatie()] = raport[obj.getLocatie()] + obj.getPret()
			else:
				raport[obj.getLocatie()] = obj.getPret()
		return raport

	def doUndo(self):
		# restaureaza lista de obiecte la starea precedenta ultimei operatii
		# date de iesire: True daca s-a facut operatia de undo, False altfel
		if len(self.undo) > 0:
			objects, ids = self.undo.pop()
			self.domain.setObjects(objects)
			self.domain.setIds(ids)
			return True
		return False
