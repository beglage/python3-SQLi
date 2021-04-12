import sys
import B_SQL2
import U_SQL
import E_SQL
import T_SQL
import test_bihe
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class window1(QWidget):
    def __init__(self):
        super().__init__()
        self.newwindowUI()
    def newwindowUI(self):
        self.setWindowTitle('布尔盲注')
        self.resize(500,500)
        self.setWindowOpacity(0.9)
        label1=QLabel('测试结果:',self)
        label1.move(0,280)
        self.text1=QTextBrowser(self)
        self.text1.move(0,300)
        self.text1.resize(500,200)
        self.text1.setPlainText('')
        button1=QPushButton('检验',self)
        button1.move(200,50)
        button1.clicked.connect(self.jianyan)
        button3=QComboBox(self)
        button3.addItems(["获取数据库名","获取表名","获取字段名","获取用户信息"])
        button3.move(185,150)
        button3.activated[str].connect(self.get)

        label1=QLabel('表名：',self)
        label1.move(130,190)

        label2=QLabel('字段名1：',self)
        label2.move(130,220)

        label3=QLabel('字段名2：',self)
        label3.move(130,250)

        self.text2=QLineEdit(self)#表名
        self.text2.move(190,180)
        self.text2.resize(100,30)
        button0 = QPushButton('确定', self)
        button0.move(300,180)
        button0.resize(70,30)
        button0.clicked.connect(self.save)


        self.text3=QLineEdit(self)#字段名1
        self.text3.move(190,210)
        self.text3.resize(100,30)
        button2 = QPushButton('确定', self)
        button2.move(300,210)
        button2.resize(70,30)
        button2.clicked.connect(self.save1)

        self.text4=QLineEdit(self)#字段名2
        self.text4.move(190,240)
        self.text4.resize(100,30)
        button4 = QPushButton('确定', self)
        button4.move(300,240)
        button4.resize(70,30)
        button4.clicked.connect(self.save2)


    def jianyan(self):
        URL=open("1.txt","r").read()
        A=B_SQL2.B(URL)
        if "error" in A.isBoolSQLI():
            QMessageBox.critical(self, '警告', '该url不能使用布尔盲注！请使用其他注入方式', QMessageBox.Ok)
            self.close()
        else:
            QMessageBox.information(self,'合理','可以使用布尔盲注，请继续！',QMessageBox.Ok)
            self.text1.setPlainText('[+]检验完成！')

    def get(self,text):
        URL=open("1.txt","r").read()
        A=B_SQL2.B(URL)
        if text=="获取数据库名":
            self.text1.setPlainText('当前数据库名为：'+A.getCurrentDbName())
        if text=="获取表名":
            self.text1.setPlainText('当前表名为：' + A.getTableName(A.getCurrentDbName()))
        if text=="获取字段名":
            if self.text2.text()=='':
                QMessageBox.critical(self, '警告', '请输入表名', QMessageBox.Ok)
            else :
                self.text1.setPlainText("当前字段名为："+A.getColumnName(open("2.txt","r").read()))
        if text=="获取用户信息":
            if self.text3.text()=='' or self.text4.text()=='' or self.text2.text()=='':
                QMessageBox.critical(self, '警告', '请输入表名(字段名)', QMessageBox.Ok)
            else:
                self.text1.setPlainText("当前用户信息为（用户名:密码）："+A.getUserInfo(open("3.txt","r").read(),open("4.txt","r").read(),open("2.txt","r").read()))

    def save(self):
        open("2.txt", "w").write(self.text2.text())
    def save1(self):
        open("3.txt", "w").write(self.text3.text())
    def save2(self):
        open("4.txt", "w").write(self.text4.text())


