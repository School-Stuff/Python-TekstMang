
from func_file import *


def ravala(löögid, müüa, joogid, raha, xp, skill_point, health, vitality):
    clearconsol()
    ravalas = True

    lause = ""

    while ravalas:

        xp, skill_point = xp_kalk(xp, skill_point, raha, health, vitality)

        print("\tRävala")

        print("\n1. Pood")
        print("2. Kuula")
        if lause != "":
            print(lause)
        print("3. Baar")
        print("4. tuletorn")
        print("5. ↑ joksi")
        print("6. → carsten")
        print("7. ↖ Arel")
        print("8. ↓ hatu")
        print("9. SKill")
        print("10. Vaheta võitlus lööke")
        print("11. Välju")

        tegevus = int(input("Sisesta tegevus: "))

        while tegevus > 11 or tegevus < 1:
            tegevus = int(input("Sisesta tegevus (1 - 11): "))

        match tegevus:
            case 1:
                clearconsol()
                löögid, müüa, raha = pood_löögid(löögid, müüa, raha)

            case 2:
                clearconsol()
                lause = räägime()

            case 3:
                clearconsol()
                joogid, raha = baar(joogid, raha)
                #joogid, raha = pood_joogid(joogid, raha)

            case 4:
                clearconsol()
                tuletorn()

            case 5:
                clearconsol()
                return 6, löögid, müüa, joogid, raha, xp, skill_point

            case 6:
                clearconsol()
                return 8, löögid, müüa, joogid, raha, xp, skill_point

            case 7:
                clearconsol()
                return 7, löögid, müüa, joogid, raha, xp, skill_point

            case 8:
                clearconsol()
                return 4, löögid, müüa, joogid, raha, xp, skill_point

            case 9:
                clearconsol()
                return 9, löögid, müüa, joogid, raha, xp, skill_point

            case 10:
                clearconsol()
                return 10, löögid, müüa, joogid, raha, xp, skill_point

            case 11:
                clearconsol()
                return 11, löögid, müüa, joogid, raha, xp, skill_point


def pood(löögid, müüa, joogid, raha):

    välju = True

    while välju:

        print("1. Osta lööke")
        print("2. Osta joogid")
        print("3. Välju")

        valik = int(input("Vali tegevus: "))

        while valik > 3 or valik < 1:
            valik = int(input("Vali tegevus (1 - 3): "))

        match valik:
            case 1:
                löögid, müüa, raha = pood_löögid(löögid, müüa, raha)

            case 2:
                joogid, raha = pood_joogid(joogid, raha)

            case 3:
                return löögid, müüa, joogid, raha


def poe_kontroll(temp_list, löögid, müüa, vali, raha, poes, alg, lõpp, kuhu):

    if temp_list[vali-1][0] == "Tagasi poodi":
        poes = False

    elif temp_list[vali-1][0] == "Edasi" and lõpp < len(müüa):
        alg += 5
        lõpp += 5

    elif temp_list[vali-1][0] == "Tagasi" and alg > 0:
        alg -= 5
        lõpp -= 5

    elif kuhu == False:
        löögid.append(temp_list[vali-1])
        raha -= temp_list[vali-1][3]
        #del temp_list[vali-1]
        del müüa[vali-1]

    #for i in range(0, 3):
        #temp_list.pop(-1)

    return müüa, löögid, raha, poes, alg, lõpp


