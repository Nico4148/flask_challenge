import sqlite3

def get_student_by_id(str_database_filename, student_id):
    conn = sqlite3.connect(str_database_filename)
    curs = conn.cursor()
    curs.execute("""SELECT Code, Name, Email, Address, Phone, DateOfBirth FROM Student AS S WHERE S.Code = %s""" % student_id)
    data = curs.fetchall()
    #print(data)
    #print(type(data))
    conn.close()
    return data


def create_student(str_database_filename, student_data):
    student_data_list = student_data.split('_')
    data = 'pass'
    if len(student_data_list) != 7:
        return { 'error': 'error data lenght'}
    else:
        def check_string(str_attr):
            for char in str_attr:
                if char.isdigit():
                    return False
            return True

        def check_date(str_date):
            return True

        def check_student_database(student_code):
            conn=sqlite3.connect(str_database_filename)
            curs=conn.cursor()
            str_query = '''
                SELECT *
                FROM Student AS s
                WHERE s.Code = '%s' ;
            ''' % student_code
            result = curs.execute(str_query)
            data = ''
            for i in result:
                data += str(i)
            conn.close()
            return data
        def commit_new_student(data):
            buffer_cmd = ''' INSERT INTO Student VALUES(%s,'%s %s','%s','%s',%s,'%s'); ''' %(data[0],data[1],data[2],data[3],data[4], data[5], data[6])
            conn=sqlite3.connect(str_database_filename)
            curs=conn.cursor()
            curs.execute(buffer_cmd)
            conn.commit()
            conn.close()
            return
        Code = student_data_list[0]
        if not Code.isnumeric() or len(Code) != 8:
            return { 'error': 'error student code'}

        Name = student_data_list[1]

        if not check_string(Name):
            return { 'error':  'error student name'}

        LastName = student_data_list[2]
        if not check_string(LastName):
            return { 'error':  'error student last name'}

        Email = student_data_list[3]
        if '@' not in Email:
            return { 'error':  'error student email'}

        Address = student_data_list[4]

        Phone = student_data_list[5]
        if not Phone.isnumeric() or len(Phone) != 10:
            return { 'error':  'error student phone'}

        DateOfBirth = student_data_list[6]
        if not check_date(DateOfBirth):
            return { 'error':  'error student date of birth'}

        data = check_student_database(Code)
        if data:
            return { 'error':  'error student %s allready exists' %Code}

        data = []
        data.append(Code)
        data.append(Name)
        data.append(LastName)
        data.append(Email)
        data.append(Address)
        data.append(Phone)
        data.append(DateOfBirth)
        commit_new_student(student_data_list)
        return { 'error': None, 'success_msg': 'new student saved'}



