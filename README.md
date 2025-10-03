Prerequisites:
1. Python 3.10+ (install Flask, Flask-SQLAlchemy, Flask-CORS via pip install flask flask-sqlalchemy flask-cors).
2. Go 1.20+ (install Gin via go mod init frontend && go get github.com/gin-gonic/gin).
3. Run backend: cd backend && python app.py (runs on http://localhost:5000).
4. Run frontend: cd frontend && go run main.go (runs on http://localhost:8080, proxies API calls to backend).
