from teste import teste
from Domain import Domain
from Logic import Logic
from UI import UserInterface

if __name__ == "__main__":
        file = "myPrettyDomain.txt"
        domain = Domain(file)
        logic = Logic(domain)
        UI = UserInterface(logic)

        running = True
        while running:
                UI.display()
                option = UI.getOption()
                if option == "0":
                        running = False
                elif option == "-1":
                        teste()
                else:
                        UI.doOption(option)

