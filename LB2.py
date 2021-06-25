import pylightxl as xl
import Func2

def build_seg(price,start,fin,seg,load,build,valid,sets,segs,size,wires,five_per):

    help = Func2.copy_dict(build)
    if(seg==size):
        #print("Found")
        end = Func2.checks(price,start,seg,load,help,valid)
        temp_value = end.get_price()
        if(temp_value < Func2.min) and (load < five_per):
            Func2.min = temp_value
        else:
            end.invalid()

        return end

    elif (load > five_per or price > Func2.min):
        end = Func2.checks(price,start,seg,load,help,valid)
        #print('Not Found')
        end.invalid()
        return end
    else:
        end = Func2.checks(0.0,0,0,0.0,{},True)
        end.invalid()
        for i in range(start,fin+1):

            temp = Func2.checks(price,start,seg,load,help,valid)
            temp.next();
            temp2 = Func2.checks(0.0,0,0,0.0,{},True)
            wire = sets[i]
            #print(wire)
            leng = segs[temp.seg][1]
            amp = segs[temp.seg][0]
            res = wires[wire][0]
            cost = wires[wire][1] * leng * 2
            ld = leng * res * amp * 2
            temp.add(ld,cost,wire)
            temp.check(i,fin)
            #print(type(temp2))
            temp2 = build_seg(temp.get_price(),temp.get_start(),temp.get_end(),temp.get_seg(),temp.get_load(),temp.get_build(),temp.get_valid(),sets,segs,size,wires,five_per)
            #print(type(temp2))
            if(temp2.get_valid()):
                end  = Func2.checks(temp2.get_price(),temp2.get_start(),temp2.get_seg(),temp2.get_load(),temp2.get_build(),temp2.get_valid())
        return end

def Main(input,output):
    file1 = input + ".xlsx"
    file2 = output + ".xlsx"
    db = xl.readxl(fn=file1)
    db.add_ws(ws="New Build")
    uf = db.ws(ws = "New Build")
    wires = Func2.build_list(db)
    segs = Func2.build_segs(db)
    sws = db.ws(ws = "LINES")
    volt = sws.address(address = 'F2')
    size = sws.address(address = 'G2')
    min = sws.address(address = 'H2')
    max = sws.address(address = 'I2')
    five_per = volt * .05
    length = Func2.get_length(segs)
    Func2.min = length * wires[max][1]
    print(Func2.min)
    starting_min = Func2.min
    temp = Func2.checks(0.0,0,0,0.0,{},True)
    finals = Func2.checks(0.0,0,0,0.0,{},True)
    sets = Func2.build_set(wires.keys())
    first = Func2.get_index(sets,min)
    last = Func2.get_index(sets,max)
    temp.check(first,last)
    #print(finals.get_build())
    finals = build_seg(temp.get_price(),temp.get_start(),temp.get_end(),temp.get_seg(),temp.get_load(),temp.get_build(),temp.get_valid(),sets,segs,size,wires,five_per)
    uf.update_index(row=1,col = 1,val = 'Segment')
    uf.update_index(row=1,col = 2,val = 'Length')
    uf.update_index(row=1,col = 3,val = 'Amp')
    uf.update_index(row=1,col = 4,val = 'Wire')
    for i in range(1,size+1):
        uf.update_index(row=i+1,col = 1, val = i)
        uf.update_index(row=i+1,col = 2,val = segs[i][1])
        uf.update_index(row=i+1,col = 3,val = segs[i][0])
        uf.update_index(row=i+1,col = 4,val = finals.get_build()[i])
    #print(Func2.min)
    #print(finals.get_build())

    xl.writexl(db=db, fn=file2)
