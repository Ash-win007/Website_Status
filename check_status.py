import requests
from dotenv import load_dotenv
import os
import smtplib
from http.client import responses
from urllib.request import urlopen
from time import time
import streamlit as st


def check(url):
    req = requests.get(url, headers={'User-Agent': 'custom user agent'},timeout=5)
    if req.status_code == 200:
        header=req.headers
        try:
            website = urlopen(url)
            open_time = time()
            output = website.read()
            close_time = time()
            website.close()
            time_taken=str(round(close_time-open_time,3))
        except:
            time_taken="-"
        return str(req.status_code),time_taken,header

    else:
        return str(req.status_code),"-",header