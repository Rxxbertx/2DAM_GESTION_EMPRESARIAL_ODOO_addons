from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Patient(models.Model):
    _name = 'hospital.patient'
    _description = 'Patient Information'

    name = fields.Char(string='Name', required=True)
    last_name = fields.Char(string='Last Name', required=True)
    full_name = fields.Char(string='Full Name', compute='_get_full_name', store=True)
    date_of_birth = fields.Date(string='Date of Birth')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other')], string='Gender')
    age = fields.Integer(string='Age', compute='_get_age', store=True)
    address = fields.Text(string='Address')
    phone = fields.Char(string='Phone')
    allergies = fields.Text(string='Allergies')
    preexisting_conditions = fields.Text(string='Preexisting Conditions')
    state = fields.Selection([
        ('admitted', 'Admitted'),
        ('not_admitted', 'Not Admitted'),
    ], string='State', default='not_admitted')
    bed_id = fields.Many2one('hospital.bed', string='Bed', domain="[('state', '=', 'available')]")
    doctor_id = fields.Many2one('hospital.doctor', string='Doctor')

    @api.constrains('bed_id')
    def check_bed_availability(self):
        for record in self:
            if record.bed_id and record.bed_id.state == 'occupied':
                raise ValidationError("The bed is already occupied.")

    def write(self, vals):
        res = super(Patient, self).write(vals)
        if 'bed_id' in vals:
            self.bed_id.state = 'occupied' if vals['bed_id'] else 'available'
            self.state = 'admitted' if vals['bed_id'] else 'not_admitted'

        if 'doctor_id' in vals:
            if self.doctor_id:
                self.state = 'admitted' if vals['doctor_id'] else 'not_admitted'

        return res

    def discharge(self):
        if self.bed_id:
            self.bed_id.state = 'available'
            self.bed_id = False
        if self.doctor_id:
            self.doctor_id.treated_patients_ids += self
            self.doctor_id = False
        self.state = 'not_admitted'


    @api.depends('name', 'last_name')
    def _get_full_name(self):
        for patient in self:
            patient.full_name = patient.name + ' ' + patient.last_name


    @api.depends('date_of_birth')
    def _get_age(self):
        for patient in self:
            if patient.date_of_birth:
                today = fields.Date.today()
                dob = fields.Datetime.from_string(patient.date_of_birth)
                age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
                patient.age = age

