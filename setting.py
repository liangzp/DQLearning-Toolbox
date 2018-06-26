# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
import setting_resource

class SETTING(QtWidgets.QWidget):
    def __init__(self):

        #父类初始化
        super().__init__()

        #主窗口初始化
        self.setObjectName("Dialog")
        self.resize(547, 402)
        self.setStyleSheet("")

        #初始化确定按钮
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(160, 320, 75, 23))
        self.pushButton.setStyleSheet("color: rgb(255, 255, 255);\n""border-image: url(:/image/resource/设定确定按钮.png);")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")

        #初始化取消按钮
        self.pushButton_2 = QtWidgets.QPushButton(self)
        self.pushButton_2.setGeometry(QtCore.QRect(320, 320, 75, 23))
        self.pushButton_2.setStyleSheet("color: rgb(255, 255, 255);\n""border-image: url(:/image/resource/设定取消按钮.png);")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")

        #初始化各个编辑框
        self.line_explore = QtWidgets.QLineEdit(self)
        self.line_explore.setGeometry(QtCore.QRect(450, 60, 61, 20))
        self.line_explore.setStyleSheet("color: rgb(0, 0, 0);")
        self.line_explore.setObjectName("line_explore")
        self.line_initial = QtWidgets.QLineEdit(self)
        self.line_initial.setGeometry(QtCore.QRect(450, 100, 61, 20))
        self.line_initial.setStyleSheet("color: rgb(0, 0, 0);")
        self.line_initial.setObjectName("line_Initial")
        self.line_final = QtWidgets.QLineEdit(self)
        self.line_final.setGeometry(QtCore.QRect(450, 140, 61, 20))
        self.line_final.setStyleSheet("color: rgb(0, 0, 0);")
        self.line_final.setObjectName("line_final")
        self.line_gamma = QtWidgets.QLineEdit(self)
        self.line_gamma.setGeometry(QtCore.QRect(450, 180, 61, 20))
        self.line_gamma.setStyleSheet("color: rgb(0, 0, 0);")
        self.line_gamma.setObjectName("line_gamma")
        self.line_replay = QtWidgets.QLineEdit(self)
        self.line_replay.setGeometry(QtCore.QRect(450, 220, 61, 20))
        self.line_replay.setStyleSheet("color: rgb(0, 0, 0);")
        self.line_replay.setObjectName("line_replay")
        self.line_batch = QtWidgets.QLineEdit(self)
        self.line_batch.setGeometry(QtCore.QRect(450, 260, 61, 20))
        self.line_batch.setStyleSheet("color: rgb(0, 0, 0);")
        self.line_batch.setObjectName("line_batch")
        self.exploreSlider = QtWidgets.QSlider(self)
        self.exploreSlider.setGeometry(QtCore.QRect(120, 60, 300, 19))
        self.exploreSlider.setStyleSheet("QSlider::handle:horizontal {     \n""    image: url(:/image/resource/Handle.png);\n""}\n""QSlider::groove:horizontal {        \n""    image: url(:/image/resource/Base.png);\n""}\n""")
        self.exploreSlider.setMinimum(200000)
        self.exploreSlider.setMaximum(10000000)
        self.exploreSlider.setProperty("value", 200000)
        self.exploreSlider.setOrientation(QtCore.Qt.Horizontal)
        self.exploreSlider.setObjectName("exploreSlider")
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(50, 60, 48, 19))
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(50, 100, 48, 19))
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.initialSlider = QtWidgets.QSlider(self)
        self.initialSlider.setGeometry(QtCore.QRect(120, 100, 300, 19))
        self.initialSlider.setStyleSheet("QSlider::handle:horizontal {     \n""    image: url(:/image/resource/Handle.png);\n""}\n""QSlider::groove:horizontal {        \n""    image: url(:/image/resource/Base.png);\n""}\n""")
        self.initialSlider.setMaximum(1000)
        self.initialSlider.setProperty("value", 0)
        self.initialSlider.setOrientation(QtCore.Qt.Horizontal)
        self.initialSlider.setObjectName("initialSlider")
        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(50, 140, 42, 19))
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.finalSlider = QtWidgets.QSlider(self)
        self.finalSlider.setGeometry(QtCore.QRect(120, 140, 300, 19))
        self.finalSlider.setStyleSheet("QSlider::handle:horizontal {     \n""    image: url(:/image/resource/Handle.png);\n""}\n""QSlider::groove:horizontal {        \n""    image: url(:/image/resource/Base.png);\n""}\n""")
        self.finalSlider.setMaximum(1000)
        self.finalSlider.setProperty("value", 0)
        self.finalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.finalSlider.setObjectName("finalSlider")
        self.label_4 = QtWidgets.QLabel(self)
        self.label_4.setGeometry(QtCore.QRect(50, 180, 42, 19))
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.gammaSlider = QtWidgets.QSlider(self)
        self.gammaSlider.setGeometry(QtCore.QRect(120, 180, 300, 19))
        self.gammaSlider.setStyleSheet("QSlider::handle:horizontal {     \n""    image: url(:/image/resource/Handle.png);\n""}\n""QSlider::groove:horizontal {        \n""    image: url(:/image/resource/Base.png);\n""}\n""")
        self.gammaSlider.setMaximum(100)
        self.gammaSlider.setProperty("value", 99)
        self.gammaSlider.setOrientation(QtCore.Qt.Horizontal)
        self.gammaSlider.setObjectName("gammaSlider")
        self.label_6 = QtWidgets.QLabel(self)
        self.label_6.setGeometry(QtCore.QRect(50, 220, 42, 19))
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_6.setObjectName("label_6")
        self.replaySlider = QtWidgets.QSlider(self)
        self.replaySlider.setGeometry(QtCore.QRect(120, 220, 300, 19))
        self.replaySlider.setStyleSheet("QSlider::handle:horizontal {     \n""    image: url(:/image/resource/Handle.png);\n""}\n""QSlider::groove:horizontal {        \n""    image: url(:/image/resource/Base.png);\n""}\n""")
        self.replaySlider.setMaximum(100000)
        self.replaySlider.setProperty("value", 50000)
        self.replaySlider.setOrientation(QtCore.Qt.Horizontal)
        self.replaySlider.setObjectName("replaySlider")
        self.label_7 = QtWidgets.QLabel(self)
        self.label_7.setGeometry(QtCore.QRect(50, 260, 36, 19))
        self.label_7.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_7.setObjectName("label_7")
        self.batchSlider = QtWidgets.QSlider(self)
        self.batchSlider.setGeometry(QtCore.QRect(120, 260, 300, 19))
        self.batchSlider.setStyleSheet("QSlider::handle:horizontal {     \n""    image: url(:/image/resource/Handle.png);\n""}\n""QSlider::groove:horizontal {        \n""    image: url(:/image/resource/Base.png);\n""}\n""")
        self.batchSlider.setMaximum(100)
        self.batchSlider.setProperty("value", 32)
        self.batchSlider.setOrientation(QtCore.Qt.Horizontal)
        self.batchSlider.setObjectName("batchSlider")
        self.label_5 = QtWidgets.QLabel(self)
        self.label_5.setGeometry(QtCore.QRect(0, 0, 551, 411))
        self.label_5.setStyleSheet("background-image: url(:/background/resource/设定背景.png);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")

        #组件挂起待用
        self.label_5.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.line_explore.raise_()
        self.line_initial.raise_()
        self.line_final.raise_()
        self.line_gamma.raise_()
        self.line_replay.raise_()
        self.line_batch.raise_()
        self.exploreSlider.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.initialSlider.raise_()
        self.label_3.raise_()
        self.finalSlider.raise_()
        self.label_4.raise_()
        self.gammaSlider.raise_()
        self.label_6.raise_()
        self.replaySlider.raise_()
        self.label_7.raise_()
        self.batchSlider.raise_()

        #重设界面
        self.retranslateUi(self)

        #编辑框和滑条互联
        self.connect()

        #按钮消息槽激活
        self.pushButton.clicked.connect(self.saveSetting)
        self.pushButton_2.clicked.connect(self.cancel)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "设置"))

        #初始化各编辑框
        self.line_explore.setText(_translate("Dialog", "200000"))
        self.line_initial.setText(_translate("Dialog", "0"))
        self.line_final.setText(_translate("Dialog", "0"))
        self.line_gamma.setText(_translate("Dialog", "0.99"))
        self.line_replay.setText(_translate("Dialog", "50000"))
        self.line_batch.setText(_translate("Dialog", "32"))
        self.label.setText(_translate("Dialog", "Explore:"))
        self.label_2.setText(_translate("Dialog", "Initial:"))
        self.label_3.setText(_translate("Dialog", "Final:"))
        self.label_4.setText(_translate("Dialog", "Gamma:"))
        self.label_6.setText(_translate("Dialog", "Replay:"))
        self.label_7.setText(_translate("Dialog", "Batch:"))

        #初始化设定
        self.setting={"Explore":200000,"Initial":0,"Final":0,"Gamma":0.99,"Replay":50000,"Batch":32}

    #编辑框和滑动条互联
    def connect(self):

        self.exploreSlider.valueChanged.connect(self.changeLineExplore)
        self.line_explore.textChanged.connect(self.changeSliderExplore)

        self.initialSlider.valueChanged.connect(self.changeLineInitial)
        self.line_initial.textChanged.connect(self.changeSliderInitial)

        self.finalSlider.valueChanged.connect(self.changeLineFinal)
        self.line_final.textChanged.connect(self.changeSliderFinal)

        self.gammaSlider.valueChanged.connect(self.changeLineGamma)
        self.line_gamma.textChanged.connect(self.changeSliderGamma)

        self.replaySlider.valueChanged.connect(self.changeLineReplay)
        self.line_replay.textChanged.connect(self.changeSliderReplay)

        self.batchSlider.valueChanged.connect(self.changeLineBatch)
        self.line_batch.textChanged.connect(self.changeSliderBatch)

    def changeLineExplore(self):
        try:
            self.line_explore.setText(str(self.exploreSlider.value()))
        except:
            pass

    def changeSliderExplore(self):
        try:
            self.exploreSlider.setValue(int(self.line_explore.text()))
        except:
            pass

    def changeLineInitial(self):
        try:
            self.line_initial.setText(str(self.initialSlider.value()/1000))
        except:
            pass

    def changeSliderInitial(self):
        try:
            self.initialSlider.setValue(int(float(self.line_initial.text())*1000))
        except:
            pass

    def changeLineFinal(self):
        try:
            self.line_final.setText(str(self.finalSlider.value()/1000))
        except:
            pass

    def changeSliderFinal(self):
        try:
            self.finalSlider.setValue(int(float(self.line_final.text()*1000)))
        except:
            pass

    def changeLineGamma(self):
        try:
            self.line_gamma.setText(str(self.gammaSlider.value()/100))
        except:
            pass

    def changeSliderGamma(self):
        try:
            self.gammaSlider.setValue(int(100*float(self.line_gamma.text())))
        except:
            pass

    def changeLineReplay(self):
        try:
            self.line_replay.setText(str(self.replaySlider.value()))
        except:
            pass

    def changeSliderReplay(self):
        try:
            self.replaySlider.setValue(int(self.line_replay.text()))
        except:
            pass

    def changeLineBatch(self):
        try:
            self.line_batch.setText(str(self.batchSlider.value()))
        except:
            pass

    def changeSliderBatch(self):
        try:
            self.batchSlider.setValue(int(self.line_batch.text()))
        except:
            pass

    #外部获取AI设置
    def getSetting(self):
        return self.setting

    #保存设定
    def saveSetting(self):
        self.setting={"Explore":self.line_explore.text(),"Initial":self.line_initial.text(),"Final":self.line_final.text(),"Gamma":self.line_gamma.text(),"Replay":self.line_replay.text(),"Batch":self.line_batch.text()}#还要做一个数字判断
        self.hide()

    #取消设定
    def cancel(self):
        self.hide()
        return 0

    #通过导入文档更新设定
    def updateSetting(self,setting):
        self.setting={"Explore":setting["Explore"],"Initial":setting["Initial"],"Final":setting["Final"],"Gamma":setting["Gamma"],"Replay":setting["Replay"],"Batch":setting["Batch"]}#还要做一个数字判断
        self.line_explore.setText(str(setting["Explore"]))
        self.line_final.setText(str(setting["Final"]))
        self.line_Initial.setText(str(setting["Initial"]))
        self.line_gamma.setText(str(setting["Gamma"]))
        self.line_replay.setText(str(setting["Replay"]))
        self.line_batch.setText(str(setting["Batch"]))




