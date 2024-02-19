from odoo import models, fields, api
from odoo.exceptions import ValidationError


class AdmissionHistory(models.Model):
    _name = 'hospital.admission.history'
    _description = 'Patient Admission History'

    patient_id = fields.Many2one('hospital.patient', string='Patient')
    doctor_id = fields.Many2one('hospital.doctor', string='Doctor')
    bed_id = fields.Many2one('hospital.bed', string='Bed')
    floor_id = fields.Char(related='bed_id.floor_id.name', string='Floor')
    admission_date = fields.Datetime(string='Admission Date and Time')
    discharge_date = fields.Datetime(string='Discharge Date and Time')
    diagnosis = fields.Text(string='Diagnosis')
    treatment = fields.Text(string='Treatment')

    patient_name = fields.Char(string='Patient Name', related='patient_id.name', readonly=True)
    patient_last_name = fields.Char(string='Patient Last Name', related='patient_id.last_name', readonly=True)
    patient_phone = fields.Char(string='Patient Phone', related='patient_id.phone', readonly=True)
    patient_admitted = fields.Selection(string='Admitted', related='patient_id.state', readonly=True)

    @api.constrains('admission_date', 'discharge_date')
    def _check_dates(self):
        for history in self:
            if history.discharge_date and history.admission_date > history.discharge_date:
                raise ValidationError("Discharge date should be greater than admission date")
