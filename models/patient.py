# -*- coding: utf-8 -*-
from email.policy import default

from odoo import api, fields, models
from datetime import date


class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Patient Record'


    name = fields.Char(string="Name", tracking=True)
    date_of_birth = fields.Date(string='Date of Brith')
    ref=fields.Char(string="Reference", tracking=True)
    age = fields.Integer(string="Age",compute='_compute_age' ,tracking=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string="Gender", tracking=True, default='female')
    active= fields.Boolean(string="Active", default=True, tracking=True)
    image = fields.Image(string="Image")

    @api.depends('date_of_birth')
    def _compute_age(self):
        for rec in self:
            today = date.today()
            print(date.today())
            if rec.date_of_birth:
                rec.age = today.year - rec.date_of_birth.year
            else:
                rec.age = 0