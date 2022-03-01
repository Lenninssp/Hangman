import os


class List:

    def add_word():
        word = input('>')
        with open('lista.txt', 'a') as f:
            f.write('\n' + word.strip() + '\n')
        f.close()

    def read():
        with open('lista.txt', 'r') as f:
            print(f.read())
            f.close()

    def delete():
        word = input('>')
        with open('lista.txt', 'r') as f:
            texto = list([x.strip() for x in f.readlines()])
            if word == '*all':
                with open('lista.txt', 'w') as g:
                    g.write('')
            print(texto)
            print(word)
            for a in texto:
                if word == a:
                    texto.remove(word)
            print(texto)

            f.seek(0, os.SEEK_SET)
            final = [a + '\n' for a in texto if a != '']
            print(final)
            with open('lista.txt', 'w') as g:
                g.write(''.join(final))
                g.seek(0, os.SEEK_SET)
            print(f.read())

    list_options = {'add': add_word, 'read': read, 'delete': delete}
