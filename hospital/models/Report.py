from odoo import models, fields


class Report(models.Model):
    _name = 'hospital.report'
    _description = 'Report Information'

    name = fields.Char(string='Report', required=True)
    description = fields.Text(string='Description')
    date = fields.Date(string='Date', default=fields.Date.today())
    state = fields.Selection([('in_progress', 'In Progress'), ('completed', 'Completed')], string='State',
                             default='in_progress')
    admission_id = fields.Many2one('hospital.admission', string='Admission')
    patient_id = fields.Many2one('hospital.patient', string='Patient', related='admission_id.patient_id', readonly=True)
    doctor_id = fields.Many2one('hospital.doctor', string='Doctor', related='admission_id.doctor_id', readonly=True)
    bed_id = fields.Many2one('hospital.bed', string='Bed', related='admission_id.bed_id', readonly=True)
    admission_date = fields.Date(string='Admission Date', related='admission_id.admission_date', readonly=True)
    discharge_date = fields.Date(string='Discharge Date', related='admission_id.discharge_date', readonly=True)
    diagnosis_ids = fields.Many2many('hospital.diagnosis', string='Diagnosis.xml', related='admission_id.diagnosis_ids',
                                     readonly=True)
    treatment_ids = fields.Many2many('hospital.treatment', string='Treatment', related='admission_id.treatment_ids',
                                     readonly=True)
    priority = fields.Selection([('low', 'Low'), ('normal', 'Normal'), ('high', 'High')], string='Priority',
                                related='admission_id.priority', readonly=True)
