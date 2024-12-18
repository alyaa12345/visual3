# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'supplierfull.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import mysql.connector as mc
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem


class Ui_FormSupplier(object):
    def setupUi(self, FormSupplier):
        FormSupplier.setObjectName("FormSupplier")
        FormSupplier.resize(566, 699)
        self.verticalLayoutWidget = QtWidgets.QWidget(FormSupplier)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 160, 281))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.verticalLayout.addWidget(self.label_8)
        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.verticalLayout.addWidget(self.label_9)
        self.label_10 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_10.setObjectName("label_10")
        self.verticalLayout.addWidget(self.label_10)
        self.label_11 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_11.setObjectName("label_11")
        self.verticalLayout.addWidget(self.label_11)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(FormSupplier)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(190, 10, 281, 281))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEdit_id = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_id.setObjectName("lineEdit_id")
        self.verticalLayout_2.addWidget(self.lineEdit_id)
        self.lineEdit_nik = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_nik.setObjectName("lineEdit_nik")
        self.verticalLayout_2.addWidget(self.lineEdit_nik)
        self.lineEdit_name = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.verticalLayout_2.addWidget(self.lineEdit_name)
        self.lineEdit_telp_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_telp_2.setObjectName("lineEdit_telp_2")
        self.verticalLayout_2.addWidget(self.lineEdit_telp_2)
        self.lineEdit_email = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_email.setObjectName("lineEdit_email")
        self.verticalLayout_2.addWidget(self.lineEdit_email)
        self.lineEdit_alamat_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_alamat_2.setObjectName("lineEdit_alamat_2")
        self.verticalLayout_2.addWidget(self.lineEdit_alamat_2)
        self.lineEdit_perusahaan = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_perusahaan.setObjectName("lineEdit_perusahaan")
        self.verticalLayout_2.addWidget(self.lineEdit_perusahaan)
        self.lineEdit_namabank = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_namabank.setObjectName("lineEdit_namabank")
        self.verticalLayout_2.addWidget(self.lineEdit_namabank)
        self.lineEdit_namaakunbank = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_namaakunbank.setObjectName("lineEdit_namaakunbank")
        self.verticalLayout_2.addWidget(self.lineEdit_namaakunbank)
        self.lineEdit_noakunbank = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_noakunbank.setObjectName("lineEdit_noakunbank")
        self.verticalLayout_2.addWidget(self.lineEdit_noakunbank)
        self.horizontalLayoutWidget = QtWidgets.QWidget(FormSupplier)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 320, 461, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)

        self.pushButton.clicked.connect(self.insertSupplier)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)

        self.pushButton_2.clicked.connect(self.updateSupplier)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget)

        self.pushButton_3.clicked.connect(self.deleteSupplier)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.horizontalLayoutWidget)

        self.pushButton_4.clicked.connect(self.loadSupplier)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.label_3 = QtWidgets.QLabel(FormSupplier)
        self.label_3.setGeometry(QtCore.QRect(20, 390, 451, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(FormSupplier)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 440, 461, 161))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tableWidget = QtWidgets.QTableWidget(self.verticalLayoutWidget_3)
        self.tableWidget.cellClicked.connect(self.cellClick)

        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(10)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, item)
        self.verticalLayout_3.addWidget(self.tableWidget)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(FormSupplier)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 630, 461, 51))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_2.addWidget(self.lineEdit_3)
        self.pushButton_5 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)

        self.pushButton_5.clicked.connect(self.cariData)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_2.addWidget(self.pushButton_5)

        self.retranslateUi(FormSupplier)
        QtCore.QMetaObject.connectSlotsByName(FormSupplier)

    def cellClick(self, row, column):
        try:
            id = self.tableWidget.item(row, 0).text()
            nik = self.tableWidget.item(row, 1).text()
            name = self.tableWidget.item(row, 2).text()
            telp = self.tableWidget.item(row, 3).text()
            email = self.tableWidget.item(row, 4).text()
            alamat = self.tableWidget.item(row, 5).text()
            perusahaan = self.tableWidget.item(row, 6).text()
            nama_bank = self.tableWidget.item(row, 7).text()
            nama_akun_bank = self.tableWidget.item(row, 8).text()
            no_akun_bank = self.tableWidget.item(row, 9).text()

            self.lineEdit_id.setText(id)
            self.lineEdit_nik.setText(nik)
            self.lineEdit_name.setText(name)
            self.lineEdit_telp_2.setText(telp)
            self.lineEdit_email.setText(email)
            self.lineEdit_alamat_2.setText(alamat)
            self.lineEdit_perusahaan.setText(perusahaan)
            self.lineEdit_namabank.setText(nama_bank)
            self.lineEdit_namaakunbank.setText(nama_akun_bank)
            self.lineEdit_noakunbank.setText(no_akun_bank)

        except Exception as e:
            error_message = f"Error: {e}"
            self.label_3.setText(error_message)

    def insertSupplier(self):
        try:
            mydb = mc.connect(
                host = "localhost",
                user = "root",
                password = "",
                database = "penjualan"
            )
            cursor = mydb.cursor()
            id = self.lineEdit_id.text()
            nik = self.lineEdit_nik.text()
            name = self.lineEdit_name.text()
            telp = self.lineEdit_telp_2.text()
            email = self.lineEdit_email.text()
            alamat = self.lineEdit_alamat_2.text()
            perusahaan = self.lineEdit_perusahaan.text()
            nama_bank = self.lineEdit_namabank.text()
            nama_akun_bank = self.lineEdit_namaakunbank.text()
            no_akun_bank = self.lineEdit_noakunbank.text()

            sql = "INSERT INTO supplier (id, nik, name, telp, email, alamat, perusahaan, nama_bank, nama_akun_bank, no_akun_bank) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            val = (id, nik, name, telp, email, alamat, perusahaan, nama_bank, nama_akun_bank, no_akun_bank)
            cursor.execute(sql, val)
            mydb.commit()
            self.label_3.setText("Data Supplier Berhasil Dimasukkan!")
            self.lineEdit_id.setText("")
            self.lineEdit_nik.setText("")
            self.lineEdit_name.setText("")
            self.lineEdit_telp_2.setText("")
            self.lineEdit_email.setText("")
            self.lineEdit_alamat_2.setText("")
            self.lineEdit_perusahaan.setText("")
            self.lineEdit_namabank.setText("")
            self.lineEdit_namaakunbank.setText("")
            self.lineEdit_noakunbank.setText("")
        except mc.Error as e:
            error_message = f"Error: {e}"
            self.label_3.setText(error_message)

    def updateSupplier(self):
        try:
            mydb = mc.connect(
                host = "localhost",
                user = "root",
                password = "",
                database = "penjualan"
            )
            cursor = mydb.cursor()
            id = self.lineEdit_id.text()
            nik = self.lineEdit_nik.text()
            name = self.lineEdit_name.text()
            telp = self.lineEdit_telp_2.text()
            email = self.lineEdit_email.text()
            alamat = self.lineEdit_alamat_2.text()
            perusahaan = self.lineEdit_perusahaan.text()
            nama_bank = self.lineEdit_namabank.text()
            nama_akun_bank = self.lineEdit_namaakunbank.text()
            no_akun_bank = self.lineEdit_noakunbank.text()

            sql = "UPDATE supplier SET nik = %s, name = %s, telp = %s, email = %s, alamat = %s, perusahaan = %s, nama_bank = %s, nama_akun_bank = %s, no_akun_bank = %s WHERE id = %s"
            val = (nik, name, telp, email, alamat, perusahaan, nama_bank, nama_akun_bank, no_akun_bank, id)
            cursor.execute(sql, val)
            mydb.commit()
            self.label_3.setText("Data Supplier Berhasil Diubah!")
            self.lineEdit_id.setText("")
            self.lineEdit_nik.setText("")
            self.lineEdit_name.setText("")
            self.lineEdit_telp_2.setText("")
            self.lineEdit_email.setText("")
            self.lineEdit_alamat_2.setText("")
            self.lineEdit_perusahaan.setText("")
            self.lineEdit_namabank.setText("")
            self.lineEdit_namaakunbank.setText("")
            self.lineEdit_noakunbank.setText("")
            self.loadSupplier()
        except mc.Error as e:
            error_message = f"Error: {e}"
            self.label_3.setText(error_message)


    def deleteSupplier(self):
        try:
            mydb = mc.connect(
                host = "localhost",
                user = "root",
                password = "",
                database = "penjualan"
            )
            cursor = mydb.cursor()
            id = self.lineEdit_id.text()
            nik = self.lineEdit_nik.text()
            name = self.lineEdit_name.text()
            telp = self.lineEdit_telp_2.text()
            email = self.lineEdit_email.text()
            alamat = self.lineEdit_alamat_2.text()
            perusahaan = self.lineEdit_perusahaan.text()
            nama_bank = self.lineEdit_namabank.text()
            nama_akun_bank = self.lineEdit_namaakunbank.text()
            no_akun_bank = self.lineEdit_noakunbank.text()

            sql = "DELETE FROM supplier WHERE id = %s AND nik =%s AND name =%s AND telp=%s AND email = %s AND alamat = %s AND perusahaan = %s AND nama_bank = %s AND nama_akun_bank = %s AND no_akun_bank = %s"
            val = (id, nik, name, telp, email, alamat, perusahaan, nama_bank, nama_akun_bank, no_akun_bank)
            cursor.execute(sql, val)
            mydb.commit()
            self.label_3.setText("Data Supplier Berhasil Dihapus!")
            self.lineEdit_id.setText("")
            self.lineEdit_nik.setText("")
            self.lineEdit_name.setText("")
            self.lineEdit_telp_2.setText("")
            self.lineEdit_email.setText("")
            self.lineEdit_alamat_2.setText("")
            self.lineEdit_perusahaan.setText("")
            self.lineEdit_namabank.setText("")
            self.lineEdit_namaakunbank.setText("")
            self.lineEdit_noakunbank.setText("")
        except mc.Error as e:
            error_message = f"Error: {e}"
            self.label_3.setText(error_message)


    def loadSupplier(self):
        try:
            mydb = mc.connect(
                host = "localhost",
                user = "root",
                password = "",
                database = "penjualan"
            )
            mycursor = mydb.cursor()
            mycursor.execute("SELECT * FROM supplier ORDER BY id ASC")
            result = mycursor.fetchall()
            self.tableWidget.setRowCount(0)
            for row_number, row_data in enumerate(result):
                self.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))
                    self.label_3.setText("Data Supplier Berhasil Ditampilkan!")
        except mc.Error as err:
            self.label_3.setText("Data Supplier Gagal Ditampilkan!")

    def cariData(self):
        try:
            keyword = self.lineEdit_3.text()
            mydb = mc.connect(
                host="localhost",
                user="root",
                password="",
                database="penjualan"
            )
            cursor = mydb.cursor()
            sql = "SELECT * FROM supplier WHERE id LIKE %s OR nik LIKE %s OR name LIKE %s OR telp LIKE %s OR email LIKE %s OR alamat LIKE %s OR perusahaan LIKE %s OR nama_bank LIKE %s OR nama_akun_bank LIKE %s OR no_akun_bank LIKE %s"
            val = ("%{}%".format(keyword), "%{}%".format(keyword), "%{}%".format(keyword),  "%{}%".format(keyword),  "%{}%".format(keyword),  "%{}%".format(keyword),  "%{}%".format(keyword),  "%{}%".format(keyword),  "%{}%".format(keyword),  "%{}%".format(keyword))
            cursor.execute(sql, val)
            result = cursor.fetchall()
        
            if not result:
                self.label_3.setText("Data Supplier Yang Dicari Tidak Ada")
                self.tableWidget.setRowCount(0)
                return

            self.tableWidget.setRowCount(0)
            for row_number, row_data in enumerate(result):
                self.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        
            self.label_3.setText("Data Supplier Yang Dicari Ditampilkan")
        except mc.Error as e:
            self.label_3.setText(f"Terjadi Kesalahan Saat Mencari Data: {e}")

    def retranslateUi(self, FormSupplier):
        _translate = QtCore.QCoreApplication.translate
        FormSupplier.setWindowTitle(_translate("FormSupplier", "Form"))
        self.label.setText(_translate("FormSupplier", "ID Supplier"))
        self.label_2.setText(_translate("FormSupplier", "NIK"))
        self.label_4.setText(_translate("FormSupplier", "Nama"))
        self.label_6.setText(_translate("FormSupplier", "Telpon"))
        self.label_5.setText(_translate("FormSupplier", "Email"))
        self.label_7.setText(_translate("FormSupplier", "Alamat"))
        self.label_8.setText(_translate("FormSupplier", "Perusahaan"))
        self.label_9.setText(_translate("FormSupplier", "Nama Bank"))
        self.label_10.setText(_translate("FormSupplier", "Nama Akun Bank"))
        self.label_11.setText(_translate("FormSupplier", "No Akun Bank"))
        self.pushButton.setText(_translate("FormSupplier", "INSERT"))
        self.pushButton_2.setText(_translate("FormSupplier", "UPDATE"))
        self.pushButton_3.setText(_translate("FormSupplier", "DELETE"))
        self.pushButton_4.setText(_translate("FormSupplier", "LOAD DATA"))
        self.label_3.setText(_translate("FormSupplier", "TextLabel"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("FormSupplier", "No"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("FormSupplier", "NIK"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("FormSupplier", "Name"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("FormSupplier", "Telpon"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("FormSupplier", "Email"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("FormSupplier", "Alamat"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("FormSupplier", "Perusahaan"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("FormSupplier", "Nama Bank"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("FormSupplier", "Nama Akun Bank"))
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("FormSupplier", "No Akun Bank"))
        self.pushButton_5.setText(_translate("FormSupplier", "SEARCHING"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FormSupplier = QtWidgets.QWidget()
    ui = Ui_FormSupplier()
    ui.setupUi(FormSupplier)
    FormSupplier.show()
    sys.exit(app.exec_())