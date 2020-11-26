#!/usr/bin/python3

from wsgiref.handlers import CGIHandler
from flask import Flask
from flask import render_template, request, redirect, url_for

## Libs postgres
import psycopg2
import psycopg2.extras

app = Flask(__name__)

## SGBD configs
DB_HOST = "db.tecnico.ulisboa.pt"
DB_USER = "ist192446" 
DB_DATABASE = DB_USER
DB_PASSWORD = "tqtg4683"
DB_CONNECTION_STRING = "host=%s dbname=%s user=%s password=%s" % (DB_HOST, DB_DATABASE, DB_USER, DB_PASSWORD)

## Runs the function once the root page is requested.
## The request comes with the folder structure setting ~/web as the root
@app.route('/')
def index():
	return render_template("index.html")

@app.route('/index')
def _index():
	return redirect(url_for('index'))

@app.route('/medicos', methods=['GET', 'POST'])
def medicos():
	dbConn=None
	cursor=None
	try:
		dbConn = psycopg2.connect(DB_CONNECTION_STRING)
		cursor = dbConn.cursor(cursor_factory = psycopg2.extras.DictCursor)

		if request.method == 'POST':
			query = "INSERT INTO medico(num_cedula, nome, especialidade) VALUES(%s, %s, %s);"
			data = (request.form["num_cedula"], request.form["nome"], request.form["especialidade"])
			cursor.execute(query, data)
				
		query = "SELECT num_cedula, nome, especialidade FROM medico;"
		cursor.execute(query)
		return render_template("medicos.html", cursor=cursor)
	except Exception as e:
		return str(e)
	finally:
		dbConn.commit()	
		cursor.close()
		dbConn.close()

@app.route('/editar_medico', methods=['GET', 'POST'])
def editar_medico():
	dbConn=None
	cursor=None
	try:
		dbConn = psycopg2.connect(DB_CONNECTION_STRING)
		cursor = dbConn.cursor(cursor_factory = psycopg2.extras.DictCursor)

		if request.method == 'POST':
			query = "UPDATE medico SET nome = %s, especialidade = %s WHERE num_cedula = %s;"
			data = (request.form["nome"], request.form["especialidade"], request.form["num_cedula"])
			cursor.execute(query, data)

			return redirect(url_for('medicos'))
		else:
			query = "SELECT num_cedula, nome, especialidade FROM medico WHERE num_cedula = %s;"
			data = (request.args.get('num_cedula'),)
			cursor.execute(query, data)

			return render_template("editar_medico.html", cursor=cursor)
	except Exception as e:
		return str(e)
	finally:
		dbConn.commit()
		cursor.close()
		dbConn.close()

@app.route('/apagar_medico', methods=['GET'])
def apagar_medico():
	dbConn=None
	cursor=None
	try:
		dbConn = psycopg2.connect(DB_CONNECTION_STRING)
		cursor = dbConn.cursor(cursor_factory = psycopg2.extras.DictCursor)
		query = "DELETE FROM medico WHERE num_cedula = %s;"
		data = (request.args.get('num_cedula'),)
		cursor.execute(query, data)
		return redirect(url_for('medicos'))
	except Exception as e:
		return str(e)
	finally:
		dbConn.commit()
		cursor.close()
		dbConn.close()

@app.route('/prescricoes', methods=['GET', 'POST'])
def prescricoes():
	dbConn=None
	cursor=None
	try:
		dbConn = psycopg2.connect(DB_CONNECTION_STRING)
		cursor = dbConn.cursor(cursor_factory = psycopg2.extras.DictCursor)

		if request.method == 'POST':
			query = "INSERT INTO prescricao(num_cedula, num_doente, data_consulta, substancia, quant) VALUES(%s, %s, %s, %s, %s);"
			data = (request.form["num_cedula"], request.form["num_doente"], request.form["data_consulta"], request.form["substancia"], request.form["quant"])
			cursor.execute(query, data)
				
		query = "SELECT num_cedula, num_doente, data_consulta, substancia, quant FROM prescricao;"
		cursor.execute(query)
		return render_template("prescricoes.html", cursor=cursor)
	except Exception as e:
		return str(e)
	finally:
		dbConn.commit()	
		cursor.close()
		dbConn.close()