def pood_löögid(löögid, müüa, raha):
    clearconsol()
    functid = [["Edasi"], ["Tagasi"], ["Tagasi poodi"]]
    poes = True

    alg = 0
    lõpp = 5

    while poes:
        temp_list = []

        if len(müüa) == 0:
            print("Pood on tühi")
            #poes = False
            #break

        print(f"\t\t\t\t\t\t\t\t\t\t\t\t\t Sinu raha: {raha}")
        print(f"     ↓Nimi↓     ↓Kulu↓   ↓Tugevus↓   ↓Hind↓")
        siin_temp = 0
        temt = 1
        kuhu = False

        for i in range(alg, lõpp + 3):
            if len(müüa) > i and i <= lõpp - 1:
                print(f"{i + 1}.  {müüa[i][0]}\t\t{müüa[i][1]}\t\t{müüa[i][2]}\t\t{müüa[i][3]}")
                temp_list.append(müüa[i])

                temt += 1

            elif temt > len(müüa) and siin_temp < 3 or temt - len(müüa) <= len(functid) and siin_temp < 3:
                print(f"{temt}.  {functid[siin_temp][0]}")
                temp_list.append(functid[siin_temp])
                temt += 1
                siin_temp += 1

        vali = int(input("Valii: "))

        while vali > temt:
            vali = int(input("Valii uuesti: "))

        while len(temp_list) < vali:
            vali = int(input("Valikut pole olemas vali uuesti: "))

        if temp_list[vali - 1][0] == "Edasi" or temp_list[vali - 1][0] == "Tagasi" or temp_list[vali - 1][0] == "Tagasi poodi":
            kuhu = True

        while kuhu == False and raha < temp_list[vali - 1][3]:
            vali = int(input("Pole piisavalt raha vali uuesti: "))

        match vali:
            case 1:
                müüa, löögid, raha, poes, alg, lõpp = poe_kontroll(temp_list, löögid, müüa, vali, raha, poes, alg, lõpp, kuhu)

            case 2:
                müüa, löögid, raha, poes, alg, lõpp = poe_kontroll(temp_list, löögid, müüa, vali, raha, poes, alg, lõpp, kuhu)

            case 3:
                müüa, löögid, raha, poes, alg, lõpp = poe_kontroll(temp_list, löögid, müüa, vali, raha, poes, alg, lõpp, kuhu)

            case 4:
                müüa, löögid, raha, poes, alg, lõpp = poe_kontroll(temp_list, löögid, müüa, vali, raha, poes, alg, lõpp, kuhu)

            case 5:
                müüa, löögid, raha, poes, alg, lõpp = poe_kontroll(temp_list, löögid, müüa, vali, raha, poes, alg, lõpp, kuhu)

            case 6:
                müüa, löögid, raha, poes, alg, lõpp = poe_kontroll(temp_list, löögid, müüa, vali, raha, poes, alg, lõpp, kuhu)

            case 7:
                müüa, löögid, raha, poes, alg, lõpp = poe_kontroll(temp_list, löögid, müüa, vali, raha, poes, alg, lõpp, kuhu)

            case 8:
                müüa, löögid, raha, poes, alg, lõpp = poe_kontroll(temp_list, löögid, müüa, vali, raha, poes, alg, lõpp, kuhu)

    return löögid, müüa, raha


def pood_joogid(joogid, raha):
    # nimi, elud, endurance, raha
    müüa = [["elud      ", 100, 0, 50], ["endurance", 0, 100, 50], ["suur jook", 100, 100, 90]]

    poes = True

    while poes:

        print(f"     ↓Nimi↓ \t ↓elud↓\t↓endurance↓\t↓hind↓\t\t\t\tSinu raha: {raha}")

        for i in range(len(müüa)):
            print(f"{i+1}.  {müüa[i][0]}\t\t{müüa[i][1]}\t\t{müüa[i][2]}\t\t{müüa[i][3]}")
        print("4. Vaata selja kotti")
        print("5. Tagasi")

        kogu = 1

        vali = int(input("Valii: "))

        while len(müüa) + 1 < vali:
            vali = int(input("Valikut pole olemas vali uuesti: "))

        if len(müüa) == 0:
            print("Pood on tühi\n")
            poes = False

        elif vali != 4:
            kogu = int(input("Sisesta kogus: "))

        while vali != 4 and vali != 5 and raha < müüa[vali - 1][3] * kogu:

            for i in range(len(müüa)):
                print(f"{i + 1}.  {müüa[i][0]}\t\t{müüa[i][1]}\t\t{müüa[i][2]}")
            print("4. Vaata selja kotti")
            print("5. Tagasi")

            vali = int(input("Pole piisavalt raha vali uuesti: "))

            if vali != 4:
                kogu = int(input("Sisesta kogus: "))

        match vali:

            case 1:
                joogid[0][3] += kogu
                raha -= müüa[0][3] * kogu

            case 2:
                joogid[1][3] += kogu
                raha -= müüa[1][3] * kogu

            case 3:
                joogid[2][3] += kogu
                raha -= müüa[2][3] * kogu

            case 4:
                clearconsol()
                print("\t\t↓Seljakott↓")
                print("#######################################")
                print("Nimi \t Kogus")
                for i in range(0, len(joogid) - 1):
                    print(f"{joogid[i][0]} \t {joogid[i][3]}")
                print("#######################################")

            case 5:
                poes = False

            case _:
                pass

    return joogid, raha


