from odoo import models, fields, api
from datetime import timedelta


class ClipmetrajesWorkflowManager(models.Model):
    _inherit = 'project.task'

    @api.model
    def create(self, values):
        mailactivity = super().create(values)

        noteName = ""
        summary = ""

        if "Peticion CM" in mailactivity.name:
            summary = "Clipmetrajes - Nueva Peticion"
            noteName = "Se ha hecho una nueva peticion para el modulo de Clipmetrajes."
            if "Clipmetraje" in mailactivity.name:
                noteName = "Se requiere insertar un nuevo clipmetraje."
        elif "Revision CM" in mailactivity.name:
            summary = "Clipmetrajes - Nueva Revision"
            noteName = "Se requiere una nueva revision para informacion en el modulo Clipmetrajes."
        else:
            summary = "Nueva tarea ha sido asignada"
            noteName = "Se le ha asignado a usted una nueva tarea."

        notifyRequest = self.env['mail.activity'].create({
            'user_id': mailactivity.user_id.id,
            'res_model_id': mailactivity.project_id.alias_model_id.id,
            'res_id': mailactivity.id,
            'create_date': fields.Date.today(),
            'date_deadline': fields.Date.today() + timedelta(days=2),
            'res_name': mailactivity.name,
            'note': f'<p>{noteName}<p>',
            'summary': summary,
            'activity_type_id': 4,
        })

        return mailactivity
