import xlrd
planilhaBalanco = xlrd.open_workbook("../balanco.xls")
balanco = planilhaBalanco.sheet_by_index(0)
demonstrativo = planilhaBalanco.sheet_by_index(1)
class Trimestre:

	def __init__(self, data, ativoTotal, ativoCirculante, caixaEequivalentesDeCaixa, aplicacaoFinanceira, contasAreceber, estoques):
		self.data = data
		self.ativoTotal = ativoTotal
		self.ativoCirculante = ativoCirculante
		self.caixaEequivalentesDeCaixa = caixaEequivalentesDeCaixa
		self.aplicacaoFinanceira = aplicacaoFinanceira
		self.contasAreceber = contasAreceber
		self.estoques = estoques

	def getData(self):
		return self.data

	def getAtivoTotal(self):
		return self.ativoTotal

	def getAtivoCirculante(self):
		return self.ativoCirculante

	def getCaixaEequivalenciaDeCaixa(self):
		return self.caixaEequivalentesDeCaixa

	def getAplicacaoFinanceira(self):
		return self.aplicacaoFinanceira

	def getContasAreceber(self):
		return self.contasAreceber

	def getEstoques(self):
		return self.estoques

class Variaveis:

	def __init__(self, cotacao,quantidadeAcoes):
		self.cotacao = cotacao
		self.quantidadeAcoes = quantidadeAcoes

	def getEbit(self,coluna):
		return demonstrativo.cell_value(6,coluna)+demonstrativo.cell_value(7,coluna)+demonstrativo.cell_value(8,coluna)

	def getLucroLiquido(self,coluna):
		return demonstrativo.cell_value(25,coluna)
	
	def getLucroBruto(self,coluna):
		return demonstrativo.cell_value(6,coluna)
	
	def getReceitaLiquida(self,coluna):
		return demonstrativo.cell_value(4,coluna)

	def getPatrimonioLiquido(self,coluna):
		return balanco.cell_value(47,coluna)

	def getAtivoTotal(self,coluna):
		return balanco.cell_value(2,coluna)

	def getAtivoCirculante(self,coluna):
		return balanco.cell_value(3,coluna)	

	def getPassivoCirculante(self,coluna):
		return balanco.cell_value(27,coluna)

	def getDividasDeCurtoElongoPrazo(self,coluna):
		return balanco.cell_value(28,coluna) + balanco.cell_value(29,coluna) + balanco.cell_value(30,coluna) + balanco.cell_value(31,coluna) + balanco.cell_value(33,coluna) + balanco.cell_value(38,coluna)

	def getDividendos(self,coluna):
		return balanco.cell_value(30,coluna) + balanco.cell_value(31,coluna) + balanco.cell_value(33,coluna)

	def getValorMercado(self):
		return self.cotacao * self.quantidadeAcoes

	def getDividaBruta(self,coluna):
		return balanco.cell_value(31,coluna) + balanco.cell_value(38,coluna)

	def getDisponibilidades(self,coluna):
		return balanco.cell_value(4,coluna) + balanco.cell_value(5,coluna)

	def getDividaLiquida(self,coluna):
		return self.getDividaBruta(coluna) - self.getDisponibilidades(coluna)

	def getValorFirma(self,coluna):
		return self.getValorMercado() + self.getDividaLiquida(coluna)

	def getCaixa(self,coluna):
		return balanco.cell_value(4,coluna)

	def getFornecedores(self,coluna):
		return balanco.cell_value(29,coluna)

	def getAtivosTotaisPorAcao(self,coluna):
		return self.getAtivoTotal(coluna)/self.quantidadeAcoes

	def getCapitalDeGiro(self,coluna):
		return self.getAtivoCirculante(coluna) - self.getPassivoCirculante(coluna)

	def getCapitalDeGiroPorAcao(self,coluna):
		return self.getCapitalDeGiro(coluna)/self.quantidadeAcoes

	def getAtivoCirculanteLiquido(self,coluna):
		return self.getAtivoCirculante(coluna) - getDividasDeCurtoElongoPrazo(coluna)

	def getAtivoCirculanteLiquidoPorAcao(self,coluna):
		return self.getAtivoCirculanteLiquido(coluna)/self.quantidadeAcoes

	def getDividendoPorAcao(self,coluna):
		return self.getDividendos(coluna)/self.quantidadeAcoes

	# Lucro Liquido nos ultimos 12 meses
	def getLucroLiquidoUltimos12meses(self,coluna):
		return self.getLucroLiquido(coluna) + self.getLucroLiquido(coluna+1) + self.getLucroLiquido(coluna+2) + self.getLucroLiquido(coluna+3) 

	def getReceitaLiquidaUltimos12meses(self,coluna):
		return self.getReceitaLiquida(coluna) + self.getReceitaLiquida(coluna+1) + self.getReceitaLiquida(coluna+2) + self.getReceitaLiquida(coluna+3)
	
	# Receita Liquida por acao nos ultimos 12 meses
	def getReceitaLiquidaPorAcao(self,coluna):
		return self.getReceitaLiquidaUltimos12meses(coluna)/self.quantidadeAcoes

	def getEbitUltimos12meses(self,coluna):
		return self.getEbit(coluna) + self.getEbit(coluna+1) + self.getEbit(coluna+2) + self.getEbit(coluna+3)

	def getEbitUltimos12mesesPorAcao(self,coluna):
		return self.getEbitUltimos12meses(coluna)/self.quantidadeAcoes

	def getLucroBrutoUltimos12meses(self,coluna):
		return self.getLucroBruto(coluna) + self.getLucroBruto(coluna+1) + self.getLucroBruto(coluna+2) + self.getLucroBruto(coluna+3)

	# INDICADORES FUNDAMENTALISTAS

	# LP (Lucro por acao Ultimos 12 meses)
	def getLucroPorAcao(self,coluna):
		return self.getLucroLiquidoUltimos12meses(coluna)/self.quantidadeAcoes

	# VPA (Patrimonio Liquido por acao)
	def getPatrimonioLiquidoPorAcao(self,coluna):
		return self.getPatrimonioLiquido(coluna)/self.quantidadeAcoes

	# Marg. Bruta (Lucro Bruto/ Receita Liquida) - ultimos 12 meses
	def getMargBruta(self,coluna):
		return self.getLucroBrutoUltimos12meses(coluna)/self.getReceitaLiquidaUltimos12meses(coluna)

	# Marg. Ebit (EBIT/Receita Liquida) - ultimos 12 meses
	def getMargEBIT(self,coluna):
		return self.getEbitUltimos12meses(coluna)/self.getReceitaLiquidaUltimos12meses(coluna)
	
	# Marg Liquida (Lucro Liquido/ Receita Liquida) ultimos 12 meses
	def getMargLiquida(self,coluna):
		return self.getLucroLiquidoUltimos12meses(coluna)/self.getReceitaLiquidaUltimos12meses(coluna)

	# EBIT/ATIVO (EBIT ultimos 12 meses/ Ativos totais ultimo trimestre)
	def getEBITporAtivos(self,coluna):
		return self.getEbitUltimos12meses(coluna)/self.getAtivoTotal(coluna)

	# ROIC = EBIT ultimos 12 meses/ (Ativos Totais - caixa - fornecedores) ultimo trimestre
	def getROIC(self,coluna):
		return self.getEbitUltimos12meses(coluna)/(self.getAtivoTotal(coluna)-self.getCaixa(coluna)-self.getFornecedores(coluna))

	# ROE = Lucro Liquido ultimos 12 meses/ Patrimonio Liquido ultimo trimestre
	def getROE(self,coluna):
		return self.getLucroLiquidoUltimos12meses(coluna)/self.getPatrimonioLiquido(coluna)
	
	# Liquidez Corr (Ativo Circulante/Passivo Circulante)
	def getLiquidezCorr(self,coluna):
		return self.getAtivoCirculante(coluna)/self.getPassivoCirculante(coluna)
	
	# Div Br / Patrim (Divida Bruta / Patrimonio Liquido)
	def getDividaBrutaPorPatrimonioLiquido(self,coluna):
		return self.getDividaBruta(coluna)/self.getPatrimonioLiquido(coluna)

	#####################

	# P/L
	def getPrecoAcaoPorLucro(self,coluna):
		return self.cotacao/self.getLucroPorAcao(coluna)

	# P/VP
	def getPrecoAcaoPorPatrimonioLiquidoPorAcao(self,coluna):
		return self.cotacao/self.getPatrimonioLiquidoPorAcao(coluna)

	# P/EBIT
	def getPrecoAcaoPorEBITUltimo12mesesPorAcao(self,coluna):
		return self.cotacao/self.getEbitUltimos12mesesPorAcao(coluna)

	# PSR
	def getPrecoAcaoPorReceitaLiquidaPorAcao(self,coluna):
		return self.cotacao/self.getReceitaLiquidaPorAcao(coluna)

	# P/Ativos
	def getPrecoAcaoPorAtivosTotais(self,coluna):
		return self.cotacao/self.getAtivosTotaisPorAcao(coluna)

	# P/Cap. Giro
	def getPrecoAcaoPorCapitalGiroPorAcao(self,coluna):
		return self.cotacao/self.getCapitalDeGiroPorAcao(coluna)

	# P/Ativ Circ Liq
	def getPrecoAcaoPorAtivoCirculanteLiquidoPorAcao(self,coluna):
		return self.cotacao/self.getAtivoCirculanteLiquidoPorAcao(coluna)

	# Div. Yield
	def getDividendoYield(self,coluna):
		return self.getDividendoPorAcao(coluna)/self.contacao

	# EV/EBIT
	def getValorDaFirmaPorEBITUltimos12meses(self,coluna):
		return self.getValorFirma(coluna)/self.getEbitUltimos12meses(coluna)

	# Giros Ativos	
	def getGirosAtivos(self,coluna):
		return self.getReceitaLiquidaUltimos12meses(coluna)/self.getAtivoTotal(coluna)

