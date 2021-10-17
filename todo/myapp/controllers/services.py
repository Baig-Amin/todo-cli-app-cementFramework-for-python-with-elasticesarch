from datetime import datetime


def addIndex():
    data = {
        "author": "John",
        "text": "Interesting content.",
        "timestamp": datetime.now(),
    }
    return data


def updateIndex():
    data = {
        "author": "Anna",
        "text": "Not Interesting content.",
        "timestamp": datetime.now(),
    }
    return data
