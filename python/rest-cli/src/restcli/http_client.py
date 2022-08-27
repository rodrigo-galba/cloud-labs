import requests

def get(url):
    return requests.get(url)

def post(url):
    return requests.post(url)

def put(url):
    return requests.put(url)

def delete(url):
    return requests.delete(url)

def head(url):
    return requests.head(url)

def options(url):
    return requests.options(url)
