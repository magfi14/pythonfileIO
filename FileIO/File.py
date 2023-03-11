import os
import Directory as d


class file:

    path = ""
    filename = ""

    def __init__(self):
        pass

    def setfilename(self, filename, pipe=True):
        if not pipe:
            self.filename = filename
        else:
            self.setpath()
            self.filename = (self.path + "/" +
                             filename).replace(chr(92), chr(47))
        return self.filename

    def create(self, mode="a"):
        with open(self.filename, mode) as filex:
            filex.write("")
            filex.close()

    def delete(self, filename=""):
        try:
            if len(filename) == 0:
                self.delete(self.filename)
            else:
                os.remove(filename)
        except FileNotFoundError:
            print("File {f} does not exist.".format(f=self.filename))

    def getextension(self):
        filenamex = self.filename.split(sep=".")
        return filenamex[-1]

    def getfilename(self):
        filenamex = self.filename.replace(chr(47), " ")
        filenamex = filenamex.split()
        return filenamex[-1]

    def getpath(self):
        filenamex = self.filename.replace(chr(47), " ")
        filenamex = filenamex.split()
        filenamey = ""
        idx = 0
        for folder in filenamex:
            if idx < len(filenamex) - 1:
                filenamey += folder + ("/" if idx < len(filenamex) - 2 else "")
            idx += 1
        return filenamey

    def getfilelist(self, ext=""):
        path = self.setpath()
        filelist = os.listdir(path)
        actfilelist = []
        for filex in filelist:
            if filex.endswith("." + ext):
                actfilelist.append(filex)
        return actfilelist if len(ext) > 0 else filelist

    def infilelist(self, ext):
        return self.getfilename() in self.getfilelist(ext)

    def setpath(self, path=""):
        if len(path) < 1:
            self.path = os.path.dirname(__file__)
        else:
            self.path = path
        return self.path

    def createfolder(self, foldername):
        directoryx = d.directory()
        directoryx.setpath(self.getpath())
        directoryx.create(foldername)
        return directoryx.getpath()
