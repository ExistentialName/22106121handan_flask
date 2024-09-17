from flask import Flask,render_template,request,redirect,url_for
import requests
from bs4 import BeautifulSoup
import re

app = Flask(__name__)

@app.route('/')
def hello_world():  # put application's code here
    return render_template('login.html')

@app.route('/data' ,methods=['GET','POST'])
def getData():
    #添加爬取数据的代码
    url="https://tophub.today/n/WnBe01o371"
    headers={
        'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36'
    }
    codes = requests.get(url,headers=headers).text
    bs = BeautifulSoup(codes,'html.parser')
    result = []
    for item in bs.select(selector= 'a.al'):
        result.append(item.text)
    return str(result)


@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        print(username,password)
        return redirect('/data')
    return render_template('login.html')


if __name__ == '__main__':
    app.run()
