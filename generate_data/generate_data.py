# -*- coding: utf-8 -*-
from faker import Faker
import random
from pymongo import MongoClient
import os
os.environ["PYTHONIOENCODING"] = "utf-8"

fake = Faker()

# Kết nối đến MongoDB
client = MongoClient('mongodb+srv://news:xwt87J6PFmUsvnyB@cluster0.9qven.mongodb.net/?retryWrites=true&w=majority&appName=News')  # Thay đổi thông tin kết nối nếu cần
db = client['News']  # Thay đổi tên database
news_collection = db['tin_tucs'] 

# Tạo 20.000 dòng dữ liệu và chèn vào MongoDB
for _ in range(20000):
    news_data = {
        'title': fake.sentence(nb_words=10),
        'summary': fake.paragraph(nb_sentences=2),
        'content': fake.text(max_nb_chars=500)
    }
    news_collection.insert_one(news_data)

print("Đã thêm dữ liệu vào MongoDB!".encode('utf-8').decode('utf-8'))