@app.route('/editar_prescricao', methods=['GET', 'POST'])
def editar_prescricao():
	dbConn=None
	cursor=None
	try:
		dbConn = psycopg2.connect(DB_CONNECTION_STRING)
		cursor = dbConn.cursor(cursor_factory = psycopg2.extras.DictCursor)

		if request.method == 'POST':
			query = "UPDATE prescricao SET quant = %s WHERE num_cedula = %s AND num_doente = %s AND data_consulta = %s AND substancia = %s;"
			data = (request.form["quant"], request.form["num_cedula"], request.form["num_doente"], request.form["data_consulta"], request.form["substancia"])
			cursor.execute(query, data)

			return redirect(url_for('prescricoes'))
		else:
			query = "SELECT num_cedula, num_doente, data_consulta, substancia, quant FROM prescricao WHERE num_cedula = %s AND num_doente = %s AND data_consulta = %s AND substancia = %s;"
			data = (request.args.get('num_cedula'), request.args.get('num_doente'), request.args.get('data_consulta'), request.args.get('substancia'),)
			cursor.execute(query, data)

			return render_template("editar_prescricao.html", cursor=cursor)
	except Exception as e:
		return str(e)
	finally:
		dbConn.commit()
		cursor.close()
		dbConn.close()

@app.route('/apagar_prescricao', methods=['GET'])
def apagar_prescricao():
	dbConn=None
	cursor=None
	try:
		dbConn = psycopg2.connect(DB_CONNECTION_STRING)
		cursor = dbConn.cursor(cursor_factory = psycopg2.extras.DictCursor)
		query = "DELETE FROM prescricao WHERE num_cedula = %s AND num_doente = %s AND data_consulta = %s AND substancia = %s;"
		data = (request.args.get('num_cedula'), request.args.get('num_doente'), request.args.get('data_consulta'), request.args.get('substancia'),)
		cursor.execute(query, data)
		return redirect(url_for('prescricoes'))
	except Exception as e:
		return str(e)
	finally:
		dbConn.commit()
		cursor.close()
		dbConn.close()

@app.route('/instituicoes', methods=['GET', 'POST'])
def instituicoes():
	dbConn=None
	cursor=None
	try:
		dbConn = psycopg2.connect(DB_CONNECTION_STRING)
		cursor = dbConn.cursor(cursor_factory = psycopg2.extras.DictCursor)

		if request.method == 'POST':
			items = request.form['num_regiao_concelho'].split('_')
			num_regiao = items[0]
			num_concelho = items[1]
			query = "INSERT INTO instituicao(nome, tipo, num_regiao, num_concelho) VALUES(%s, %s, %s, %s);"
			data = (request.form["nome"], request.form["tipo"], num_regiao, num_concelho)
			cursor.execute(query, data)

		query = 'SELECT num_concelho, num_regiao, nome FROM concelho ORDER BY nome;'
		cursor.execute(query)
		concelhos = cursor.fetchall()
		
		query = "SELECT nome, tipo, num_regiao, num_concelho FROM instituicao;"
		cursor.execute(query)

		return render_template("instituicoes.html", cursor=cursor, concelhos=concelhos)
	except Exception as e:
		ex = str(type(e).__name__)

		if ex == 'IntegrityError':
			return str('Verifique os dados inseridos')
		elif ex == 'DataError':
			return str('Tem de preencher todos os campos')
		else:
			return str(e)
	finally:
		dbConn.commit()	
		cursor.close()
		dbConn.close()

@app.route('/editar_instituicao', methods=['GET', 'POST'])
def editar_instituicao():
	dbConn=None
	cursor=None
	try:
		dbConn = psycopg2.connect(DB_CONNECTION_STRING)
		cursor = dbConn.cursor(cursor_factory = psycopg2.extras.DictCursor)

		if request.method == 'POST':
			items = request.form['num_regiao_concelho'].split('_')
			num_regiao = items[0]
			num_concelho = items[1]

			query = "UPDATE instituicao SET nome = %s, tipo = %s, num_regiao = %s , num_concelho = %s WHERE nome = %s;"
			data = (request.form['nome'], request.form["tipo"], num_regiao, num_concelho, request.form["nome_old"])
			cursor.execute(query, data)

			return redirect(url_for('instituicoes'))
		else:
			query = 'SELECT num_concelho, num_regiao, nome FROM concelho ORDER BY nome;'
			cursor.execute(query)
			concelhos = cursor.fetchall()

			query = "SELECT nome, tipo, num_regiao, num_concelho FROM instituicao WHERE nome = %s;"
			data = (request.args.get('nome'),)
			cursor.execute(query, data)

			return render_template("editar_instituicao.html", cursor=cursor, concelhos=concelhos)
	except Exception as e:
		return str(e)
	finally:
		dbConn.commit()
		cursor.close()
		dbConn.close()

@app.route('/apagar_instituicao', methods=['GET'])
def apagar_instituicao():
	dbConn=None
	cursor=None
	try:
		dbConn = psycopg2.connect(DB_CONNECTION_STRING)
		cursor = dbConn.cursor(cursor_factory = psycopg2.extras.DictCursor)
		query = "DELETE FROM instituicao WHERE nome = %s;"
		data = (request.args.get('nome'),)
		cursor.execute(query, data)
		return redirect(url_for('instituicoes'))
	except Exception as e:
		return str(e)
	finally:
		dbConn.commit()
		cursor.close()
		dbConn.close()


