import unittest

# def buscar_datos(*args, **kwargs):
#     for key, value in kwargs.items():
#         esta = True
#         for i, n in value.items():
#             if n not in args:
#                 esta = False
#         if esta:
#             return key
#     return "Los datos no se encuentran en la base de datos"


database = {
            "1":{
                "nombre1":"Pablo",
                "nombre2":"Diego",
                "apellido1":"Ruiz",
                "apellido2":"Picasso"
            },
            "2":{
                "nombre1":"Elio",
                "apellido1":"Anci"
            },
            "3":{
                "nombre1":"Elias",
                "nombre2":"Marcos",
                "nombre3":"Luciano",
                "apellido1":"Marcelo",
                "apellido2":"Gonzalez"
            }
}

def buscar_datos(*words, **kwords):
    for num, dic in kwords.items():
        if all(word in dic.values() for word in words):
            return num
    return None

class TestBusqueda(unittest.TestCase):
    def test_ordenado(self):
        resultado = buscar_datos("Pablo", "Diego", "Ruiz", "Picasso", **database)
        self.assertEqual(resultado,"1")

    def test_no_ordenado(self):
        resultado = buscar_datos("Anci","Elio", **database)
        self.assertEqual(resultado,"2")


    def test_no_existente(self):
        resultado = buscar_datos("Celina", "Guerra Díaz", **database)
        self.assertEqual(resultado,None)

    def test_no_ordenado_extra(self):
        resultado = buscar_datos("Diego", "Pablo", "Ruiz", "Martinez", "Picasso", **database)
        self.assertEqual(resultado,None)


if __name__ == '__main__':
    unittest.main()