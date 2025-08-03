import json

kolejki = {
    "Energuś": 120,
    "Hyperion": 150,
    "Formuła": 130,
    "Pociąg": 125,
    "Kaczki": 110,
    "Zjeżdżalnia": 110,
    "Zadra": 145,
    "Wodne": 120
}

def Start():
    print("🤖: Witaj w mierzeniu twojego wzrostu.")
    print("🤖: Jak masz na imię?")
    imie = input()

    print(f"🤖: Witaj {imie}. Ile masz wzrostu w cm?")
    try:
        wzrost = int(input())
    except ValueError:
        print("🤖: Podaj liczbę jako wzrost (np. 130).")
        return

    print(f"🤖: Masz {wzrost} cm wzrostu. Możesz wejść na:")
    
    dostepne = []
    for nazwa, wymagany_wzrost in kolejki.items():
        if wzrost >= wymagany_wzrost:
            dostepne.append(nazwa)

    if dostepne:
        for kolejka in dostepne:
            print(f"✅ {kolejka}")
    else:
        print("❌ Niestety, nie możesz wejść na żadną kolejkę.")

Start()
