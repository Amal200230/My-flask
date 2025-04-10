from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# ✅ Configuring the SQLAlchemy URI properly
app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc://LAPTOP-U2S02IPI\\MSSQLSERVER01/amal?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Details(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    place = db.Column(db.String(50))


with app.app_context():
    db.create_all()


@app.route('/users', methods=['GET'])
def get_users():
    new = Details.query.all()
    return jsonify([   {"id": n.id, "name": n.name, "place": n.place} for n in new]), 200
    
     
@app.route('/user', methods=['POST'])
def post_user():
    data = request.json
    new_user = Details(name=data['name'], place=data['place'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"status": "new user added"}), 201


@app.route('/user/<int:id>', methods=['PUT'])
def put_user(id):
    user = Details.query.get(id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    data = request.json
    user.name = data['name']
    user.place = data['place']
    db.session.commit()
    return jsonify({"status": "user updated"}), 200

@app.route('/user/<int:id>', methods=['DELETE'])
def del_user(id):
    user = Details.query.get(id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    db.session.delete(user)
    db.session.commit()
    return jsonify({"status": "user deleted"}), 200


if __name__ == '__main__':
    app.run(debug=True)
