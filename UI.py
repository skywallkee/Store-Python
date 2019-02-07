from Object import Object

class UserInterface():
	def __init__(self, logic):
		self.menu = self.mainMenu()
		self.logic = logic
		
	def clear(self):
		print("\n"*100)
	
	def mainMenu(self):
		menu = {"1":"Adauga obiect (add)",
		"2":"Sterge obiect (sterge)",
		"3":"Modifica obiect (modifica)",
		"4":"Muta obiecte (muta)",
		"5":"Concatenare descrieri cu string (concat)",
		"6":"Raport cel mai mare pret (max)",
		"7":"Afisare obiecte ordonate crescator (sort)",
		"8":"Raport suma preturi locatii (suma)",
		"9":"Undo (undo)",
		"0":"Iesire"}
		return menu
		
	def display(self):
		self.clear()
		print("---Inventar---")
		for opt in range(0, len(self.menu)):
			opt = str(opt)
			print(opt + ". " + self.menu[opt])
		print("--------------")
	
	def validCommandLine(self, opt):
		if opt == "":
			return False
		opt = opt.split(" ")
		optiuni = ["add", "sterge", "modifica", "muta", "concat", "max", "sort", "suma", "undo"]
		for optiune in opt:
			if optiune not in optiuni:
				return False
		return True

	def getCommandLine(self, cmd):
		cmds = cmd.split(" ")
		for i, cmd in enumerate(cmds):
			if cmd == "add":
				cmds[i] = "1"
			if cmd == "sterge":
				cmds[i] = "2"
			if cmd == "modifica":
				cmds[i] = "3"
			if cmd == "muta":
				cmds[i] = "4"
			if cmd == "concat":
				cmds[i] = "5"
			if cmd == "max":
				cmds[i] = "6"
			if cmd == "sort":
				cmds[i] = "7"
			if cmd == "suma":
				cmds[i] = "8"
			if cmd == "undo":
				cmds[i] = "9"
		return cmds

	def validOption(self, opt):
		if opt in self.menu or opt == "-1" or self.validCommandLine(opt):
			return True
		return False
	
	def getOption(self):
		opt = input("Introduceti optiunea dorita: ")
		while not self.validOption(opt):
			opt = input("Optiune invalida, incercati din nou: ")
		return opt
	
	def validPret(self, pret):
		if pret == "":
			return False
		numbers = "1234567890"
		for number in numbers:
			pret = pret.replace(number, "")
		if pret == "" or pret == ".":
			return True
		return False
	
	def validId(self, ido):
		if ido == "":
			return False
		numbers = "1234567890"
		for number in numbers:
			ido = ido.replace(number, "")
		if ido == "":
			return True
		return False
		
	def requestNewObject(self, cmd):
		ido = self.logic.getUnusedID()
		nume = ""
		while nume == "":
			nume = input("Dati numele obiectului: " + cmd)
		descriere = ""
		while descriere == "":
			descriere = input("Dati descrierea obiectului: " + cmd)
		pret = "invalid"
		while not self.validPret(pret):
			pret = input("Dati pretul obiectului: " + cmd)
		pret = float(pret)
		locatie = ""
		while len(locatie) < 4:
			locatie = input("Dati locatia obiectului: " + cmd)
		return Object(ido, nume, descriere, pret, locatie)
	
	def requestId(self, cmd):
		ido = 0
		while self.logic.existingId(ido) == False:
			ido = "invalid"
			while not self.validId(ido):
				ido = input("Dati idul obiectului: " + cmd)
			ido = int(ido)
		return ido

	def requestPret(self, cmd):
		pret = -1
		ok = False
		while not ok:
			pret = input("Dati pretul obiectului: " + cmd)
			if self.validPret(pret):
				ok = True
				pret = float(pret)
		return pret
	
	def doOption(self, option):
		if self.validCommandLine(option):
			commands = self.getCommandLine(option)
			cmds = True
		else:
			commands = [option]
			cmds = False
		for option in commands:
			print(option)
			if option == "1":
				if cmds == True:
					cmd = "(add)"
				else:
					cmd = ""
				self.clear()
				newObj = self.requestNewObject(cmd)
				self.logic.addObject(newObj)
				print("S-a adaugat obiectul: " + str(newObj.getId()) + " " + newObj.getNume() + " " + newObj.getDescriere() + " " + str(newObj.getPret()) + " " + newObj.getLocatie())
			elif option == "2":
				if cmds == True:
					cmd = "(sterge)"
				else:
					cmd = ""
				self.clear()
				ido = self.requestId(cmd)
				if self.logic.removeObject(ido) == True:
					print("Obiectul cu idul " + str(ido) + " a fost sters")
				else:
					print("Nu s-a putut sterge obiectul")
			elif option == "3":
				if cmds == True:
					cmd = "(modifica)"
				else:
					cmd = ""
				self.clear()
				ido = self.requestId(cmd)
				modObj = self.requestNewObject(cmd)
				modObj.setId(ido)
				if self.logic.modifyObject(ido, modObj) == True:
					print("Obiectul cu idul " + str(ido) + " a fost modificat")
				else:
					print("Nu s-a putut modifica obiectul")
			elif option == "4":
				if cmds == True:
					cmd = "(muta)"
				else:
					cmd = ""
				self.clear()
				sala_inceput = input("Dati sala din care sa se mute obiectele: " + cmd)
				sala_final = input("Dati sala in care sa se mute obiectele: " + cmd)
				if self.logic.moveObjects(sala_inceput, sala_final):
					print("Obiectele din sala " + sala_inceput + " au fost mutate in sala " + sala_final)
				else:
					print("Nu exista sala de inceput data")
			elif option == "5":
				if cmds == True:
					cmd = "(concat)"
				else:
					cmd = ""
				self.clear()
				concat = input("Dati stringul cu care se concateneaza: " + cmd)
				pret = self.requestPret(cmd)
				if self.logic.concatDescription(concat, pret) == True:
					print("Descrierile au fost concatenate cu succes!")
				else:
					print("Nu s-a modificat niciun obiect")
			elif option == "6":
				self.clear()
				raport = self.logic.raportPrices()
				print("----Raport locatii----")
				for locatie in raport:
					print(locatie + ": " + str(raport[locatie]))
			elif option == "7":
				self.clear()
				obiecte = self.logic.sortedObjects()
				print("----Lista obiecte sortate----")
				for obj in obiecte:
					print(str(obj.getId()) + " " + obj.getNume() + " " + obj.getDescriere() + " " + str(obj.getLocatie()) + " " + str(obj.getPret()))
			elif option == "8":
				self.clear()
				raport = self.logic.raportSumPrices()
				print("----Raport locatii----")
				for locatie in raport:
					print(locatie + ": " + str(raport[locatie]))
			elif option == "9":
				self.clear()
				if self.logic.doUndo() == True:
					print("Undo realizat cu succes!")
				else:
					print("Nu se mai poate face niciun undo")
			input("Apasati ENTER pentru a continua.")
