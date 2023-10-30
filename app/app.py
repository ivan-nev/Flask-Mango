from flask import Flask, jsonify, request
from flask_mongoengine import MongoEngine
from datetime import datetime
import config

db = MongoEngine()
app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'host': config.DB_HOST,
    'port': config.DB_PORT,
    'db': config.DB_DB,
    'username': config.DB_USER,
    'password': config.DB_PASSWORD
}

db.init_app(app)


class Memory(db.Document):
    device = db.StringField()
    memory = db.IntField()
    ts = db.DateTimeField()


@app.route('/', methods=['POST'])
def add_memory():
    body = request.get_json()
    memory = Memory(**body, ts=datetime.now()).save()
    return jsonify(memory), 201


@app.route('/all', methods=['GET'])
def get_mem():
    page = int(request.args.get('page', 1))
    limit = int(request.args.get('limit', 40))
    mems = Memory.objects.paginate(page=page, per_page=limit)
    return jsonify([mem for mem in mems.items]), 200


@app.route('/<title>', methods=['PUT'])
def update_mem_many(title):
    body = request.get_json()
    mems = Memory.objects(device=title)
    mems.update(**body)
    return jsonify([str(me.id) for me in mems]), 200


@app.route('/')
def test():
    return ('!!!OK!!!')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=config.FLASK_PORT)
