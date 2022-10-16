class Team:
    def __init__(self, name, project, role):
        self.name=name
        self.project=project
        self.role=role

if __name__=="__main__":
    dev1=Team("Ricsi", "SolArch", "Frontend")
    dev2=Team("Angéla", "ZerTeng", "Tesztelő")
    dev3=Team("Peti", "KefERP", "Backend")
    dev4=Team("Éva", "KefERP", "Frontend")
    devlist=[dev1, dev2, dev3, dev4]
    dev_a=""
    dev_b=""
    for i in devlist:
        print("-- Developer létrehozva. --")
        print(i.name, "a", i.project, "-en dolgozik", i.role, "szerepkörben.")
    for i in range(len(devlist)):
        for j in range(len(devlist)):
            if devlist[i].project==devlist[j].project and devlist[i].name!=devlist[j].name:
                if dev_a!=devlist[j].name:
                    dev_a=devlist[i].name
                    dev_b=devlist[j].name
                    print(dev_a, "és", dev_b, "egy projekten dolgoznak.")