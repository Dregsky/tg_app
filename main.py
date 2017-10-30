import trimestre
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



variaveis = trimestre.Variaveis(21.18,15717600)
print ("EBIT =" ,variaveis.getEbit(1))
print ("Lucro Liquido =", variaveis.getLucroLiquido(1))
print ("Lucro Bruto =", variaveis.getLucroBruto(1))
print ("Receita liquida =", variaveis.getReceitaLiquida(1))
print ("Patrimonio Liquido =", variaveis.getPatrimonioLiquido(1))
print ("Ativo Total =", variaveis.getAtivoTotal(1))
print ("Ativo Circulante =", variaveis.getAtivoCirculante(1))
print ("Passivo Circulante =", variaveis.getPassivoCirculante(1))
print ("Dividas de Curto e Longo prazo =", variaveis.getDividasDeCurtoElongoPrazo(1))
print ("Dividendos =", variaveis.getDividendos(1))
print ("Valor de Mercado =", variaveis.getValorMercado())
print ("Divida Bruta =", variaveis.getDividaBruta(1))
print ("Disponibilidades =", variaveis.getDisponibilidades(1))
print ("Divida Liquida =", variaveis.getDividaLiquida(1))
print ("Valor Firma =", variaveis.getValorFirma(1))
print ("Caixa =", variaveis.getCaixa(1))
print ("Fornecedores =", variaveis.getFornecedores(1))



planilhaBalanco = xlrd.open_workbook("../balanco.xls")
balanco = planilhaBalanco.sheet_by_index(0)
demonstrativo = planilhaBalanco.sheet_by_index(1)

planilha = xlwt.Workbook(encoding = 'utf-8')

sheet = planilha.add_sheet('indicadores')

for curr_col in range(balanco.ncols):
	for curr_row in range(1,balanco.nrows):	
		writeInvertido(sheet,curr_col,curr_row,balanco.cell_value(curr_row,curr_col))

for curr_col in range(demonstrativo.ncols):		
	for curr_row in range(2,demonstrativo.nrows):
		row = curr_row + balanco.nrows - 2
		writeInvertido(sheet,curr_col,row,demonstrativo.cell_value(curr_row,curr_col))

planilha.save('indicadores.xls')


