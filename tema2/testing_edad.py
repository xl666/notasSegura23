
import datetime

# calcularEdad(fecha_actual, fecha_nacimiento)

def test_edad_bisiesto():
    fecha_actual = datetime.datetime(2012, 2, 28)
    fecha_nacimiento = datetime.datetime(2000, 2, 29)
    resultado = calcularEdad(fecha_actual, fecha_nacimiento)
    assert resultado == 11
    

test_edad_bisiesto()
