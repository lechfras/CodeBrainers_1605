plansza = {'7':' ', '8':' ', '9':' ',
           '4':' ', '5':' ', '6':' ',
           '1':' ', '2':' ', '3': ' '}

pola_planszy =[]
for pole in plansza:
    pola_planszy.append(pole)

def wyswietlPlansze(plansza):
    print(plansza['7'] + '|' + plansza['8'] + '|' + plansza['9'])
    print('-+-+-')
    print(plansza['4'] + '|' + plansza['5'] + '|' + plansza['6'])
    print('-+-+-')
    print(plansza['1'] + '|' + plansza['2'] + '|' + plansza['3'])


def graj():
    turn ='X'
    count=0

    for i in range(10):
        wyswietlPlansze(plansza)
        print("teraz Twoja kolej, " + turn + " gdzie sie chcesz ruszyc? ")

        move = input()

        if plansza[move] ==' ':
            plansza[move]=turn
            count+=1
        else:
            print("to miesjce jest zajete. \n Wybierz inne miejsce")
            continue

        if count >=5:
            if plansza['7']==plansza['8']==plansza['9'] != ' ':
                wyswietlPlansze(plansza)
                print("\n Koniec Gry")
                print("Wygrał" + turn )
                break
            elif plansza['4']==plansza['5']==plansza['6'] != ' ':
                wyswietlPlansze(plansza)
                print("\n Koniec Gry")
                print("Wygrał" + turn )
                break

            elif plansza['1']==plansza['2']==plansza['3'] != ' ':
                wyswietlPlansze(plansza)
                print("\n Koniec Gry")
                print("Wygrał" + turn )
                break

            elif plansza['1']==plansza['4']==plansza['7'] != ' ':
                wyswietlPlansze(plansza)
                print("\n Koniec Gry")
                print("Wygrał" + turn )
                break

            elif plansza['2']==plansza['5']==plansza['8'] != ' ':
                wyswietlPlansze(plansza)
                print("\n Koniec Gry")
                print("Wygrał" + turn )
                break

            elif plansza['3']==plansza['6']==plansza['9'] != ' ':
                wyswietlPlansze(plansza)
                print("\n Koniec Gry")
                print("Wygrał" + turn )
                break

            elif plansza['7']==plansza['5']==plansza['3'] != ' ':
                wyswietlPlansze(plansza)
                print("\n Koniec Gry")
                print("Wygrał" + turn )
                break

            elif plansza['1']==plansza['5']==plansza['9'] != ' ':
                wyswietlPlansze(plansza)
                print("\n Koniec Gry")
                print("Wygrał" + turn )
                break

        if count ==9:
            print("\n Zakoncz Gre" )
        if turn =='X':
            turn ='O'
        else:
            turn ='X'

nowa_gra = input("Czy chcesz grac w nowa gre? (T/N)")
if nowa_gra == 'T' or 'N':
    for pole in pola_planszy:
        plansza[pole]=" "

    graj()

if __name__ == "__main__":
    graj()