class window2(QWidget):
    def __init__(self):
        super().__init__()
        self.newwindowUI()
    def newwindowUI(self):
        self.setWindowTitle('联合注入')
        self.resize(500,500)
        self.setWindowOpacity(0.9)
        label1=QLabel('测试结果:',self)
        label1.move(0,280)
        self.text1=QTextBrowser(self)
        self.text1.move(0,300)
        self.text1.resize(500,200)
        self.text1.setPlainText('')
        button1=QPushButton('检验',self)
        button1.move(200,50)
        button1.clicked.connect(self.jianyan)
        button3=QComboBox(self)
        button3.addItems(["获取数据库名", "获取表名", "获取字段名", "获取用户信息"])
        button3.move(185,150)
        button3.activated[str].connect(self.get)

        label1=QLabel('表名：',self)
        label1.move(130,190)

        label2=QLabel('字段名1：',self)
        label2.move(130,220)

        label3=QLabel('字段名2：',self)
        label3.move(130,250)

        self.text2=QLineEdit(self)
        self.text2.move(190,180)
        self.text2.resize(100,30)
        button0 = QPushButton('确定', self)
        button0.move(300,180)
        button0.resize(70,30)
        button0.clicked.connect(self.save)


        self.text3=QLineEdit(self)
        self.text3.move(190,210)
        self.text3.resize(100,30)
        button2 = QPushButton('确定', self)
        button2.move(300,210)
        button2.resize(70,30)
        button2.clicked.connect(self.save1)

        self.text4=QLineEdit(self)
        self.text4.move(190,240)
        self.text4.resize(100,30)
        button4 = QPushButton('确定', self)
        button4.move(300,240)
        button4.resize(70,30)
        button4.clicked.connect(self.save2)

    def jianyan(self):
        URL=open("1.txt","r").read()
        A=U_SQL.U(URL)
        if "error" in A.isUnionSQLI():
            QMessageBox.critical(self, '警告', '该url不能使用联合注入！请使用其他注入方式', QMessageBox.Ok)
            self.close()
        else:
            QMessageBox.information(self,'合理','可以使用联合注入，请继续！',QMessageBox.Ok)
            self.text1.setPlainText('[+]检验完成！')

    def get(self,text):
        URL=open("1.txt","r").read()
        A=U_SQL.U(URL)
        payload=A.getTestPayload()
        point=A.getInjectionPoint(payload)
        if text=="获取数据库名":
            self.text1.setPlainText('当前数据库名为：'+A.getCurrentDbName(point,payload))
        if text == "获取表名":
            self.text1.setPlainText('当前表名为：' + A.getTableName(point,payload,A.getCurrentDbName(point,payload)))
        if text == "获取字段名":
            if self.text2.text()=='':
                QMessageBox.critical(self, '警告', '请输入表名', QMessageBox.Ok)
            else:
                self.text1.setPlainText('当前字段名为：'+A.getColumnName(point,payload,open("2.txt", "r").read()))
        if text == "获取用户信息":
            if self.text3.text()=='' or self.text4.text()=='' or self.text2.text()=='':
                QMessageBox.critical(self, '警告', '请输入表名(字段名)', QMessageBox.Ok)
            else:
                self.text1.setPlainText('当前用户信息为（用户名:密码）：' + A.getUserInfo(point, payload, open("3.txt", "r").read(),open("4.txt", "r").read(),open("2.txt", "r").read()))

    def save(self):
        open("2.txt", "w").write(self.text2.text())
    def save1(self):
        open("3.txt", "w").write(self.text3.text())
    def save2(self):
        open("4.txt", "w").write(self.text4.text())


