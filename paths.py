import os

class Paths:
    
    def __init__(self, relative_path):


        if os.name == 'posix':
            relative_path = relative_path.replace('\\', '/')


        # Ruta absoluta del directorio donde se encuentra el script main de Python
        self.path_main = os.path.dirname(os.path.abspath(__file__))

        # Ruta absoluta del archivo que queremos
        self.absolute_path = os.path.join(self.path_main, relative_path)

    def __str__(self):
            
        return self.absolute_path
