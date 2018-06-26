# -*- coding: utf-8 -*-

import game_setting
import resource
from PyQt5 import QtWidgets,QtCore,QtGui
from collections import deque
from threading import Thread
from multiprocessing import Process
import shelve
import os
import sqlite3
import socket
import pyperclip
from DQL import AI
import setting
import message_box
import flask_tk


game_start=False

class myThread(Thread):
    def __init__(self,game,model,replay_memory,timestep,setting):
        Thread.__init__(self)
        self.game=game
        self.model=model
        self.setting=setting
        self.replay_memory=replay_memory
        self.timestep=timestep

    def run(self):
        self.AI = AI(self.game,self.model,self.replay_memory,self.timestep,int(self.setting["Explore"]),float(self.setting["Initial"]),float(self.setting["Final"]),float(self.setting["Gamma"]),int(self.setting["Replay"]),int(self.setting["Batch"]),)
        self.AI.playGame()


    def stop(self):
        self.AI.closeGame()


class MAINWINDOW(QtWidgets.QWidget):
    def __init__(self, parent=None):

        #父类初始化
        super().__init__()

        #主窗体对象初始化
        self.setObjectName("Form")
        self.setEnabled(True)
        self.resize(681, 397)
        self.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        #进度条初始化
        self.progressBar = QtWidgets.QProgressBar(self)
        self.progressBar.setEnabled(True)
        self.progressBar.setGeometry(QtCore.QRect(140, 348, 291, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName("progressBar")

        #启动按钮初始化
        self.control = QtWidgets.QPushButton(self)
        self.control.setGeometry(QtCore.QRect(10, 325, 71, 71))
        self.control.setStyleSheet("border-image: url(:/bottom/resource/开始按钮.png);")
        self.control.setText("")
        self.control.setObjectName("control")
        self.control_state=False

        #下拉框初始化
        self.game_selection = QtWidgets.QComboBox(self)
        self.game_selection.setEnabled(True)
        self.game_selection.setGeometry(QtCore.QRect(530, 343, 141, 31))
        self.game_selection.setAutoFillBackground(False)
        self.game_selection.setStyleSheet("QComboBox{border-image: url(:/list/resource/下拉框.png)} \n""QComboBox::drop-down {image: url(:/bottom/resource/下拉框按钮.png)  }")
        self.game_selection.setEditable(False)
        self.game_selection.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.game_selection.setIconSize(QtCore.QSize(0, 0))
        self.game_selection.setFrame(False)
        self.game_selection.setObjectName("game_selection")

        #模式选择按钮加载
        self.mode = QtWidgets.QPushButton(self)
        self.mode.setGeometry(QtCore.QRect(440, 340, 71, 41))
        self.mode.setStyleSheet("border-image: url(:/bottom/resource/空白模式.png);\n""")
        self.mode.setText("")
        self.mode.setObjectName("mode")
        self.mode_state = False

        #背景图初始化
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(0, 0, 681, 331))
        self.label.setStyleSheet("border-image: url(:/image/resource/Background.png);")
        self.label.setText("")
        self.label.setObjectName("label")

        #设置按钮初始化
        self.setting = QtWidgets.QPushButton(self)
        self.setting.setGeometry(QtCore.QRect(570, 10, 31, 21))
        self.setting.setStyleSheet("border-image: url(:/bottom/resource/菜单.png);")
        self.setting.setText("")
        self.setting.setObjectName("setting")

        #获取ip地址按钮初始化
        self.pushButton_3 = QtWidgets.QPushButton(self)
        self.pushButton_3.setGeometry(QtCore.QRect(610, 10, 31, 23))
        self.pushButton_3.setStyleSheet("border-image: url(:/bottom/resource/最小化.png);")
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")

        #关闭按钮初始化
        self.bottom_close = QtWidgets.QPushButton(self)
        self.bottom_close.setGeometry(QtCore.QRect(650, 10, 21, 23))
        self.bottom_close.setStyleSheet("border-image: url(:/bottom/resource/关闭.png);")
        self.bottom_close.setText("")
        self.bottom_close.setObjectName("bottom_close")


        #重设界面
        self.retranslateUi(self)

        #按键消息槽设置
        self.connectBottom()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "深度强化学习工具箱"))

        #子窗口对象获取
        self.setting_form =  setting. SETTING()
        self.message_box=message_box.MESSAGE_BOX()

        #游戏列表加载
        game_setting_dict = game_setting.getSetting()
        for i,game in enumerate(game_setting_dict.keys()):
            self.game_selection.addItem("")
            self.game_selection.setItemText(i, _translate("Form", game))
        self.game_selection.setCurrentText(_translate("Form", list(game_setting_dict.keys())[0]))
        self.game_selection.setCurrentIndex(0)

        #启动服务器
        flask_process = Process(target=flask_tk.start)
        flask_process.daemon = True
        flask_process.start()


    def connectBottom(self):
        self.control.clicked.connect(self.loadGame)
        self.bottom_close.clicked.connect(self.closeWindow)
        self.mode.clicked.connect(self.setMode)
        self.setting.clicked.connect(self.openSetting)
        self.pushButton_3.clicked.connect(self.getIp)

    #界面可拖动设置
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.m_drag = True
            self.m_DragPosition = event.globalPos() - self.pos()
            event.accept()
            self.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))

    def mouseMoveEvent(self, QMouseEvent):
        if QtCore.Qt.LeftButton and self.m_drag:
            self.move(QMouseEvent.globalPos() - self.m_DragPosition)
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_drag = False
        self.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))


    #设置案件操作
    def openSetting(self):
        self.setting_form.show()

    #加载按键操作
    def loadGame(self):
        self.mode.setEnabled(False)
        self.setting.setEnabled(False)

        #开启游戏标志
        global game_start
        game_start=True

        #control_state为按键标志，false为还没开始游戏，true为已经开始游戏。按键外形随状态改变
        if self.control_state:
            self.closeWindow()
        else:
            #改变按键状态
            self.control.setStyleSheet("border-image: url(:/bottom/resource/终止按钮.png);")
            self.control_state =True

            #初始化AI需要的变量
            self.program_name = ""
            game=self.game_selection.currentText()
            model = ""
            replay_memory = deque()
            self.actual_timestep=0
            setting=self.setting_form.getSetting()

            #如果导入已有项目文件，那么更新上述变量
            if self.mode_state:
                program_path = QtWidgets.QFileDialog.getOpenFileName(self, "请选择你想要加载的项目",
                                                               "../",
                                                               "Model File (*.dat)")
                try:
                    #获取项目名字(无后缀，包含地址)
                    self.program_name=program_path[0][:-7]

                    #打开项目文件
                    with shelve.open(self.program_name+'.db') as f:
                        #加载项目信息
                        game=f["game"]
                        model = self.program_name
                        replay_memory = f["replay"]
                        setting=f["setting"]
                        self.actual_timestep = int(f["timestep"])
                        self.setting_form.updateSetting(setting)
                        self.update_dataset(f["result"])
                except:
                    pass

            #启动游戏线程
            self.game_thread = myThread(game,model,replay_memory,self.actual_timestep,setting)
            self.game_thread.start()

            #启动状态更新计时器
            self.state_Timer = QtCore.QTimer()
            self.state_Timer.timeout.connect(self.updateState)
            self.state_Timer.start(5000)

    def updateDataset(self,results):
        with shelve.open('temp.db',writeback=True) as f:
            c=f.cursor()
            for result in results:
                c.execute("insert into scores values (%s,%s)" % (result[0], result[1]))
            f.commit()


    def updateState(self):
        #尝试获取游戏状态，如果启动时间过慢仍未启动则跳过此次获取
        try:
            self.state = self.game_thread.AI.getState()
        except:
            pass
        else:
            actual_timestep=self.actual_timestep+self.state["TIMESTEP"]
            self.progressBar.setToolTip("Timestep:"+str(actual_timestep)+"    STATE:"+self.state["STATE"]+"     EPSILON:"+str(self.state["EPSILON"]))
            self.progressBar.setProperty("value",min(float(actual_timestep)/float(self.setting_form.getSetting()["Explore"])*100,100))

        #每隔5秒才向数据库读取一次，优化速度
        try:
            self.game_thread.AI.data_base.commit()
        except:
            pass

    #通过按键更改AI模式
    def setMode(self):
        if not self.mode_state:
            self.mode_state=True
            self.mode.setStyleSheet("border-image: url(:/bottom/resource/加载模式.png);\n""")
        else:
            self.mode_state = False
            self.mode.setStyleSheet("border-image: url(:/bottom/resource/空白模式.png);\n""")

    #获取本机ip地址
    def getIp(self):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.connect(('8.8.8.8', 80))
            ip = sock.getsockname()[0]
        finally:
            sock.close()
        pyperclip.copy(ip+':9090')


    def closeWindow(self):
        timestep=0
        #如果游戏根本没启动或者启动时间过短，那么按退出键则直接退出
        try:
            timestep=self.state["TIMESTEP"]
        except:
            pass

        if timestep>1000:
            #启动对话框
            reply = self.message_box.exec_()
            if reply:
                #新建模式
                if not self.program_name:
                    save_program_path = QtWidgets.QFileDialog.getSaveFileName(self, "请选择你保存项目的位置",
                                                                         "../",
                                                                         "Program File(*.db)")
                    #确保完成了完整保存操作后再进行操作
                    if save_program_path:
                        #获取保存的程序地址和名称（无后缀）
                        program_name = save_program_path[0].split(".")[0]
                        #打开程序地址
                        with shelve.open(save_program_path[0]) as f:
                            #AI运行的设定
                            f["setting"] = self.setting_form.getSetting()

                            #AI运行的状态
                            state = self.game_thread.AI.getState()

                            f["game"]=self.game_selection.currentText()
                            f["epsilon"] = state["EPSILON"]
                            f["result"] = [[i[0] * 1000, i[1]] for i in sqlite3.connect('temp.db', check_same_thread=False).cursor().execute( 'select * from scores').fetchall()]
                            f["replay"] = self.game_thread.AI.getReplay()
                            f["timestep"] = state["TIMESTEP"]


                        #保存模型
                        time=self.game_thread.AI.getState()["TIMESTEP"]
                        name = "network-dqn-" + str(int(time) // 1000 * 1000)
                        os.rename('./saved_networks/' + name + ".data-00000-of-00001",
                                  program_name + ".data-00000-of-00001")
                        os.rename('./saved_networks/' + name + ".index",program_name + ".index")
                        os.rename('./saved_networks/' + name + ".meta", program_name + ".meta")
                #加载模式
                else:
                    program_name=self.program_name

                    with shelve.open(program_name+'.db', writeback=True) as f:
                        # AI运行的状态
                        state = self.game_thread.AI.getState()
                        f["epsilon"] = state["EPSILON"]
                        new_result=[[i[0] * 1000, i[1]] for i in sqlite3.connect('temp.db',check_same_thread=False).cursor().execute('select * from scores').fetchall()]
                        f["result"].extend(new_result)
                        f["replay"] = self.game_thread.AI.getReplay()
                        f["timestep"] = int(state["TIMESTEP"]) + int(f["timestep"])#这次跑的时间加上项目中记录的时间


                    #保存模型
                    time=state["TIMESTEP"]
                    name = "network-dqn-" + str(time//1000 * 1000)
                    os.rename('./saved_networks/' + name + ".data-00000-of-00001",
                              program_name+".data-00000-of-00001")
                    os.rename('./saved_networks/' + name + ".index",  program_name+ ".index")
                    os.rename('./saved_networks/' + name + ".meta",  program_name+".meta")

        #关闭游戏窗口
        try:
            self.game_thread.AI.closeGame()
        except:
            pass

        #清空临时数据库
        with sqlite3.connect('temp.db', check_same_thread=False) as f:
            c = f.cursor()
            c.execute('delete from scores')
            f.commit()

        #关闭主界面窗口并终止计时器、服务器线程
        self.close()


