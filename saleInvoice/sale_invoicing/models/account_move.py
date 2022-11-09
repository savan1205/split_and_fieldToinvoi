from odoo import fields, models,api
from datetime import date,datetime


class AccountMove(models.Model):
	_inherit="account.move"

	vendor = fields.Char(string='vendor')
	city_name = fields.Char(string='city name')

class AccountMoveLine(models.Model):
	_inherit="account.move.line"	

	weight = fields.Char(string='weight')
	manu_before = fields.Char(string='manufactured before')
