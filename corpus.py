#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Definicion de clase Corpus, para consulta y 
uso de la base de datos .xml.
"""
from lxml import etree
from datetime import date
from datetime import timedelta
from nltk.tokenize import word_tokenize
import matplotlib.pyplot as plt
import numpy as np
import codecs

week_days = ['Lun', 'Mar', 'Mier', 'Jue', 'Vier', 'Sab', 'Dom']

# Auxiliar functions and things 
from nltk.corpus import swadesh
from nltk.corpus import stopwords
common_words = swadesh.words('es') + stopwords.words('spanish')

def phrase_variation(phrase):

    phrase_lower = phrase.lower()
    phrase_upper = phrase.upper()
    phrase_capitalize = phrase.capitalize()
    phrase_title = phrase.title()

    phrases2check = [phrase, phrase_lower, \
                 phrase_upper, phrase_capitalize, \
                 phrase_title]

    return phrases2check

# Class Note 
class Note(object):

    def __init__(self, note):

        self.idNote = int(note.get('id'))

        self.title = note.find('title').text
        if self.title == None or self.title == '[]':
            self.title = ''

        self.section = note.find('section').text
        if self.section == None or self.section == '[]':
            self.section = ''

        self.subtitle = note.find('subtitle').text
        if self.subtitle == None or self.subtitle == '[]':
            self.subtitle = ''

        self.body = note.find('body').text
        if self.body == None or self.body == '[]':
            self.body = ''

        self.day = int(note.find('date/day').text)
        self.month = int(note.find('date/month').text)
        self.year = int(note.find('date/year').text)

        self.date = date(self.year, self.month, self.day)
        self.day_of_the_week = week_days[int(note.find('date/day_of_the_week').text)]

    def __eq__(self, other):

        if self.title == other.title \
        and self.body == other.body \
        and self.subtitle == other.subtitle \
        and self.section == other.section:
            return True
        else:
            return False

    def phraseInNote(self, phrase):

        phrases2check = phrase_variation(phrase)

        for phrase2check in phrases2check:
            if phrase2check in self.title \
            or phrase2check in self.subtitle \
            or phrase2check in self.body:
                return True

        return False
        
    def numberOfBodyWords(self):

        tokens = word_tokenize(self.body)
        return len(tokens)

    def principal_words(self):

        title_tokenized = word_tokenize(self.title)
        subtitle_tokenized = word_tokenize(self.subtitle)
        body_tokenized = word_tokenize(self.body)

        # Remove common words
        for word in common_words:

            for word_variation in phrase_variation(word):

                while word_variation in title_tokenized:
                    title_tokenized.remove(word_variation)

                while word_variation in subtitle_tokenized:
                    subtitle_tokenized.remove(word_variation)                

                while word_variation in body_tokenized:
                    body_tokenized.remove(word_variation)

        # Remove punctuation symbols
        for word in title_tokenized:
            if len(word) == 1:
                title_tokenized.remove(word)
        for word in subtitle_tokenized:
            if len(word) == 1:
                subtitle_tokenized.remove(word)
        for word in body_tokenized:
            if len(word) == 1:
                body_tokenized.remove(word)

        ans = {}
        ans['title'] = ', '.join(list(set(title_tokenized)))
        ans['subtitle'] = ', '.join(list(set(subtitle_tokenized)))
        ans['body'] = ', '.join(list(set(body_tokenized)))

        return ans

    def print2file(self, fname):

        fp = codecs.open(fname,'a','utf8')
        fp.write(self.title + '\n')
        fp.write(self.section + '\n')
        fp.write(self.subtitle + '\n')
        fp.write(self.body + '\n')
        fp.close()


# Corpus
class Corpus(object):

    def __init__(self, document):

        xmldoc = etree.parse(document)
        root = xmldoc.getroot()

        self.xmldoc = xmldoc
        self.newspaper_name = root.find('name').text
        self.description = root.find('description').text

        initial_date_day = int(root.find('initial_date/day').text)
        initial_date_month = int(root.find('initial_date/month').text)
        initial_date_year = int(root.find('initial_date/year').text)
        self.initial_date = date(initial_date_year, initial_date_month, \
                            initial_date_day)
        
        final_date_day = int(root.find('final_date/day').text)
        final_date_month = int(root.find('final_date/month').text)
        final_date_year = int(root.find('final_date/year').text)
        self.final_date = date(final_date_year, final_date_month, \
                            final_date_day)

        self.notes = []
        for note in root.findall('note'):
            self.notes.append(Note(note))

        self.deleteRepeatedNotes()
        
    def deleteRepeatedNotes(self):

        notes2remove = []
        
        for note in self.notes:
            for note2compare in self.notes:
                if note2compare == note and note2compare.date >= note.date \
                and note2compare.idNote != note.idNote:
                    notes2remove.append(note2compare.idNote)

        notes_removed = 0
        for idNote in notes2remove:
            for note in self.notes:
                if note.idNote == idNote:
                    self.notes.remove(note)
                    notes_removed += 1
                    break

        return notes_removed

    def getNoteById(self, idNote):

        for note in self.notes:
            if note.idNote == idNote:
                return note       
        return 'id not found'        

    def evolOfSectionPlot(self, section):

        days = []

        current_date = self.initial_date
        while current_date <= self.final_date:
            days.append(current_date)
            current_date += timedelta(days = 1)
        
        notes = np.zeros(len(days))
        for note in self.notes:
            if note.section == section:
                ind_date = days.index(note.date)
                notes[ind_date] += 1

        plt.plot(range(len(days)), notes, '.-', markersize = 10)
        plt.xticks(range(len(days)), days, rotation = 'vertical')
        plt.grid('on')
        plt.show()

