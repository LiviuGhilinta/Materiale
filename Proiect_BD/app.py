from flask import Flask, render_template, request,session,redirect,url_for
from db_manager import PythonCon  

app = Flask(__name__)
app.secret_key = "cheiefoartesigura"
db = PythonCon()

@app.route('/') 
def index():
    cont_creat = request.args.get('succes')
    eroare_cont = request.args.get('eroare')
    return render_template('index.html',cont_creat = cont_creat,eroare= eroare_cont)

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

@app.route('/dupa_acces', methods = ['GET',"POST"])
def acces():
    if request.method == 'POST':    
        user = request.form.get("username")
        password = request.form.get("password")
        print(user,password)
        try:
            db.connect(user=user,password=password)
            db.disconnect()
            session['user'] = user
            session['password'] = password
            if user == 'root':
                return render_template('acces_root.html')
            return render_template('dupa_acces.html')
        except Exception as e:
            return redirect(url_for('index',eroare = 1))

    else:
        if 'user' in session and 'password' in session:
            db.connect(user=session['user'],password=session['password'])
            db.disconnect()
            return render_template('dupa_acces.html')
        else:
            return redirect(url_for('index'))    
@app.route('/acces_root')
def root():
    if session.get('user') == 'root':
        return render_template('acces_root.html')

@app.route('/afisare_user')
def vede_user():

    if session.get('user') != 'root':
        return render_template('status.html', titlu="Acces Refuzat", mesaj="Nu aveți permisiunea de a vedea utilizatorii sistemului.")

    try:
        
        db.connect(user=session['user'], password=session['password'])
        date = db.vede_user()
        db.disconnect() 
        
        return render_template('afisare_user.html', users=date)
    except Exception as e:
        if db.con: db.disconnect()
        return f"Eroare la preluarea listei: {e}"
    
@app.route('/sterge_user', methods=['POST'])
def sterge_user_route():
    if session.get('user') != 'root':
        return redirect(url_for('index'))

    selected_users = request.form.getlist('primarykey')
    if not selected_users:
        return render_template('status.html', titlu="Atentie", mesaj="Nu ati selectat niciun user.")

    db.connect(user=session['user'], password=session['password'])
    try:
        count = 0
        for u in selected_users:
            if u == 'root':
                continue 
            db.sterge_user(u)
            count +=1 
        users = db.vede_user()  
        return render_template('status.html', titlu="Felicitari!", mesaj=f"Au fost șterși {count} useri cu succes!.")
    except Exception as e:
        db.disconnect()
        return f"Eroare la ștergere: {e}"
       
@app.route('/create_user',methods = ['GET', 'POST'])
def create_user():
    if request.method == 'POST':
        nou_user = request.form.get('username')
        nou_password = request.form.get('password')
        try:
            db.connect()
            if len(db.active_account(nou_user)) == 0:
                db.create_user(nou_user,nou_password)    
                print(f"Contul a fost realizat cu succes!")
                db.disconnect()
                return redirect(url_for('index',succes = 1))
            else:
                print(db.active_account(nou_user))
                print("Contul deja exista!")
                db.disconnect()
                return render_template('eroare_user.html',eroare_user = nou_user)
           
        except Exception as e:
            return f"A aparut eroarea: {e}"
    return render_template('create_user.html')    
@app.route('/tabela_profesori') 
def afiseaza_profesori():
    try:
        db.connect(user=session['user'],password=session['password'])
        date = db.vedeTabela("profesori")
        db.disconnect()
        return render_template('tabela_profesori.html', profesori=date)
    except Exception as e:
        return f"Eroare: {e}"
    
@app.route('/tabela_cursuri')
def afiseaza_cursuri():
    try:
        db.connect(user=session['user'],password=session['password'])
        date = db.vedeTabela("curs")
        db.disconnect()
        return render_template('tabela_cursuri.html',curs=date)   
    except Exception as e:
        return f"Eroare : {e}"
    
@app.route('/tabela_clasa')
def afiseaza_clasa():
    try:
        db.connect(user=session['user'],password=session['password'])
        date= db.vedeclasa()
        db.disconnect()
        return render_template("tabela_clasa.html",clasa = date)
    except Exception as e:
        return f"Eroare : {e}"

@app.route('/m1_clasa',methods = ['POST','GET'])
def pagina_modifica_clasa():
    try:
        id = request.form.getlist('primarykey')
        if not id:
            return render_template('status.html', titlu = 'Atentie' , mesaj= 'Nu ati setelectat curs')
        id_clasa = id[0]
        db.connect(user=session['user'],password=session['password'])
        rezultat = db.intoarceClasa(id_clasa)
        lista_profesori = db.vedeTabela('profesori')
        lista_curs = db.vedeTabela("curs")
        db.disconnect()
        if rezultat:
            return render_template("m1_clasa.html",clasa = rezultat[0],profesori = lista_profesori, curs = lista_curs , id_aux = id_clasa)
        else:
            return render_template('status.html', titlu="Atentie", mesaj="Clasa nu a fost gasita.")
    except Exception as e:
        return f"Eroare: {e}"
    
