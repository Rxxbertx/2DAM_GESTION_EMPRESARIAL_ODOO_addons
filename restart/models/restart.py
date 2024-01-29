import os
import sys

from odoo import models, api, exceptions


class Restart(models.Model):
    _name = 'module.restart'

    @api.model
    def do_restart(self):
        if self.env.user.has_group('base.group_system'):
            try:
                self.env.cr.commit()  # Confirmar cualquier cambio pendiente en la base de datos
                self.env.cr.close()  # Cerrar la conexión a la base de datos actual
                self.env.registry.clear_cache()  # Limpiar la caché del registro
                os.execv(sys.executable, ['python3'] + sys.argv)
                # raise exceptions.RestartOdoo("Reinicio de Odoo")  # Utiliza odoo.exceptions.RestartOdoo
            except Exception as e:
                raise exceptions.UserError(f"Error al reiniciar Odoo: {e}")  # Utiliza odoo.exceptions.UserError
        else:
            raise exceptions.AccessError("No tienes permiso para reiniciar Odoo")  # Utiliza odoo.exceptions.AccessError
