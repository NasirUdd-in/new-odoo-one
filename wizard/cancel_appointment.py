from odoo import api, fields, models

class CancelAppointmentWizzard(models.TransientModel):
    _name = "cancel.appointment.wizard"
    _description = "Cancel Appoinment Wizard"

    appointment_id = fields.Many2one('hospital.appointment', string="Appointment")

    def action_cancel(self):
        return