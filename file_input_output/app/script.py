""" Read a file and translate it to another language"""
from translate import Translator

translator = Translator(to_lang='ja')
try:
    with open('./translate.txt', mode='r') as file:
        file_translate = file.read()
        print(file_translate)
        translation = translator.translate(file_translate)
        print(translation)
        with open('./test-ja.txt', mode='w') as ja_file:
            ja_file.write(translation)
except FileNotFoundError as e:
    print('file does not exist! check your file path silly!')
    raise e
