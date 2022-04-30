def delete_students_content(str_database_file_name):
    import sqlite3

    def insert_data(single_cmd):
        conn = sqlite3.connect(str_database_file_name)
        curs = conn.cursor()
        curs.execute(single_cmd)
        conn.commit()
        conn.close()

    buffer_cmd = '''
        DELETE FROM Student Where True
        ; '''
    insert_data(buffer_cmd)
    print(buffer_cmd)


def insert_test_student():
    import sqlite3

    def insert_data(single_cmd):
        conn = sqlite3.connect(str_database_file_name)
        curs = conn.cursor()
        curs.execute(single_cmd)
        conn.commit()
        conn.close()

    '''
    [Student]
    Code Name Email Address Phone DateOfBirth
    '''
    buffer_cmd = '''
        INSERT INTO Student
        VALUES(
            95562304,
            'Nicolas Bernal',
            'nicobernal187@gmail.com',
            'Bernardo Houssay 1042',
            1154711031,
            '1989-12-18'
        ); '''
    insert_data(buffer_cmd)
    print(buffer_cmd)


def create_tables_sql(str_database_file_name):
    import sqlite3

    def create_tables(str_list):
        for i in str_list:
            try:
                conn = sqlite3.connect(str_database_file_name)
                curs = conn.cursor()
                curs.execute(i)
                conn.commit()
                conn.close()
            except:
                str_error = 'Error on executing: {}'.format(i)
                print(str_error)

    cmd_string_list = []
    '''
    [Student]
    Code Name Email Address Phone DateOfBirth
    '''
    buffer_cmd = '''
            CREATE TABLE Student
            (
                Code numeric, 
                Name text, 
                Email text, 
                Address text, 
                Phone numeric, 
                DateOfBirth datetime 
            ); '''
    cmd_string_list.append(buffer_cmd)

    '''
    [StudentState]
    StudentCode State StateDate
    '''
    buffer_cmd = '''
        CREATE TABLE StudentState
        (
            StudentCode numeric,
            State numeric,
            StateDate datetime 
        );'''
    cmd_string_list.append(buffer_cmd)

    '''
    [Course]
    Code Name
    '''
    buffer_cmd = '''
            CREATE TABLE Course
            (
            Code numeric,
            Name text 
            );'''
    cmd_string_list.append(buffer_cmd)

    '''
    [Inscription]
    StudentCode CourseCode InscriptionDate
    '''
    buffer_cmd = '''
            CREATE TABLE Inscription
            (
                StudentCode numeric,
                CourseCode numeric,
                InscriptionDate datetime 
            );'''
    cmd_string_list.append(buffer_cmd)

    '''
    [DefinitiveGrade]
    InscriptionCode Grade GradeDate
    '''
    buffer_cmd = '''
            CREATE TABLE DefinitiveGrade
            (
                InscriptionCode numeric,
                Grade numeric,
                GradeDate datetime 
            );'''
    cmd_string_list.append(buffer_cmd)

    '''
    [InscriptionStatus]
    InscripctionCode Status StatusDate
    '''
    buffer_cmd = '''
            CREATE TABLE InscriptionStatus
            (
                InscripctionCode numeric,
                Status numeric,
                StatusDate datetime 
            );'''
    cmd_string_list.append(buffer_cmd)

    '''
    [Exam]
    CourseCode Order Ponderation 
    '''
    buffer_cmd = '''
            CREATE TABLE Exam
            (
                CourseCode numeric,
                eOrder numeric,
                Ponderation numeric
            );'''
    cmd_string_list.append(buffer_cmd)

    '''
    [ExamGrade]
    ExamCode Grade GradeDate
    '''
    buffer_cmd = '''
            CREATE TABLE ExamGrade
            (
                ExamCode numeric,
                Grade numeric,
                GradeDate datetime
            );'''
    cmd_string_list.append(buffer_cmd)

    '''
    [Carreer]
    Code Name
    '''
    buffer_cmd = '''
            CREATE TABLE Carrer
            (
                Code numeric,
                Name text
            );'''
    cmd_string_list.append(buffer_cmd)

    '''
    [CarreerCourses]
    CarreerCode CourseCode
    '''
    buffer_cmd = '''
            CREATE TABLE CarreerCourses
            (
                CarreerCode numeric,
                CourseCode numeric
            );'''
    cmd_string_list.append(buffer_cmd)

    '''
    [CarreerInscription]
    CarreerCode InscriptionDate
    '''
    buffer_cmd = '''
            CREATE TABLE CarreerInscription
            (
                CarreerCode numeric,
                InscriptionDate datetime
            );'''
    cmd_string_list.append(buffer_cmd)

    '''
    [CarreerInscriptionStatus]
    CarreerInscriptionCode Status StatusDate
    '''
    buffer_cmd = '''
            CREATE TABLE CarreerInscriptionStatus
            (
                CarreerInscriptionCode numeric,
                Status numeric,
                StatusDate datetime
            );'''
    cmd_string_list.append(buffer_cmd)

    create_tables(cmd_string_list)
