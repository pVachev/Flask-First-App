from flask import Flask, request
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)

api = Api(app)

students = []

class Student(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name',
                        required=True,
                        help="This field cannot be left blank!"
                        )

    def get(self, id):
        for student in students:
            if student['id'] == id:
                return student
            
        return {'student': None}, 404

    def post(self, id):
        if next(filter(lambda x: x['id'] == id, students), None) is not None:
            return {'message': "A student with id '{}' already exists.".format(id)}
        data_easy = request.get_json()
        data = Student.parser.parse_args()
     
        student = {'id': id, 'name': data['name']}
        students.append(student)
        return student, 201

    def delete(self, id):
        global students
        students = list(filter(lambda x: x['id'] != id, students))
        return {'message': 'Student deleted'}

    def put(self, id):
        data = Student.parser.parse_args()
        student = next(filter(lambda x: x['id'] == id, students), None)
        if student is None:
            student = {'id': id, 'name': data['name']}
            students.append(student)
        else:
            student.update(data)
        return student


class StudentList(Resource):
    def get(self):
        return {'students': students}


api.add_resource(Student, '/student/<int:id>')
api.add_resource(StudentList, '/students')

courses = []

class Course(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name',
                        required=True,
                        help="This field cannot be left blank!"
                        )

    def get(self, id):
        for course in courses:
            if course['id'] == id:
                return course
            
        return {'course': None}, 404

    def post(self, id):
        if next(filter(lambda x: x['id'] == id, courses), None) is not None:
            return {'message': "A course with id '{}' already exists.".format(id)}
        data_easy = request.get_json()
        data = Course.parser.parse_args()
     
        course = {'id': id, 'name': data['name']}
        courses.append(course)
        return course, 201

    def delete(self, id):
        global courses
        courses = list(filter(lambda x: x['id'] != id, courses))
        return {'message': 'Course deleted'}

    def put(self, id):
        data = Course.parser.parse_args()
        course = next(filter(lambda x: x['id'] == id, courses), None)
        if course is None:
            course = {'id': id, 'name': data['name']}
            courses.append(course)
        else:
            course.update(data)
        return course


class CoursesList(Resource):
    def get(self):
        return {'courses': courses}


api.add_resource(Course, '/course/<int:id>')
api.add_resource(CoursesList, '/courses')

events = []

class Event(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name',
                        required=True,
                        help="This field cannot be left blank!"
                        )

    def get(self, id):
        for event in events:
            if event['id'] == id:
                return event
            
        return {'event': None}, 404

    def post(self, id):
        if next(filter(lambda x: x['id'] == id, events), None) is not None:
            return {'message': "An event with id '{}' already exists.".format(id)}
        data_easy = request.get_json()
        data = Event.parser.parse_args()
     
        event = {'id': id, 'name': data['name']}
        events.append(event)
        return event, 201

    def delete(self, id):
        global events
        events = list(filter(lambda x: x['id'] != id, events))
        return {'message': 'Event deleted'}

    def put(self, id):
        data = Event.parser.parse_args()
        event = next(filter(lambda x: x['id'] == id, events), None)
        if event is None:
            event = {'id': id, 'name': data['name']}
            events.append(event)
        else:
            event.update(data)
        return event


class EventsList(Resource):
    def get(self):
        return {'events': events}


api.add_resource(Event, '/event/<int:id>')
api.add_resource(EventsList, '/events')
