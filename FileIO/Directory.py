import os
import File as f


class directory:
    path = None
    tree = []
    visited = []

    def __init__(self):
        pass

    def setpath(self, path=""):
        if len(path) > 0:
            self.path = path
        else:
            self.path = os.path.dirname(os.path.abspath(__file__))
        self.path = self.path.replace(chr(92), chr(47))
        os.chdir(self.path)
        return 0 if len(path) > 0 else -1

    def getpath(self):
        return self.path if self.path is not None else -1

    def create(self, folder, seek=True):
        if not os.path.exists(folder):
            os.makedirs(folder)
            if seek:
                self.changeforward(folder)
            return 0
        else:
            return -1

    def changeforward(self, folder):
        if os.path.exists(folder):
            self.setpath(self.path + "/" + folder)
        return self.getpath()

    def changebackward(self):
        os.chdir("..")
        self.setpath(os.getcwd())
        return self.getpath()

    def gettree(self):
        path = self.getpath().split(sep="/")
        return path

    def getlist(self, specific="", foldersonly=False):
        wholething = os.listdir(self.getpath()) if len(
            specific) == 0 else os.listdir(specific)
        foldersonlyx = []
        for item in wholething:
            if os.path.isdir(item) and not item.endswith("__"):
                foldersonlyx.append(item)
        return foldersonlyx if foldersonly else wholething

    def hasdirectories(self, path=""):
        return any(os.path.isdir(os.path.join(path if len(path) > 0 else self.getpath(), item)) for item in os.listdir(path if len(path) > 0 else self.getpath()))

    def cantranscend(self, folderno=0):
        transcendence = 0
        if self.hasdirectories():
            transcendence = 1
        elif len(self.getlist()) > 1 and folderno < len(self.getlist()) - 1:
            transcendence = 2
        elif len(self.getlist()) == 1 and folderno == 0:
            transcendence = 3
        else:
            transcendence = 4
        return transcendence

    def getlevel(self, level):
        path = self.gettree()
        return path[level * -1]

    def edit(self, oldfolder, newfolder, seek=True):
        if os.path.exists(oldfolder):
            os.rename(oldfolder, newfolder)
            if seek:
                self.changebackward()
                self.changeforward(newfolder)
            return 0
        else:
            return -1

    def delete(self, folder, seek=True):
        if os.path.exists(folder):
            if seek:
                self.changebackward()
            os.rmdir(folder)
            return 0
        else:
            return -1

    def bulkdelete(self, ext=""):
        for filename in self.getfilelist(ext):
            if filename.endswith(ext) and ext != "py":
                tempfilex = f.file()
                tempfilex.setfilename(filename)
                tempfilex.create()
                tempfilex.delete()

    def folderexistssub(self, foldername, path=""):
        return foldername in self.getlist(path, foldersonly=True)

    def markvisitedpath(self, path):
        if not path in self.visited:
            self.visited.append(path)

    def markvisitedtree(self, treex):
        if not treex in self.tree:
            self.tree.append(treex)

    def markvisited(self, pathx="", treex=[]):
        if len(pathx) > 0:
            self.markvisitedpath(pathx)
        if len(treex) > 0:
            self.markvisitedtree(treex)

    def buildbranch(self, folderno=0, depth=0, reference=0, smart=False):
        folderlist = self.getlist(foldersonly=True)
        if self.hasdirectories():
            print(self.getpath())
            self.changeforward(folderlist[folderno])
            self.buildbranch(folderno, depth + 1)
        else:
            path = self.getpath()
            treex = self.gettree()
            self.markvisited(path, treex)
            i = depth
            if not smart:
                while i > reference:
                    print(self.getpath())
                    self.changebackward()
                    i -= 1
            else:
                while not self.hasdirectories():
                    print(self.getpath())
                    self.changebackward()
                    i -= 1
            print(self.getpath())
            print(path)
            return path

    def existsintree(self, foldername, folderno, depth=0):
        folderlist = self.getlist(foldersonly=True)
        if foldername in self.getpath():
            print("Found in {p}".format(p=self.getpath()))
            return self.getpath()
        else:
            if self.hasdirectories():
                print(self.getpath())
                self.changeforward(folderlist[folderno])
                self.existsintree(foldername, folderno, depth + 1)
            else:
                print("Not found.")
                return self.getpath()

    def backtrack(self, visited=[], depth=0, breadth=0):
        folderlist = self.getlist(foldersonly=True)
        foldertree = self.gettree()
        foldername = foldertree[-1]
        criteria = foldername in visited or foldername in folderlist or not self.hasdirectories()
        if criteria:
            visitedx = visited
            visitedx.append(self.getpath())
            self.changebackward()
            print("Backtracked to: {p}".format(p=self.getpath()))
            self.backtrack(visited=visitedx, depth=depth-1)
        else:
            print("Directory reset to {p}".format(p=self.getpath()))
            return -1

    def existsinfolder(self, foldername):
        folderlist = self.getlist(foldersonly=True)
        if foldername in folderlist:
            print("Found in {p}".format(p=self.getpath()))
            return self.getpath()
        else:
            print("Not found.")
            return self.getpath()


directoryx = directory()
directoryx.setpath()
directoryx.buildbranch(smart=True)
print(directoryx.tree)
