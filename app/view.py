from app import app, md
from flask import render_template, request


@app.route('/')
def index():
    form = md.TodoForm(request.form)
    todos = md.Todo.objects.all()
    return render_template("index.html", todos=todos, form=form)


@app.route('/add', methods=['POST', ])
def add():
    form = md.TodoForm(request.form)
    if form.validate():
        content = form.content.data
        todo = md.Todo(content=content)
        todo.save()
    todos = md.Todo.objects.all()
    return render_template("index.html", todos=todos, form=form)


@app.route('/done/<string:todo_id>')
def done(todo_id):
    form = md.TodoForm(request.form)
    todo = md.Todo.objects.get_or_404(id=todo_id)
    todo.status = 1
    todo.save()
    todos = md.Todo.objects.all()
    return render_template("index.html", todos=todos, form=form)


@app.route('/undone/<string:todo_id>')
def undone(todo_id):
    form = md.TodoForm(request.form)
    todo = md.Todo.objects.get_or_404(id=todo_id)
    todo.status = 0
    todo.save()
    todos = md.Todo.objects.all()
    return render_template("index.html", todos=todos, form=form)


@app.route('/delete/<string:todo_id>')
def delete(todo_id):
    form = md.TodoForm(request.form)
    todo = md.Todo.objects.get_or_404(id=todo_id)
    todo.delete()
    todos = md.Todo.objects.all()
    return render_template("index.html", todos=todos, form=form)
