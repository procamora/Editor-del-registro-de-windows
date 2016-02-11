# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EditorRegistro.ui'
#
# Created: Fri Feb 12 00:10:35 2016
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(1009, 553)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Icons/Principal.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.gridLayout_2 = QtGui.QGridLayout(Dialog)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.listWidget = QtGui.QListWidget(Dialog)
        self.listWidget.setEditTriggers(QtGui.QAbstractItemView.AllEditTriggers)
        self.listWidget.setLayoutMode(QtGui.QListView.Batched)
        self.listWidget.setSelectionRectVisible(False)
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.gridLayout.addWidget(self.listWidget, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 6, 1)
        self.widget = QtGui.QWidget(Dialog)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.radioButtonBorrar = QtGui.QRadioButton(self.widget)
        self.radioButtonBorrar.setObjectName(_fromUtf8("radioButtonBorrar"))
        self.verticalLayout.addWidget(self.radioButtonBorrar)
        self.radioButtonFinalizada = QtGui.QRadioButton(self.widget)
        self.radioButtonFinalizada.setObjectName(_fromUtf8("radioButtonFinalizada"))
        self.verticalLayout.addWidget(self.radioButtonFinalizada)
        self.gridLayout_2.addWidget(self.widget, 1, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 102, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 0, 1, 1, 1)
        self.pushButtonAnadir = QtGui.QPushButton(Dialog)
        self.pushButtonAnadir.setObjectName(_fromUtf8("pushButtonAnadir"))
        self.gridLayout_2.addWidget(self.pushButtonAnadir, 2, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 158, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 4, 1, 1, 1)
        self.widget_3 = QtGui.QWidget(Dialog)
        self.widget_3.setObjectName(_fromUtf8("widget_3"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.pushButtonAplicar = QtGui.QPushButton(self.widget_3)
        self.pushButtonAplicar.setObjectName(_fromUtf8("pushButtonAplicar"))
        self.horizontalLayout_2.addWidget(self.pushButtonAplicar)
        self.pushButtonCerrar = QtGui.QPushButton(self.widget_3)
        self.pushButtonCerrar.setObjectName(_fromUtf8("pushButtonCerrar"))
        self.horizontalLayout_2.addWidget(self.pushButtonCerrar)
        self.gridLayout_2.addWidget(self.widget_3, 5, 1, 1, 1)
        self.pushButtonRefresh = QtGui.QPushButton(Dialog)
        self.pushButtonRefresh.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("iCONS/menu-32/icon-refreshalt.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonRefresh.setIcon(icon1)
        self.pushButtonRefresh.setObjectName(_fromUtf8("pushButtonRefresh"))
        self.gridLayout_2.addWidget(self.pushButtonRefresh, 3, 1, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.pushButtonCerrar, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.radioButtonBorrar.setText(_translate("Dialog", "Borrar Key", None))
        self.radioButtonFinalizada.setText(_translate("Dialog", "No hacer nada", None))
        self.pushButtonAnadir.setText(_translate("Dialog", "Añadir", None))
        self.pushButtonAplicar.setText(_translate("Dialog", "Aplicar", None))
        self.pushButtonCerrar.setText(_translate("Dialog", "Cerrar", None))

