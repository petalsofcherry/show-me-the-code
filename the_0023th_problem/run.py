# -*- coding:utf-8 -*-

'''
之前没写过后端的程序，第一次写成这样我已经很开心了（虽然知道很菜
'''
from flask import Flask, redirect, url_for, render_template, request
from flask.ext.wtf import Form
from wtforms import StringField, TextField, SubmitField
from wtforms.validators import  DataRequired

app = Flask(__name__)
app.secret_key = 'you-will-never-guess'


class pulishform(Form):
    name = StringField('name', validators = [DataRequired()])
    comment = TextField('comment', validators = [DataRequired()])
    submit = SubmitField("submit")

@app.route('/', methods = ['GET', 'POST'])
def pulish(comment_list = []):
    form = pulishform()
    if request.method == 'POST' and form.validate_on_submit():
        comment_list.append(form.name.data + '：' + form.comment.data)
        return redirect(url_for('pulish'))
    return render_template('content.html', form=form, comment_list=comment_list)

if __name__ == '__main__':
    app.run(debug=True)