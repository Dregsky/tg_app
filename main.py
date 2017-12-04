import trimestre,sql
import xlwt
import xlrd
from datetime import datetime
from dateutil.relativedelta import relativedelta

def last_day_of_month(any_day):
    next_month = any_day.replace(day=28) + relativedelta(days=4)  # this will never fail
    return next_month - relativedelta(days=next_month.day)

def writeInvertido(sheet,col,row,value):
	if col == 0:
		sheet.write(col, row-1, value)			
	# se for na linha da data
	elif row == 1:
		col = col * 3
		ultimo_mes_trimestre = datetime.strptime(value, '%d/%m/%Y').date()
		primeiro_mes_trimestre = ultimo_mes_trimestre - relativedelta(months=2)
		segundo_mes_trimestre = ultimo_mes_trimestre - relativedelta(months=1)
		primeiro_mes_trimestre = last_day_of_month(primeiro_mes_trimestre)
		segundo_mes_trimestre = last_day_of_month(segundo_mes_trimestre)
		sheet.write(col, row-1, primeiro_mes_trimestre.strftime('%d/%m/%Y'))			
		sheet.write(col-1, row-1, segundo_mes_trimestre.strftime('%d/%m/%Y'))			
		sheet.write(col-2, row-1, value)
	else:	
		col = col * 3
		sheet.write(col-2, row-1, value)			
		sheet.write(col-1, row-1, value)			
		sheet.write(col, row-1, value)

