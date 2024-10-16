from tp3_ciphers import *
from tp3_image_functions import *

class TeamProjectDemo:

    def __init__(self, method=None, text=None, key=None, start_sequence=None, end_sequence=None, offset=None, input_path=None, output_path=None):
        self.method = method if method is not None else input("Enter the cipher you want to use for encryption: ")
        self.text = text if text is not None else input("Enter the plaintext you want to encrypt: ")
        self.key = key if key is not None else input("Enter key: ")
        self.start_sequence = start_sequence if start_sequence is not None else input("Enter start sequence: ")
        self.end_sequence = end_sequence if end_sequence is not None else input("Enter end sequence: ")
        self.offset = offset if offset is not None else input("Enter offset: ")
        self.input_path = input_path if input_path is not None else input("Enter input path: ")
        self.output_path = output_path if output_path is not None else input("Enter output path: ")

    def task1():
        

    

    
