import os
import requests
import anapioficeandfire
import base64

def Get_Books(): #pega todos os livros, teoricamente
    url: "https://anapioficeandfire.com/api/books/"
    r = requests.get(url)
    books = r.json()
    bookslist = []
    for i in range(len(books['books'])):
        bookslist.append(books['books'][i])
    return bookslist

def Get_PovCharacter():
    '''pega os principais personagens do livro'''
    url : 'https://anapioficeandfire.com/api/books/'
    r = requests.get(url)
    povcha = r.json()
    povchalist = []
    for i in range(len(povcha['Cronicas do Gelo e Fogo'])):
        povchalist.append(povcha['povCharacters'][1])
    return povchalist

def Get_Covers():
    '''pega as capas e coverte para o formato base64'''
    url = 'https://openlibrary.org/dev/doc/api/covers'
    r = requests.get(url)
    cover = r.json()
    coverb64 = base64.b64enconde(cover.encode())
    return coverb64


def Get_Details(): 
    '''pega os detalhes dos personagens'''
    url: 'https://anapioficeandfire.com/api/books/'
    r = requests.get(url)
    character = r.json()
    characterlist = []
    for i in range(len(character['character'])):
        characterlist.append(character[i][i])
    return  characterlist