def indicadores(i,row,col,col_data):
	variaveis1 = trimestre.Variaveis(float(cotacoes.cell_value(row,4)),quantidadeAcoes)
	variaveis2 = trimestre.Variaveis(float(cotacoes.cell_value(row+1,4)),quantidadeAcoes)
	variaveis3 = trimestre.Variaveis(float(cotacoes.cell_value(row+2,4)),quantidadeAcoes)
	# P/L
	if i == 0:	
		sheet.write(row-1, col, str(variaveis1.getPrecoAcaoPorLucro(col_data)))
		sheet.write(row, col, str(variaveis2.getPrecoAcaoPorLucro(col_data)))
		sheet.write(row+1, col, str(variaveis3.getPrecoAcaoPorLucro(col_data)))
	# P/VP
	elif i == 1:
		sheet.write(row-1, col, str(variaveis1.getPrecoAcaoPorPatrimonioLiquidoPorAcao(col_data)))
		sheet.write(row, col, str(variaveis2.getPrecoAcaoPorPatrimonioLiquidoPorAcao(col_data)))
		sheet.write(row+1, col, str(variaveis3.getPrecoAcaoPorPatrimonioLiquidoPorAcao(col_data)))
	# P/EBIT
	elif i == 2:
		sheet.write(row-1, col, str(variaveis1.getPrecoAcaoPorEBITUltimo12mesesPorAcao(col_data)))
		sheet.write(row, col, str(variaveis2.getPrecoAcaoPorEBITUltimo12mesesPorAcao(col_data)))
		sheet.write(row+1, col, str(variaveis3.getPrecoAcaoPorEBITUltimo12mesesPorAcao(col_data)))
	# PSR
	elif i == 3:
		sheet.write(row-1, col, str(variaveis1.getPrecoAcaoPorReceitaLiquidaPorAcao(col_data)))
		sheet.write(row, col, str(variaveis2.getPrecoAcaoPorReceitaLiquidaPorAcao(col_data)))
		sheet.write(row+1, col, str(variaveis3.getPrecoAcaoPorReceitaLiquidaPorAcao(col_data)))
	# P/Ativos
	elif i == 4:
		sheet.write(row-1, col, str(variaveis1.getPrecoAcaoPorAtivosTotais(col_data)))
		sheet.write(row, col, str(variaveis2.getPrecoAcaoPorAtivosTotais(col_data)))
		sheet.write(row+1, col, str(variaveis3.getPrecoAcaoPorAtivosTotais(col_data)))
	# P/Cap. Giro
	elif i == 5:
		sheet.write(row-1, col, str(variaveis1.getPrecoAcaoPorCapitalGiroPorAcao(col_data)))
		sheet.write(row, col, str(variaveis2.getPrecoAcaoPorCapitalGiroPorAcao(col_data)))
		sheet.write(row+1, col, str(variaveis3.getPrecoAcaoPorCapitalGiroPorAcao(col_data)))	
	# P/Ativ Circ Liq
	elif i == 6:
		sheet.write(row-1, col, str(variaveis1.getPrecoAcaoPorAtivoCirculanteLiquidoPorAcao(col_data)))
		sheet.write(row, col, str(variaveis2.getPrecoAcaoPorAtivoCirculanteLiquidoPorAcao(col_data)))
		sheet.write(row+1, col, str(variaveis3.getPrecoAcaoPorAtivoCirculanteLiquidoPorAcao(col_data)))
	# Div. Yield
	elif i == 7:
		sheet.write(row-1, col, str(variaveis1.getDividendoYield(col_data)))
		sheet.write(row, col, str(variaveis2.getDividendoYield(col_data)))
		sheet.write(row+1, col, str(variaveis3.getDividendoYield(col_data)))
	# EV/EBIT
	elif i == 8:
		sheet.write(row-1, col, str(variaveis1.getValorDaFirmaPorEBITUltimos12meses(col_data)))
		sheet.write(row, col, str(variaveis2.getValorDaFirmaPorEBITUltimos12meses(col_data)))
		sheet.write(row+1, col, str(variaveis3.getValorDaFirmaPorEBITUltimos12meses(col_data)))
	# Giros Ativos
	elif i == 9:
		sheet.write(row-1, col, str(variaveis1.getGirosAtivos(col_data)))
		sheet.write(row, col, str(variaveis2.getGirosAtivos(col_data)))
		sheet.write(row+1, col, str(variaveis3.getGirosAtivos(col_data)))
	# LP (Lucro por acao Ultimos 12 meses)
	elif i == 10:
		sheet.write(row-1, col, str(variaveis1.getLucroPorAcao(col_data)))
		sheet.write(row, col, str(variaveis2.getLucroPorAcao(col_data)))
		sheet.write(row+1, col, str(variaveis3.getLucroPorAcao(col_data)))
	# VPA (Patrimonio Liquido por acao)
	elif i == 11:
		sheet.write(row-1, col, str(variaveis1.getPatrimonioLiquidoPorAcao(col_data)))
		sheet.write(row, col, str(variaveis2.getPatrimonioLiquidoPorAcao(col_data)))
		sheet.write(row+1, col, str(variaveis3.getPatrimonioLiquidoPorAcao(col_data)))	
	# Marg. Bruta (Lucro Bruto/ Receita Liquida) - ultimos 12 meses
	elif i == 12:
		sheet.write(row-1, col, str(variaveis1.getMargBruta(col_data)))
		sheet.write(row, col, str(variaveis2.getMargBruta(col_data)))
		sheet.write(row+1, col, str(variaveis3.getMargBruta(col_data)))
	# Marg. Ebit (EBIT/Receita Liquida) - ultimos 12 meses
	elif i == 13:
		sheet.write(row-1, col, str(variaveis1.getMargEBIT(col_data)))
		sheet.write(row, col, str(variaveis2.getMargEBIT(col_data)))
		sheet.write(row+1, col, str(variaveis3.getMargEBIT(col_data)))
	# Marg Liquida (Lucro Liquido/ Receita Liquida) ultimos 12 meses
	elif i == 14:
		sheet.write(row-1, col, str(variaveis1.getMargLiquida(col_data)))
		sheet.write(row, col, str(variaveis2.getMargLiquida(col_data)))
		sheet.write(row+1, col, str(variaveis3.getMargLiquida(col_data)))
	# EBIT/ATIVO (EBIT ultimos 12 meses/ Ativos totais ultimo trimestre)
	elif i == 15:
		sheet.write(row-1, col, str(variaveis1.getEBITporAtivos(col_data)))
		sheet.write(row, col, str(variaveis2.getEBITporAtivos(col_data)))
		sheet.write(row+1, col, str(variaveis3.getEBITporAtivos(col_data)))
	# ROIC = EBIT ultimos 12 meses/ (Ativos Totais - caixa - fornecedores) ultimo trimestre
	elif i == 16:
		sheet.write(row-1, col, str(variaveis1.getROIC(col_data)))
		sheet.write(row, col, str(variaveis2.getROIC(col_data)))
		sheet.write(row+1, col, str(variaveis3.getROIC(col_data)))
	# ROE = Lucro Liquido ultimos 12 meses/ Patrimonio Liquido ultimo trimestre
	elif i == 17:
		sheet.write(row-1, col, str(variaveis1.getROE(col_data)))
		sheet.write(row, col, str(variaveis2.getROE(col_data)))
		sheet.write(row+1, col, str(variaveis3.getROE(col_data)))
	# Liquidez Corr (Ativo Circulante/Passivo Circulante)
	elif i == 18:
		sheet.write(row-1, col, str(variaveis1.getLiquidezCorr(col_data)))
		sheet.write(row, col, str(variaveis2.getLiquidezCorr(col_data)))
		sheet.write(row+1, col, str(variaveis3.getLiquidezCorr(col_data)))
	# Div Br / Patrim (Divida Bruta / Patrimonio Liquido)
	elif i == 19:
		sheet.write(row-1, col, str(variaveis1.getDividaBrutaPorPatrimonioLiquido(col_data)))
		sheet.write(row, col, str(variaveis2.getDividaBrutaPorPatrimonioLiquido(col_data)))
		sheet.write(row+1, col, str(variaveis3.getDividaBrutaPorPatrimonioLiquido(col_data)))


