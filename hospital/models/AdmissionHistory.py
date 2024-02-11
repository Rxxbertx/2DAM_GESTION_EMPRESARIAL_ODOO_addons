from odoo import models, fields, api
from odoo.exceptions import ValidationError


class AdmissionHistory(models.Model):
    _name = 'hospital.admission.history'
    _description = 'Patient Admission History'

    patient_id = fields.Many2one('hospital.patient', string='Patient')
    bed_id = fields.Many2one('hospital.bed', string='Bed')
    admission_date = fields.Datetime(string='Admission Date and Time')
    discharge_date = fields.Datetime(string='Discharge Date and Time')
    diagnosis = fields.Text(string='Diagnosis')
    treatment = fields.Text(string='Treatment')

    # Creamos una constraint de que el paciente no puede tener dos camas asignadas
    @api.constrains('patient_id')
    def _check_patient_bed(self):
        for history in self:
            admission_history = self.env['hospital.admission.history'].search(
                [('patient_id', '=', history.patient_id.id), ('id', '!=', history.id)])
            if admission_history:
                raise ValidationError("Patient is already admitted in another bed")

    # Creamos una constraint de que la fecha de ingreso no puede ser mayor a la fecha de salida
    @api.constrains('admission_date', 'discharge_date')
    def _check_dates(self):
        for history in self:
            if history.discharge_date and history.admission_date > history.discharge_date:
                raise ValidationError("Discharge date should be greater than admission date")

    # Creamos una cosntraint en la que si la cama esta ocupada no se pueda asignar
    @api.constrains('bed_id')
    def _check_bed_limit(self):
        for history in self:
            bed = self.env['hospital.bed'].search([('id', '=', history.bed_id.id)])
            if bed.state == 'occupied':
                raise ValidationError("Bed is occupied")
            if bed.state == 'available':
                bed.state = 'occupied'
            if bed.state == 'occupied':
                bed.state = 'available'
