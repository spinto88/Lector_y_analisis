from corpus import Corpus

lanacion = Corpus('LaNacion.xml')

palabra = 'Brexit'

for note in lanacion.notes:

    if note.phraseInNote(palabra):

        print note.idNote, note.title, note.date