class window3(QWidget):
    def __init__(self):
        super().__init__()
        self.newwindowUI()
    def newwindowUI(self):
        self.setWindowTitle('延时注入')
        self.resize(500, 500)
        self.setWindowOpacity(0.9)
        label1 = QLabel('测试结果:', self)
        label1.move(0, 280)
        self.text1 = QTextBrowser(self)
        self.text1.move(0, 300)
        self.text1.resize(500, 200)
        self.text1.setPlainText('')
        button1 = QPushButton('检验', self)
        button1.move(200, 50)
        button1.clicked.connect(self.jianyan)
        button3 = QComboBox(self)
        button3.addItems(["获取数据库名","获取表名","获取字段名","获取用户信息"])
        button3.move(185, 150)
        button3.activated[str].connect(self.get)

        label1=QLabel('表名：',self)
        label1.move(130,190)

        label2=QLabel('字段名1：',self)
        label2.move(130,220)

        label3=QLabel('字段名2：',self)
        label3.move(130,250)

        self.text2=QLineEdit(self)
        self.text2.move(190,180)
        self.text2.resize(100,30)
        button0 = QPushButton('确定', self)
        button0.move(300,180)
        button0.resize(70,30)
        button0.clicked.connect(self.save)


        self.text3=QLineEdit(self)
        self.text3.move(190,210)
        self.text3.resize(100,30)
        button2 = QPushButton('确定', self)
        button2.move(300,210)
        button2.resize(70,30)
        button2.clicked.connect(self.save1)

        self.text4=QLineEdit(self)
        self.text4.move(190,240)
        self.text4.resize(100,30)
        button4 = QPushButton('确定', self)
        button4.move(300,240)
        button4.resize(70,30)
        button4.clicked.connect(self.save2)

    def jianyan(self):
        URL = open("1.txt", "r").read()
        A = T_SQL.T(URL)
        if "error" in A.isTimeSQLI():
            QMessageBox.critical(self, '警告', '该url不能使用延时注入！请使用其他注入方式', QMessageBox.Ok)
            self.close()
        else:
            QMessageBox.information(self, '合理', '可以使用延时注入，请继续！', QMessageBox.Ok)
            self.text1.setPlainText('[+]检验完成！')
    def get(self,text):
        URL=open("1.txt","r").read()
        A = T_SQL.T(URL)
        if text=="获取数据库名":
            self.text1.setPlainText('当前数据库名为：'+A.getCurrentDbName())
        if text=='获取表名':
            self.text1.setPlainText("当前表名为："+A.getTableName(A.getCurrentDbName()))
        if text=='获取字段名':
            if self.text2.text()=='':
                QMessageBox.critical(self, '警告', '请输入表名', QMessageBox.Ok)
            else:
                self.text1.setPlainText('当前字段名为：'+A.getColumnName(open("2.txt",'w').read()))
        if text =='获取用户信息':
            if self.text2.text()=='' or self.text3.text()=='' or self.text4.text()=='':
                QMessageBox.critical(self, '警告', '请输入表名(字段名)', QMessageBox.Ok)
            else:
                self.text1.setPlainText('当前用户信息为（用户名:密码）：' + A.getUserInfo(point, payload, open("3.txt", "r").read(),open("4.txt", "r").read(),open("2.txt", "r").read()))


    def save(self):
        open("2.txt", "w").write(self.text2.text())
    def save1(self):
        open("3.txt", "w").write(self.text3.text())
    def save2(self):
        open("4.txt", "w").write(self.text4.text())

class window4(QWidget):
    def __init__(self):
        super().__init__()
        self.newwindowUI()
    def newwindowUI(self):
        self.setWindowTitle('报错注入')
        self.resize(500, 500)
        self.setWindowOpacity(0.9)
        label1 = QLabel('测试结果:', self)
        label1.move(0, 280)
        self.text1 = QTextBrowser(self)
        self.text1.move(0, 300)
        self.text1.resize(500, 200)
        button1 = QPushButton('检验', self)
        button1.move(200, 50)
        button1.clicked.connect(self.jianyan)
        button3 = QComboBox(self)
        button3.addItems(["获取数据库名","获取表名","获取字段名","获取用户信息"])
        button3.move(185, 150)
        button3.activated[str].connect(self.get)

        label1=QLabel('表名：',self)
        label1.move(130,190)

        label2=QLabel('字段名1：',self)
        label2.move(130,220)

        label3=QLabel('字段名2：',self)
        label3.move(130,250)

        self.text2=QLineEdit(self)
        self.text2.move(190,180)
        self.text2.resize(100,30)
        button0 = QPushButton('确定', self)
        button0.move(300,180)
        button0.resize(70,30)
        button0.clicked.connect(self.save)


        self.text3=QLineEdit(self)
        self.text3.move(190,210)
        self.text3.resize(100,30)
        button2 = QPushButton('确定', self)
        button2.move(300,210)
        button2.resize(70,30)
        button2.clicked.connect(self.save1)

        self.text4=QLineEdit(self)
        self.text4.move(190,240)
        self.text4.resize(100,30)
        button4 = QPushButton('确定', self)
        button4.move(300,240)
        button4.resize(70,30)
        button4.clicked.connect(self.save2)

    def jianyan(self):
        URL = open("1.txt", "r").read()
        A = E_SQL.E(URL)
        if "error" in A.isErrorSQLI():
            QMessageBox.critical(self, '警告', '该url不能使用报错注入！请使用其他注入方式', QMessageBox.Ok)
            self.close()
        else:
            QMessageBox.information(self, '合理', '可以使用报错注入，请继续！', QMessageBox.Ok)
            self.text1.setPlainText('[+]检验完成！')

    def get(self, text):
        URL = open("1.txt", "r").read()
        A = E_SQL.E(URL)
        if text == "获取数据库名":
            self.text1.setPlainText('当前数据库名为：' +A.getCurrentDbName())
        if text=='获取表名':
            self.text1.setPlainText('当前数据库名为：' + A.getTableName(A.getCurrentDbName()))
        if text=='获取字段名':
            if self.text2.text()=='':
                QMessageBox.critical(self, '警告', '请输入表名', QMessageBox.Ok)
            else:
                self.text1.setPlainText('当前表名为：' + A.getColumnName( open("2.txt", "r").read()))
        if text=='获取用户信息':
            if self.text2.text()=='' or self.text3.text()=='' or self.text4.text()=='':
                QMessageBox.critical(self, '警告', '请输入表名(字段名)', QMessageBox.Ok)
            else:
                self.text1.setPlainText('当前用户信息为（用户名:密码）：' + A.getUserInfo(open("3.txt", "r").read(),open("4.txt", "r").read(),open("2.txt", "r").read()))



    def save(self):
        open("2.txt", "w").write(self.text2.text())
    def save1(self):
        open("3.txt", "w").write(self.text3.text())
    def save2(self):
        open("4.txt", "w").write(self.text4.text())

