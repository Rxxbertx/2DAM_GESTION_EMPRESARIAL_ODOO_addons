from datetime import datetime

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Admission(models.Model):
    _name = 'hospital.admission'
    _description = 'Admission Information'

    name = fields.Char(string='Admission')
    patient_id = fields.Many2one('hospital.patient', string='Patient', required=True)
    patient_social_security_number = fields.Char(related='patient_id.social_security_number', string='Social Security')
    
    doctor_admissions_id = fields.Many2one('hospital.doctor', string='Doctor', required=True)
    doctor_patients_id = fields.Many2one('hospital.doctor', string='Doctor')

    bed_id = fields.Many2one('hospital.bed', string='Bed', domain="[('state', '=', 'available')]")
    admission_date = fields.Datetime(string='Admission Date', default=datetime.now())
    discharge_date = fields.Datetime(string='Discharge Date')
    diagnosis_ids = fields.Many2many('hospital.diagnosis', string='Diagnosis')
    treatment_ids = fields.Many2many('hospital.treatment', string='Treatment')
    state = fields.Selection([('admitted', 'Admitted'), ('discharged', 'Discharged')], string='State',
                             default='admitted')
    priority = fields.Selection([('low', 'Low'), ('normal', 'Normal'), ('high', 'High')], string='Priority',
                                default='normal')

    report_id = fields.One2many('hospital.report', 'admission_id', string='Report')

    @api.constrains('report_id')
    def _check_report_id(self):
        for admission in self:
            if len(admission.report_id) > 1:
                raise ValidationError('Only one report per admission')

    @api.model
    def create(self, vals):

        record = super().create(vals)
        record.name = "Admission for " + record.patient_id.full_name
        report = self.env['hospital.report'].create({
            'name': 'Report for ' + record.patient_id.name,
            'admission_id': record.id,
        })
        record.patient_id.state = 'admitted'
        if record.bed_id:
            record.bed_id.state = 'occupied'

        record.doctor_patients_id = record.doctor_admissions_id
        record.report_id = [(6, 0, [report.id])]
        return record

    def write(self, vals):
        res = super().write(vals)
        if 'state' in vals and vals['state'] == 'discharged':
            for record in self:
                if record.report_id:
                    record.report_id.write({
                        'state': 'completed',
                    })
        return res

    def discharge(self):

        if self.discharge_date:
            self.discharge_date
        else:
            self.discharge_date = datetime.now()

        self.state = 'discharged'
        self.patient_id.state = 'not_admitted'
        self.bed_id.state = 'available'
        self.doctor_admissions_id.treated_patients_ids |= self
        self.doctor_admissions_id.patients -= self

    @api.constrains('doctor_admissions_id')
    def _check_doctor_admissions_id(self):
        for admission in self:
            if admission.doctor_admissions_id:
                admission.doctor_patients_id = admission.doctor_admissions_id
            
    @api.constrains('patient_id')
    def _check_patient_id(self):
        for admission in self:
            if admission.patient_id.state == 'admitted':
                raise ValidationError('Patient already admitted')

    @api.constrains('discharge_date')
    def _check_discharge_date(self):
        for admission in self:
            if admission.discharge_date and admission.discharge_date < admission.admission_date:
                raise ValidationError('Discharge date cannot be set before admission date')
            else:
                if admission.discharge_date:
                    self.discharge()

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
