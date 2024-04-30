# Solicitar información
rut = input("Ingrese rut apoderado: ")
nomAlum = input("Ingrese el nombre del alumno: ")
curso = input("Ingrese curso al cual el alumno debe matricularse: ")

# Definir valores de matrícula, mensualidad y resultado anual
matricula = 25000
mensualidad = 30000
resultadoAnual = (mensualidad * 10) + matricula

# Imprimir detalles de la anualidad del colegio
print("-----Detalle Anualidad Colegio----")
print(f"VALOR MATRÍCULA: {matricula}")
print(f"VALOR MENSUALIDAD: {mensualidad}")
print(f"VALOR TOTAL A PAGAR: {resultadoAnual}")
print(f"NOMBRE ALUMNO: {nomAlum}")
print(f"RUT APODERADO: {rut}")
print(f"CURSO MATRICULADO: {curso}")