@app.route('/analises', methods=['GET', 'POST'])
def analises():
	dbConn=None
	cursor=None
	try:
		dbConn = psycopg2.connect(DB_CONNECTION_STRING)
		cursor = dbConn.cursor(cursor_factory = psycopg2.extras.DictCursor)
	
		if request.method == 'POST':
			if request.form['num_cedula'] == '' or request.form['num_doente'] == '' or request.form['data_consulta'] == '':
				query = "INSERT INTO analise(num_analise, especialidade, data_registo, nome, quant, inst ) VALUES(%s, %s, %s, %s ,%s, %s);"
				data = (request.form["num_analise"], request.form["especialidade"], request.form["data_registo"], request.form["nome"], request.form["quant"], request.form["inst"])
			else:
				query = "INSERT INTO analise(num_analise, especialidade, num_cedula, num_doente, data_consulta, data_registo, nome, quant, inst ) VALUES(%s, %s, %s, %s, %s, %s, %s ,%s, %s);"
				data = (request.form["num_analise"], request.form["especialidade"], request.form["num_cedula"], request.form["num_doente"], request.form["data_consulta"], request.form["data_registo"], request.form["nome"], request.form["quant"], request.form["inst"])
			cursor.execute(query, data)
			
		query = "SELECT * FROM analise ORDER BY num_analise;"
		cursor.execute(query)
		return render_template('analises.html', cursor=cursor)
	except Exception as e:
		return str(e)
	finally:
		dbConn.commit()
		cursor.close()
		dbConn.close()

@app.route('/editar_analise', methods=['GET', 'POST'])
def editar_analise():
	dbConn=None
	cursor=None
	try:
		dbConn = psycopg2.connect(DB_CONNECTION_STRING)
		cursor = dbConn.cursor(cursor_factory = psycopg2.extras.DictCursor)

		if request.method == 'POST':
			query = "UPDATE analise SET especialidade = %s, num_cedula = %s, num_doente = %s, data_consulta = %s, data_registo = %s, nome = %s, quant = %s, inst = %s WHERE num_analise = %s;"
			data = (request.form['especialidade'], request.form['num_cedula'], request.form['num_doente'], request.form['data_consulta'], request.form['data_registo'], request.form['nome'], request.form['quant'], request.form['inst'], request.form['num_analise'])
			cursor.execute(query, data)

			return redirect(url_for('analises'))
		else:
			query = "SELECT * FROM analise WHERE num_analise = %s;"
			data = (request.args.get('num_analise'),)
			cursor.execute(query, data)

			return render_template("editar_analise.html", cursor=cursor)
	except Exception as e:
		return str(e)
	finally:
		dbConn.commit()
		cursor.close()
		dbConn.close()
		
@app.route('/apagar_analise', methods=['GET'])
def apagar_analise():
	dbConn=None
	cursor=None
	try:
		dbConn = psycopg2.connect(DB_CONNECTION_STRING)
		cursor = dbConn.cursor(cursor_factory = psycopg2.extras.DictCursor)

		query = "DELETE FROM analise WHERE num_analise = %s;"
		data = (request.args.get('num_analise'),)
		cursor.execute(query, data)

		return redirect(url_for('analises'))
	except Exception as e:
		return str(e)
	finally:
		dbConn.commit()
		cursor.close()
		dbConn.close()


@app.route('/venda', methods=['GET', 'POST'])
def venda():
	dbConn=None
	cursor=None
	try:
		dbConn = psycopg2.connect(DB_CONNECTION_STRING)
		cursor = dbConn.cursor(cursor_factory = psycopg2.extras.DictCursor)

		if request.method == 'POST':
			query = "INSERT INTO venda_farmacia(num_venda, data_registo,substancia, quant, preco, inst) VALUES(%s, current_date, %s, %s, %s, %s);"
			data = (request.form["num_venda"], request.form["substancia"], request.form["quant"], request.form["preco"], request.form["inst"])
			cursor.execute(query, data)

		return render_template('venda.html')
	except Exception as e:
		return str(e)
	finally:
		dbConn.commit()
		cursor.close()
		dbConn.close()

@app.route('/venda_prescricao', methods=['GET', 'POST'])
def venda_prescricao():
	dbConn=None
	cursor=None
	try:
		dbConn = psycopg2.connect(DB_CONNECTION_STRING)
		cursor = dbConn.cursor(cursor_factory = psycopg2.extras.DictCursor)

		query = "SELECT * FROM prescricao;"
		cursor.execute(query)
		
		return render_template('venda_prescricao.html', cursor=cursor)
	except Exception as e:
		return str(e)
	finally:
		cursor.close()
		dbConn.close()

