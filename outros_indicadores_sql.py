import MySQLdb
import xlrd
# Open database connection
db = MySQLdb.connect("localhost","root","root","tg")

# prepare a cursor object using cursor() method
cursor = db.cursor()

def insertOutrosIndicadores(nome):
	print nome
	cursor.execute('INSERT into outros_indicadores (nome) values (%s)',(nome,))
	db.commit()

planilhas = ['indice_de_commodites_agropecuaria','indice_de_commodites_metal','indice_de_commodites_energia','indice_de_commodites_crb', 'indicadores_de_nivel_de_emprego_formal_industria_de_transformacao','indicadores_de_nivel_de_emprego_formal_comercio','indicadores_de_nivel_de_emprego_formal_servico','indicadores_de_nivel_de_emprego_formal_construcao_civil','indicadores_da_conjuntura_economica_vendas_industriais_reais','indicadores_da_conjuntura_economica_horas_trabalhadas_na_producao_na_industria_de_transformacao','indicadores_da_conjuntura_economica_emprego_na_industria_de_transformacao','indicadores_da_conjuntura_economica_salario_real_na_industria_de_transformacao','taxa_de_desocupacao_media']

for i in range(len(planilhas)):
	insertOutrosIndicadores(planilhas[i])
	planilhaDados = xlrd.open_workbook("outros_indicadores/"+planilhas[i]+".xlsx")
	dados = planilhaDados.sheet_by_index(0)
	id_indicador = cursor.lastrowid
	id_ano = 0
	for curr_row in range(dados.nrows):	
	#for curr_row in range(1,53):	
		id_ano+=1
		valores = []
		valores.append(id_indicador)
		valores.append(id_ano)
		valores.append(dados.cell_value(curr_row,1))
		
		query_string = 'INSERT INTO outros_indicadores_por_mes_ano VALUES ({})'.format(", ".join('%s' for _ in range(len(valores))))
		cursor.execute(query_string, valores)
		db.commit()