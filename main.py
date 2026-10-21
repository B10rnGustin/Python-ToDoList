import sqlite3
import datetime

connection = sqlite3.connect("tasks.db")

cursor = connection.cursor()

command1 = """CREATE TABLE IF NOT EXISTS
tasks(Id INTEGER PRIMARY KEY, Titel TEXT, Aanmaakdatum TEXT, Startdatum TEXT, Einddatum TEXT, Status TEXT, Opmerking TEXT)"""

cursor.execute(command1)
connection.commit()

def task_making():
    titel = input("Geef een titel op: ")
    aanmaakdatum = datetime.datetime.now().isoformat(sep=" ", timespec="seconds")

    while True:
        try:
            startdatum_tekst = input("Geef de startdatum op (dd-mm-jjjj): ")
            startdatum = datetime.datetime.strptime(startdatum_tekst, "%d-%m-%Y")
            startdatum = startdatum.strftime("%Y-%m-%d")
            break
        except ValueError:
            print("Voer eem juiste datum in. ")
    while True:
        try:
            einddatum_tekst = input("Geef de einddatum op (dd-mm-jjjj): ")
            einddatum = datetime.datetime.strptime(einddatum_tekst, "%d-%m-%Y")
            einddatum = einddatum.strftime("%Y-%m-%d")
            break
        except ValueError:
            print("Voer eem juiste datum in. ")

    status = "Active"
    opmerking = input("Opmerking voor bij de taak:\n")

    sql_opdracht = """
    INSERT INTO tasks (Titel, Aanmaakdatum, Startdatum, Einddatum, Status, Opmerking)
    VALUES (?, ?, ?, ?, ?, ?)
    """
    cursor.execute(sql_opdracht, (titel, aanmaakdatum, startdatum, einddatum, status, opmerking))
    connection.commit()
    print("Taak goed opgeslagen.\n ")

def task_viewing():
    sql_opdracht = "SELECT * FROM tasks"
    cursor.execute(sql_opdracht)
    tasks = cursor.fetchall()

    if not tasks:
        print("Er zijn geen opgeslagen taken. \n")
        return

    for task in tasks:
        print("\nID: ", task[0])
        print("Titel: ", task[1])
        print("Aanmaakdatum: ", task[2])
        print("Startdatum: ", task[3])
        print("Einddatum: ", task[4])
        print("Status: ", task[5])
        print("\nOpmerking: ")
        print(task[6] or "", "\n")

    input("Druk op enter om terug te gaan naar het menu.")
    print()

