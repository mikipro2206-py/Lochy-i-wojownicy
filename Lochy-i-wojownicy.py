#   importowanie random itd
import random
import time


#   dla lepszej efektywnosci definiuje sobie funkcje przydatne
def czysc_i_czekaj(sekundy):
    time.sleep(sekundy)
    print("\n" * 100)


def pusto():
    print("\n" * 100)


# kolory
ZIELONY = "\033[92m"
CZERWONY = "\033[91m"
RESET = "\033[0m"

#   ustawianie hp i innych zmiennych
runda = 0
hp = 100
jedzenie = 3
pieniadze = 0
luck = 0
#   powitanie i zaczynanie
print(f"Witaj w tym pięknym świecie stworzonym przezemnie. Masz {hp} zdrowia, {jedzenie} jedzenia i {pieniadze} monet.")
czysc_i_czekaj(5)
imie = str(input("Jak masz na imię wojowniku? "))
czysc_i_czekaj(0)
print(f"Miło mi cię poznać {imie}")
czysc_i_czekaj(3)

# wybór
while True:
    pusto()
    print(f"Zaczyna się {runda} runda.")
    print("\n" * 5)
    wybor = int(input(
        "Pora na twój pierwszy wybór wojowniku. 1-ulepsz szczęście(potrzebne 25 monet. 2-walcz(dosatniesz monety ale jest ryzyko że zginiesz). 3-ulecz się(maks zdrowia to 100, nie lecz się jeżeli masz więcej niż 75 zdrowia bo wtedy zmarnujesz jedzenie, ale rób co chcesz. "))
    print("\n" * 2)
    if wybor == 1:
        if pieniadze < 25:
            pusto()
            print("Masz za mało monet")
            print("Wybierz jeszcze raz")
            czysc_i_czekaj(3)
            continue
        elif luck >= 10:
            print("Masz juz maks lucka, nie mozesz więcej")
        else:
            luck = luck + 1
            print(f"Kupiłeś miksture na szczęście, masz teraz {luck} szczęścia(przyda ci się ono w walce).")
            runda += 1
            continue
    if wybor == 2:
        print("Wybrałeś walkę, więc się zaczyna zaraz.")
        czysc_i_czekaj(3)
        potwor = 1
        if potwor == 1:
            potworek_hp = 50
            print("Przyszło ci się zmierzyć z goblinem")
            while True:
                # czysc_i_czekaj(3)
                szansa = random.randint(luck, 10)
                if szansa >= 4:
                    uderzenie_gracza = random.randint(luck, 15)
                    potworek_hp = potworek_hp - uderzenie_gracza
                    print(f"Uderzyłeś potwora za {uderzenie_gracza} hp, zostało mu {potworek_hp} zdrowia. ")
                    czysc_i_czekaj(7)
                    unik = random.randint(0, 10)
                    if unik >= 5:
                        uderzenie_potwora = random.randint(0, 20)
                        if uderzenie_potwora > 0:
                            hp = hp - uderzenie_potwora
                            print(f"Potwór cie uderzył za {uderzenie_potwora} hp, zostało ci {hp} zdrowia.")
                            czysc_i_czekaj(6)
                    else:
                        print("WOW udało ci się zrobić unik")
                        czysc_i_czekaj(3)
                if szansa <= 3:
                    print("Pudlo!")
                    czysc_i_czekaj(2)
                    unik = random.randint(luck, 10)
                    if unik >= 5:
                        uderzenie_potwora = random.randint(0, 20)
                        if uderzenie_potwora > 0 and uderzenie_potwora < 7:
                            hp = hp - uderzenie_potwora
                            print(f"Potwór cie uderzył za {uderzenie_potwora} hp, zostało ci {hp} zdrowia.")
                            czysc_i_czekaj(6)
                    else:
                        print("WOW udało ci się zrobić unik")
                        czysc_i_czekaj(5)
                if szansa >= 7:
                    uderzenie_gracza = random.randint(10, 20)
                    potworek_hp = potworek_hp - uderzenie_gracza
                    print(
                        f"Wow, krytyk i unik, zadałeś potworowi {uderzenie_gracza} zdrowia, zostało mu {potworek_hp} zdrowia.")
                    czysc_i_czekaj(7)
                if potworek_hp <= 0:
                    nagroda = random.randint(10, 25)
                    pieniadze += nagroda
                    print(
                        f"Pokonałeś potwora, zostało ci {hp} zdrowia, dosatłeś {nagroda} nagrody w monetach, masz łącznie {pieniadze} monet.")
                    czysc_i_czekaj(7)
                    runda += 1
                    break
                if hp <= 0:
                    print("Przegrałeś")
                    exit()
