from fastapi import FastAPI
from reverseanalytics import analyticslookup
from urlscan import urlscan
app = FastAPI()

@app.get("/analyticslookup")
def lookup(domain:str):
    data = analyticslookup(domain)
    return data

@app.get("/urlscan")
def lookup(domain:str):
    data = urlscan(domain)
    return data