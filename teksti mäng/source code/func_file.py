import os
import random
import pickle

# from m_game import *

# stats print
def stats_print(endurance, vitality, strength, luck, stat_punkte):

    print(f"Punkte mida kasutada on: {stat_punkte}")
    print(f"vitality = {vitality}")
    print(f"endurance = {endurance}")
    print(f"strength = {strength}")
    print(f"luck = {luck}")


def stats_print_select(endurance, vitality, strength, luck, stat_punkte):
    
    print(f"Punkte mida kasutada on: {stat_punkte}")
    print(f"1. vitality = {vitality}")
    print(f"2. endurance = {endurance}")
    print(f"3. strength = {strength}")
    print(f"4. luck = {luck}")
    print(f"5. Finish")
    stat = int(input("Millist stati tahate muuta: "))
    clearconsol()
    
    return stat


# Clear consol
def clearconsol():
    os.system("cls")


def statsid(vitality, endurance, strength, luck, stat_punkte):

    stat_done = False
    #stat = 0

    while stat_done == False:

        stat = stats_print_select(endurance, vitality, strength, luck, stat_punkte)

        if stat == 1 and stat_punkte > 0:

            stats_print(endurance, vitality, strength, luck, stat_punkte)
            vitality_s = int(input("Sisesta vitality: "))

            while stat_punkte < vitality_s:
                print(f"Punkte on vähem kui sisestasid arvu")
                stats_print(endurance, vitality, strength, luck, stat_punkte)
                vitality_s = int(input("Sisesta vitality: "))
                clearconsol()

            vitality += vitality_s
            stat_punkte -= vitality_s
            clearconsol()

        elif stat == 2 and stat_punkte > 0:

            stats_print(endurance, vitality, strength, luck, stat_punkte)
            endurance_s = int(input("Sisesta endurance: "))

            while stat_punkte < endurance_s:
                print(f"Punkte on vähem kui sisestasid arvu")
                stats_print(endurance, vitality, strength, luck, stat_punkte)
                endurance_s = int(input("Sisesta endurance: "))
                clearconsol()

            endurance += endurance_s
            stat_punkte -= endurance_s
            clearconsol()

        elif stat == 3 and stat_punkte > 0:

            stats_print(endurance, vitality, strength, luck, stat_punkte)
            strength_s = int(input("Sisesta strength: "))

            while stat_punkte < strength_s:
                print(f"Punkte on vähem kui sisestasid arvu")
                stats_print(endurance, vitality, strength, luck, stat_punkte)
                strength_s = int(input("Sisesta strength: "))
                clearconsol()

            strength += strength_s
            stat_punkte -= strength_s
            clearconsol()

        elif stat == 4 and stat_punkte > 0:

            stats_print(endurance, vitality, strength, luck, stat_punkte)
            luck_s = int(input("Sisesta luck: "))

            while stat_punkte < luck_s:
                print(f"Punkte on vähem kui sisestasid arvu")
                stats_print(endurance, vitality, strength, luck, stat_punkte)
                luck_s = int(input("Sisesta luck: "))
                clearconsol()

            luck += luck_s
            stat_punkte -= luck_s
            clearconsol()

        elif stat == 5:
            return vitality, endurance, strength, luck, stat_punkte

        else:

            stat = stats_print_select(endurance, vitality, strength, luck, stat_punkte)


def moveset():

    print("1. Tavaline löök")
    print("2. Block")
    print("3. Kott")
    print("4. Puhka")
    print("5. Jookse")


def show_map(map):

    print(map)