def print_vaade():
    print("Siin pole midagi!!!\n")


def tuletorn():
    clearconsol()

    koht = True

    while koht:

        clearconsol()

        print("\tTuletorn")

        print("\n1. Vaata")
        print("2. ↓  Tagasi")

        tegevus = int(input("Sisesta tegevus: "))

        while tegevus > 2 or tegevus < 1:
            tegevus = int(input("Sisesta tegevus (1 - 2): "))

        match tegevus:
            case 1:
                clearconsol()
                print_vaade()

            case 2:
                clearconsol()
                koht = False


def baar(joogid, raha):

    lause = ""
    kohal = True
    while kohal:

        clearconsol()

        print("\tbaar")

        print("\n1. Osta")
        print("2. Räägi")
        if lause != "":
            print(lause)
        print("3. ↓  Tagasi")

        tegevus = int(input("Sisesta tegevus: "))

        while tegevus > 3 or tegevus < 1:
            tegevus = int(input("Sisesta tegevus (1 - 3): "))

        match tegevus:
            case 1:
                clearconsol()
                joogid, raha = pood_joogid(joogid, raha)

            case 2:
                clearconsol()
                lause = räägime()

            case 3:
                clearconsol()
                kohal = False
                return joogid, raha


def arel(löögid, müüa, joogid, raha, xp, skill_point, health, vitality):

    clearconsol()
    lause = ""
    kohal = True
    while kohal:

        xp, skill_point = xp_kalk(xp, skill_point, raha, health, vitality)

        print("\tArel")

        print("\n1. Pood")
        print("2. Baar")
        print("3. Räägi")
        if lause != "":
            print(lause)
        print("4. → Joksi")
        print("5. ↘ Rävala")
        print("6. SKill")
        print("7. Vaheta võitlus lööke")
        print("8. Välju")

        tegevus = int(input("Sisesta tegevus: "))

        while tegevus > 8 or tegevus < 1:
            tegevus = int(input("Sisesta tegevus (1 - 8): "))

        match tegevus:
            case 1:
                clearconsol()
                löögid, müüa, raha = pood_löögid(löögid, müüa, raha)

            case 2:
                clearconsol()
                joogid, raha = pood_joogid(joogid, raha)

            case 3:
                clearconsol()
                lause = räägime()

            case 4:
                clearconsol()
                return 5, löögid, müüa, joogid, raha, xp, skill_point

            case 5:
                clearconsol()
                return 7, löögid, müüa, joogid, raha, xp, skill_point

            case 6:
                clearconsol()
                return 9, löögid, müüa, joogid, raha, xp, skill_point

            case 7:
                clearconsol()
                return 10, löögid, müüa, joogid, raha, xp, skill_point

            case 8:
                clearconsol()
                return 11, löögid, müüa, joogid, raha, xp, skill_point


