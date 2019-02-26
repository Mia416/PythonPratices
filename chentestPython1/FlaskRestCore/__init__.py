from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)
todos = {}

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

class FlaskRestTest(Resource):
    #def get(self):
        # return {'hello': 'test get !'}
    def get(self, todo_id):
         return {todo_id: todos[todo_id]}
    
    
api.add_resource(HelloWorld, '/')
api.add_resource(FlaskRestTest, '/todos/')

if __name__ == '__main__':
    app.run(debug=True)