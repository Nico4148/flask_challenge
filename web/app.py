from flask import Flask, request, jsonify
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

@app.route("/online_status")
def online_status():
    return "<p> Online </p>"

@app.route("/api_docs")
def show_api_docs():
    api_docs_dict = {
            'endpoints': {
                '/online_status': 'returns online if working properly',
                '/create_tables': 'calls the sqlite3 create tables script',
                '/student_data': {
                        'GET': {
                            '0.Use':'to consult an specific Student by id',
                            '1.Example JSON': { "id": 95562304 }    
                            },
                        'POST': {
                            '0.Use':'to define a new Student with all the required data',
                            '1.Example JSON': {    
                                                "Code":95562304,
                                                "Name":"Nico",
                                                "LastName": "Bernal",
                                                "Email": "nicobernal187@gail.com",
                                                "Address": "Bernardo Houssay 1042",
                                                "Phone": 1154711031,
                                                "DateOfBirth": "1989-12-18" 
                                           }    
                            }
                    }
                }
            }
    return jsonify(api_docs_dict)


class CreateTables(Resource):

    def get(self):
        str_message = 'tables created'
        from table_scripts import create_tables_sql
        create_tables_sql('challenge.db')
        #---Agregar validacion---
        answer_dict = {
                'message': str_message
                }
        return jsonify(answer_dict)


class Student(Resource):
    
    def get(self):
        incoming_data = request.get_json()
        student_id = incoming_data["id"]
        from tools import get_student_by_id
        student_data = get_student_by_id('challenge.db', student_id)
        return_data = {
                'id': student_id,
                'student_data': student_data
                }
        return jsonify(return_data)
    
    def post(self):
        student_data = request.get_json()
        student_str_data = ''
        attr_str_list = [
                'Code', 
                'Name', 
                'LastName', 
                'Email', 
                'Address', 
                'Phone',
                'DateOfBirth']
        for attr_val in attr_str_list:
            attr = student_data.get(attr_val, False)
            if attr:
                student_str_data += str(attr) + '_'
            else:
                return jsonify({'message':'error'})
        student_str_data = student_str_data[:-1]
        #return jsonify({'message':'full object',
        #                'debug': student_str_data})        

        from tools import create_student
        res_dict = create_student('challenge.db',student_str_data) 
        if res_dict['error']:
            return jsonify({'message': res_dict['error']})

        #str_msg = 'failed'
        return_data = {
                'message': 'commit!!!'
                    #'message': str_msg
                }
        return jsonify(return_data)


api.add_resource(CreateTables, "/create_tables")
api.add_resource(Student, "/student_data")

if __name__=="__main__":
    app.run(host='0.0.0.0')
    

