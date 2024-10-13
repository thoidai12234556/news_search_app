# File chạy ứng dụng Flask
import os
print(f"Đường dẫn thư mục hiện tại: {os.getcwd()}") 
from app import create_app 

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)