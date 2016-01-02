#!/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
import re

from PyQt4 import QtCore, QtGui, uic
from _winreg import HKEY_LOCAL_MACHINE, HKEY_CURRENT_USER

import _winreg
from EditorRegistro_ui import Ui_Dialog
from ConnectSQLite import ConectionSQLite
#http://code.activestate.com/recipes/66011-reading-from-and-writing-to-the-windows-registry/

with open('res.txt', 'w') as outfile: # gorma rapida de vaciar el fichero
	pass

def creaEntrada(hkey, ruta, nombre, rutaFichero):
	aReg = _winreg.ConnectRegistry(None, hkey)
	print r'*** Escribiendo %s\%s ***'%(ruta, nombre)
	aKey = _winreg.OpenKey(aReg, ruta, 0, _winreg.KEY_WRITE)
	try:
		_winreg.SetValueEx(aKey, nombre, 0, _winreg.REG_SZ, rutaFichero) 
	except EnvironmentError:
		print 'Encountered problems writing into the Registry...'

	_winreg.CloseKey(aKey)
	_winreg.CloseKey(aReg)

ruta = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Run'
rutaFichero = r'C:\Users\procamora\Documents\gestor-series\build\exe.win32-2.7\Series.exe'
creaEntrada(HKEY_CURRENT_USER, ruta, 'test', rutaFichero)



class MiFormulario(QtGui.QDialog):
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)
		self.ui = Ui_Dialog()
		self.ui.setupUi(self)
		self.EstadoI = 'Ok' # estado inicial
		self.EstadoF = 'Cancelado' #final
		self.EstadoA = self.EstadoI #actual
		self.db = 'regedit.db'
		self.QueryCompleta = list()   # lista de consultas que se ejecutaran al final
		self.setWindowTitle('Visor del editor de registros')

		self.ui.listWidget.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection) # esto permite selecionar multiples

		self.__sacaSeries()

		self.ui.pushButtonRefresh.clicked.connect(self.__sacaSeries)
		self.ui.pushButtonAnadir.clicked.connect(self.__printCurrentItems)
		self.ui.pushButtonAplicar.clicked.connect(self.__borraEntrada)
		self.ui.pushButtonCerrar.clicked.connect(self.__cancela)


	def __creaEntrada(self, ruta, nombre, rutaFichero):
		aReg = _winreg.ConnectRegistry(None, self.valor_hkey)
		print r'*** Escribiendo %s\%s ***'%(ruta, nombre)
		aKey = _winreg.OpenKey(aReg, ruta, 0, _winreg.KEY_WRITE)
		try:
			_winreg.SetValueEx(aKey, nombre, 0, _winreg.REG_SZ, rutaFichero) 
		except EnvironmentError:
			print 'Encountered problems writing into the Registry...'

		_winreg.CloseKey(aKey)
		_winreg.CloseKey(aReg)


	def __borraEntrada(self):
		for i in self.QueryCompleta:
			nombre = i.split(' ')[0]
			ruta = i.split('|')[-1]

			aReg = _winreg.ConnectRegistry(None, self.valor_hkey)
			print r'*** Borrando  %s\%s ***'%(ruta, nombre)
			aKey = _winreg.OpenKey(aReg, ruta, 0, _winreg.KEY_ALL_ACCESS)

			_winreg.DeleteValue(aKey, nombre)

			_winreg.CloseKey(aKey)
			_winreg.CloseKey(aReg)



	def __muestraEntradas(self):
		self.dictReg = list()
		for i in self.datos:
			#print r'*** Leyendo %s\%s ***'%(i['HKEY'], i['Ruta'])
			
			if i['HKEY'] == 'HKEY_LOCAL_MACHINE':
				self.valor_hkey = HKEY_LOCAL_MACHINE
			elif i['HKEY'] == 'HKEY_CURRENT_USER':
				self.valor_hkey = HKEY_CURRENT_USER
			else:
				self.valor_hkey = HKEY_CURRENT_USER
			

			aReg = _winreg.ConnectRegistry(None, self.valor_hkey)

			aKey = _winreg.OpenKey(aReg, i['Ruta']) 
			for j in range(_winreg.QueryInfoKey(aKey)[1]):
				try:
					n,v,t = _winreg.EnumValue(aKey, j)
					with open('res.txt', 'a') as outfile:
						outfile.write('%s %s %s %s\n'%(j, n, v, t))
					#print i, n, v, t
					self.dictReg.append(r'%s    |%s    |%s'%(n, v, i['Ruta']))

				except EnvironmentError:
					print 'You have',j ,' tasks starting at logon...'
					break

			_winreg.CloseKey(aKey)
			_winreg.CloseKey(aReg)




	def __sacaSeries(self):
		'''
		Saca todas las series de la bd y las mete en una lista de diccionarios accesible en todo el objeto
		'''
		query = '''SELECT Rutas.Ruta, Hkey.HKEY  FROM Rutas  INNER JOIN Hkey ON Hkey.ID = Rutas.id_Hkey'''
		self.datos = ConectionSQLite(self.db, query, True)

		self.ui.radioButtonFinalizada.setChecked(True)
		self.__muestraEntradas()
		self.__buttonAct(self.dictReg)



	def __buttonAct(self, seriesTest):
		'''
		Creo una lista con todas las series que estoy siguiendo
		'''

		self.ui.listWidget.clear()
		if len(seriesTest) != 0:
			for i in seriesTest:
				item=QtGui.QListWidgetItem()
				item.setText(i)
				self.ui.listWidget.addItem(item)
			self.ui.pushButtonAnadir.setVisible(True)
			
		else:
			item=QtGui.QListWidgetItem()
			item.setText('No hay ninguna registro')
			self.ui.listWidget.addItem(item)
			self.ui.pushButtonAnadir.setVisible(False)

		try:   # si no hay ninguno, da fallo
			self.ui.listWidget.setCurrentItem(item)   # establezco por defecto el ultimo, que es el que tiene el valor del item
		except:
			pass


	def __ejecutaQuery(self):
		'''
		Ejecuta todas las consultas que hay en la lista
		'''
		
		for i in self.QueryCompleta:    
			print i
			ConectionSQLite(self.db, i)

		self.QueryCompleta = list()


	def __cancela(self):
		'''
		Establece el estado actual en cancelado para retornar None y ejecuta reject
		'''

		self.EstadoA = self.EstadoF
		self.reject()


	def __printCurrentItems(self):
		'''
		Coge todas las series seleccionadas y las mete en una lista con su respectiva consulta para despues ejecutarlas
		'''
		for i in self.ui.listWidget.selectedItems():
			if self.ui.radioButtonBorrar.isChecked():
				query = r'%s'%i.text()
				self.QueryCompleta.append(query)

		print self.QueryCompleta


	@staticmethod
	def getDatos(parent = None):
		dialog = MiFormulario(parent)
		result = dialog.exec_()


def main():
	app = QtGui.QApplication(sys.argv)
	MiFormulario.getDatos()


if __name__ == '__main__':
	main()
