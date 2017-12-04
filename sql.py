import MySQLdb
import xlrd
# Open database connection
db = MySQLdb.connect("localhost","root","root","tg")

# prepare a cursor object using cursor() method
cursor = db.cursor()

def insertEmpresa(nome,numero_acoes):
	cursor.execute('INSERT into empresa (nome,numero_acoes) values (%s,%s)',(nome,numero_acoes))
	db.commit()

def insertDadosEmpresaMesAno(nomeEmpresa):
	planilhaDados = xlrd.open_workbook("empresa_dados_mes_ano/"+nomeEmpresa+".xls")
	dados = planilhaDados.sheet_by_index(0)
	planilhaCotacao = xlrd.open_workbook("cotacao/"+nomeEmpresa+".xlsx")
	cotacoes = planilhaCotacao.sheet_by_index(0)
	id_ano = 58
	id_empresa = cursor.lastrowid
	for curr_row in range(1,58):	
	#for curr_row in range(1,53):	
		id_ano-=1
		valores = []
		valores.append(id_empresa)
		valores.append(id_ano)
		valores.append(cotacoes.cell_value(curr_row+1,4))
		
		for curr_col in range(1,dados.ncols):
			valores.append(dados.cell_value(curr_row,curr_col))
		
		query_string = 'INSERT INTO dados_e_indicadores_empresa_mes_ano VALUES ({})'.format(", ".join('%s' for _ in range(len(valores))))
		cursor.execute(query_string, valores)
		db.commit()			