@app.route('/m1_curs',methods = ['POST','GET'])
def pagina_modifica_curs():
    try:
        id = request.form.getlist('primarykey')
        if not id:
            return render_template('status.html', titlu = 'Atentie' , mesaj= 'Nu ati setelectat curs')
        id_curs = id[0]
        db.connect(user=session['user'],password=session['password'])
        rezultat = db.intoarcereliniedupaID("curs", "idcurs", id_curs)
        db.disconnect()

        if rezultat:
            return render_template('m1_curs.html', curs=rezultat[0], id_aux=id_curs)
        else:
            return render_template('status.html', titlu="Atentie", mesaj="Cursul nu a fost gasit.")
    except Exception as e:
        return f"Eroare: {e}"

@app.route('/m1_profesor',methods = ['POST','GET'])
def pagina_modifica_profesor():
    try:
        id = request.form.getlist('primarykey')
        if not id:
            return render_template('status.html', titlu = 'Atentie' , mesaj= 'Nu ati setelectat profesorul')
        
        id_profesor = id[0]
        db.connect(user=session['user'],password=session['password'])
        rezultat = db.intoarcereliniedupaID("profesori", "idprofesor", id_profesor)
        db.disconnect()

        if rezultat:
            return render_template('m1_profesor.html', prof=rezultat[0], id_aux=id_profesor)
        else:
            return render_template('status.html', titlu="Atentie", mesaj="Profesorul nu a fost gasit.")
    except Exception as e:
        return f"Eroare: {e}" 

@app.route('/m2_clasa',methods = ['POST'])
def proceseaza_modificare_clasa():
    try:
        aux_id = int(request.form.get('idclasa'))
        idprofesor = request.form.get('idprofesor')
        idcurs = request.form.get('idcurs')
        Datacurs = request.form.get('DataCurs')
        Clasa = request.form.get('Clasa')
        NumarElevi = request.form.get('NumarElevi')
        valori = [idprofesor,idcurs,Datacurs,Clasa,NumarElevi]
        campuri = ['idprofesor','idcurs','DataCurs','Clasa','NumarElevi']

        db.connect(user=session['user'],password=session['password'])
        db.modificaTabela("clasa",'idclasa',aux_id,campuri,valori)
        db.disconnect()
        return render_template('status.html', titlu="Felicitari", mesaj="Modificarile au fost realizate cu succes!")    
    except Exception as e:
        return f"A apărut o eroare la modificare: {e}"

@app.route('/m2_curs', methods=['POST'])
def proceseaza_modificare_curs():
    try:
        aux_id = int(request.form.get('idcurs'))
        nume = request.form.get('Nume')
        disciplina = request.form.get('Disciplina')
        valori = [nume, disciplina]
        campuri = ["Nume", "Disciplina"]

        db.connect(user=session['user'],password=session['password'])
        db.modificaTabela("curs", "idcurs", aux_id, campuri, valori)
        db.disconnect()
        return render_template('status.html', titlu="Felicitari", mesaj="Modificarile au fost realizate cu succes!") 

    except Exception as e:
        return f"A apărut o eroare la modificare: {e}"  
      
@app.route('/m2_profesor',methods=['POST'])
def proceseaza_modificare_profesor():
    try:
        aux_id = int(request.form.get('idprofesor'))
        nume = request.form.get('Nume')
        prenume = request.form.get("Prenume")
        disciplina = request.form.get("Disciplina")
        valori = [nume,prenume,disciplina]
        campuri = ["Nume","Prenume","Disciplina"]

        db.connect(user=session['user'],password=session['password'])
        db.modificaTabela("profesori","idprofesor",aux_id,campuri,valori)
        db.disconnect()
        return render_template('status.html', titlu="Felicitari", mesaj="Modificarile au fost realizate cu succes!") 
    except Exception as e:
            return f"A apărut o eroare la modificare: {e}"

@app.route('/modifica_clasa')
def modifica_clasa():
    try:
        db.connect(user=session['user'],password=session['password'])
        date_clasa = db.vedeclasa()
        db.disconnect()
        
        return render_template('modifica_clasa.html',clasa = date_clasa)
    except Exception as e:
        return f"Eroare la încărcarea tabelului: {e}"        

@app.route('/modifica_curs' )
def modifica_curs():
    try:
        db.connect(user=session['user'],password=session['password'])
        date_curs = db.vedeTabela('curs')
        db.disconnect()
        
        return render_template('modifica_curs.html',curs = date_curs)
    except Exception as e:
        return f"Eroare la încărcarea tabelului: {e}"

@app.route('/modifica_profesor')
def modifica_profesor():
    try:
        db.connect(user=session['user'],password=session['password'])
        date_profesori = db.vedeTabela("profesori")
        db.disconnect()
        
        return render_template('modifica_profesor.html', profesori=date_profesori)
    except Exception as e:
        return f"Eroare la încărcarea tabelului: {e}"   

