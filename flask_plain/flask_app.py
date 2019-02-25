from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


my_students = []
@app.route('/student/<int:id>', methods=['GET', 'POST', 'DELETE'])
def student_method(id):
    if request.method == 'POST':
        if "Student " + str(id) not in my_students:
            my_students.append('Student ' + str(id))
            return jsonify(my_students)
        else:
            return "400 Bad Request: Student with id: " + str(id) + " already exists"
    elif request.method == 'DELETE':
        if "Student " + str(id) in my_students:
            my_students.remove(my_students[my_students.index("Student " + str(id))])
            return jsonify(my_students)
        else:
            return "400 Bad Request: Student with id: " + str(id) + " was not found"
    elif request.method == 'GET':
        if "Student " + str(id) in my_students:
            return jsonify(my_students[my_students.index("Student " + str(id))])
        else:
            return "400 Bad Request: Student with id: " + str(id) + " was not found"

@app.route('/student/<int:id>/<int:id_put>', methods=['PUT'])
def student_PUT_method(id, id_put):
    if "Student " + str(id) in my_students:
        if "Student " + str(id_put) not in my_students:
            my_students[my_students.index( "Student " + str(id))] = 'Student ' + str(id_put)
        else:
            return "400 Bad Request: Student with id: " + str(id_put) + " already exists"
        return jsonify(my_students)
    else:
        return "400 Bad Request: Student with id: " + str(id) + " was not found"

@app.route('/students', methods=['GET'])
def show_students():
    return jsonify(my_students)

my_courses = []
@app.route('/course/<id>', methods=['GET', 'POST', 'DELETE'])
def courses_method(id):
    if request.method == 'POST':
        if "Course " + id not in my_courses:
            my_courses.append('Course ' + id)
            return jsonify(my_courses)
        else:
            return "400 Bad Request: Course: " + id + " already exists"
    elif request.method == 'DELETE':
        if "Course " + id in my_courses:
            my_courses.remove(my_courses[my_courses.index("Course " + id)])
            return jsonify(my_courses)
        else:
            return "400 Bad Request: Course: " + id + " was not found"
    elif request.method == 'GET':
        if "Course " + id in my_courses:
            return jsonify(my_courses[my_courses.index("Course " + id)])
        else:
            return "400 Bad Request: Course: " + id + " was not found"

@app.route('/course/<id>/<id_put>', methods=['PUT'])
def course_PUT_method(id, id_put):
    if "Course " + id in my_courses:
        if "Course " + (id_put) not in my_courses:
           my_courses[my_courses.index( "Course " + id)] = 'Course ' + id_put
        else:
            return "400 Bad Request: Course with id: " + id_put + " already exists"
        return jsonify(my_courses)
    else:
        return "400 Bad Request: Course with id: " + id + " was not found"

@app.route('/courses', methods=['GET'])
def show_courses():
    return jsonify(my_courses)


my_events = []
@app.route('/event/<id>', methods=['GET', 'POST', 'DELETE'])
def events_method(id):
    if request.method == 'POST':
        if "Event " + id not in my_events:
            my_events.append('Event ' + id)
            return jsonify(my_events)
        else:
            return "400 Bad Request: Event: " + id + " already exists"
    elif request.method == 'DELETE':
        if "Event " + id in my_events:
            my_events.remove(my_events[my_events.index("Event " + id)])
            return jsonify(my_events)
        else:
            return "400 Bad Request: Event: " + id + " was not found"
    elif request.method == 'GET':
        if "Event " + id in my_events:
            return jsonify(my_events[my_events.index("Event " + id)])
        else:
            return "400 Bad Request: Event: " + id + " was not found"

@app.route('/event/<id>/<id_put>', methods=['PUT'])
def event_PUT_method(id, id_put):
    if "Event " + id in my_events:
        if "Event " + (id_put) not in my_events:
           my_events[my_events.index( "Event " + id)] = 'Event ' + id_put
        else:
            return "400 Bad Request: Event with id: " + id_put + " already exists"
        return jsonify(my_events)
    else:
        return "400 Bad Request: Event with id: " + id + " was not found"

@app.route('/events', methods=['GET'])
def show_events():
    return jsonify(my_events)

