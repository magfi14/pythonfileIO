import os


class dir2:

    visited = []
    path = ""
    depth = 0
    breadths = []

    def __init__(self):
        pass

    def setpath(self, path=""):
        self.path = os.path.dirname(
            os.path.abspath(__file__)).replace(chr(92), chr(47))
        if len(path) > 0 and os.path.exists(path):
            self.path = path.replace(chr(92), chr(47))
        os.chdir(self.path)
        self.path = os.getcwd()
        self.path = self.path.replace(chr(92), chr(47))
        return self.path

    def gettreefrompath(self):
        return self.getpath().split(sep="/")

    def nfolder(self, n=1):
        return self.gettreefrompath()[-1 * n]

    def changepath(self, path, direction="f"):
        breadthx = len(self.folderlist(1))
        if direction == "f":
            if os.path.exists(path) or breadthx > 0:
                self.depth += 1
                if self.depth > len(self.breadths):
                    self.breadths.append(0)
                self.path = self.path.replace(chr(92), chr(47))
                self.path += "/" + path
                os.chdir(self.path)
        elif direction == "b":
            self.depth -= 1
            os.chdir("..")
            self.path = os.getcwd().replace(chr(92), chr(47))
        elif direction == "d":
            depth = self.depth - 1
            self.breadths[depth] += 1
            folder = self.folderlist(1)[self.breadths[depth]]
            os.chdir(folder)
            self.path = os.getcwd().replace(chr(92), chr(47))
        print("DEPTH: {d} | {b} | {f} ".format(
            d=self.depth, b=self.breadths, f=self.nfolder(1)))
        return self.path

    def getpath(self, path=""):
        return self.path if len(path) == 0 else self.path + "/" + path

    def nfolderlist(self, n=1):
        folder = self.nfolder(n)
        prefolderlist = os.listdir(folder)
        actfolderlist = [folderx for folderx in prefolderlist if (
            os.path.isdir(folderx) or "." not in folderx) and not folderx.endswith("__")]
        return actfolderlist

    def folderlist(self, n=2):
        return self.nfolderlist(n)

    def forward(self, folder="", folderno=0, v=False):
        folderlist = self.folderlist(1)
        if len(folderlist) > 0 and folderno < len(folderlist):
            folderx = folderlist[folderno] if len(folder) == 0 else folder
            self.changepath(folderx, direction="f")
        else:
            print("Cannot go any deeper.")
            if v:
                self.visited.append(self.getpath())

    def backward(self):
        if self.depth > 0:
            self.changepath("", direction="b")

    def down(self):
        depth = self.depth - 1
        if self.breadths[depth] < self.countdirectories():
            folder = self.countdirectories()[self.breadths[depth + 1]]
            self.changepath(folder, direction="d")

    def countdirectories(self):
        folderlist = self.folderlist(1)
        print(len(folderlist))
        return len(folderlist)

    def hasdirectories(self):
        print(self.countdirectories() > 0)
        return self.countdirectories() > 0