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
