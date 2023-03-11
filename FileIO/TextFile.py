import File as f

class textfile:

    filex = None

    def __init__(self, filename, create=True):
        self.filex = f.file()
        self.filex.setfilename(filename + ".txt", True)
        if create:
            self.create()

    def create(self):
        self.filex.create()

    def delete(self):
        self.filex.delete()

    def addline(self, line):
        with open(self.filex.filename, "a") as filez:
            filez.write(line + "\n")
            filez.close()

    def getfilesize(self):
        with open(self.filex.filename, "r") as filezr:
            line = filezr.readlines()
        return len(line)

    def removeline(self, lineid):
        with open(self.filex.filename, "r") as filezr:
            line = filezr.readlines()
        if lineid >= 0 and lineid < len(line):
            del line[lineid]
            with open(self.filex.filename, "w") as filezw:
                filezw.write("".join(line))
            filezr.close()
            filezw.close()
        else:
            print("Out of bounds!")

    def retrievecontents(self):
        with open(self.filex.filename, "r") as filez:
            line = filez.readlines()
            if self.getfilesize() > 0:
                for linex in line:
                    print(linex)
            else:
                print("File empty!")

    def clear(self):
        while self.getfilesize() > 0:
            self.removeline(self.getfilesize() - 1)
