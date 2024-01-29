from encodings import utf_8


coding: utf_8

from odoo import models, fields, api


class Vehiculo(models.Model):
     _name = 'taller.vehiculo'
     _description='taller.vehiculo'
     
     descripcion= fields.Char("Descripcion")
     
     marca = fields.Many2one(comodel_name = 'taller.marca', string = 'Marca', required=True)
     modelo = fields.Many2one(comodel_name = 'taller.modelo', string = 'Modelo', required=True)
     owner= fields.Many2one(comodel_name = 'taller.owner', string = 'Dueño', required=True)

     ano = fields.Date(string='Año', widget="year_selector")
     color = fields.Char(string='Color', widget="color_picker")
     
     cilindrada = fields.Integer('Cilindrada en cm3',required=True,size=4)
     
     bastidor = fields.Char(required=True, size=100, string="Bastidor")
     matricula = fields.Char(required=True, size=10, string="Matrícula")
     
     imagen = fields.Image(string='Imagen')
     
     tipo_combustible = fields.Selection([("D","Diesel"), ("G","Gasolina"),("E","Electrico")], string = "Combustible",required=True)
     tipo_vehiculo =fields.Selection([('C', 'Camion'),('B','Bicicleta'),('T','Turismo'),('M','Motocultor'),('MO','Motocicleta'),('Q','Quad'),('P','Portador'),('A','Autobus'),('F','Furgón')], string="Tipo de Vehiculo",required=True)