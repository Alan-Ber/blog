from django.test import TestCase

# Create your tests here.
from django.test import TestCase

from control_blog.models import Entrada


class EntradaTests(TestCase):
    """En esta clase van todas las pruebas del modelo Entrada."""

    def test_creacion_entrada(self):
        # caso uso esperado
        nueva_entrada = Entrada(titulo="titulo", autor="autor")
        nueva_entrada.save()

        # Compruebo que la entrada fue creada y la data fue guardada correctamente
        self.assertEqual(Entrada.objects.count(), 1)
        self.assertEqual(nueva_entrada.titulo, "titulo")
        self.assertEqual(nueva_entrada.autor, "autor")