def battle(health, vitality, strength, endurance, liv_endurance, luck, xp, löögid, joogid, raha):
    # nimi, elud, tugevus, xp, raha
    monsters = [["Alp", 30, 5, 30, 60], ["Wraith", 20, 2, 20, 40], ["Bruxa", 40, 8, 40, 80]]

    random_num = random.randint(0, len(monsters)-1)

    v_nimi = monsters[random_num][0]
    v_elud = monsters[random_num][1]
    v_dmg = monsters[random_num][2]
    pool_v_dmg = v_dmg / 2
    v_xp = monsters[random_num][3]
    v_rünnak = 0
    raha_saab = monsters[random_num][4]

    elud = health

    run = False
    block = False
    v_kord = False

    while round(v_elud) > 0 and round(elud) > 0 and run == False:

        number_kord = False
        tegevus = True

        if run:
            break

        if v_kord and block == False:
            v_rünnak = random.randint(round(pool_v_dmg), v_dmg)
            elud -= v_rünnak

        print(f"Sind ründab {v_nimi} \t\t\t\t\t\t\t player")
        print(f"Elud: {round(v_elud)} \t\t\t\t\t\t\t\t\t Sinu elud: {round(elud)}")
        print(f"\t\t\t\t\t\t\t\t\t\t\t Sinu endurance: {liv_endurance}\n")

        if v_kord and block == False:
            print(f"Sina tegid -{round((dmg * (strength / 100)) + dmg)} dmg\n")
            print(f"{v_nimi} tegi -{v_rünnak} dmg\n")
            v_kord = False

        elif block:
            print("Sa blockisid")
            print(f"{v_nimi} tegi -0 dmg")
            print("BLOCKED\t")

            block = False
            v_kord = False  # saad dmg kui False käigu lõppus / vaenlase kord

        if round(v_elud) <= 0 or round(elud) <= 0:
            clearconsol()
            break

        while tegevus:

            if number_kord:
                print(f"Sind ründab {v_nimi} \t\t\t\t\t\t\t player")
                print(f"Elud: {round(v_elud)} \t\t\t\t\t\t\t\t\t Sinu elud: {round(elud)}")
                print(f"\t\t\t\t\t\t\t\t\t\t\t Sinu endurance: {liv_endurance}\n")

            moveset()
            tegu = int(input("Sisesta tegevus: "))

            match tegu:

                case 1:
                    loogid(löögid)
                    löögi_valik = int(input("Vali löök: "))

                    while löögi_valik > len(löögid) and löögi_valik != 6:
                        löögi_valik = int(input("Sellist valikut pole: "))

                    while löögi_valik != 6 and löögid[löögi_valik-1][1] > liv_endurance:
                        löögi_valik = int(input("Pole piisavalt energiat vali uuesti: "))

                    if löögi_valik == 6:
                        pass

                    else:
                        dmg = löögid[löögi_valik-1][2]
                        v_elud -= (dmg * (strength / 100)) + dmg
                        liv_endurance -= löögid[löögi_valik-1][1]
                        v_kord = True
                        tegevus = False

                case 2:
                    block = True
                    v_kord = True
                    tegevus = False

                case 3:
                    joogid_print(joogid)

                    vali_jook = int(input("Vali jook: "))

                    while vali_jook > 4:
                        clearconsol()
                        joogid_print(joogid)
                        vali_jook = int(input("Valikut pole sisesta valik uuesti: "))

                    while vali_jook != 4 and joogid[vali_jook - 1][3] <= 0:
                        clearconsol()
                        joogid_print(joogid)
                        vali_jook = int(input("Valikut pole sisesta valik uuesti: "))

                    match vali_jook:
                        case 1:
                            elud += joogid[0][1]
                            joogid[0][3] -= 1

                            if elud > vitality:
                                elud = vitality

                        case 2:
                            liv_endurance += joogid[1][2]
                            joogid[1][3] -= 1

                            if liv_endurance > endurance:
                                liv_endurance = endurance

                        case 3:
                            elud += joogid[2][1]
                            joogid[2][3] -= 1

                            if elud > vitality:
                                elud = vitality

                            liv_endurance += joogid[2][2]
                            if liv_endurance > endurance:
                                liv_endurance = endurance

                        case 4:
                            print("Tagasi")

                    number_kord = True

                    clearconsol()

                case 4:
                    liv_endurance += endurance / 2
                    if liv_endurance > endurance:
                        liv_endurance = endurance

                    dmg = 0
                    tegevus = False
                    v_kord = True

                case 5:
                    print("jookse")
                    kas_jooksen = random.randint(0, luck)

                    if kas_jooksen > luck / 2:
                        run = True

                    else:
                        v_kord = True

                    tegevus = False

                case _:
                    print("Vali 1-4")

            clearconsol()

    clearconsol()

    if round(v_elud) <= 0:
        print(f"Tapsid vaenlase said +{v_xp} XP ja +{raha_saab} raha\n")
        xp += v_xp
        raha += raha_saab

    elif round(elud) <= 0:
        print("Said surma mine linna ja maga elud täis\n")

    elif run:

        print("Jooksid Minema\n")


    return round(elud), xp, joogid, raha


def loogid(löögid):

    print("#################################")
    print("\t\t\t↓ Sinu löögid ↓")
    print("     ↓Nimi↓ \t ↓Kulu↓\t↓Tugevus↓")

    mitu = 0

    if len(löögid) < 5:
        mitu = len(löögid)

    else:
        mitu = 5

    for i in range(mitu):
        print(f"{i+1}.  {löögid[i][0]}\t\t{löögid[i][1]}\t\t{löögid[i][2]}")

    print("6. Tagasi")
    print("#################################")


def joogid_print(joogid):

    print("\t\t\t↓ Sinu löögid ↓")
    print("     ↓Nimi↓ \t ↓Elud↓\t↓Endurance↓\t↓Kogus↓")

    for i in range(len(joogid)):
        print(f"{i + 1}.  {joogid[i][0]}\t\t{joogid[i][1]}\t\t{joogid[i][2]}\t\t{joogid[i][3]}")

    print("4. Tagasi")


