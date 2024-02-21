## si, un paciente, un doctor, una cama(opcional), un diagnosis(o varios), un tratamiento, prioridad colores,

##la archivo si ya se ha realizado

##cada admision tendra un reporte

from datetime import datetime

from odoo import models, fields, api
from odoo.exceptions import ValidationError


##one to many de consultas, sola 1 activa.

class Admission(models.Model):
    _name = 'hospital.admission'
    _description = 'Admission Information'

    patient_id = fields.Many2one('hospital.patient', string='Patient', required=True)
    doctor_id = fields.Many2one('hospital.doctor', string='Doctor', required=True)
    bed_id = fields.Many2one('hospital.bed', string='Bed', domain="[('state', '=', 'available')]")
    admission_date = fields.Date(string='Admission Date', default=datetime.now())
    discharge_date = fields.Date(string='Discharge Date')
    diagnosis_ids = fields.Many2many('hospital.diagnosis', string='Diagnosis')
    treatment_ids = fields.Many2many('hospital.treatment', string='Treatment')
    state = fields.Selection([('admitted', 'Admitted'), ('discharged', 'Discharged')], string='State',
                             default='admitted')
    priority = fields.Selection([('low', 'Low'), ('normal', 'Normal'), ('high', 'High')], string='Priority',
                                default='normal')

    @api.constrains('patient_id')
    def _check_patient_id(self):
        for admission in self:
            admission_ids = self.env['hospital.admission'].search([('patient_id', '=', admission.patient_id.id)])
            if len(admission_ids) > 1:
                raise ValidationError('Patient already admitted')

    @api.constrains('discharge_date')
    def _check_discharge_date(self):
        for admission in self:
            if admission.discharge_date and admission.discharge_date < admission.admission_date:
                raise ValidationError('Discharge date cannot be set before admission date')

    @api.constrains('bed_id')
    def _check_bed_id(self):
        for admission in self:
            if admission.bed_id and admission.bed_id.state == 'occupied':
                raise ValidationError('Bed already occupied')

    @api.constrains('state')
    def _check_state(self):
        for admission in self:
            if admission.state == 'discharged' and not admission.discharge_date:
                raise ValidationError('Discharge date is required')
            if admission.state == 'admitted' and admission.discharge_date:
                raise ValidationError('Discharge date must be empty')
            if admission.state == 'discharged' and admission.bed_id:
                admission.bed_id.state = 'available'
            if admission.state == 'admitted' and admission.bed_id:
                admission.bed_id.state = 'occupied'
