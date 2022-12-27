# -*- coding : utf-8 -*-

# context manager 작성

# 라이브러리 불러오기
import contextlib
import sqlite3
from contextlib import asyncontextmanager

# context manager 패턴
# open / close
# Lock / Release
# Change / Reset
# Enter / Exit
# Start / Stop
# Setup / Teardown
# Connect / Disconnect


@contextlib.contextmanager
def db_connect(url):

    db = selite3.connect(url)
    yield db
    
    db.close()

def main():
    url = None
    db_connect(url)


@asyncontextmanager # 비동기화
def db_connect(url):

    db = selite3.connect(url)
    yield db
    
    db.close()

def main():
    url = None
    db_connect(url)