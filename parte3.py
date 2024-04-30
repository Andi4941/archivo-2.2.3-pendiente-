#solicitar datos de entrada
rut= input("ingrese rut apoderado: ")
nomAlum= input("ingrese el nombre del alumno: ")
curso= input("ingrese curso al cual el alumno debe marticularse.")

#procesar la informacion 

matricula= 25000
mensualidad= 30000
resultadoAnual =(mensualidad * 10) + matricula 

#mostrar datos de salida 

print("----detalle anulidad colegio---")
print("NOMBRE ALUMNI: " , nomAlum)
print("RUT APODERADO", rut)
print("CURSO MARTICULADO:", curso)
print("VALOR MATRICULADO:", matricula)
print("VALOR MENSUALIDA:", mensualidad)
print("VALOR TOTAL A PAGAR:", resultadoAnual)