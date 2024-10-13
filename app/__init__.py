from flask import Flask, render_template  # Import render_template
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app) # Cho phép Cross-Origin Resource Sharing

     # In ra danh sách templates
    print(app.jinja_env.list_templates()) 
    
    # Các cấu hình khác (ví dụ: database)
    # ...

    from app.api import bp as api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    from app.api import routes
    routes.register_routes(app)  # Đăng ký routes sau khi app đã được tạo

     # Định nghĩa route cho trang chủ
    @app.route('/')
    def index():
         return render_template('index.html')

    return app