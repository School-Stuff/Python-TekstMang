# Karl Jugapuu

from pathlib import Path

from func_file import *
from map import *


# nimi, kulu, tugevus
müüa = [["Bolo    ", 3, 7, 300], ["Lõuahaak", 5, 10, 500], ["Lükka   ", 1, 2, 200], ["Haak    ", 3, 8, 400], ["Ristlöök", 2, 6, 399], ["Sirge   ", 1, 2, 200], ["Ülekäe  ", 3, 9, 300], ["Jalaga  ", 4, 7, 350]]
# ["Kannaga", 3, 6], ["Mõõgaga", 5, 10], ["Lükka  ", 2, 2], ["a", 3, 6], ["b", 5, 10], ["c  ", 2, 2]
löögid = [["Lõõ", 2, 5]]
b_löögid = []
#löögid = []
# nimi, elud, endurance, kogus
joogid = [["elud", 100, 0, 1], ["endurance", 0, 100, 1], ["suur jook", 100, 100, 0]]



vitality = 10 # default 20?   / max
health = vitality
endurance = 5 # default 10?
liv_endurance = endurance
strength = 3 # default 5?
luck = 1 # default 1
raha = 300 # default 200?
xp = 0
skill_point = 30


save_file_check = Path("pickle_save.pickle")
if save_file_check.is_file():

    print("1. Jätka")
    print("2. Uus mäng")
    print("3. Välju")

    valik_menu = int(input("Sisesta valik: "))

    while valik_menu > 3 or valik_menu < 1:
        valik_menu = int(input("Sisesta valik (1 - 3): "))

    match valik_menu:

        case 1:
            löögid, b_löögid, joogid, vitality, health, endurance, strength, luck, raha, xp, skill_point, valik = read_save()
            stat_done = True
            print(valik)

        case 2:
            stat_done = False

        case 3:
            exit()

else:
    print("1. Uus mäng")
    print("2. Välju")

    valik_menu = int(input("Sisesta valik: "))

    while valik_menu > 2 or valik_menu < 1:
        valik_menu = int(input("Sisesta valik (1 - 2): "))

    match valik_menu:

        case 1:
            stat_done = False

        case 2:
            exit()


if stat_done == False:
    vitality, endurance, strength, luck, skill_point = statsid(vitality, endurance, strength, luck, skill_point)
    health = vitality
    valik = 1
    temp = 1


# valik 1 = Rävala, 2 = Arel, 3 = carsten, 4 = hatu, 5 = joksi, 6 = mets, 7 = suurmets, 8 = väikemets       9 = kasuta skill pointe, 10 = muuda oma oskusi
mangib = True
while mangib:

    match valik:

        case 1:
            save(löögid, b_löögid, joogid, vitality, health, endurance, strength, luck, raha, xp, skill_point, valik)
            valik, löögid, müüa, joogid, raha, xp, skill_point = ravala(löögid, müüa, joogid, raha, xp, skill_point, health, vitality)

            temp = 1

        case 2:
            save(löögid, b_löögid, joogid, vitality, health, endurance, strength, luck, raha, xp, skill_point, valik)
            valik, löögid, müüa, joogid, raha, xp, skill_point = arel(löögid, müüa, joogid, raha, xp, skill_point, health, vitality)

            temp = 2

        case 3:
            save(löögid, b_löögid, joogid, vitality, health, endurance, strength, luck, raha, xp, skill_point, valik)
            valik, löögid, müüa, joogid, raha, xp, skill_point = carsten(löögid, müüa, joogid, raha, xp, skill_point, health, vitality)

            temp = 3

        case 4:
            save(löögid, b_löögid, joogid, vitality, health, endurance, strength, luck, raha, xp, skill_point, valik)
            valik, löögid, müüa, joogid, raha, xp, skill_point = hatu(löögid, müüa, joogid, raha, xp, skill_point, health, vitality)

            temp = 4

        case 5:
            save(löögid, b_löögid, joogid, vitality, health, endurance, strength, luck, raha, xp, skill_point, valik)
            valik, löögid, müüa, joogid, raha, xp, skill_point = joksi(löögid, müüa, joogid, raha, xp, skill_point, health, vitality)

            temp = 5

        case 6:
            save(löögid, b_löögid, joogid, vitality, health, endurance, strength, luck, raha, xp, skill_point, valik)
            valik, health, vitality, strength, endurance, liv_endurance, luck, xp, skill_point, löögid, joogid, raha = mets(health, vitality, strength, endurance, liv_endurance, luck, xp, skill_point, löögid, joogid, raha)

            temp = 6

        case 7:
            save(löögid, b_löögid, joogid, vitality, health, endurance, strength, luck, raha, xp, skill_point, valik)
            valik, health, vitality, strength, endurance, liv_endurance, luck, xp, skill_point, löögid, joogid, raha = suurmets(health, vitality, strength, endurance, liv_endurance, luck, xp, skill_point, löögid, joogid, raha)

            temp = 7

        case 8:
            save(löögid, b_löögid, joogid, vitality, health, endurance, strength, luck, raha, xp, skill_point, valik)
            valik, health, vitality, strength, endurance, liv_endurance, luck, xp, skill_point, löögid, joogid, raha = väikemets(health, vitality, strength, endurance, liv_endurance, luck, xp, skill_point, löögid, joogid, raha)

            temp = 8

        case 9:
            vitality, endurance, strength, luck, skill_point = statsid(vitality, endurance, strength, luck, skill_point)
            health = vitality
            valik = temp
            save(löögid, b_löögid, joogid, vitality, health, endurance, strength, luck, raha, xp, skill_point, valik)

        case 10:
            b_löögid = battle_oskuse_vahetus(löögid, b_löögid)
            valik = temp
            save(löögid, b_löögid, joogid, vitality, health, endurance, strength, luck, raha, xp, skill_point, valik)

        case 11:
            valik = temp
            save(löögid, b_löögid, joogid, vitality, health, endurance, strength, luck, raha, xp, skill_point, valik)
            exit()
