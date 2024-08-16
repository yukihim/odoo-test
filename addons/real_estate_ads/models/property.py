from odoo import fields, models



class Property(models.Model):
    _name = 'estate.property'
    _description = 'Estate Properties'
    
    name = fields.Char(string="Name", required=True)
    description = fields.Char(string="Description")
    postcode = fields.Char(string="Postcode")
    date_availability = fields.Date(string="Available from")
    expected_price = fields.Float(string="Expected Price")
    best_offer = fields.Float(string="Best offer")
    selling_price = fields.Float(string="Selling Price")
    bedrooms = fields.Integer(string="Bedrooms")
    living_area = fields.Integer(string="Living Area (sqm)")
    facades = fields.Integer(string="Facades")
    garage = fields.Boolean(string="Garage", default=False)
    garden = fields.Boolean(string="Garden", default=False)
    garden_area = fields.Integer(string="Garden Area (sqm)")
    garden_orientation = fields.Selection(
        [
            ('north', 'North'),
            ('south', 'South'),
            ('east', 'East'),
            ('west', 'West')
        ], string="Garden Orientation", default='north')
    total_area = fields.Integer(string="Total Area (sqm)")
    
    # id = fields.Integer()
