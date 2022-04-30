# flask_challenge

# challenge
#Para implementar sobre el directorio base 
#sudo docker compose build
#sudo docker compose up
#endpoints de prueba /online_status y /api_docs

0) Listado de archivos:  

directorio base (Docker necesario):
docker-compose.yml

directorio web (Aplicacion):
app.py
challenge.db
table_scripts.py
tools.py

directorio web (Docker necesario):
Dockerfile
requirements.txt

1) Estructura de la base de datos realizada en SQLite3:  
  
[Tabla]:  
Atributo0 Atributo1 Atributo2 ...  
#TipoAtributo0 TipoAtributo1 TipoAtributo2 ...  
#Descripción  
  
  
[Student]:  
Code Name Email Address Phone DateOfBirth  
numérico texto texto texto numérico fecha  
#Tabla estudiante: Posee códgio único y corresponde al documento de identidad.  
  
[StudentState]:  
StudentCode State StateDate  
numérico numérico fecha  
#Tabla Estado de Estudiante: Para generar un historial del estado del estudiante (inscripto, abandono, graduado...)  
  
[Course]:  
Code Name  
numérico texto  
#Taba curso: Código y nombre de cada curso.  
  
[Inscription]:  
StudentCode CourseCode InscriptionDate  
numérico numñerico fecha  
#Tabla Inscripción: Correponde a la materia inscripta por el estudiante.  
  
[DefinitiveGrade]:  
InscriptionCode Grade GradeDate  
numérico numérico fecha  
#Tabla nota definitiva: corresponde a la nota definitiva de la materia cursada.  
  
[InscriptionStatus]:  
InscripctionCode Status StatusDate  
numérico numérico fecha  
#Tabla estado de inscripción: Corresponde al estado de la marteria inscripta (inscripta, abandonada, completada).  
  
[Exam]:  
CourseCode Order Ponderation   
numérico numérico fecha  
#Tabla Exámen: Corresponde a cada examen de l materia y posee una poderación sobre la nota definitiva.  
  
[ExamGrade]:  
ExamCode Grade GradeDate  
numérico numérico fecha  
#Tabla calificación de exámen: corresponde a la calificación obtenida por el estudiante en un exámen específico.  
  
[Carreer]:  
Code Name  
numñerico texto  
#Tabla Carrera: corresponde a la carrera que está cursando el estudiante.  
  
[CarreerCourses]:  
CarreerCode CourseCode  
numérico numérico  
#Tabla cursos de carrera: corresponde a las materias que componen estudiar una carrera. Una materia puede ser común entre varias carreras.  
  
[CarreerInscription]:  
CarreerCode InscriptionDate  
numñerico fecha  
#Tabla inscripción en carrera: Correpsodne al historial de inscripción en una carrera del estudiante.  
  
[CarreerInscriptionStatus]:  
CarreerInscriptionCode Status StatusDate  
numérico numérico fecha  
#Tabla Estado de inscricpión de carrera: Corresponde al historial de la inscri`ción de un estudiante en una carrera (inscripto, en curso, abandono, completado).  
  
2) Comando de interfaz:
Ver JSON de ejemplos en endpoint /api_docs

endpoint /student_data metodo GET
enviar JSON { "id": 95562304 } para consultar por el Student de ID 95562304 el servidor contesta en formato JSON.

endpoint /student_data metodo POST
enviar JSON {    "Code":95562304,
"Name":"Nico",
"LastName": "Bernal",
"Email": "nicobernal187@gail.com",
"Address": "Bernardo Houssay 1042",
"Phone": 1154711031,
"DateOfBirth": "1989-12-18" 
}    
para definir un nuevo Student, el servidor contesta en formato JSON.

Ya existen las tablas, se dejo disponible de igual forma el endpoint para ejecutar el script que las genera, el script posee try except en caso se intente crear tablas que ya existen.
