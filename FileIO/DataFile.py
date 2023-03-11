import File as f
import pandas as p


class frame:

    framex = None

    def __init__(self):
        pass

    def importff(self, csvfile):
        self.framex = p.read_csv(csvfile)

    def exporttf(self, csvfile):
        filex = datafile(csvfile, mode="w")
        self.framex.to_csv(filex.getfilename(), index=False)

    def create(self, csvfile=""):
        if len(csvfile) == 0:
            self.framex = p.DataFrame()
        else:
            self.importff(csvfile)

    def getcolumns(self):
        return self.framex.columns

    def addcolumn(self, key):
        if key not in self.getcolumns():
            self.framex[key] = []

    def addcolumns(self, keys):
        for key in keys:
            self.addcolumn(key)

    def removecolumn(self, key):
        if key in self.getcolumns():
            self.framex = self.framex.drop(key, axis=1)

    def removecolumns(self, keys):
        for key in keys:
            self.removecolumn(key)

    def editcolumn(self, oldkey, newkey):
        if newkey not in self.getcolumns():
            self.framex = self.framex.rename(columns={oldkey: newkey})

    def addrow(self, values):
        self.framex.loc[len(self.framex)] = values

    def getsize(self):
        return len(self.framex)

    def removerow(self, rowid=-1):
        if rowid == -1:
            self.framex = self.framex.drop(len(self.framex) - 1, axis=0)
        elif rowid > -1 and rowid < self.getsize():
            self.framex = self.framex.drop(rowid, axis=0)
        else:
            print("Out of bounds!")

    def removerows(self, start, end):
        if end < self.getsize() and start > -1:
            if end >= start:
                self.removerow(end)
                self.removerows(start, end - 1)

    def editrow(self, rowid, values):
        if rowid > -1 and rowid < self.getsize():
            self.framex.iloc[rowid] = values

    def swaprows(self, rowid1, rowid2):
        self.framex.loc[[rowid1, rowid2]
                        ] = self.framex.loc[[rowid2, rowid1]].to_numpy()

    def getframe(self):
        return self.framex


class datafile:

    filex = None

    def __init__(self, filename, create=True, mode="a"):
        self.filex = f.file()
        self.filex.setfilename(filename + ".csv", True)
        if create:
            self.create(mode)

    def getfilename(self):
        return self.filex.filename

    def create(self, mode="a"):
        self.filex.create(mode)

    def delete(self):
        self.filex.delete()
