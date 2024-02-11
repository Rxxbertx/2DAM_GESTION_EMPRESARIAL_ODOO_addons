from odoo import models, fields
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



