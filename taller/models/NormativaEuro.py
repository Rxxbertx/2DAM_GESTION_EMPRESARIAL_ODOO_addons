from odoo import models, fields

class NormativaEuro(models.Model):
    _name = 'taller.normativa.euro'
    _description = 'Normativa Model'
    
    MONTH_SELECTION = [
        ('01', 'January'),
        ('02', 'February'),
        ('03', 'March'),
        ('04', 'April'),
        ('05', 'May'),
        ('06', 'June'),
        ('07', 'July'),
        ('08', 'August'),
        ('09', 'September'),
        ('10', 'October'),
        ('11', 'November'),
        ('12', 'December'),
    ]

    selected_month = fields.Selection(
        MONTH_SELECTION,
        string='Select a Month',
        default='01',  # Puedes establecer el valor predeterminado según tus necesidades
    )
    
    name = fields.Char(string="")
    year = fields.Integer(string="Año",required=True)