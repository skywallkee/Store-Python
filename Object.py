class Object():
	""" 
	Clasa de tip object ce contine fieldurile:
    Id - int
    nume - string nenul
    descriere - string nenul
    pret - float
    locatie - string de minim 4 caractere
	"""
	def __init__(self, ido, nume, descriere, pret, locatie):
		# constructor
		self.id = ido
		self.nume = nume
		self.descriere = descriere
		self.pret = pret
		self.locatie = locatie
		
	def getId(self):
		# returneaza idul obiectului
		# date iesire: id - int
		return self.id
		
	def setId(self, ido):
		# seteaza idul obiectului cu valoarea lui ido
		# date intrare: ido - int
		self.id = ido
		
	def getNume(self):
		# returneaza numele obiectului
		# date iesire: nume - string
		return self.nume
		
	def setNume(self, nume):
		# seteaza numele obiectului cu valoarea lui nume
		# date intrare: nume - string
		self.nume = nume
		
	def getDescriere(self):
		# returneaza descrierea obiectului
		# date iesire: descriere - string
		return self.descriere
		
	def setDescriere(self, descriere):
		# seteaza descrierea obiectului cu valoarea lui descriere
		# date intrare: descriere - string
		self.descriere = descriere
		
	def getPret(self):
		# returneaza pretul obiectului
		# date iesire: pret - int
		return self.pret
		
	def setPret(self, pret):
		# seteaza pretul obiectului cu valoarea lui pret
		# date intrare: pret - int
		self.pret = pret
		
	def getLocatie(self):
		# returneaza locatia obiectului
		# date iesire: locatie - string
		return self.locatie
		
	def setLocatie(self, locatie):
		# seteaza locatia obiectului cu valoarea lui locatie
		# date intrare: locatie - string
		self.locatie = locatie
