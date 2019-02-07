from Object import Object
import copy

class Domain():
	"""
	Clasa de tip domain ce contine:
	database - fisier text
	objects - lista de obiecte
	ids - lista de inturi
	"""
		
	def __init__(self, db):
		# constructor
		self.database = db
		self.checkDB(db)
		self.objects = []
		self.ids = []
		self.loadObjects()
		
	def checkDB(self, db):
		# verifica daca fisierul baza de date este existent, daca nu il creaza
		# date intrare: db - numele fisierului baza de date
		try:
			f = open(db, "r")
		except:
			f = open(db, "w")
		f.close()
			
	def loadObjects(self):
		# incarca obiectele din fisierul baza de date
		self.objects = []
		dbfile = open(self.database, "r")
		for line in dbfile:
			line = line.strip().split(" ")
			newObj = Object(int(line[0]), line[1], line[2], float(line[3]), line[4])
			self.objects.append(newObj)
			self.ids.append(int(newObj.getId()))
		dbfile.close()
		
	def saveObjects(self):
		# salveaza obiectele curente in baza de date
		f = open(self.database, "w")
		for obj in self.objects:
			line = str(obj.getId()) + " " + obj.getNume() + " " + obj.getDescriere() + " " + str(obj.getPret()) + " " + obj.getLocatie()
			f.write(line + "\n")
		f.close()
	
	def getObjects(self):
		# returneaza lista de obiecte din baza de date
		# date iesire: objects - lista de obiecte
		return copy.deepcopy(self.objects)
	
	def setObjects(self, obj):
		# seteaza lista de obiecte cu una noua
		# date intrare: objects - lista de obiecte
		self.objects = obj
		self.saveObjects()
	
	def getIds(self):
		# returneaza lista de iduri
		# date de iesire: ids - lista de inturi
		return copy.deepcopy(self.ids)
	
	def setIds(self, ids):
		# seteaza lista de iduri cu una noua
		# date de intrare: ids - lista de inturi
		self.ids = ids
	
	def add(self, obj):
		# adauga un obiect in baza de date
		# date de intrare: obj - de tip Obiect
		self.objects.append(obj)
		self.ids.append(obj.getId())
		self.saveObjects()
