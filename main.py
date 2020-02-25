# -*- coding: utf-8 -*-
from flask import Flask, request, render_template, make_response, send_from_directory, redirect, url_for, session, jsonify, Response
import subprocess
import os
import time
import uuid
import base64
import hashlib

from PIL import Image
from io import BytesIO


from flask_dropzone import Dropzone

from model import app, User, db, Msg

import datetime  # , random

from datetime import timedelta

app.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(seconds=5)
app.secret_key = 's82;asdf4idsdf'
app.config['SESSION_TYPE'] = 'filesystem'

dropzone = Dropzone(app)
# from flask_redis import FlaskRedis
# rd = FlaskRedis(app)
# REDIS_URL='redis://127.0.0.1:6379/trans'

app.config[
    'SQLALCHEMY_DATABASE_URI'] = "mysql://root:ricardo@localhost/Ricardo"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

path = './static/uploads/'


is_login_require = False


def login_require(func):
    """
    """
    def decorator(*args, **kwargs):
        if is_login_require:
            # 现在是模拟登录，获取用户名，项目开发中获取session
            username = session.get('username', None)
            # 判断用户名存在且用户名是什么的时候直接那个视图函数
            if(username and db.session.query(User).filter_by(UserName=username).first()):
                print('session --> ', username)
                return func(*args, **kwargs)
            else:
                username = request.cookies.get("username")
                if(username and db.session.query(User).filter_by(UserName=username).first()):
                    print('cookie --> ', username)
                    return func(*args, **kwargs)
                # 如果没有就重定向到登录页面
                return redirect("login")

        else:
            return func(*args, **kwargs)
    # decorator.__name__ = func.__name__
    return decorator


@app.route('/', endpoint='index')
@login_require
def index():
    try:
        user = get_user()
        print('index -> ', user)
        info = request.args.get('info')
        return render_template('index.html', username=user.UserName, info='【%s】欢迎回来！'%user.UserName)
    except:
        return render_template('index.html', username='游客')


@app.route('/login', methods=['get', 'post'])
def login():
    if(request.method == 'GET'):
        return render_template("login.html")
    else:
        username = request.form['username']
        pwd = request.form['pwd']
        user = db.session.query(User).filter_by(
            UserName=username, Passwd=pwd).first()
        print('login -> ', user)
        response = make_response(redirect('/?info=登陆成功'))
        if(user):
            session['username'] = user.UserName
            response.set_cookie('username', user.UserName,
                                max_age=10 * 60 * 60 * 24 * 365)
        return response


@app.route('/terminal/[<cmd>]', methods=['POST'])
def terminal(cmd):
    print(cmd)
    cmd = cmd.strip().split(' ')
    try:
        out_bytes = subprocess.check_output(list(cmd))
        out_put = out_bytes.decode('utf-8').replace('\n', '\n\t')
        print(out_put)
        return jsonify({
            'errcode': 0,
            'output': out_put
        })
    except subprocess.CalledProcessError as e:
        out_bytes = e.output       # Output generated before error
        code      = e.returncode   # Return code
        out_put = out_bytes.decode('utf-8')
        return jsonify({
            'errcode': code,
            'output': out_put
        })
    except Exception as e:
        print(e)
        return jsonify({
            'errcode': -1,
            'output': str(e)
        })


@app.route('/msg')
def msg():
    #with open('./msg', 'r', encoding='utf-8') as f:
    #    msg = f.read()
    msg = db.session.query(Msg).order_by(Msg.id.desc()).first()

    return render_template('msg.html', msg=msg)


@app.route('/setmsg', methods=['post'], endpoint='setmsg')
@login_require
def setmsg():
    text = request.form['text']
    #with open('./msg', 'w', encoding='utf-8') as f:
    #    f.write(text)
    msg = Msg(get_user().UserName, text)
    db.session.add(msg)
    db.session.commit()

    return 'ok'



def get_user():
    try:
        username = session.get('username')
        if not username:
            username = request.cookies.get('username')
        if not username:
            return redirect(url_for(login))
        user = db.session.query(User).filter_by(UserName=username).first()
        return user
    except:
        return User(UserName='游客', UserLevel = 1000)


@app.route('/del/<filename>', endpoint='delfile')
@login_require
def delfile(filename):
    user = get_user()
    if(not user.Level > 99):
        # return getfilelist(options="无权限")
        os.remove(path + filename)
    return redirect(url_for('getfilelist'))
    # return getfilelist(options="删除成功")


