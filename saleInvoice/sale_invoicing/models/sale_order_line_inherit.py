from odoo import fields, models,api
from datetime import date,datetime


class SaleOrderLine(models.Model):
	_inherit="sale.order.line"


	
	weight = fields.Char(string='weight')
	manu_before= fields.Char(string='manufactured before ')

	def _prepare_invoice_line(self, **optional_values):
		ress=super(SaleOrderLine,self)._prepare_invoice_line()
		ress['weight']=self.weight
		ress['manu_before']=self.manu_before
		return ress


	