    import pytest
    from backend.app import app
    from backend.models import db, Declaration

    @pytest.fixture
    def client():
        app.config['TESTING'] = True
        with app.test_client() as client:
            with app.app_context():
                db.create_all()
            yield client

    def test_create_declaration(client):
        response = client.post('/api/declarations', json={'cargo_type': 'Electronics', 'value': 1000.0, 'user_id': 1})
        assert response.status_code == 200
        assert response.json['success'] == True
    
