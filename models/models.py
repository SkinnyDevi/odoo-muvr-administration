# -*- coding: utf-8 -*-

from odoo import models, fields, api


class clipmetrajes_usuarios(models.Model):
    _name = "clipmetrajes.usuarios"
    _description = "clipmetrajes.usuarios"
    _rec_name = "username"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Integer(string="ID Usuario")
    password = fields.Char(string="Contraseña", required=True)
    user_email = fields.Char(string="Email", required=True)
    username = fields.Char(string="Nombre de Usuario", compute="_generateUsername", store=True)
    is_admin = fields.Boolean(string="Administrador")

    @api.depends('user_email')
    def _generateUsername(self):
        for r in self:
            email = str(r.user_email)
            if email == "False" or email == "True":
                r.username = "Esperando un correo..."
            else:
                r.username = email.split('@')[0].replace(".", "_")


class clipmetrajes_clipmetrajes(models.Model):
    _name = "clipmetrajes.clipmetrajes"
    _description = "clipmetrajes.clipmetrajes"
    _rec_name = "clip_name"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Integer(string="ID Clipmetraje")
    clip_name = fields.Char(string="Nombre Clipmetraje", required=True)
    clip_duration = fields.Char(string="Duracion (mm:ss)", required=True)
    clip_image = fields.Image(string="Imagen de Portada")
    clip_ratings = fields.One2many("clipmetrajes.valoraciones", "clip_name", string="Valoraciones")
    project = fields.Many2one("project.task", string="Peticion Actual")


class clipmetrajes_valoraciones(models.Model):
    _name = "clipmetrajes.valoraciones"
    _description = "clipmetrajes.valoraciones"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    username = fields.Many2one("clipmetrajes.usuarios", string="Usuario", required=True, ondelete="cascade")
    clip_name = fields.Many2one("clipmetrajes.clipmetrajes", string="Clipmetraje", required=True, ondelete="cascade")
    rating = fields.Selection(string="Valoracion", selection=[('like', "Me Gusta"), ('regular', "Regular"), ('dislike', "No Me Gusta")])


class clipmetrajes_clipmetrajes_in_project(models.Model):
    _name = "project.task"
    _inherit = "project.task"

    clips_list = fields.One2many("clipmetrajes.clipmetrajes", "project", string="Clipmetrajes")
