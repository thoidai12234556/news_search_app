# app/api/routes.py

from flask import jsonify, request
from pymongo import MongoClient
import time

# Kết nối đến MongoDB
client = MongoClient('mongodb+srv://news:xwt87J6PFmUsvnyB@cluster0.9qven.mongodb.net/?retryWrites=true&w=majority&appName=News')
db = client['News']
news_collection = db['tin_tucs']

def register_routes(app):
    @app.route('/api/search', methods=['GET'])
    def search():
        start_time = time.time()
        search_query = request.args.get('q')

        if not search_query:
            return jsonify({'error': 'Vui lòng nhập từ khóa tìm kiếm.'}), 400  # Bad Request

        try:
            # Thực hiện truy vấn tìm kiếm trên MongoDB (không phân biệt chữ hoa/thường)
            results = news_collection.find(
                {'title': {'$regex': f'.*{search_query}.*', '$options': 'i'}}
            )

            # Chuyển đổi kết quả từ pymongo cursor sang list dictionaries
            results_list = []
            for doc in results:
                results_list.append({
                    'title': doc.get('title'),
                    'summary': doc.get('summary'),
                    'content': doc.get('content'),
                })
            
            end_time = time.time()
            search_time = round((end_time - start_time) * 1000, 2)  # Tính thời gian tìm kiếm (ms)

            return jsonify({'results': results_list, 'search_time': search_time})

        except Exception as e:
            return jsonify({'error': f'Lỗi khi truy vấn MongoDB: {str(e)}'}), 500  # Internal Server Error