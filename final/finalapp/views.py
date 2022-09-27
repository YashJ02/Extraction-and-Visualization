import mimetypes
from re import search
from urllib import response
from django.shortcuts import render, HttpResponse
import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.figure_factory as ff
import seaborn as sns
from glob import glob
import os

# Create your views here.

def index(request):
	return render(request, 'index.html')

response = ()
def extract(request):
    global response
    # get the response in the form of html
    search =request.POST['search']
    wikiurl = "https://en.wikipedia.org/wiki/" + search
    table_class = "wikitable sortable jquery-tablesorter"
    response = requests.get(wikiurl)
    if (response.status_code == 200):
        wcon = ("Website Connected")
        return render(request, 'index.html', {"result": wcon})
    
    else:
        print("Error")
        wcon = ("Check the letter case")
        return render(request, 'index.html', {"result": wcon})

def data(request):
    global response
    # parse data from the html into a beautifulsoup object
    soup = BeautifulSoup(response.text, 'html.parser')
    indiatable = soup.find_all('table', {"class": "wikitable", "class": "sortable"})
    #indiatable

    df = ()
    # checking if string is empty
    if (len(indiatable) == 0):
        dcon= ("No tables found")
        return render(request, 'index.html', {"dresult": dcon})
    else:
        df = pd.read_html(str(indiatable))
        # convert list to dataframe
        df = pd.DataFrame(df[0])
        dcon= ("Table Generated")
        df.to_csv('data.csv')
        return render(request, 'index.html', {"dresult": dcon})


def download_file(request):
    # Define Django project base directory
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # Define text file name
    filename = 'data.csv'
    # Define the full file path
    filepath = BASE_DIR + '/' + filename
    # Open the file for reading content
    path = open(filepath, 'r')
    # Set the mime type
    mime_type, _ = mimetypes.guess_type(filepath)
    # Set the return value of the HttpResponse
    response = HttpResponse(path, content_type=mime_type)
    # Set the HTTP header for sending to browser
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    # Return the response value
    return response


def plot(request):
    
	os.system('cd -')
	os.system('streamlit run visual.py')
