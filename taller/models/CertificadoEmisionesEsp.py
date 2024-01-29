from odoo import models, fields

class NormativaEuro(models.Model):
    _name = 'taller.certificado.emisiones'
    _description = 'Certificado Model'

    name = fields.Char(srting = "Nombre",required=True)
    image = fields.Image(string='Imagen',widget="image",required=True)
    description = fields.Text(string = "Descripcion")