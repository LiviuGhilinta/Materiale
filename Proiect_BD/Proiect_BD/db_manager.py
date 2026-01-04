import mysql.connector
from mysql.connector import errorcode

class PythonCon:
    def __init__(self):
        self.error = None
        self.con = None

    def connect(self,bd="proiectbd_java", ip="localhost",user = 'root',password = 'abcd1234'): 
        try:
            self.con = mysql.connector.connect(
                host=ip, 
                port=3306,
                database=bd,
                user = user,
                password = password
            )
            print(f"Conexiune reusita la {bd} pe {ip}")

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                self.error = "Utilizator sau parola gresita."
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                self.error = f"Baza de date {bd} nu exista."    
            else:
                self.error = f"SQLException: {err.msg}"
            raise Exception(self.error)
        except Exception as e:
            self.error = f"A aparut o eroare neprevazuta: {e}"
            raise Exception(self.error)
        
    def create_user(self,user,password):
        try:
            cursor = self.con.cursor(buffered=True)
            query = "create user %s@'localhost' identified by %s;"
            cursor.execute(query,(user,password))

            query_grant = "grant create,select,insert,update,delete on proiectbd_java.* to %s@'localhost';"
            cursor.execute(query_grant,(user,))
            self.con.commit()
            cursor.close()
        except mysql.connector.Error as e:
            return f"Eroarea: {e.msg}"

    def active_account(self,user):
        rs = None
        try:
            cursor = self.con.cursor()
            query = 'select user from mysql.user where user =%s'
            cursor.execute(query,(user,))
            rs = cursor.fetchall()
            cursor.close()
            return rs
        except mysql.connector.Error as e:
            return f"Eroarea: {e.msg}"
    def disconnect(self):
        try:
            if self.con is not None:
                self.con.close()
        except mysql.connector.Error:
            self.error = "Nu se poate inchide conexiunea la baza de date!"
            raise Exception(self.error)
    def adaugaProfesori(self,Nume,Prenume,Disciplina):
        if self.con is not None:
            try:
                cursor = self.con.cursor()
                query = "insert into profesori(Nume, Prenume, Disciplina) values(%s, %s, %s)"
                values = (Nume,Prenume,Disciplina)
                cursor.execute(query,values)
                self.con.commit()
                print("Datele au fost inserate cu succes!")
                cursor.close()
            except mysql.connector.Error as err:
                self.error = "ExceptieSQL: Reactualizare nereusita; este posibil sa existe duplicate sau erori de sintaxa."
                raise Exception(self.error)
        else:
            self.error = "Conexiunea cu baza de date a fost pierduta!"
            raise Exception(self.error)
            
    def adaugaCursuri(self,Nume,Disciplina):
        if self.con is not None:    
            try:
                cursor = self.con.cursor()
                query = "insert into curs(Nume, Disciplina) values(%s,%s)"
                cursor.execute(query,(Nume, Disciplina))
                self.con.commit()
                print("Datele au fost inserate cu succes!")
                cursor.close()
            except mysql.connector.Error:
                self.error = "ExceptieSQL: Reactualizare nereusita; este posibil sa existe duplicate sau erori de sintaxa."
                raise Exception(self.error)  
        else:
            self.error = "Conexiunea cu baza de date a fost pierduta!"
            raise Exception(self.error)
    def adaugaclasa(self,idprofesor,idcurs,DataCurs,Clasa,NumarElevi): 
        if self.con is not None:
            try:
                cursor = self.con.cursor()
                query = "insert into clasa(idprofesor, idcurs, DataCurs,Clasa,NumarElevi) values(%s,%s,%s,%s,%s);"
                cursor.execute(query,(idprofesor,idcurs,DataCurs,Clasa,NumarElevi))
                self.con.commit()
                print("Datele au fost inserate cu succes!")
                cursor.close()
            except mysql.connector.Error:
                self.error = "ExceptieSQL: Reactualizare nereusita; este posibil sa existe duplicate sau erori de sintaxa."
                raise Exception(self.error)  
        else:
            self.error = "Conexiunea cu baza de date a fost pierduta!"
            raise Exception(self.error)

    def vedeTabela(self,tabel):
        rs = None
        try:
            cursor = self.con.cursor()
            query = f"select * from `proiectbd_java`.`{tabel}`"
            cursor.execute(query)
            rs = cursor.fetchall()
            print("Selectarea a fost facuta cu succes")
            cursor.close()
            return rs
        except  mysql.connector.Error as inter_err:
            self.error = f"Eroarea: {inter_err.errno}: {inter_err.msg};"
            raise Exception(self.error)
        except Exception:
            self.error = "A aparut o exceptie in timp ce se extrageau datele."
            raise Exception(self.error)

    def vedeclasa(self):
        rs = None
        try:
            query = f"select a.Nume NumeProfesor, a.Prenume PrenumeProfesor, a.Disciplina, b.Nume NumeCurs, b.Disciplina DisciplinaCurs, c.idclasa, c.idprofesor idprofesor, c.idcurs idcurs, c.DataCurs, c.Clasa, c.NumarElevi from profesori a, curs b, clasa c where a.idprofesor = c.idprofesor and b.idcurs = c.idcurs;"
            cursor = self.con.cursor()
            cursor.execute(query)
            rs = cursor.fetchall()
            print("Selectarea a fost facuta cu succes")
            return rs
        except  mysql.connector.Error as inter_err:
            self.error = f"Eroarea: {inter_err.errno}: {inter_err.msg};"
            raise Exception(self.error)
        except Exception:
            self.error = "A aparut o exceptie in timp ce se extrageau datele."
            raise Exception(self.error)
        
    def stergeDateTabela(self, primaryKeys, tabela, dupaID):
        if self.con is not None:
            try:
                cursor = self.con.cursor()
                delete = f"delete from {tabela} where {dupaID} = %s;"
                for i in primaryKeys:
                    aux = int(i)
                    cursor.execute(delete, (aux,))    
                self.con.commit()
                cursor.close()
                print(f"S-au sters {len(primaryKeys)} inregistrari")
            except mysql.connector.Error as sqle:
                self.error = f"ExceptieSQL ({sqle.errno}): Reactualizare nereusita; {sqle.msg}"
                self.con.rollback()
                raise Exception(self.error)
            except Exception as e:
                self.error = f"A aparut o exceptie in timp ce erau sterse inregistrarile: {e}"
                raise Exception(self.error)
        else:
            self.error = "Exceptie: Conexiunea cu baza de date a fost pierduta."
            raise Exception(self.error)
        
    def stergeTabela(self,tabela):
        if self.con is not None:
            try:
                cursor = self.con.cursor()
                query = f"delete from {tabela};"
                cursor.execute(query)
                self.con.commit()
                cursor.close()
            except mysql.connector.Error as errors:
                self.error = f"Stergere nereusita! A aparut eroarea:{errors.errno}"
                raise Exception(self.error)
        else:
            self.error = "Exceptie: Conexiunea cu baza de date a fost pierduta."
            raise Exception(self.error)

    def modificaTabela(self, tabela,IDTabela,ID,campuri,valori):
        if self.con is not None:
            try:
                set_parts = [f"`{campuri[i]}` = %s" for i in range(len(campuri))]
                query = f"UPDATE `{tabela}` SET {', '.join(set_parts)} WHERE `{IDTabela}` = %s"
                valori_update = list(valori) + [ID]
                cursor = self.con.cursor()
                cursor.execute(query, valori_update)
                self.con.commit()
                cursor.close()
                print("Update realizat cu succes!")
            except mysql.connector.Error as errors:
                self.error = f"Modificare nereusita! A aparut eroarea:{errors.errno}"
                raise Exception(self.error)
        else:
            self.error = "Exceptie: Conexiunea cu baza de date a fost pierduta."
            raise Exception(self.error)
    def intoarceLinie(self,tabela,ID):
        rs = None
        try:
            query = f"Select * from `{tabela}` where idprofesor='{ID}';"
            cursor = self.con.cursor(buffered=True)
            cursor.execute(query)
            rs = cursor.fetchall()
            cursor.close()
            return rs
        except mysql.connector.Error as errors:
                self.error = f"Interogare nereusita! A aparut eroarea:{errors.errno}"
                raise Exception(self.error)
        except Exception:
            self.error = f"Exceptie: {Exception}"
            raise Exception(self.error)
        
    def intoarcereliniedupaID(self,tabela,denumireID,ID):
        rs = None
        try:
            query = f"Select * from `{tabela}` where `{denumireID}` = %s;"
            cursor = self.con.cursor(buffered=True)
            cursor.execute(query,(ID,))
            rs = cursor.fetchall()
            cursor.close()
            return rs
        except mysql.connector.Error as errors:
                self.error = f"Interogare nereusita! A aparut eroarea:{errors.errno}"
                raise Exception(self.error)
        except Exception:
            self.error = f"Exceptie: {Exception}"
            raise Exception(self.error)
    def intoarceClasa(self,ID):
        rs = None
        try:
            query = "select a.Nume NumeProfesor, a.Prenume PrenumeProfesor, a.Disciplina, b.Nume NumeCurs, b.Disciplina DisciplinaCurs, c.idclasa, c.idprofesor idprofesor, c.idcurs idcurs, c.DataCurs, c.Clasa,c.NumarElevi from profesori a,curs b, clasa c where a.idprofesor = c.idprofesor and b.idcurs = c.idcurs and idclasa = %s;"        
            cursor = self.con.cursor(buffered=True)
            cursor.execute(query,(ID,))
            rs = cursor.fetchall()
            cursor.close()
            return rs
        except mysql.connector.Error as errors:
                self.error = f"Interogare nereusita! A aparut eroarea:{errors.errno}"
                raise Exception(self.error)
        except Exception:
            self.error = f"Exceptie: {Exception}"
            raise Exception(self.error)
        
    def vede_user(self):
        rs = None
        try:
            cursor = self.con.cursor()
            query = 'select user,host from mysql.user;'
            cursor.execute(query)
            rs = cursor.fetchall()
            print("Lista cu userii este afisata!")
            return rs
        except  mysql.connector.Error as inter_err:
            self.error = f"Eroarea: {inter_err.errno}: {inter_err.msg};"
            raise Exception(self.error)
        except Exception:
            self.error = "A aparut o exceptie in timp ce se extrageau datele."
            raise Exception(self.error)            


    def sterge_user(self,user,host = 'localhost'):
        try:
            cursor = self.con.cursor()
            query = f"DROP USER `{user}`@`{host}`;"
            cursor.execute(query)
            self.con.commit()
            cursor.close()
            print(f"Userul {user}@{host} a fost sters!")
        except Exception:
            self.error = f"Exceptie: {Exception}"
            raise Exception(self.error)      
