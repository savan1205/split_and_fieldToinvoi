from odoo import fields, models,api
from datetime import date,datetime


class SaleOrder(models.Model):
	_inherit="sale.order"

	vendor = fields.Char(string="Vendor")
	city_name = fields.Char(string='city name')

	def action_split(self):
		form_id = self.env.ref('sale_invoicing.wizard_split_stock_form').id
		ctx = {'order_id':self.id}
		# ctx.update({'products':self.order_line.mapped("product_id").ids})
		# print('-------------------------------------------------',self.order_line.product_id)
		return {
             'type': 'ir.actions.act_window',
        	 'name': 'Sale Order Form',
             'view_type': 'form',
             'view_mode': 'form',
             'view_id': form_id,
             'res_model': 'sale.order',
             'domain':[()],
             'context':ctx,
             'target':'new',
         }

	def _prepare_invoice(self):
		invoices = super(SaleOrder,self)._prepare_invoice()
		invoices['vendor']=self.vendor
		invoices['city_name']=self.city_name
		return invoices

		
		# return {
           	# 'view_type': 'form',
           	# 'view_mode': 'form',
           	# 'view_id': 'action_wizard_split',
            # 'res_model':'split.wizard',
            # 'target': 'current',
            # 'type': 'ir.actions.act_window',
            # "type": "ir.actions.act_window",
		# 	"res_model": "split.wizard",
		# 	"views": "form",
		# 	"name": "Wizard name",
		# }
        