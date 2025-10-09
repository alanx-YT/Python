import random

xyz = "Czatuś:"

print("podaj swoje dane!")
user_name = input("Imię: ")
print("\n")

def app():
    while True:
        msg = input("Ty: ").lower().strip()

        if msg in ["wyjdź", "exit", "quit"]:
            losowe_odp = [
                f"Papa {user_name}",
                f"Do zobaczenia {user_name} 👋",
                f"Narazie 👋"
            ]
            print(f"{xyz} {random.choice(losowe_odp)}")
            break

        elif any(x in msg for x in ["hej", "elo", "witaj", "yo", "siema", "cześć"]):
            losowe_odp = [
                f"Hej {user_name}",
                f"Witaj {user_name}",
                f"Yo {user_name}",
                f"Siema {user_name}",
                f"Cześć {user_name}",
                f"Elo {user_name}"
            ]
            print(f"{xyz} {random.choice(losowe_odp)}")

        elif any(x in msg for x in ["kim jesteś"]):
            losowe_odp = [
                f"Jestem twoim asystentem AI!😁",
                f"Jestem asystentem AI 😎"
            ]
            print(f"{xyz} {random.choice(losowe_odp)}")
        
        elif any(x in msg for x in ["co robisz", "co porabiasz"]):
            print(f"{xyz} Pisze z tobą 😀")

        elif any(x in msg for x in ["smutno"]):
            print(f"{xyz} nie martw się ❤")
        
        elif msg == "!command start":
            print(f"{xyz} Tryb komend aktywny 🟢")
            print(f"{xyz} Napisz komende list aby zobaczyć wszystkie komendy!")

            lista = """
\t!stop
\t!user <name, ip>
\t!hello_world
\t!list
\t!start <program>
                    """

            while True:
                command = input("Ty (tryb komend): ")
                if command == "!list":
                    print(f"{lista}")
                elif command == "!user name":
                    print(f"{xyz} {user_name}")
                elif command == "!user ip":
                    print(f"{xyz} IP jest tajne! 🔒")
                elif any(x in command for x in ["!start"]):
                    print(f"{xyz} Błąd (503)")
                elif command == "!stop":
                    print(f"{xyz} Tryb komend nie aktywny 🔴")
                    break
                else:
                    print(f"Nieznana komenda: ['{command}']")
            
        elif any(x in msg for x in ["co u cb", "co u ciebie", "jak się masz", "jak sie masz"]):
            losowe_odp = [
                f"U mnie dobrze, a co u ciebie?",
                f"Dobrze 😀, dzięki że pytasz",
                f"Fantastycznie, a ty jak się masz?",
            ]
            print(f"{xyz} {random.choice(losowe_odp)}")

        elif any(x in msg for x in ["Pomożesz"]):
            losowe_odp = [
                f"Jasne {user_name} pokaż mi z czym masz problem a spróbuję go rozwiązać 😎",
                f"Dobrze {user_name} zobaczymy z czym masz problem",
                f"Jasne"
            ]
            print(f"{xyz} {random.choice(losowe_odp)}")

        elif any(x in msg for x in ["znasz jakieś strony internetowe", "strona www"]):
            losowe_odp = [
                f"Tak znam np. https://www.puczniewski.pl",
                f"tak znam np. https://www.youtube.com",
                f"Tak znam np. https://www.chatgpt.com"
            ]
            print(f"{xyz} {random.choice(losowe_odp)}")

        else:
            losowe_odp = [
                f"Ciekawe opowiec więcej! ",
                f"Hmm... rozwiń to bardziej"
            ]
            print(f"{xyz} {random.choice(losowe_odp)}")

app()