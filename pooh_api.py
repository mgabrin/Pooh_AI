from flask_restful import reqparse, abort, Api, Resource
from flask import request
from pooh_delegator import delegator, startThread

class General(Resource):
	def post(self):
		response = delegator(getApp(), request.data.decode("utf-8"))()
		return response