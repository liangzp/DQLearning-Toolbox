# -*- coding: utf-8 -*-

import sys
from  mainwindow import MAINWINDOW
from PyQt5.QtWidgets import QApplication,QSplashScreen
from PyQt5 import QtCore,QtGui,QtWidgets


if __name__ == '__main__':
    app = QApplication(sys.argv)
    #初始化启动界面
    splash=QtWidgets.QSplashScreen(QtGui.QPixmap("启动界面.png"))
    #展示启动界面
    splash.show()
    #设置计时器
    timer = QtCore.QElapsedTimer()
    #计时器开始
    timer.start()
    #保证启动界面出现3s
    while timer.elapsed() < 3000:
        app.processEvents()
    #初始化主界面
    MainWindow = MAINWINDOW()
    #展示主界面
    MainWindow.show()
    #主界面完全加载后，启动界面消失
    splash.finish(MainWindow)
    sys.exit(app.exec_())

