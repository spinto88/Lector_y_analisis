from corpus import Corpus

newspaper = Corpus('Infobae.xml')

print newspaper.notes[0].title
print newspaper.notes[1].title

print len(newspaper.notes)
"""
palabra = 'Brexit'

for note in newspaper.notes:
    try:
        if note.phraseInNote(palabra):
            print note.idNote, note.title, note.day_of_the_week, note.date
    except:
        print note.idNote
        break
"""
