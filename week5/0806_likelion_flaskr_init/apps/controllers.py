# -*- coding: utf-8 -*-
from flask import render_template, request, flash, url_for, redirect
from apps import app, db
from sqlalchemy import desc
from setKST import *

from apps.models import Article, Comment
#
#타임라인
#
@app.route('/', methods=['GET'])
def article_list():
	context = {}

	context['article_list'] = Article.query.order_by(desc(Article.date_created)).all()

	return render_template("home.html", context = context, active_tab='timeline')
#
#글수정
#

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def article_update(id):
	article = Article.query.get(id)
	if request.method == 'GET':
		return render_template('article/update.html', article = article )
	elif request.method == 'POST':

		article_data = request.form

		#article = Article.query.get(id)

		article.title = article_data['title']
		article.author = article_data['author']
		article.category = article_data['category']
		article.content = article_data['content']

		db.session.commit()

		flash(u'게시글이 수정되었습니다.', 'success')
		return redirect(url_for('article_detail', id=id))
#
#글쓰기
#
@app.route('/create', methods=['GET','POST'])
def article_create():
	if request.method =='GET':
		return render_template("article/create.html", active_tab = 'article_create') 
	elif request.method == 'POST':
		article_data = request.form

		article = Article(
			title = article_data['title'],
			author = article_data['author'],
			category = article_data['category'],
			content = article_data['content'],
			date_created = setKST(datetime.now(),9)
		)

		db.session.add(article)
		db.session.commit()

		flash(u'게시글이 작성되었습니다.', 'success')

		return redirect(url_for('article_list'))
#
#글 상세보기&댓글보기
#
@app.route('/detail/<int:id>', methods=['GET'])
def article_detail(id):
	article = Article.query.get(id)

	comments = article.comments.all()

	return render_template('article/detail.html', article=article, comments = comments)
#
#글 삭제
#

@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def article_delete(id):
	article = Article.query.get(id)

	if request.method == "GET":
		return render_template('article/delete.html')
	elif request.method =="POST":

		db.session.delete(article)
		db.session.commit()

		flash(u'게시글을 삭제하였습니다.', 'success')
		return redirect(url_for('article_list'))
#
#
#댓글쓰기
@app.route('/comment/create/<int:article_id>', methods=['GET', 'POST'])
def comment_create(article_id):
	if request.method =='GET':
		return render_template('comment/create.html')
	elif request.method =='POST':
		comment_data = request.form

		comment = Comment(
			content = comment_data['content'],
			author = comment_data['author'],
			password= comment_data['password'],
			email = comment_data['email'],
			article = Article.query.get(article_id),
			date_created = setKST(datetime.now(),9)
		)

		db.session.add(comment)
		db.session.commit()

		flash(u'댓글이 작성되었습니다.', 'success')

		return redirect(url_for('article_detail', id = article_id))
#
#댓글 좋아요
#
@app.route('/comment/like/<int:id>', methods=['GET', 'POST'])
def comment_like(id):
	comment = Comment.query.get(id)
	comment.like += 1

	db.session.commit()

	id = comment.article_id

	return redirect(url_for('article_detail', id=id))
#
#댓글 삭제
#
@app.route('/comment/delete/<int:id>', methods=['GET', 'POST'])
def comment_delete(id):
	comment = Comment.query.get(id)

	if request.method == "GET":
		return render_template('comment/delete.html')
	elif request.method =="POST":
		if request.form["password"] == comment.password:
			db.session.delete(comment)
			db.session.commit()

			flash(u'댓글을 삭제하였습니다.', 'success')
			return redirect(url_for('article_detail', id = comment.article_id))
		elif request.form["password"] != comment.password:
			flash(u'비밀번호가 틀렸습니다.', 'danger')
			return redirect(url_for('comment_delete', id=id))
#
# @error Handlers
#
# Handle 404 errors
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


# Handle 500 errors
@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500

