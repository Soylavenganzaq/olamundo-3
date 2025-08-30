from flask import Blueprint

band_bp = Blueprint ("band_bp", __name__)

@band_bp.route ('/bands', methods =['GET'])
print ("Hola mundo")

@band_bp.route('/bands/<int:band_id>', methods=['GET'])
print ("Hola mundo")

@band_bp.route('/bands', methods=['POST'])
print ("Hola mundo")

@band_bp.route('/bands/<int:band_id>', methods=['PUT'])
print ("Hola mundo")

@band_bp.route('/bands/<int:band_id>', methods=['DELETE'])
print ("Hola mundo")