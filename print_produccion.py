# -*- encoding: utf-8 -*-
###########################################################################
#    Module Writen to OpenERP, Open Source Management Solution
#
#    Authors: Aktiva (<http://www.aktiva.com.mx/>)
#             
#    Coded by: Luis Felipe Lores Caignet (luisfqba@gmail.com  llores@aktiva.com.mx)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

import openerp
from openerp.tools.translate import _
from openerp.report import report_sxw
import time

class PrintProduccion(report_sxw.rml_parse):
    
    def __init__(self, cr, uid, name, context):
        super(PrintProduccion, self).__init__(cr, uid, name, context=context)
        
        self.localcontext.update({
            'get_suma': self._get_suma(),
            'time':time.strftime('%d de %B del %Y'),
        })
    def _get_partner_invoice(self,invoice): 
        sql_query = "SELECT id, number, date_invoice, num_fact_proyecto,sale_ext_origin, state from account_invoice  where partner_id = "+str(invoice.partner_id.id)+" and state in ('paid','open')"
        self.cr.execute(sql_query)    
        result = self.cr.fetchall()
        return result     
   

    
report_sxw.report_sxw(
    'report.print.produccion.webkit', 
    'mrp.servicemc', 
    'addons/mrp_servicemc/report/print_produccion.mako', 
    parser=PrintProduccion,
)
    
           
