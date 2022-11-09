from odoo import fields, models,api
from datetime import date,datetime

# class Stock(models.Model):
#     _inherit='stock.picking'

#     location_id=fields.Many2one(required=False)
#     location_dest_id=fields.Many2one(required=False)
#     picking_type_id=fields.Many2one(required=False)

# class StockMove(models.Model):
#     _inherit='stock.move'

#     name=fields.Char(required=False)
#     product_uom = fields.Many2one(required=False)
#     location_id=fields.Many2one(required=False)
#     location_dest_id=fields.Many2one(required=False)

class CreateStock(models.TransientModel):
    _name = "split.wizard"
    _description = "split stock or not"

    stock_split = fields.One2many(comodel_name="split.split",inverse_name="stock_id", string="Stock")
    
    # company_id = fields.One2many(comodel_name="sale.order.line",readonly=False,inverse_name='order_id', string="order")
    # product_id=fields.Many2one(related="company_id.product_id",readonly=False)
    


    @api.model
    def default_get(self,fields):
        res=super(CreateStock,self).default_get(fields)
        # print("\n\n\n\n\nctx\n\n\n",self._context)
        # # res['product_id']=self.env.context.get('active_id')
        # add_data=[]
        # for rec in self._context.get('products',False):
        #     print("\n\n\n\nself,rex---------",self,rec)

        #     val=self.env['product.product'].browse(rec)
        #     lines=(0,0,{
        #         'product_id':val.id,  
        #         })
            
        #     print("-----------------------------------",add_data)
        #     add_data.append(lines)

        # res.update({
        #     'stock_split':add_data
        #     })
        sale_active_id=self.env['sale.order'].browse(self.env.context.get('order_id'))
        print("------------------------------",sale_active_id)
        add_lines=[]
        for value in sale_active_id.picking_ids.move_ids_without_package:
            print("_________________________________________vvv",value.product_id.name)
            print("_________________________________________vvvidddddd",value.id)
            line=(0,0,{
                'product_id':value.product_id,
                'hidden_picking_id':value.id
                })

            add_lines.append(line)
            res.update({
                'stock_split':add_lines
                })                
            print("((((((((((((((((((((((((((((((((((((",line)

        return res

    def btn_split(self):
        sale_id=self.env['sale.order'].browse(self.env.context.get('order_id'))
        new_picking=self.env['stock.picking'].create({
            'picking_type_id': 2,
            'location_id': 8,
            'location_dest_id' :10,
            'note' : "note",
            'origin':sale_id.name
            })
        print("++++++++++++++++++++++++++++",new_picking)

        for wizard_lines in self.stock_split:
            if wizard_lines.split_check == True:
                wizard_lines.hidden_picking_id.write({
                    'picking_id':new_picking
                    })

        # for rec in self.stock_split:
        #     if rec.split_check==True:
        #         print("--------------------------------",rec.product_id.name)
        #         line=(0,0,{
        #             'product_id':rec.product_id.id
        #         })
        #         list1.append(line)

        #         products = self.env['stock.move.line'].search([('product_id','=',rec.product_id.id)])
        #         print("++++++++++++++++++++++++++++++",products)  
        
        # self.env['stock.picking'].create({
        #     'move_ids_without_package':list1})


        # self.ensure_one()

        # magic code
        # duplicate_rec = self.copy()
        # result= self.env['stock.picking'].search([('origin','=',self.sale_active_id.name)])


        # duplicate_rec1 = self.env['stock.picking'].copy().id
        # print("_--------------------------------123546456-",duplicate_rec)
        # print("_---------------------------------",result)
        # return duplicate_rec
        #         return self.env['stock.picking'].copy(default) 
                # vals[]
    
    # @api.model
    # def create(self,vals):
        



class SplitStock(models.TransientModel):
    _name='split.split'
    # _inherit="sale.order"

    stock_id = fields.Many2one(comodel_name="split.wizard",string="split" )
    
    product_id=fields.Many2one('product.product',string="product",readonly=False)
    split_check=fields.Boolean(string="Split Stock?")
    hidden_picking_id=fields.Many2one(comodel_name="stock.move",string="Hidden picking_id")
    # sale_orderr_id = fields.Many2one(comodel_name="sale.order", string="order")
    # company_id=fields.Many2one('sale.order.line',string="product",readonly=False)
    #pro_id=fields.Many2one('product.products')

    # @api.model
    # def default_get(self,fields):
    #     res=super(SplitStock,self).default_get(fields)
    #     res['sale_orderr_id']=self.env.context.get('active_id')
    #     return res


    # def product_get(self):
        # for rec in self:
        #     records=self.env['product.product'].search([('name','=',rec.sale_orderr_id.product_id)])
        #     print("___________________________________",records)
    