def task_editing():

    task_ID = int(input("Welke taak wil je wijzigen? "))

    sql_opdracht = "SELECT * FROM tasks WHERE Id = ?"
    cursor.execute(sql_opdracht, (task_ID,))
    task = cursor.fetchone()

    if task is None:
        print("Er bestaat geen taak met dit ID.")
        return

    print("\nHuidige titel:", task[1])
    print("Huidige status:", task[5])
    print("Einddatum:", task[4])
    print("Opmerking: " )
    print(task[6] or "", "\n")

    print("1. Titel wijzigen")
    print("2. Huidige status wijzigen")
    print("3. Einddatum wijzigen")
    print("4. Opmerking aanpassen")

    try:
        editing_choice = int(input("Wat wil je wijzigen? "))
    except ValueError:
        print("Verkeerde invoertype.\n")
        return

    if editing_choice == 1:
        new_titel = input("Voer de nieuwe titel in: ")
        sql_opdracht = "UPDATE tasks SET Titel = ? WHERE Id = ?"
        cursor.execute(sql_opdracht, (new_titel, task_ID))
        connection.commit()

        print("Titel succesvol gewijzigd.\n")

    elif editing_choice == 2:
        geldige_statussen = ["Active", "Started", "In progress", "On Hold", "Done"]
        while True:
            new_status = input("Wat wordt de nieuwe status? (Active, Started, In progress, On Hold, Done)")
            if new_status in geldige_statussen:
                break
            print("Ongeldige status. Kies een status uit de lijst.\n")

        sql_opdracht = "UPDATE tasks SET Status = ? WHERE Id = ?"
        cursor.execute(sql_opdracht, (new_status, task_ID))
        connection.commit()

        print("Status succesvol gewijzigd.\n")

    elif editing_choice == 3:
        while True:
            try:
                new_einddatum = input("Voer de nieuwe Einddatum in dd-mm-jjjj: ")
                new_einddatum = datetime.datetime.strptime(new_einddatum, "%d-%m-%Y")
                new_einddatum = new_einddatum.strftime("%Y-%m-%d")
                break
            except ValueError:
                print("Voer eem juiste datum in. ")

        sql_opdracht = "UPDATE tasks SET Einddatum = ? WHERE Id = ?"
        cursor.execute(sql_opdracht, (new_einddatum, task_ID))
        connection.commit()

        print("Einddatum succesvol gewijzigd.\n")

    elif editing_choice == 4:
        huidige_opmerking = task[6] or ""

        print("1. Opmerking vervangen")
        print("2. Opmerking aanvullen")
        print("3. Opmerking verwijderen")

        try:
            note_choice = int(input("Maak een keuze: "))

        except ValueError:
            print("Verkeerde invoer. Voer een getal in.\n")
            return

        if note_choice == 1:
            nieuwe_opmerking = input("Voer de nieuwe opmerking in:\n ")

            sql_opdracht = """UPDATE tasks SET Opmerking = ? WHERE Id = ? """
            cursor.execute(sql_opdracht, (nieuwe_opmerking, task_ID))
            connection.commit()

            print("Opmerking succesvol vervangen.\n")

        elif note_choice == 2:
            extra_opmerking = input("Welke tekst wil je toevoegen? ")

            if huidige_opmerking:
                nieuwe_opmerking = huidige_opmerking + "\n" + extra_opmerking
            else:
                nieuwe_opmerking = extra_opmerking

            sql_opdracht = """ UPDATE tasks SET Opmerking = ? WHERE Id = ? """
            cursor.execute(sql_opdracht, (nieuwe_opmerking, task_ID))
            connection.commit()

            print("Opmerking succesvol aangevuld.\n")

        elif note_choice == 3:
            sql_opdracht = """ UPDATE tasks SET Opmerking = '' WHERE Id = ? """
            cursor.execute(sql_opdracht, (task_ID,))
            connection.commit()
            print("Opmerking succesvol verwijderd.\n")
        else:
            print("Ongeldige keuze. Kies een getal tussen 1 en 3.\n")

def task_deleting():
    while True:
        try:
            task_ID = int(input("Geef het taak-ID op dat je wilt verwijderen: "))
            break
        except ValueError:
            print("Ongeldige invoer. Voer een numeriek taak-ID in.\n")

    sql_opdracht = "DELETE FROM tasks WHERE Id = ?"
    cursor.execute(sql_opdracht, (task_ID,))
    connection.commit()

    if cursor.rowcount > 0:
        print("Taak succesvol verwijderd.\n")
    else:
        print("Er bestaat geen taak met dit ID.\n")

while True:
    print("1. Taak aanmaken")
    print("2. Taak inzien")
    print("3. Taak wijzigen")
    print("4. Taak verwijderen")
    print("5. Afsluiten")

    try:
        choice = int(input("\nMaak eem keuze: "))
        if choice == 1:
            task_making()
        elif choice == 2:
            task_viewing()
        elif choice == 3:
            task_editing()
        elif choice == 4:
            task_deleting()
        elif choice == 5:
            print("Een fijne dag verder! ")
            break
        else:
            print("Geen juiste invoer gegeven.\n")
    except ValueError:
        print("Voer een getal tussen de 1 en 5 in.\n")

connection.close()