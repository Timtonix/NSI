import sqlite3



class Candidats:
    def __init__(self) -> None:
        self.con = sqlite3.connect("candidats.db")
        self.cursor = self.con.cursor()
        self.cursor.execute(
            """CREATE TABLE IF NOT EXISTS candidats(nom TEXT NOT NULL, votes INT NOT NULL)"""
        )

        self.con.commit()

    def add_candidat(self, nom):
        self.cursor.execute("INSERT INTO candidats VALUES(?,?)", (nom, 0))
        self.con.commit()
    
    def get_candidats(self):
        self.cursor.execute("SELECT * FROM candidats")
        return self.cursor.fetchall()
    
    def get_candidats_name(self):
        self.cursor.execute("SELECT nom FROM candidats")
        sale = self.cursor.fetchall()
        propre = []
        for c in sale:
            propre.append(c[0])
        return propre
        
    
    def candidat_exist(self, nom):
        self.cursor.execute("SELECT COUNT(*) FROM candidats WHERE nom = ?", (nom, ))
        return self.cursor.fetchone()[0]
    
    def voter(self, nom):
        self.cursor.execute("UPDATE candidats SET votes = votes + 1 WHERE nom = ?", (nom, ))
        print("OKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKk")
        self.con.commit()

    def clear_table(self):
        self.cursor.execute("DROP TABLE candidats")
        self.con.commit()
        self.__init__()

if __name__ == "__main__":
    bdd = Candidats()
    bdd.clear_table()