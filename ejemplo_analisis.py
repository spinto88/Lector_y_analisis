from corpus import Corpus

newspaper = Corpus('Infobae.xml')

palabra = 'macri'

for note in newspaper.notes:
    if note.phraseInNote(palabra):
        print note.idNote, note.title, note.day_of_the_week, note.date
