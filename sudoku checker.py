def sudoku_oikein(sudoku: list):

    def nelio_oikein(sudoku):
        lista = []
        sarake = 0
        rivi = 0
        raja = sarake + 3
        while True:
            for i in range(0, 9):
                lahto = sudoku[rivi][sarake]
                if lahto > 0 and lahto in lista:
                    return False
                lista.append(lahto)
                sarake += 1
                if sarake == raja:
                    sarake = raja - 3
                    rivi += 1
                if sarake == 2 and rivi == 2:
                    if sudoku[2][2] in lista and sudoku[2][2] > 0:
                        return False
                    lista = []
                    sarake += 1
                    rivi = 0
                    raja = sarake + 3
                    continue
                if sarake == 5 and rivi == 2:
                    if sudoku[2][5] in lista and sudoku[2][5] > 0:
                        return False
                    lista = []
                    sarake += 1
                    rivi = 0
                    raja = sarake + 3
                    continue
                if sarake == 2 and rivi == 5:
                    if sudoku[5][2] in lista and sudoku[5][2] > 0:
                        return False
                    lista = []
                    sarake += 1
                    rivi -= 2
                    raja = sarake + 3
                    continue
                if sarake == 5 and rivi == 5:
                    if sudoku[5][5] in lista and sudoku[5][5] > 0:
                        return False
                    lista = []
                    sarake += 1
                    rivi -= 2
                    raja = sarake + 3
                    continue
                if sarake == 8 and rivi == 5:
                    if sudoku[5][8] in lista and sudoku[5][8] > 0:
                        return False
                    lista = []
                    rivi += 1
                    sarake = 0
                    raja = sarake + 3
                    continue
                if sarake == 2 and rivi == 8:
                    if sudoku[8][2] in lista and sudoku[8][2] > 0:
                        return False
                    lista = []
                    sarake += 1
                    rivi -= 2
                    raja = sarake + 3
                    continue
                if sarake == 5 and rivi == 8:
                    if sudoku[8][5] in lista and sudoku[8][5] > 0:
                        return False
                    lista = []
                    sarake += 1
                    rivi -= 2
                    raja = sarake + 3
                    continue
                if sarake == 8 and rivi == 2:
                    if sudoku[2][8] in lista and sudoku[2][8] > 0:
                        return False
                    lista = []
                    rivi += 1
                    sarake = 0
                    raja = sarake + 3
                    continue
                if sarake == 8 and rivi == 8:
                    if sudoku[8][8] in lista and sudoku[8][8] > 0:
                        return False
                    return True

    def sarake_oikein(sudoku):
        lista = []
        sarake = 0
        while sarake < 9:
            for rivi in sudoku:
                if rivi[sarake] > 0 and rivi[sarake] in lista:
                    return False
                lista.append(rivi[sarake])
            if len(lista) == 9:
                sarake += 1
                lista = []
                continue
        return True

    def rivi_oikein(sudoku):
        lista = []
        rivi = 0
        while rivi < 9:
            for luku in sudoku[rivi]:
                if luku > 0 and luku in lista:
                    return False
                lista.append(luku)
            if len(lista) == 9:
                rivi += 1
                lista = []
                continue
        return True

    if nelio_oikein(sudoku) == True and sarake_oikein(sudoku) == True and rivi_oikein(sudoku) == True:
        return True
    else:
        return False

if __name__ == "__main__":
    sudoku = [
    [9, 0, 0, 0, 8, 0, 3, 0, 0],
    [2, 0, 0, 2, 5, 0, 7, 0, 0],
    [0, 2, 0, 3, 0, 0, 0, 0, 4],
    [2, 9, 4, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 7, 3, 0, 5, 6, 0],
    [7, 0, 5, 0, 6, 0, 4, 0, 0],
    [0, 0, 7, 8, 0, 3, 9, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 3],
    [3, 0, 0, 0, 0, 0, 0, 0, 2]
    ]

    print(sudoku_oikein(sudoku))

    sudoku = [
    [2, 6, 7, 8, 3, 9, 5, 0, 4],
    [9, 0, 3, 5, 1, 0, 6, 0, 0],
    [0, 5, 1, 6, 0, 0, 8, 3, 9],
    [5, 1, 9, 0, 4, 6, 3, 2, 8],
    [8, 0, 2, 1, 0, 5, 7, 0, 6],
    [6, 7, 4, 3, 2, 0, 0, 0, 5],
    [0, 0, 0, 4, 5, 7, 2, 6, 3],
    [3, 2, 0, 0, 8, 0, 0, 5, 7],
    [7, 4, 5, 0, 0, 3, 9, 0, 1]
    ]

    print(sudoku_oikein(sudoku))
