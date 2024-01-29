from encodings import utf_8


coding: utf_8

from odoo import models, fields, api
 
class Owner(models.Model):
     _name = 'taller.owner'
     _description='taller.owner'
     
     name = fields.Char(required=True,size=20,string = 'Nombre')
     surname = fields.Char(required=True,size=30,string = 'Apellidos')
     dni = fields.Char(required=True, size=9, string = 'Dni')
     phone = fields.Char(required=True, size=10, string = 'Numero de Telefono')
     
     @api.constrains('dni')
     def _check_valid_dni(self):
        for record in self:
            dni = record.dni
            # Verificar que el DNI tenga 9 caracteres (8 números y 1 letra)
            if len(dni) != 9:
                raise ValidationError("El DNI debe tener 9 caracteres.")
            
            # Verificar que los primeros 8 caracteres sean números
            if not dni[:8].isdigit():
                raise ValidationError("Los primeros 8 caracteres del DNI deben ser números.")
            
            # Verificar que el último caracter sea una letra
            if not dni[8].isalpha():
                raise ValidationError("El último caracter del DNI debe ser una letra.")
            
            # Verificar que la letra sea correcta según el algoritmo de validación del DNI español
            letras_validas = 'TRWAGMYFPDXBNJZSQVHLCKE'
            numero = int(dni[:8])
            if letras_validas[numero % 23] != dni[8].upper():
                raise ValidationError("La letra del DNI no es válida.")