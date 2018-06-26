# -*- coding: utf-8 -*-

from flask import Flask,render_template,request
import sqlite3
import json

app=Flask(__name__)

#连接临时数据库
data_base = sqlite3.connect('temp.db', check_same_thread=False)
c = data_base.cursor()

#设置前端模板
@app.route('/')
def index():
    return render_template("index.html")


#设置数据来源
@app.route('/data')
def data():
    global tmp_time,c
    sql='select * from scores'
    c.execute(sql)
    arr=[]
    for i in c.fetchall():
        arr.append([i[0]*1000,i[1]])
    return json.dumps(arr)

#启动服务器并设定端口
def start():
    app.run(host='0.0.0.0',port=9090)



