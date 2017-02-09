#!/usr/bin/env python3
#coding: utf-8

from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import  DataRequired
import pymysql
import json
import os

app = Flask(__name__)
app.secret_key = os.environ.get('secret_key')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@localhost/test1'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

class schedules(db.Model):
        __tablename__ = 'schedules'
        id = db.Column(db.Integer, primary_key=True)
        task = db.Column(db.Text)

db.create_all()

class create_form(Form):
        create = StringField('create', validators=[DataRequired()])
        submit = SubmitField("submit")

class search_form(Form):
        search = StringField('search', validators=[DataRequired()])
        submit = SubmitField("submit")

@app.route('/task/<int:task_id>/delete')
def task_delete(task_id):
        resp = {
                "status": 1,
                "message": "success"
        }
        #如果不行就返回错误信息
        if not resp:
                resp['status'] = 404
                resp["message"] = "Post Not Found"
                return json.dumps(resp)

        task = schedules.query.filter_by(id=task_id).first()
        db.session.delete(task)
        db.session.commit()
        return json.dumps(resp)

@app.route('/', methods = ['GET', 'POST'])
def task_create():
        form1 = search_form()
        form2 = create_form()

        #创建任务
        if request.method == 'POST' and form2.validate_on_submit():
                task = form2.create.data
                schedule = schedules(task=task)
                db.session.add(schedule)
                db.session.commit()

        #搜索任务
        if request.method == 'POST' and form1.validate_on_submit():
                task = form1.search.data
                return render_template("table.html", form1=form1, form2=form2,\
                                       schedules=schedules.query.filter_by(task=task).all())
        return render_template("table.html", form1=form1, form2=form2, schedules=schedules.query.all())


if __name__ == '__main__':
    app.run(debug=True)