@app.route('/rename/<old>/<newname>')
def renamefile(old, newname):
    if os.path.exists(path + old):
        os.rename(path + old, path + newname)
        return 'ok'
    else:
        return 'error'


def image_to_base64(image_path, img_type):
    img = Image.open(image_path)
    img.thumbnail((800, 600))
    output_buffer = BytesIO()
    img.save(output_buffer, format=img_type)
    byte_data = output_buffer.getvalue()
    base64_str = base64.b64encode(byte_data)
    return base64_str


@app.route('/filelist', endpoint='getfilelist')
@login_require
def getfilelist(options=None):
    print(options)
    files = os.listdir(path)
    filedict = []
    if files:
        files.sort(key=lambda fn: os.path.getmtime(path + '/' + fn))
        files.reverse()
        for f in files:
            filetime = time.strftime(
                "%Y-%m-%d %H:%M:%S", time.localtime(os.path.getmtime(path + '/' + f)))
            thum, t = '', ''
            if(f.split('.')[-1] in ['jpg', 'jpeg']):
                thum = str(image_to_base64(path + f, 'JPEG')).split("'")[1]
                
                t = 'jpg'
            elif(f.split('.')[-1] in ['png']):
                thum = str(image_to_base64(path + f, 'PNG')).split("'")[1]
                t = 'png'
            filedict.append((f, filetime, thum, t))
    return render_template('file.html', file_list=filedict, msg=options)


@app.route('/file', methods=['POST'], endpoint='upload')
@login_require
def upload():
    user = get_user()
    print(user)
    if user.Level > 99:
        # redirect('getfilelist',
        return render_template('index.html', msg='无权限')
    f = request.files.get('file')  # 获取文件对象
    f.save(os.path.join(path, f.filename))  # 保存文件
    return 'ok'


@app.route('/download/<filename>', endpoint='download')
@login_require
def download(filename):
    file_path = path + '/' + filename
    user = get_user()
    print(user)
    if user.Level > 200:
        # redirect('getfilelist',
        return render_template('index.html', msg='无权限')

    def generate():
        if not os.path.exists(file_path):
            raise "File not found."
        with open(file_path, "rb") as f:
            while True:
                chunk = f.read(10 * 1024 * 1024)
                if not chunk:
                    break
                yield chunk
        # 流式传输解决大文件
        # 问题：同一时间只能下载一个文件
    res = Response(generate(), content_type="application/octet-stream")
    res.headers['content-length'] = os.stat(str(file_path)).st_size
    # res.headers['Content-Disposition'] = 'attachment; filename={}'.format(filename)
    return res
    # directory = os.path.join(path)  # 假设在当前目录
    # response = make_response(send_from_directory(directory, filename, as_attachment=True))
    # response.headers["Content-Disposition"] = "attachment; filename={}".format(filename.encode().decode('latin-1'))
    # return response


@app.route('/open/<filename>')
@login_require
def openfile(filename):
    types = ['java', 'css', 'js', 'txt', 'html', 'jsp', 'htm', 'sql', 'xml']
    filetype = filename.split('.')[-1]
    if(filetype in types):
        with open(path + filename, 'r') as f:
            content = f.read()
        return render_template('msg.html', msg=content)
    elif(filetype.lower() in ['png', 'jpg', 'jpeg']):
        #image = open("static/uploads/{}".format(filename), 'r')
        #resp = Response(image, mimetype="image/jpeg" if filetype == 'jpg' else 'image/png')
        #img = ''
        #with open("static/uploads/{}".format(filename), 'r') as f:
        #    img = f.read()
        #    img = base64.b64encode(img)
        return send_from_directory('static/uploads', request.path[1:].split('/')[-1])
    else:
        return redirect(url_for('getfilelist'))


@app.route('/robots.txt')
@app.route('/sitemap.xml')
def static_from_root():
    return send_from_directory('static', request.path[1:])

@app.route('/uuid', methods=['GET', 'POST'])
def get_uuid():
    uid = uuid.uuid1()
    m = hashlib.md5()
    m.update(str(uid).encode(encoding='utf-8'))
    md5_uuid = m.hexdigest()
    if request.method == 'GET':
        return render_template('msg.html', msg=md5_uuid)
    elif request.method == 'POST':
        return jsonify({
            'timestamp': time.time()[:11],
            'uuid': md5_uuid
        })

if __name__ == "__main__":
    app.run('0.0.0.0', 9999, debug=True, threaded=True)
    # app.run('0.0.0.0', 9999, debug=True, threaded=True, ssl_context=('./ssl.crt', './ssl.key'))
