min = 0

def build_list(db):
    catg = db.ws(ws='Catalog')
    wires = {}
    for row in catg.range(address = 'A2:C13'):
        stats = [row[1],row[2]]
        wires[row[0]] = stats
    return wires

def build_segs(db):
    catg = db.ws(ws='LINES')
    lines = {}
    start = 1
    for row in catg.range(address = 'A2:B22'):
        stats = [row[0],row[1]]
        lines[start] = stats
        start = start + 1
    return lines

def build_set(list):
    set = []
    for i in list:
        set.append(i)
    return set

def get_length(segs):
    length = 0
    for i in range(1,len(segs)+1):
        length = length + segs[i][1]
    return length

def get_index(list,item):
    index = 0
    for i in list:
        if(item == i):
            return index
        else:
            index += 1

    return -1

def copy_dict(dict):
    new_dict = {}
    for key,item in dict.items():
        new_dict[key] = item
    return new_dict
class checks():


    def __init__(self,pr,st,sg,ld,bd,vd):
        self.price = pr
        self.load = ld
        self.start = st
        self.seg = sg
        self.valid = vd
        self.build = bd



    def add(self,ld,pr,wire):
        self.load=self.load + ld
        self.price=self.price + pr
        self.build[self.seg]=wire


    def next(self):
        self.seg = self.seg + 1

    def check(self,type,fin):
        self.start = type
        self.end = fin

    def invalid(self):
        self.valid = False

    def get_price(self):
        return self.price

    def get_start(self):
        return self.start

    def get_end(self):
        return self.end

    def get_seg(self):
        return self.seg

    def get_load(self):
        return self.load

    def get_build(self):
        return self.build

    def get_valid(self):
        return self.valid