# Näitab su XP'd
def xp_kalk(xp, skill_point, raha, health, vitality):
    max_xp = 200

    if xp >= max_xp:
        xp -= max_xp
        skill_point += 1

    kuni = xp / 6

    print("\t\t\t\t\t XP [", end="")

    for i in range(0, 33):
        if i <= kuni:
            print("#", end="")
        else:
            print("_", end="")

    print(f"]\t\t\t\tRaha: {raha}")
    print(f"\t\t\t\t\t\t\t xp: {xp} / {max_xp}\t\t\t\t\tElud: {health} / {vitality}")
    print(f"\t\t\t\t\t\t\t Skill poin: {skill_point}")

    return xp, skill_point


def battle_oskuse_vahetus(löögid, b_löögid):

    tegevus = True
    tagasi_tf = 0

    while tegevus:

        temp_num = 1
        vaata = False

        if len(löögid) <= 5:
            for i in range(len(löögid)):
                print(f"{i + 1}. {löögid[i][0]}\t\t{löögid[i][1]}\t\t{löögid[i][2]}")

                temp_num += 1

                if temp_num > len(löögid):
                    print(f"\n{temp_num} Tagasi")
                    tagasi_tf = temp_num
                    print(f"{temp_num + 1} Vaata praegust setupi")

        elif len(löögid) > 5 and len(löögid) <= 10:
            for i in range(5):

                if len(löögid) >= i + 6:
                    print(f"{i + 1}. {löögid[i][0]}\t\t{löögid[i][1]}\t\t{löögid[i][2]}\t|\t{i + 6}. {löögid[i + 5][0]}\t\t{löögid[i + 5][1]}\t\t{löögid[i + 5][2]}")

                else:
                    print(f"{i + 1}. {löögid[i][0]}\t\t{löögid[i][1]}\t\t{löögid[i][2]}\t|")

                temp_num += 1

                if temp_num > 5:
                    print(f"\n{len(löögid) + 1} Tagasi")
                    tagasi_tf = len(löögid) + 1
                    print(f"{len(löögid) + 2} Vaata praegust setupi")

        valik = int(input("Vali löök: "))

        while valik > len(löögid) + 2 or valik < 1:
            valik = int(input("Vali löök uuesti: "))

        if valik == tagasi_tf:
            break

        if valik == tagasi_tf + 1:
            vaata = True

        for i in range(len(b_löögid)):
            print(f"{i + 1}. {b_löögid[i][0]}\t\t{b_löögid[i][1]}\t\t{b_löögid[i][2]}")

            if len(b_löögid) < i:
                print(f"{i + 1}.")

        if vaata == False:
            valik_b = int(input("Vali millega välja vahetada (1-5): "))

            while valik_b > 5:
                valik_b = int(input("Vali uuesti (1-5)"))

            if valik_b > len(b_löögid):
                valik -= 1
                b_löögid.append(löögid[valik])

            else:
                valik -= 1
                valik_b -= 1
                b_löögid[valik_b] = löögid[valik]

    return b_löögid


def save(löögid, b_löögid, joogid, vitality, health, endurance, strength, luck, raha, xp, skill_point, valik):

    with open("pickle_save.pickle", "wb") as save_data:

        pickle.dump(löögid, save_data, protocol=-1)
        pickle.dump(b_löögid, save_data, protocol=-1)
        pickle.dump(joogid, save_data, protocol=-1)
        pickle.dump(vitality, save_data, protocol=-1)
        pickle.dump(health, save_data, protocol=-1)
        pickle.dump(endurance, save_data, protocol=-1)
        pickle.dump(strength, save_data, protocol=-1)
        pickle.dump(luck, save_data, protocol=-1)
        pickle.dump(raha, save_data, protocol=-1)
        pickle.dump(xp, save_data, protocol=-1)
        pickle.dump(skill_point, save_data, protocol=-1)
        pickle.dump(valik, save_data, protocol=-1)



def read_save():

    with open("pickle_save.pickle", "rb") as save_file:

        löögid = pickle.load(save_file)
        b_löögid = pickle.load(save_file)
        joogid = pickle.load(save_file)
        vitality = pickle.load(save_file)
        health = pickle.load(save_file)
        endurance = pickle.load(save_file)
        strength = pickle.load(save_file)
        luck = pickle.load(save_file)
        raha = pickle.load(save_file)
        xp = pickle.load(save_file)
        skill_point = pickle.load(save_file)
        valik = pickle.load(save_file)

    return löögid, b_löögid, joogid, vitality, health, endurance, strength, luck, raha, xp, skill_point, valik

def räägime():

    laused = ["Tere.", "Kuhu Lähed.", "Üle oja mäele, läbi oru jõele.", "Küll küllale liiga ei tee.", "Ämber läks ümber.", "Mahlakas jõhvikas maitses soisel kaldal hää.", "Tilluke talleke tatsas tasasel pinnal."]

    rand_int = random.randint(0, len(laused) - 1)

    #print(laused[rand_int], "\n")

    return laused[rand_int]
