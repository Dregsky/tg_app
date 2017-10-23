#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xlrd
import trimestre
book = xlrd.open_workbook("../balanco.xls")
print "Número de abas: ", book.nsheets
print "Nomes das Planilhas:", book.sheet_names()
sh = book.sheet_by_index(0)
print(sh.name, sh.nrows, sh.ncols)
print("Valor da célula D30 é ", sh.cell_value(rowx=29, colx=3))
#for rx in range(sh.nrows):
#   print(sh.row(rx))
print range(sh.ncols)
carro = trimestre.Carro("Logan")
print("",carro.getNome())
for curr_col in range(sh.ncols):
    if(curr_col == 2):
    	break
    for curr_row in range(sh.nrows): 
    	data = ""
    	ativoTotal,caixaEequivalenciaDeCaixa,aplicacaoFinanceira,contasAreceber,estoques = 0.0,0.0,0.0,0.0,0.0 
    	if curr_row == 1:
    		data = sh.cell_value(curr_row,curr_col)
    		print("", data)
    	elif curr_row == 2:
    		ativoTotal = sh.cell_value(curr_row,curr_col)
    	elif curr_row == 3:
    		caixaEequivalenciaDeCaixa = sh.cell_value(curr_row,curr_col)
    	elif curr_row == 4:
    		aplicacaoFinanceira = sh.cell_value(curr_row,curr_col)
    	elif curr_row == 5:
    		contasAreceber = sh.cell_value(curr_row,curr_col)
    	elif curr_row == 6:
    		estoques = sh.cell_value(curr_row,curr_col)
    	else :
    		pass		
    	#trimestre = Trimestre(data,ativoTotal,caixaEequivalenciaDeCaixa,aplicacaoFinanceira,contasAreceber,estoques)
    	#print("",trimestre.getData())		
