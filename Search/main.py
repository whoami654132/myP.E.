from flask import Flask, render_template, request, redirect, url_for
from flask import Flask, render_template, request, redirect, url_for, flash, get_flashed_messages
from gevent import pywsgi
import pandas as pd

app = Flask(__name__)
app.secret_key = 'your-secret-key'
users = {}


def readfile():
    excel_file = './shuju.xlsx'  # 导入文件

    data = pd.read_excel(excel_file, engine='openpyxl')  # 读入数据

    Name = data['姓名'].tolist()
    Password = data['密码'].tolist()
    High = data['身高'].tolist()
    Zhong = data['体重'].tolist()
    M50 = data['50M'].tolist()
    Jump = data['跳绳'].tolist()

    for i in range(len(Name)):
        users[Name[i]] = []
        users[Name[i]].append(Password[i])
        users[Name[i]].append(High[i])
        users[Name[i]].append(Zhong[i])
        users[Name[i]].append(M50[i])
        users[Name[i]].append(Jump[i])


readfile()
print(users)


readfile()


@app.route('/')
def login():
    error = None
    for category, message in get_flashed_messages(with_categories=True):
        if category == 'error':
            error = message
    return render_template('login.html', error=error)


@app.route('/verify', methods=['POST'])
def verify():
    username = request.form['username']
    password = request.form['password']

    if username in users and str(users[username][0]) == password:
        # 核对成功，将value列表中的第1项放入session或者直接渲染到页面
        # 这里我们使用session来存储用户信息（可选）
        # session['user_info'] = users[username][1]
        global High1,Zhong1,M501,Jump1
        
        High1 = str(users[username][1])
        Zhong1 = str(users[username][2])
        M501 = str(users[username][3])
        Jump1 = str(users[username][4])
        return redirect(url_for('success', info='查询成功'))
    else:
        # 核对失败
        flash('密码或者用户名出错', 'error')
        return redirect(url_for('login'))  # 重定向回登录页面


@app.route('/success/<info>')
def success(info):
    # 这里的<info>是从verify函数中传递过来的
    return render_template('success.html', info=info,jok=High1,Z=Zhong1,M5=M501,T=Jump1)


if __name__ == '__main__':
    server = pywsgi.WSGIServer(('127.0.0.1',5000),app)
    server.serve_forever()