class mainwindow(QWidget):
    def __init__(self):
        super().__init__()
        self.windowUI()
    def windowUI(self):
        label1=QLabel('URL：',self)
        label1.move(20,100)
        self.text2=QTextBrowser(self)
        self.text2.move(160,130)
        self.text2.resize(175,30)
        self.text1=QLineEdit(self)
        self.text1.move(60,90)
        self.text1.resize(350,30)
        button0 = QPushButton('确定', self)
        button0.move(420,90)
        button0.resize(70,30)
        button0.clicked.connect(self.save)
        button1=QPushButton('布尔盲注',self)
        button1.move(200,400)
        button1.resize(100,50)
        button1.clicked.connect(self.onclick1)

        button2=QPushButton('联合注入',self)
        button2.move(200,200)
        button2.resize(100,50)
        #button2.setStyleSheet("color:black;font-size:20px;background-color:white;"
        #                     "border-style:none;border:3px ; padding:5px;"
         #                     "min-height:20px;border-radius:15px;")
        button2.clicked.connect(self.onclick2)

        button3=QPushButton('延时注入',self)
        button3.move(200,500)
        button3.resize(100,50)
        button3.clicked.connect(self.onclick3)

        button4=QPushButton('报错注入',self)
        button4.move(200,300)
        button4.resize(100,50)
        button4.clicked.connect(self.onclick4)

    def onclick1(self):
        self.newwindow=window1()
        self.newwindow.show()

    def onclick2(self):
        self.newwindow=window2()
        self.newwindow.show()

    def onclick3(self):
        self.newwindow = window3()
        self.newwindow.show()

    def onclick4(self):
        self.newwindow = window4()
        self.newwindow.show()

    def save(self):
        open("1.txt","w").write(self.text1.text())
        QMessageBox.information(self, '提示', '请开始选择注入方式！', QMessageBox.Ok)
        URL = open("1.txt", "r").read()
        self.text2.setPlainText('闭合方式：'+test_bihe.bihefangshi(URL))

class menu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.menuUI()
    def menuUI(self):
        self.setWindowTitle('SQL注入工具')
        self.resize(500,700)
        icon=QIcon()
        icon.addPixmap(QPixmap('1.jpg'))
        self.setWindowIcon(icon)
        self.setWindowOpacity(0.9)
        mainmenu=self.menuBar()
        about_memu=mainmenu.addMenu('关于')
        action=QAction('软件',self)
        action.triggered.connect(self.showmsg)
        about_memu.addAction(action)
    def showmsg(self):
        QMessageBox.information(self,'关于','该软件为sql注入工具',QMessageBox.Ok | QMessageBox.Cancel)

if __name__=="__main__":
    app=QApplication(sys.argv)
    a=menu()
    a.setCentralWidget(mainwindow())
    a.show()
    sys.exit(app.exec_())

