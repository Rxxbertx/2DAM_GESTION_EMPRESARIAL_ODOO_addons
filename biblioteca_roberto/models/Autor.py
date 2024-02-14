from odoo import models, fields, api


class Autor(models.Model):
    _name = 'biblioteca_roberto.autor'
    _description = 'autor'

    nombre = fields.Char(string="Nombre", required=True)
    libro_ids = fields.One2many(comodel_name="biblioteca_roberto.libro", inverse_name="autor_id")
    biografia = fields.Text(string="Biografia", required=True)
    cantidad_libros = fields.Integer(string='Cantidad de Libros', compute='_compute_cantidad_libros')

    @api.depends('libro_ids')
    def _compute_cantidad_libros(self):
        for autor in self:
            autor.cantidad_libros = len(autor.libro_ids)
