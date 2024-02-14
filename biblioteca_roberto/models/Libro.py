from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Libro(models.Model):
    _name = 'biblioteca_roberto.libro'
    _description = 'libro'

    titulo = fields.Char(string="Titulo", required=True)
    isbn = fields.Char(string="ISBN", required=True)
    autor_id = fields.Many2one(string="Autor", comodel_name="biblioteca_roberto.autor")
    fecha_publicacion = fields.Date(string="Fecha Publicacion", required=True)
    estado = fields.Selection([('disponible', 'Disponible'), ('prestado', 'Prestado'), ('reparacion', 'Reparacion')],
                              string='Estado', required=True)

    @api.constrains('isbn')
    def _check_isbn(self):
        for libro in self:
            if self.search_count([('isbn', '=', libro.isbn)]) > 1:
                raise ValidationError("El ISBN debe ser único")

    @api.constrains('fecha_publicacion')
    def _check_fecha_publicacion(self):
        for libro in self:
            if libro.fecha_publicacion > fields.Date.today():
                raise ValidationError("La fecha de publicación no puede ser futura")