def mets(health, vitality, strength, endurance, liv_endurance, luck, xp, skill_point, löögid, joogid, raha):

    clearconsol()
    kohal = True

    while kohal:

        xp, skill_point = xp_kalk(xp, skill_point, raha, health, vitality)
        print("\tMetsas")

        print("\n1. Ründa vaenlast")
        print("2. ↗ Joksi")
        print("3. ↙ Rävala")
        print("4. Välju")


        tegevus = int(input("Sisesta tegevus: "))

        while tegevus > 4 or tegevus < 1:
            tegevus = int(input("Sisesta tegevus (1 - 4): "))

        match tegevus:
            case 1:
                clearconsol()
                battle(health, vitality, strength, endurance, liv_endurance, luck, xp, löögid, joogid, raha)

            case 2:
                clearconsol()
                return 5, health, vitality, strength, endurance, liv_endurance, luck, xp, skill_point, löögid, joogid, raha

            case 3:
                clearconsol()
                return 1, health, vitality, strength, endurance, liv_endurance, luck, xp, skill_point, löögid, joogid, raha

            case 4:
                clearconsol()
                return 11, health, vitality, strength, endurance, liv_endurance, luck, xp, skill_point, löögid, joogid, raha



def carsten(löögid, müüa, joogid, raha, xp, skill_point, health, vitality):

    clearconsol()
    lause = ""
    kohal = True
    while kohal:

        xp, skill_point = xp_kalk(xp, skill_point, raha, health, vitality)

        print("\tCarsten")

        print("\n1. Pood")
        print("2. Baar")
        print("3. Räägi")
        if lause != "":
            print(lause)
        print("4. ← Rävala")
        print("5. SKill")
        print("6. Vaheta võitlus lööke")
        print("7. Välju")

        tegevus = int(input("Sisesta tegevus: "))

        while tegevus > 7 or tegevus < 1:
            tegevus = int(input("Sisesta tegevus (1 - 7): "))

        match tegevus:
            case 1:
                clearconsol()
                löögid, raha = pood_löögid(löögid, müüa, raha)

            case 2:
                clearconsol()
                joogid, raha = pood_joogid(joogid, raha)

            case 3:
                clearconsol()
                lause = räägime()

            case 4:
                clearconsol()
                return 8, löögid, müüa, joogid, raha, xp, skill_point

            case 5:
                clearconsol()
                return 9, löögid, müüa, joogid, raha, xp, skill_point

            case 6:
                clearconsol()
                return 10, löögid, müüa, joogid, raha, xp, skill_point

            case 7:
                clearconsol()
                return 11, löögid, müüa, joogid, raha, xp, skill_point


def hatu(löögid, müüa, joogid, raha, xp, skill_point, health, vitality):

    clearconsol()
    lause = ""
    kohal = True
    while kohal:

        xp, skill_point = xp_kalk(xp, skill_point, raha, health, vitality)

        print("\tHatu")

        print("\n1. Pood")
        print("2. Baar")
        print("3. Räägi")
        if lause != "":
            print(lause)
        print("4. ↗ Rävala")
        print("5. SKill")
        print("6. Vaheta võitlus lööke")
        print("7. Välju")

        tegevus = int(input("Sisesta tegevus: "))

        while tegevus > 7 or tegevus < 1:
            tegevus = int(input("Sisesta tegevus (1 - 7): "))

        match tegevus:
            case 1:
                clearconsol()
                löögid, raha = pood_löögid(löögid, müüa, raha)

            case 2:
                clearconsol()
                joogid, raha = pood_joogid(joogid, raha)

            case 3:
                clearconsol()
                lause = räägime()

            case 4:
                clearconsol()
                return 1, löögid, müüa, joogid, raha, xp, skill_point

            case 5:
                clearconsol()
                return 9, löögid, müüa, joogid, raha, xp, skill_point

            case 6:
                clearconsol()
                return 10, löögid, müüa, joogid, raha, xp, skill_point

            case 7:
                clearconsol()
                return 11, löögid, müüa, joogid, raha, xp, skill_point


