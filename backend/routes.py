   from flask import jsonify, request
   from models import db, User, Declaration

   def init_routes(app):
       @app.route('/api/login', methods=['POST'])
       def login():
           data = request.json
           user = User.query.filter_by(username=data['username']).first()
           if user and user.password == data['password']:  # Simple auth (hash in prod)
               return jsonify({'success': True, 'user_id': user.id})
           return jsonify({'success': False}), 401

       @app.route('/api/declarations', methods=['GET', 'POST'])
       def declarations():
           if request.method == 'POST':
               data = request.json
               decl = Declaration(cargo_type=data['cargo_type'], value=data['value'], user_id=data['user_id'])
               db.session.add(decl)
               db.session.commit()
               return jsonify({'success': True, 'id': decl.id})
           else:
               decls = Declaration.query.all()
               return jsonify([{'id': d.id, 'cargo_type': d.cargo_type, 'value': d.value} for d in decls])
   
