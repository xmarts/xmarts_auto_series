# -*- coding: utf-8 -*-

from odoo import models, fields, api


class StockPickingSeries(models.Model):
	_inherit = "stock.picking"

	@api.multi
	@api.model
	def generar_series(self):
		for ml in self.move_lines:
			cont = 0
			for mli in ml.move_line_ids:
				if ml.product_id.tracking in ['serial','lot']:
					cont = cont + 1
					part = str(self.partner_id.ref)
					pro = str(ml.product_id.default_code).upper()
					lo = str(pro[0:10]).zfill(10) + str(part[0:5]).zfill(5) + str(self.purchase_id.id).zfill(5) + str(cont).zfill(3)
					mli.lot_name = lo


class ResCompany(models.Model):
	_inherit = "res.company"

	int_ref = fields.Char(string="Referencia interna")