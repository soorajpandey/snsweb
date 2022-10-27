from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("<h1>Laudu gand mara!</h1>")

import pymongo


client = pymongo.MongoClient('mongodb://localhost:27017/')

dbname = client['admin']
collection = dbname['users']

user = {
    'name': 'bs test h ye',
    'age': 101,
    'address': 'Randi ka ghar',
}

collection.insert_one(user)