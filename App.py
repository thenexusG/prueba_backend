from flask import Flask, render_template, request, jsonify, redirect,url_for, flash
from flask_mysqldb import MySQL

from Estado import Estados

# Mysql Connection
app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'paquetes'
mysql = MySQL(app)

# settings
app.secret_key = 'key'

@app.route('/')
def Index():
    return render_template('index.html')

@app.route('/searchCP')
def searchCP():
    return render_template('searchCP.html')

@app.route('/AddEstado')
def AddEstado():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM estado')
    data = cur.fetchall()
    return render_template('AddEstado.html', estados = data)

@app.route('/AddMunicipio')
def AddMunicipio():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM municipio')
    data = cur.fetchall()
    return render_template('AddMunicipio.html', municipios = data)

@app.route('/AddColonia')
def AddColonia():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM asentamiento')
    data = cur.fetchall()
    return render_template('AddColonia.html', asentamientos = data)

@app.route('/Estado', methods=['POST'])
def addEstado():
     new_estado = {
         "id_estado": request.form['id_estado'],
         "estado": request.form['estado']
     },
     estado = request.form['estado']
     id_estado = request.form['id_estado']
     cur = mysql.connection.cursor()
     cur.execute('insert into estado (id_estado, estado) values (%s, %s)', (id_estado, estado))
     mysql.connection.commit()
     Estados.append(new_estado)
     print(new_estado)
     flash("Estado correctamente registrado")
     return redirect(url_for('AddEstado')) 
    #  return jsonify({"message": "Estado agregado", "Estado": Estados})

@app.route('/Municipio', methods=['POST'])
def addMunicipio():
     new_municipio = {
         "id_municipio": request.form['id_municipio'],
         "municipio": request.form['municipio'],
         "id_estado": request.form['id_estado']
     },
     id_municipio = request.form['id_municipio']
     municipio = request.form['municipio']
     id_estado = request.form['id_estado']
     cur = mysql.connection.cursor()
     cur.execute('insert into municipio (id_municipio, municipio, id_estado) values (%s, %s, %s)', (id_municipio, municipio, id_estado))
     mysql.connection.commit()
     Estados.append(new_municipio)
     print(new_municipio)
     flash("Municipio correctamente registrado")
     return redirect(url_for('AddMunicipio')) 
    #  return jsonify({"message": "Estado agregado", "Estado": Estados})

@app.route('/Colonia', methods=['POST'])
def addColonia():
     new_colonia = {
         "id_asenta": request.form['id_asenta'],
         "asentamiento": request.form['asentamiento'],
         "id_municipio": request.form['id_municipio'],
         "id_estado": request.form['id_estado'],
         "cp": request.form['cp']
     },
     id_asenta = request.form['id_asenta']
     asentamiento = request.form['asentamiento']
     id_municipio = request.form['id_municipio']
     id_estado = request.form['id_estado']
     cp = request.form['cp']
     cur = mysql.connection.cursor()
     cur.execute('insert into asentamiento (id_asentamiento, asentamiento, id_municipio, id_estado, cp) values (%s, %s, %s, %s,%s)', (id_asenta, asentamiento, id_municipio, id_estado, cp))
     mysql.connection.commit()
     Estados.append(new_colonia)
     print(new_colonia)
     flash("Asentamiento correctamente registrado")
     return redirect(url_for('AddColonia')) 
    #  return jsonify({"message": "Estado agregado", "Estado": Estados})

@app.route('/Municipio_Name', methods=['POST'])
def getMun_name():
    municipio = request.form['municipio']
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM municipio where municipio = %s', [municipio])
    data = cur.fetchall()
    print(data[0])
    return render_template('index.html', municipios = data)

@app.route('/Colonia_Name', methods=['POST'])
def getCol_name():
    colonia = request.form['colonia']
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM asentamiento where asentamiento = %s', [colonia])
    data = cur.fetchall()
    print(data[0])
    return render_template('index.html', asentamientos = data)

@app.route('/Estado_Name', methods=['POST'])
def getEs_name():
    estado = request.form['estado']
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM estado where estado = %s', [estado])
    data = cur.fetchall()
    print(data[0])
    return render_template('index.html', estados = data)

@app.route('/Asentamiento', methods=['POST'])
def getAsent():
    cp = request.form['CP']
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM asentamiento where cp = %s', [cp])
    data = cur.fetchall()
    print(data[0])
    return render_template('searchCP.html', municipios = data)

@app.route('/edit/<id>', methods = ['POST', 'GET'])
def get_estado(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM estado WHERE id_estado = %s', [id])
    data = cur.fetchall()
    cur.close()
    print(data[0])
    return "Recibido"

    
@app.route('/delete/<string:id_estado>')
def delete(id_estado):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM estado WHERE id_estado = {0}'.format(id_estado))
    mysql.connection.commit()
    flash('Estado eliminado')
    return redirect(url_for('Index')) 



@app.route('/Estado')
def getEstados():
    return jsonify({"Estado": Estados})

@app.route('/Estado/<string:estado_name>')
def getEstado(estado_name):
    EstadoFound = [Estados for Estados in Estados if Estados['estado'] == estado_name]
    if (len(EstadoFound) > 0):
        return jsonify({"Estado": EstadoFound[0]})
    return jsonify({"message": "Estado no encontrado"})


@app.route('/Estado/<string:estado_name>', methods=['PUT'])
def editEstado(estado_name):
    EstadosFound = [Estados for Estados in Estados if Estados['estado'] == estado_name]
    if (len(EstadosFound) > 0):
        EstadosFound[0]['estado_id'] = request.form['id_estado']
        EstadosFound[0]['estado'] = request.form['estado']
        return jsonify({
            "message": "Estado actualizado",
            "Estado": EstadosFound[0]
        })
    return jsonify({"message": "estado no encontrado"})

@app.route('/Estado/<string:estado_name>', methods=['DELETE'])
def deleteProduct(estado_name):
    EstadosFound = [Estados for Estados in Estados if Estados['estado'] == estado_name]
    if (len(EstadosFound) > 0):
        Estados.remove(EstadosFound[0])
        return jsonify({"message": "Estado eliminado", "Estados": Estados})
    return jsonify({"message": "Estado no encontrado"})

if __name__ == '__main__':
    app.run(host = "0.0.0.0", port = 3000, debug = True)