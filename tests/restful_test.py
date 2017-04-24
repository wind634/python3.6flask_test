import random

from flask import Flask, request
from flask_restful import Resource, Api
from flask_restful import reqparse,fields, marshal_with

app = Flask(__name__)
api = Api(app)

todos = {}


class TodoSimple(Resource):
    def get(self, todo_id):
        parser = reqparse.RequestParser()
        parser.add_argument('rate', type=int, required=True, help='need')
        args = parser.parse_args()
        # return {todo_id: todos[todo_id]}
        return {"abc": "124"}, 200, {'Etagsss': 'some-opaque-string'}

    def put(self, todo_id):
        todos[todo_id] = request.form['data']
        return {todo_id: todos[todo_id]}

api.add_resource(TodoSimple, '/<string:todo_id>', endpoint="abc")

# resource_fields = {
#     'task':   fields.String,
#     "todo_id": fields.String,
#     'uri':    fields.Url('abc')
# }

class RandomNumber(fields.Raw):
    def output(self, key, obj):
        return random.random()
    
resource_fields = {
    # 'name': fields.String,
    'name': fields.String(attribute='todo_id'),
    'address': fields.String,
    'date_updated': fields.DateTime(dt_format='rfc822'),
    'random': RandomNumber,
}


class TodoDao(object):
    def __init__(self, todo_id, task):
        self.todo_id = todo_id
        self.task = task

        # This field will not be sent in the response
        self.status = 'active'


class Todo(Resource):
    @marshal_with(resource_fields)
    def get(self, **kwargs):
        return TodoDao(todo_id='my_todo', task='Remember the milk')

api.add_resource(Todo, '/')
    
if __name__ == '__main__':
    app.run(debug=True)