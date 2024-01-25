
from random import randint

def make_random_move(positions):
        o = randint(0,8)
        print("KI: ", o)
        while True:
            if positions[o] == "":
                return o
            else:
                o = randint(0,8)

move_count_KI = 0

def make_good_move(positions):
        global move_count_KI
        print("move_count_KI: ", move_count_KI)
        if move_count_KI == 0:
            o = randint(0,8)
            print("KI: ", o)
            while True:
                if positions[o] == "":
                    move_count_KI += 1
                    return o
                else:
                    o = randint(0,8)
        else:
            listKIset = check_position_KI(positions)
            #print(listKIset)
            move = wining_move(positions, listKIset)
            print("KI Move: ", move)
            return move

listKIset = []
def check_position_KI(positions):
    global listKIset
    for i, e in enumerate(positions):
        if positions[i] == "O":
             listKIset.append(i)
    listKIset = list(dict.fromkeys(listKIset))
    return listKIset

def wining_move(positions, listKIset):
    print("Liste: ",listKIset)
    if 0 in listKIset:
        if positions[1] == "" or positions[1] == "O":
            if positions[2] == "" or positions[2] == "O":
                if positions[1] == "":
                    print(0,",",1)
                    return 1
                elif positions[1] == "X":
                    return make_random_move(positions)
                elif positions[2] == "":
                        print(0,",",2)
                        return 2
                elif positions[2] == "X":
                        return make_random_move(positions)
            else:
                 return make_random_move(positions)
        elif positions[4] == "" or positions[4] == "O":
            if  positions[8] == "" or positions[8] == "O":
                if positions[4] == "":
                    print(0,",",4)
                    return 4
                elif positions[4] == "X":
                    return make_random_move(positions)
                elif positions[8] == "":
                        print(0,",",8)
                        return 8
                elif positions[8] == "X":
                        return make_random_move(positions)
            else:
                 return make_random_move(positions)
        elif positions[3] == "" or positions[3] == "O":
            if positions[6] == "" or positions[6] == "O":
                if positions[3] == "":
                    print(0,",",3)
                    return 3
                elif positions[3] == "X":
                    return make_random_move(positions)
                elif positions[6] == "":
                        print(0,",",6)
                        return 6
                elif positions[6] == "X":
                        return make_random_move(positions)
            else:
                 return make_random_move(positions)
        else:
            return make_random_move(positions)
    if 1 in listKIset:
        if positions[0] == "" or positions[0] == "O":
            if positions[2] == "" or positions[2] == "O":
                if positions[0] == "":
                    print(1,",",0)
                    return 0
                elif positions[0] == "X":
                    return make_random_move(positions)
                elif positions[2] == "":
                        print(1,",",2)
                        return 2
                elif positions[2] == "X":
                        return make_random_move(positions)
            else:
                 return make_random_move(positions)
        elif positions[4] == "" or positions[4] == "O":
            if  positions[7] == "" or positions[7] == "O":
                if positions[4] == "":
                    print(1,",",4)
                    return 4
                elif positions[4] == "X":
                    return make_random_move(positions)
                elif positions[7] == "":
                        print(1,",",7)
                        return 7
                elif positions[7] == "X":
                        return make_random_move(positions)
            else:
                 return make_random_move(positions)
        else:
            return make_random_move(positions)
    if 2 in listKIset:
        if positions[1] == "" or positions[1] == "O":
            if positions[0] == "" or positions[0] == "O":
                if positions[1] == "":
                    print(2,",",1)
                    return 1
                elif positions[1] == "X":
                    return make_random_move(positions)
                elif positions[0] == "":
                        print(2,",",0)
                        return 0
                elif positions[0] == "X":
                        return make_random_move(positions)
            else:
                 return make_random_move(positions)
        elif positions[4] == "" or positions[4] == "O":
            if  positions[6] == "" or positions[6] == "O":
                if positions[4] == "":
                    print(2,",",4)
                    return 4
                elif positions[4] == "X":
                    return make_random_move(positions)
                elif positions[6] == "":
                        print(2,",",6)
                        return 6
                elif positions[6] == "X":
                        return make_random_move(positions)
            else:
                 return make_random_move(positions)
        elif positions[8] == "" or positions[8] == "O":
            if positions[5] == "" or positions[5] == "O":
                if positions[8] == "":
                    print(2,",",8)
                    return 8
                elif positions[8] == "X":
                    return make_random_move(positions)
                elif positions[5] == "":
                        print(2,",",5)
                        return 5
                elif positions[5] == "X":
                        return make_random_move(positions)
            else:
                 return make_random_move(positions)
        else:
            return make_random_move(positions)
    if 3 in listKIset:
        if positions[0] == "" or positions[0] == "O":
            if positions[6] == "" or positions[6] == "O":
                if positions[0] == "":
                    print(3,",",0)
                    return 0
                elif positions[0] == "X":
                    return make_random_move(positions)
                elif positions[6] == "":
                        print(3,",",6)
                        return 6
                elif positions[6] == "X":
                        return make_random_move(positions)
            else:
                 return make_random_move(positions)
        elif positions[4] == "" or positions[4] == "O":
            if  positions[5] == "" or positions[5] == "O":
                if positions[4] == "":
                    print(3,",",4)
                    return 4
                elif positions[4] == "X":
                    return make_random_move(positions)
                elif positions[5] == "":
                        print(3,",",5)
                        return 5
                elif positions[5] == "X":
                        return make_random_move(positions)
            else:
                 return make_random_move(positions)
        else:
            return make_random_move(positions)
    if 4 in listKIset:
        if positions[0] == "" or positions[0] == "O":
            if positions[8] == "" or positions[8] == "O":
                if positions[0] == "":
                    print(4,",",0)
                    return 0
                elif positions[0] == "X":
                    return make_random_move(positions)
                elif positions[8] == "":
                        print(4,",",8)
                        return 8
                elif positions[8] == "X":
                        return make_random_move(positions)
            else:
                 return make_random_move(positions)
        elif positions[2] == "" or positions[2] == "O":
            if  positions[6] == "" or positions[6] == "O":
                if positions[2] == "":
                    print(4,",",2)
                    return 2
                elif positions[2] == "X":
                    return make_random_move(positions)
                elif positions[6] == "":
                        print(4,",",6)
                        return 6
                elif positions[6] == "X":
                        return make_random_move(positions)
            else:
                 return make_random_move(positions)
        elif positions[1] == "" or positions[1] == "O":
            if  positions[7] == "" or positions[7] == "O":
                if positions[1] == "":
                    print(4,",",1)
                    return 1
                elif positions[1] == "X":
                    return make_random_move(positions)
                elif positions[7] == "":
                        print(4,",",7)
                        return 7
                elif positions[7] == "X":
                        return make_random_move(positions)
            else:
                 return make_random_move(positions)
        elif positions[3] == "" or positions[3] == "O":
            if  positions[5] == "" or positions[5] == "O":
                if positions[3] == "":
                    print(4,",",3)
                    return 3
                elif positions[3] == "X":
                        return make_random_move(positions)
                elif positions[5] == "":
                        print(4,",",5)
                        return 5
                elif positions[5] == "X":
                        return make_random_move(positions)
            else:
                 return make_random_move(positions)
        else:
            return make_random_move(positions)
    if 5 in listKIset:
        if positions[3] == "" or positions[3] == "O":
            if positions[4] == "" or positions[4] == "O":
                if positions[3] == "":
                    print(5,",",3)
                    return 3
                elif positions[3] == "X":
                        return make_random_move(positions)
                elif positions[4] == "":
                        print(5,",",4)
                        return 4
                elif positions[4] == "X":
                        return make_random_move(positions)
            else:
                 return make_random_move(positions)
        elif positions[2] == "" or positions[2] == "O":
            if  positions[8] == "" or positions[8] == "O":
                if positions[2] == "":
                    print(5,",",2)
                    return 2
                elif positions[2] == "X":
                        return make_random_move(positions)
                elif positions[8] == "":
                        print(5,",",8)
                        return 8
                elif positions[8] == "X":
                        return make_random_move(positions)
            else:
                 return make_random_move(positions)
        else:
            return make_random_move(positions)
    if 6 in listKIset:
        if positions[3] == "" or positions[3] == "O":
            if positions[0] == "" or positions[0] == "O":
                if positions[3] == "":
                    print(6,",",3)
                    return 3
                elif positions[3] == "X":
                        return make_random_move(positions)
                elif positions[0] == "":
                        print(6,",",0)
                        return 0
                elif positions[0] == "X":
                        return make_random_move(positions)
            else:
                 return make_random_move(positions)
        elif positions[4] == "" or positions[4] == "O":
            if  positions[2] == "" or positions[2] == "O":
                if positions[4] == "":
                    print(6,",",4)
                    return 4
                elif positions[4] == "X":
                        return make_random_move(positions)
                elif positions[2] == "":
                        print(6,",",2)
                        return 2
                elif positions[2] == "X":
                        return make_random_move(positions)
            else:
                 return make_random_move(positions)
        elif positions[8] == "" or positions[8] == "O":
            if positions[7] == "" or positions[7] == "O":
                if positions[8] == "":
                    print(6,",",8)
                    return 8
                elif positions[8] == "X":
                        return make_random_move(positions)
                elif positions[7] == "":
                        print(6,",",7)
                        return 7
                elif positions[7] == "X":
                        return make_random_move(positions)
            else:
                 return make_random_move(positions)
        else:
            return make_random_move(positions)
    if 7 in listKIset:
        if positions[1] == "" or positions[1] == "O":
            if positions[4] == "" or positions[4] == "O":
                if positions[1] == "":
                    print(7,",",1)
                    return 1
                elif positions[1] == "X":
                        return make_random_move(positions)
                elif positions[4] == "":
                        print(7,",",4)
                        return 4
                elif positions[4] == "X":
                        return make_random_move(positions)
            else:
                 return make_random_move(positions)
        elif positions[6] == "" or positions[6] == "O":
            if  positions[8] == "" or positions[8] == "O":
                if positions[2] == "":
                    print(7,",",2)
                    return 2
                elif positions[2] == "X":
                        return make_random_move(positions)
                elif positions[6] == "":
                        print(7,",",6)
                        return 6
                elif positions[6] == "X":
                        return make_random_move(positions)
            else:
                 return make_random_move(positions)
        else:
            return make_random_move(positions)
    if 8 in listKIset:
        if positions[4] == "" or positions[4] == "O":
            if positions[0] == "" or positions[0] == "O":
                if positions[4] == "":
                    print(8,",",4)
                    return 4
                elif positions[4] == "X":
                        return make_random_move(positions)
                elif positions[0] == "":
                        print(8,",",0)
                        return 0
                elif positions[0] == "X":
                        return make_random_move(positions)
            else:
                 return make_random_move(positions)
        elif positions[5] == "" or positions[5] == "O":
            if  positions[2] == "" or positions[2] == "O":
                if positions[5] == "":
                    print(8,",",5)
                    return 5
                elif positions[5] == "X":
                        return make_random_move(positions)
                elif positions[2] == "":
                        print(8,",",2)
                        return 2
                elif positions[2] == "X":
                        return make_random_move(positions)
            else:
                 return make_random_move(positions)
        elif positions[6] == "" or positions[6] == "O":
            if positions[7] == "" or positions[7] == "O":
                if positions[6] == "":
                    print(8,",",6)
                    return 6
                elif positions[6] == "X":
                        return make_random_move(positions)
                elif positions[7] == "":
                        print(8,",",7)
                        return 7
                elif positions[7] == "X":
                        return make_random_move(positions)
            else:
                 return make_random_move(positions)
        else:
            return make_random_move(positions)