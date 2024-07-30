from flask import Flask, request, jsonify

app = Flask(__name__)

clients = []
produits = []
taux_tva = []
factures = []

@app.route('/clients', methods=['GET', 'POST'])
def manage_clients():
    if request.method == 'GET':
        return jsonify(clients)
    elif request.method == 'POST':
        client = request.json
        clients.append(client)
        return jsonify(client), 201

@app.route('/clients/<int:client_id>', methods=['GET', 'PUT', 'DELETE'])
def manage_client(client_id):
    client = next((c for c in clients if c['id'] == client_id), None)
    if not client:
        return jsonify({'message': 'Client not found'}), 404

    if request.method == 'GET':
        return jsonify(client)
    elif request.method == 'PUT':
        data = request.json
        client.update(data)
        return jsonify(client)
    elif request.method == 'DELETE':
        clients.remove(client)
        return '', 204

@app.route('/produits', methods=['GET', 'POST'])
def manage_produits():
    if request.method == 'GET':
        return jsonify(produits)
    elif request.method == 'POST':
        produit = request.json
        produits.append(produit)
        return jsonify(produit), 201

@app.route('/produits/<int:produit_id>', methods=['GET', 'PUT', 'DELETE'])
def manage_produit(produit_id):
    produit = next((p for p in produits if p['id'] == produit_id), None)
    if not produit:
        return jsonify({'message': 'Produit not found'}), 404

    if request.method == 'GET':
        return jsonify(produit)
    elif request.method == 'PUT':
        data = request.json
        produit.update(data)
        return jsonify(produit)
    elif request.method == 'DELETE':
        produits.remove(produit)
        return '', 204

@app.route('/taux_tva', methods=['GET', 'POST'])
def manage_taux_tva():
    if request.method == 'GET':
        return jsonify(taux_tva)
    elif request.method == 'POST':
        taux = request.json
        taux_tva.append(taux)
        return jsonify(taux), 201

@app.route('/taux_tva/<int:taux_id>', methods=['GET', 'PUT', 'DELETE'])
def manage_taux(taux_id):
    taux = next((t for t in taux_tva if t['id'] == taux_id), None)
    if not taux:
        return jsonify({'message': 'Taux TVA not found'}), 404

    if request.method == 'GET':
        return jsonify(taux)
    elif request.method == 'PUT':
        data = request.json
        taux.update(data)
        return jsonify(taux)
    elif request.method == 'DELETE':
        taux_tva.remove(taux)
        return '', 204

@app.route('/factures', methods=['GET', 'POST'])
def manage_factures():
    if request.method == 'GET':
        return jsonify(factures)
    elif request.method == 'POST':
        facture = request.json
        factures.append(facture)
        return jsonify(facture), 201

@app.route('/factures/<int:facture_id>', methods=['GET', 'PUT', 'DELETE'])
def manage_facture(facture_id):
    facture = next((f for f in factures if f['id'] == facture_id), None)
    if not facture:
        return jsonify({'message': 'Facture not found'}), 404

    if request.method == 'GET':
        return jsonify(facture)
    elif request.method == 'PUT':
        data = request.json
        facture.update(data)
        return jsonify(facture)
    elif request.method == 'DELETE':
        factures.remove(facture)
        return '', 204

if __name__ == '__main__':
    app.run(debug=True)
