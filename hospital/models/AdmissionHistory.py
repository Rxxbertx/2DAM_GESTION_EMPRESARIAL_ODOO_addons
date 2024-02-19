from odoo import models, fields, api
from odoo.exceptions import ValidationError


class AdmissionHistory(models.Model):
    _name = 'hospital.admission.history'
    _description = 'Patient Admission History'

    patient_id = fields.Many2one('hospital.patient', string='Patient')
    doctor_id = fields.Many2one(related='patient_id.doctor_id', string='Doctor')
    bed_id = fields.Many2one(related='patient_id.bed_id', string='Bed')
    previous_bed = fields.Many2one('hospital.bed', string='Previous Bed')
    previous_doctor = fields.Many2one('hospital.doctor', string='Previous Doctor')
    floor_id = fields.Many2one(related='bed_id.floor_id', string='Floor')
    admission_date = fields.Datetime(string='Admission Date and Time')
    discharge_date = fields.Datetime(string='Discharge Date and Time')
    diagnosis = fields.Text(string='Diagnosis')
    treatment = fields.Text(string='Treatment')

    @api.constrains('admission_date', 'discharge_date')
    def _check_dates(self):
        for history in self:
            if history.discharge_date and history.admission_date > history.discharge_date:
                raise ValidationError("Discharge date should be greater than admission date")
