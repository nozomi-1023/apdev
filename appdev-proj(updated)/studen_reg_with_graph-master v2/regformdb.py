import sqlite3

class Database:
    def __init__(self, db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()
        sql = """
        CREATE TABLE IF NOT EXISTS studentreg(
            "student_number" text NOT NULL,
            "first_name" text NOT NULL,
            "last_name" text NOT NULL,
            "middle_name" text NOT NULL,
            "sex_id" text NOT NULL,
            "year_level_id" text NOT NULL,
            "sports_id" text,
            PRIMARY KEY ("student_number"),
            FOREIGN KEY ("sex_id") REFERENCES "sex_table" ("sex") ON DELETE RESTRICT ON UPDATE RESTRICT,
            FOREIGN KEY ("year_level_id") REFERENCES "year_level_table" ("year_level") ON DELETE RESTRICT ON UPDATE RESTRICT,
            FOREIGN KEY ("sports_id") REFERENCES "sports_table" ("sports") ON DELETE RESTRICT ON UPDATE RESTRICT
            )
        """
        self.cur.execute(sql)
        self.con.commit()

    # Insert Function
    def insert(self, student_number, first_name, last_name, middle_name, sex_id, year_level_id, sports_id):
        self.cur.execute("insert into studentreg values (?,?,?,?,?,?,?)",
                         (student_number, first_name, last_name, middle_name, sex_id, year_level_id, sports_id))
        self.con.commit()

    # Fetch All Data from DB
    def fetch(self):
        self.cur.execute("SELECT * from studentreg")
        rows = self.cur.fetchall()
        # print(rows)
        return rows

    # Delete a Record in DB
    def remove(self, student_number):
        self.cur.execute("delete from studentreg where student_number=?", (student_number,))
        self.con.commit()

    # Update a Record in DB
    def update(self, student_number, first_name, last_name, middle_name, sex_id, year_level_id, sports_id):
        self.cur.execute(
            "update studentreg set first_name=?, last_name=?, middle_name=?, sex_id=?, year_level_id=?, sports_id=? where student_number=?",
            (first_name, last_name, middle_name, sex_id, year_level_id, sports_id, student_number))
        self.con.commit()

    def search(self, student_number, first_name, last_name, middle_name, sex_id, year_level_id, sports_id):
        self.cur.execute("SELECT * FROM studentreg WHERE student_number=? OR first_name=? OR last_name=? OR middle_name=? OR sex_id=? OR year_level_id=? OR sports_id =?",
                         (student_number, first_name, last_name, middle_name, sex_id, year_level_id, sports_id))
        rows = self.cur.fetchall()
        self.con.commit()
        return rows

    def filterYearLevel(self):
        self.cur.execute("select year_level_id, COUNT(year_level_id) from studentreg GROUP BY year_level_id")
        rows = self.cur.fetchall()
        #print(rows)
        return rows

    def filterSports(self):
        self.cur.execute("select sports_id, COUNT(sports_id) from studentreg GROUP BY sports_id")
        rows = self.cur.fetchall()
        #print(rows)
        return rows

    def filterSex(self):
        self.cur.execute("select sex_id, COUNT(sex_id) from studentreg GROUP BY sex_id")
        rows = self.cur.fetchall()
        #print(rows)
        return rows
