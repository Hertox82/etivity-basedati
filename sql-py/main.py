from db import DB

def first_step(db: DB):
    choice=input("""Per creare e popolare le tabelle inserire: 1
    """)
    try:
        choice=int(choice)
        if choice == 1:
            db.create_tables()
            db.insert_value()
            second_step(db)
        else:
            print("Errore non hai inserito il numero 1")
            drop_db(db)
            # first_step(db)
    except:
        print("Errore non hai inserito un numero intero")
        drop_db(db)
        # first_step(db)

def second_step(db: DB):
    choice=input(""" Per usare il metodo Create inserire: 2
    """)
    try:
        choice=int(choice)
        if choice == 2:
            db.create_op()
            third_step(db)
        else:
            print("Errore non hai inserito il numero 2")
            drop_db(db)
            # first_step(db)
    except:
        print("Errore non hai inserito un numero intero")
        drop_db(db)
        # first_step(db)

def third_step(db: DB):
    choice=input("""Per usare il metodo Read inserire: 3
    """)
    try:
        choice=int(choice)
        if choice == 3:
            db.read_op()
            fourth_step(db)
        else:
            print("Errore non hai inserito il numero 3")
            drop_db(db)
            # first_step(db)
    except:
        print("Errore non hai inserito un numero intero")
        drop_db(db)
        # first_step(db)

def fourth_step(db: DB):
    choice=input("""Per usare il metodo Update inserire: 4
    """)
    try:
        choice=int(choice)
        if choice == 4:
            db.update_op()
            fifth_step(db)
        else:
            print("Errore non hai inserito il numero 4")
            drop_db(db)
            # first_step(db)
    except:
        print("Errore non hai inserito un numero intero")
        drop_db(db)
        # first_step(db)

def fifth_step(db: DB):
    choice=input("""Per usare il metodo Delete inserire: 5 
    """)
    try:
        choice=int(choice)
        if choice == 5:
            db.delete_op()
            print("Programma terminato!")
        else:
            print("Errore non hai inserito il numero 5")
            drop_db(db)
            # first_step(db)
    except:
        print("Errore non hai inserito un numero intero")
        drop_db(db)
        # first_step(db)

def drop_db(db: DB):
    print("rigenerando DB")
    db.drop_db()




print("Per far partire il programma premere in sequenza i seguenti codici:\n")

db = DB()
first_step(db)