@app.route('/nou_clasa',methods =['GET','POST'])
def nou_clasa():
    if request.method == 'POST':
        id_prof = request.form.get('idprofesor')
        id_curs = request.form.get('idcurs')
        data_curs = request.form.get("DataCurs")
        clasa = request.form.get('Clasa')
        nr_elevi = request.form.get("NumarElevi")
        if id_prof:
            try: 
                db.connect(user=session['user'],password=session['password'])
                db.adaugaclasa(int(id_prof),int(id_curs),data_curs,clasa,nr_elevi)
                db.disconnect()       
                return render_template('status.html', titlu="Succes!", mesaj="Clasa a fost adăugata cu succes în baza de date.")
            except Exception as e:
                    return f"Eroare la adaugare: {e}"
    else:
        try:
            db.connect(user=session['user'],password=session['password'])
            profesori = db.vedeTabela('profesori')
            curs = db.vedeTabela('curs')
            db.disconnect()
            return render_template('nou_clasa.html', profesori = profesori, curs = curs)
        except Exception as e:
                return f"Eroare la adaugare: {e}"
@app.route("/nou_curs",methods=['GET','POST'])
def nou_curs():
    if request.method == 'POST':
        nume = request.form.get("Nume")
        disciplina = request.form.get('Disciplina')
        if nume:
            try:
                db.connect(user=session['user'],password=session['password'])
                nume = db.adaugaCursuri(nume,disciplina)
                db.disconnect()
                return render_template('status.html', titlu="Succes!", mesaj="Cursul a fost adăugat cu succes în baza de date.")
            except Exception as e:
                    return f"Eroare la adaugare: {e}"
    else:
        try:
            db.connect(user=session['user'],password=session['password'])
            curs = db.vedeTabela('curs')
            db.disconnect()
            return render_template('nou_curs.html',curs = curs)
        except Exception as e:
                return f"Eroare la adaugare: {e}"
             
@app.route("/nou_profesor",methods=['GET','POST'])
def nou_profesor():
    if request.method == 'POST':
        nume = request.form.get("Nume")
        prenume = request.form.get("Prenume")
        disciplina = request.form.get('Disciplina')
        if nume:
            try:
                db.connect(user=session['user'],password=session['password'])
                nume = db.adaugaProfesori(nume,prenume,disciplina)
                db.disconnect()
                return render_template('status.html', titlu="Succes!", mesaj="Profesorul a fost adăugat cu succes în baza de date.")
            except Exception as e:
                    return f"Eroare la adaugare: {e}"
    else:
        try:
            db.connect(user=session['user'],password=session['password'])
            profesori = db.vedeTabela('profesori')
            db.disconnect()
            return render_template('nou_profesor.html',profesori = profesori)
        except Exception as e:
                return f"Eroare la adaugare: {e}" 

@app.route("/sterge_clasa",methods = ['POST'])
def sterge_clasa():
    try:
        s = request.form.getlist("primarykey")
        if s:
            db.connect(user=session['user'],password=session['password'])
            db.stergeDateTabela(s,'clasa','idclasa')
            db.disconnect()
            return render_template('status.html', titlu="Înregistrari sterse", mesaj=f"Cele {len(s)} înregistrari selectate au fost eliminate.")
        else:
            return render_template('status.html', titlu="Atentie", mesaj="Nu ati selectat nicio inregistrare pentru stergere.")
    except Exception as e:
        return f"Eroare la procesarea ștergerii: {e}"

@app.route("/sterge_curs",methods = ['POST'])
def sterge_curs():
    try:
        s = request.form.getlist("primarykey")
        if s:
            db.connect(user=session['user'],password=session['password'])
            db.stergeDateTabela(s,'curs','idcurs')
            db.disconnect()
            return render_template('status.html', titlu="Inregistrari sterse", mesaj=f"Cele {len(s)} înregistrari selectate au fost eliminate.")
        else:
            return render_template('status.html', titlu="Atenție", mesaj="Nu ați selectat nicio înregistrare pentru ștergere.")
    except Exception as e:
        return f"Eroare la procesarea ștergerii: {e}"

@app.route("/sterge_profesor",methods = ['POST'])
def sterge_profesor():
    try:
        s = request.form.getlist("primarykey")
        if s:
            db.connect(user=session['user'],password=session['password'])
            db.stergeDateTabela(s,'profesori','idprofesor')
            db.disconnect()
            return render_template('status.html', titlu="Inregistrari sterse", mesaj=f"Cele {len(s)} înregistrari selectate au fost eliminate.")
        else:
            return render_template('status.html', titlu="Atentie", mesaj="Nu ati selectat nicio inregistrare pentru stergere.")
    except Exception as e:
        return f"Eroare la procesarea ștergerii: {e}"


if __name__ == '__main__':
    app.run(debug=True)