nomeEmpresa = trimestre.nomeEmpresa()
planilhaBalanco = xlrd.open_workbook("balanco/"+nomeEmpresa+".xls")
balanco = planilhaBalanco.sheet_by_index(0)
demonstrativo = planilhaBalanco.sheet_by_index(1)
planilhaCotacao = xlrd.open_workbook("cotacao/"+nomeEmpresa+".xlsx")
cotacoes = planilhaCotacao.sheet_by_index(0)

planilhaSaida = xlwt.Workbook(encoding = 'utf-8')

sheet = planilhaSaida.add_sheet('dados_e_indicadores')

quantidadeAcoes = balanco.cell_value(1,0)

for curr_col in range(balanco.ncols):
	for curr_row in range(1,balanco.nrows):	
		writeInvertido(sheet,curr_col,curr_row,balanco.cell_value(curr_row,curr_col))

for curr_col in range(demonstrativo.ncols):		
	for curr_row in range(2,demonstrativo.nrows):
		row = curr_row + balanco.nrows - 2
		writeInvertido(sheet,curr_col,row,demonstrativo.cell_value(curr_row,curr_col))

indicadores_cabecalho = ["P/L","P/VP","P/EBIT","PSR","P/Ativos","P/Cap. Giro","P/Ativ Circ Liq","Div. Yield","EV/EBIT","Giros Ativos","LP","VPA","Marg. Bruta","Marg. EBIT","Marg. Liquida","EBIT/ATIVO","ROIC","ROE","Liquidez Corr","Div br/Patrim"]

for i in range(len(indicadores_cabecalho)):
  	indicador_nome = indicadores_cabecalho[i]
  	col = i + balanco.nrows + demonstrativo.nrows - 3
  	sheet.write(0, col, indicador_nome)
  	col_data = 0
  	for curr_row in range(2,43,3):
  		col_data+=1
  		indicadores(i,curr_row,col,col_data)
 	

planilhaSaida.save("empresa_dados_mes_ano/"+nomeEmpresa+".xls")

sql.insertEmpresa(nomeEmpresa,quantidadeAcoes)
sql.insertDadosEmpresaMesAno(nomeEmpresa)