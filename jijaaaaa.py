import pymysql
import pymysql.cursors

con = pymysql.connect(host='localhost',
        user='root',
        password='',
        db='si20',
        cursorclass=pymysql.cursors.DictCursor)

try:

    with con.cursor() as cur:

        cur.execute('SELECT * FROM biodata,jadwal limit 5')


        rows = cur.fetchall()
        print("\n-----------------")
        print("|  JADWAL SI 20  |")
        print("-----------------\n")

        for row in rows:
            print("===============================================================\n")
            print(row['Nama'],)
            print(row['NIM'],)
            print(row['Alamat'],)
            print(row['TTL'],)
            print("")
            print("Senin \t = ", row['senin'],)
            print("Selasa \t = ", row['selasa'],)
            print("Rabu \t = ", row['rabu'],)
            print("Kamis \t = ", row['kamis'],)
            print("Jum'at \t = ", row['jumat'],)
            print("\n===============================================================")
            print()
finally:

    con.close()