def joksi(löögid, müüa, joogid, raha, xp, skill_point, health, vitality):

    kohal = True
    lause = ""

    while kohal:
        clearconsol()
        xp, skill_point = xp_kalk(xp, skill_point, raha, health, vitality)

        print("\tJoksi")

        print("\n1. Pood")
        print("2. Baar")
        print("3. Kuula")
        if lause != "":
            print(lause)
        print("4. ← Arel")
        print("5. ↓ Rävala")
        print("6. SKill")
        print("7. Vaheta võitlus lööke")
        print("8. Välju")

        tegevus = int(input("Sisesta tegevus: "))

        while tegevus > 8 or tegevus < 1:
            tegevus = int(input("Sisesta tegevus (1 - 8): "))

        match tegevus:
            case 1:
                clearconsol()
                löögid, raha = pood_löögid(löögid, müüa, raha)

            case 2:
                clearconsol()
                joogid, raha = pood_joogid(joogid, raha)

            case 3:
                clearconsol()
                lause = räägime()

            case 4:
                clearconsol()
                return 2, löögid, müüa, joogid, raha, xp, skill_point

            case 5:
                clearconsol()
                return 6, löögid, müüa, joogid, raha, xp, skill_point

            case 6:
                clearconsol()
                return 9, löögid, müüa, joogid, raha, xp, skill_point

            case 7:
                clearconsol()
                return 10, löögid, müüa, joogid, raha, xp, skill_point

            case 8:
                clearconsol()
                return 11, löögid, müüa, joogid, raha, xp, skill_point


def suurmets(health, vitality, strength, endurance, liv_endurance, luck, xp, skill_point, löögid, joogid, raha):

    kohal = True
    while kohal:

        clearconsol()

        xp, skill_point = xp_kalk(xp, skill_point, raha, health, vitality)
        print("\tSuurmets")

        print("\n1. Ründa vaenlast")
        print("2. ↘ Rävala")
        print("3. ↖ Arel")
        print("4: Välju")

        tegevus = int(input("Sisesta tegevus: "))

        while tegevus > 4 or tegevus < 1:
            tegevus = int(input("Sisesta tegevus (1 - 4): "))

        match tegevus:
            case 1:
                clearconsol()
                battle(health, vitality, strength, endurance, liv_endurance, luck, xp, löögid, joogid, raha)

            case 2:
                clearconsol()
                return 1, health, vitality, strength, endurance, liv_endurance, luck, xp, skill_point, löögid, joogid, raha

            case 3:
                clearconsol()
                return 2, health, vitality, strength, endurance, liv_endurance, luck, xp, skill_point, löögid, joogid, raha

            case 4:
                clearconsol()
                return 11, health, vitality, strength, endurance, liv_endurance, luck, xp, skill_point, löögid, joogid, raha


def väikemets(health, vitality, strength, endurance, liv_endurance, luck, xp, skill_point, löögid, joogid, raha):

    kohal = True
    while kohal:

        clearconsol()

        xp, skill_point = xp_kalk(xp, skill_point, raha, health, vitality)
        print("\tVäikemets")

        print("\n1. Ründa vaenlast")
        print("2. ← Rävala")
        print("3. → carsten")
        print("4. Välju")

        tegevus = int(input("Sisesta tegevus: "))

        while tegevus > 4 or tegevus < 1:
            tegevus = int(input("Sisesta tegevus (1 - 4): "))

        match tegevus:
            case 1:
                clearconsol()
                battle(health, vitality, strength, endurance, liv_endurance, luck, xp, löögid, joogid, raha)

            case 2:
                clearconsol()
                return 1, health, vitality, strength, endurance, liv_endurance, luck, xp, skill_point, löögid, joogid, raha

            case 3:
                clearconsol()
                return 3, health, vitality, strength, endurance, liv_endurance, luck, xp, skill_point, löögid, joogid, raha

            case 4:
                clearconsol()
                return 11, health, vitality, strength, endurance, liv_endurance, luck, xp, skill_point, löögid, joogid, raha
