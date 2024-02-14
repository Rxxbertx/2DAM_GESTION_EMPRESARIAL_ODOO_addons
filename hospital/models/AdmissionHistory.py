from odoo import models, fields, api
from odoo.exceptions import ValidationError


class AdmissionHistory(models.Model):
    _name = 'hospital.admission.history'
    _description = 'Patient Admission History'

    patient_id = fields.Many2one('hospital.patient', string='Patient')
    floor_id = fields.Many2one('hospital.floor', string='Floor')
    bed_id = fields.Many2one('hospital.bed', string='Bed')
    admission_date = fields.Datetime(string='Admission Date and Time')
    discharge_date = fields.Datetime(string='Discharge Date and Time')
    diagnosis = fields.Text(string='Diagnosis')
    treatment = fields.Text(string='Treatment')

    patient_name = fields.Char(string='Patient Name', related='patient_id.name', readonly=True)
    patient_last_name = fields.Char(string='Patient Last Name', related='patient_id.last_name', readonly=True)
    patient_phone = fields.Char(string='Patient Phone', related='patient_id.phone', readonly=True)
    patient_admitted = fields.Selection(string='Admitted', related='patient_id.state', readonly=True)

    @api.constrains('patient_id')
    def _check_patient_bed(self):
        for history in self:
            admission_history = self.env['hospital.admission.history'].search(
                [('patient_id', '=', history.patient_id.id), ('id', '!=', history.id)])
            if admission_history:
                raise ValidationError("Patient is already admitted in another bed")

    @api.constrains('admission_date', 'discharge_date')
    def _check_dates(self):
        for history in self:
            if history.discharge_date and history.admission_date > history.discharge_date:
                raise ValidationError("Discharge date should be greater than admission date")

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

    @api.constrains('floor_id', 'bed_id', 'admission_date')
    def _check_floor_bed_admission_date(self):
        for history in self:
            if not history.floor_id or not history.bed_id or not history.admission_date or not history.discharge_date:
                raise ValidationError("Floor, Bed and Admission Date are required fields")
