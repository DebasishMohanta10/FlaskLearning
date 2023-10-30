from flask import Blueprint,render_template,redirect,url_for,request
from app.form.search import AddTaskForm
from app.form.searchform import SearchForm
from app.models import getAllTodos,addTaskData,removeTask,searchTask

bp = Blueprint(' ',__name__)

@bp.route("/",methods=['GET'])
def index():
    todos = getAllTodos()
    form = SearchForm()
    return render_template('index.html',todos=todos,form=form)

@bp.route("/add",methods=['GET','POST'])
def addTask():
    form = AddTaskForm()
    if form.validate_on_submit():
        name = request.form.get("name")
        desc = request.form.get("description")
        deadline = request.form.get("deadline") or None
        if addTaskData(name,desc,deadline):
            return redirect(url_for('.index'))
        else:
            return render_template('addTask.html',form=form)
    return render_template('addTask.html',form=form)

@bp.route("/remove/<int:id>",methods=['GET'])
def remove_task(id):
    # Logic
    removeTask(id)
    return redirect(url_for('.index'))

@bp.route("/search")
def search():
    q = request.args.get("q")
    # Logic
    form = SearchForm()
    todos=searchTask(q)
    return render_template('index.html',form=form,todos=todos,query=q)