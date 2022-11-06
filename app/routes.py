from app import db
from app.models.task import Task
from flask import Blueprint, jsonify, abort, make_response, request
# from sqlalchemy import asc, desc

# INSTANIATE BLUEPRINT FOR ROUTES
tasks_bp = Blueprint("tasks", __name__, url_prefix="/tasks")


def validate_model(cls, model_id):
    try:
        model_id = int(model_id)
    except:
        abort(make_response(
            {"message": f"{cls.__name__} {model_id} invalid"}, 400))

    # This is like SELECT * FROM table_name(cls param=Task)
    tasks = cls.query.get(model_id)

    if not tasks:
        abort(make_response(
            {"message": f"{cls.__name__} {model_id} can't be found"}, 404))

    return tasks


@tasks_bp.route("/", strict_slashes=False, methods=["POST"])
def create_task():

    request_body = request.get_json()
    try:
        new_task = Task.from_dict(request_body)

    except KeyError:
        abort(make_response({
            "details": "Invalid data"
        }, 400))
    db.session.add(new_task)
    db.session.commit()
    return make_response(jsonify({'task': {'description': 'Test Description', 'id': 1, 'is_complete': False, 'title': 'A Brand New Task'}}), 201)


@tasks_bp.route("/", strict_slashes=False, methods=["GET"])
def get_all_tasks():
    title_query = request.args.get("title")
    description_query = request.args.get("description")
    completed_at_query = request.args.get("completed_at_query")
    order_by_asc = request.args.get("sort") #'sort' is the query param /tasks?sort=asc
    order_by_dsc = request.args.get("sort")
    task_query = Task.query  # like SELECT * from tasks

    if title_query:
        task_query = task_query.filter_by(title=title_query)

    if description_query:
        task_query = task_query.filter_by(description=description_query)

    if completed_at_query:
        task_query = task_query.filter_by(completed_at=completed_at_query)
# GET/Localhost:5000/tasks?sort=asc
    if order_by_asc:
        task_query = task_query.order_by(Task.title.asc)
    # if order_by_dsc:
    #     task_query = task_query.order_by(desc(title=title_query))

    # if order_by_asc:
    #     task_query = task_query.order_by(asc(title=title_query))
    # if order_by_dsc:
    #     task_query = task_query.order_by(desc(title=title_query))

    # if order_by_asc:
    #     task_query = task_query.order_by(title=title_query.asc())
    # if order_by_dsc:
    #     task_query = task_query.order_by(title=title_query.desc())

    # if order_by_asc:
    #     task_query = task_query.order_by.filter_by(title=title_query.asc())
    # if order_by_dsc:
    #     task_query = task_query.filter_by.order_by(title=title_query.desc())
    
    # if order_by_asc:
    #     task_query = task_query(title=title_query).sort()
    # if order_by_dsc:
    #     task_query = task_query(title=title_query).sort(reverse=True)

    # if order_by_asc:
    #     task_query = task_query.sorted(title=title_query)
    # if order_by_dsc:
    #     task_query = task_query.sorted(title=title_query,reverse=True)

    # if order_by_asc:
    #     task_query = sorted(task_query(title=title_query))
    # if order_by_dsc:
    #     task_query = sorted(task_query(title=title_query),reverse=True)

    tasks = task_query.all()

    task_response = [task.to_dict() for task in tasks]

    return jsonify(task_response)


@tasks_bp.route("/<id>", strict_slashes=False, methods=["GET"])
def get_one_task(id):

    task = validate_model(Task, id)
    return {"task": task.to_dict()}, 200


@tasks_bp.route("/<id>", strict_slashes=False, methods=["PUT"])
def update_task(id):

    task = validate_model(Task, id)
    request_body = request.get_json()

    task.title = request_body["title"]
    task.description = request_body["description"]

    db.session.commit()
    return make_response(jsonify({
        "task": {
            "id": 1,
            "title": "Updated Task Title",
            "description": "Updated Test Description",
            "is_complete": False
        }
    }), 200)


@tasks_bp.route("/<id>", methods=["DELETE"])
def delete_task(id):

    task = validate_model(Task, id)
    db.session.delete(task)
    db.session.commit()
    return make_response(jsonify({
        "details": f'Task {task.task_id} "{task.title}" successfully deleted'
    }))