@app.route('/venda_prescricao_form', methods=['GET', 'POST'])
def venda_prescricao_form():
	dbConn=None
	cursor=None
	try:
		dbConn = psycopg2.connect(DB_CONNECTION_STRING)
		cursor = dbConn.cursor(cursor_factory = psycopg2.extras.DictCursor)

		if request.method == 'POST':
			query = "INSERT INTO venda_farmacia(num_venda, data_registo, substancia, quant, preco, inst) VALUES(%s, current_date, %s, %s, %s, %s);"
			data = (request.form["num_venda"], request.form["substancia"], request.form["quant"], request.form["preco"], request.form["inst"])
			cursor.execute(query, data)
			dbConn.commit()

			query = "INSERT INTO prescricao_venda(num_cedula, num_doente, data_consulta, substancia, num_venda) VALUES(%s, %s, %s, %s, %s);"
			data = (request.form["num_cedula"], request.form["num_doente"], request.form["data_consulta"], request.form["substancia"], request.form["num_venda"])
			cursor.execute(query, data)
			
			return redirect('venda_prescricao')
		else:
			query = "SELECT num_cedula, num_doente, data_consulta, substancia, quant FROM prescricao WHERE num_cedula = %s AND num_doente = %s AND data_consulta = %s AND substancia = %s;"
			data = (request.args.get("num_cedula"), request.args.get("num_doente"), request.args.get("data_consulta"), request.args.get("substancia"))
			cursor.execute(query, data)

			return render_template('venda_prescricao_form.html', cursor = cursor)
	except Exception as e:
		return str(e)
	finally:
		dbConn.commit()
		cursor.close()
		dbConn.close()


@app.route('/listar_substancias', methods=['GET', 'POST'])
def listar_substancias():
	dbConn=None
	cursor=None
	try:
		dbConn = psycopg2.connect(DB_CONNECTION_STRING)
		cursor = dbConn.cursor(cursor_factory = psycopg2.extras.DictCursor)

		if request.method == 'POST':
			query = "SELECT m.nome, substancia, EXTRACT(MONTH FROM p.data_consulta), EXTRACT(YEAR FROM p.data_consulta) FROM medico m NATURAL JOIN prescricao p WHERE num_cedula = %s AND EXTRACT(MONTH FROM p.data_consulta) = %s AND EXTRACT(YEAR FROM p.data_consulta) = %s;"
			data = (request.form['medico'], request.form['mes'], request.form['ano'])
			cursor.execute(query, data)

			return render_template('listar_substancias.html', cursor=cursor)
		
		return render_template('listar_substancias.html', cursor = None)

	except Exception as e:
		return str(e)
	finally:
		cursor.close()
		dbConn.close()

@app.route('/listar_glicemia', methods=['GET'])
def listar_glicemia():
	dbConn=None
	cursor=None
	try:
		dbConn = psycopg2.connect(DB_CONNECTION_STRING)
		cursor = dbConn.cursor(cursor_factory = psycopg2.extras.DictCursor)

		query = "SELECT * FROM (SELECT c.nome, a.num_doente, max(quant) glicemia FROM analise a JOIN instituicao i ON a.inst=i.nome JOIN concelho c ON i.num_concelho = c.num_concelho WHERE a.nome = 'glicemia' OR a.nome = 'Glicemia' GROUP BY a.num_doente, c.nome) a1 NATURAL JOIN (SELECT DISTINCT c.nome, max(quant) glicemia FROM analise a JOIN instituicao i ON a.inst=i.nome JOIN concelho c ON i.num_concelho = c.num_concelho WHERE a.nome = 'glicemia' OR a.nome = 'Glicemia' GROUP BY c.nome) a2;"
		cursor.execute(query)
		glicemia_max = cursor.fetchall()

		query = "SELECT * FROM (SELECT c.nome, a.num_doente, min(quant) glicemia FROM analise a JOIN instituicao i ON a.inst=i.nome JOIN concelho c ON i.num_concelho = c.num_concelho WHERE a.nome = 'glicemia' OR a.nome = 'Glicemia' GROUP BY a.num_doente, c.nome) a1 NATURAL JOIN (SELECT DISTINCT c.nome, min(quant) glicemia FROM analise a JOIN instituicao i ON a.inst=i.nome JOIN concelho c ON i.num_concelho = c.num_concelho WHERE a.nome = 'glicemia' OR a.nome = 'Glicemia' GROUP BY c.nome) a2;"
		cursor.execute(query)
		glicemia_min = cursor.fetchall()

		return render_template('listar_glicemia.html', max=glicemia_max, min=glicemia_min)
	except Exception as e:
		return str(e)
	finally:
		cursor.close()
		dbConn.close()

CGIHandler().run(app)

