# -*- coding: utf-8 -*-
#############################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#
#    Copyright (C) 2025-TODAY Cybrosys Technologies(<https://www.cybrosys.com>)
#    Author: SREERAG PM (<https://www.cybrosys.com>)
#
#    You can modify it under the terms of the GNU AFFERO
#    GENERAL PUBLIC LICENSE (AGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU AFFERO GENERAL PUBLIC LICENSE (AGPL v3) for more details.
#
#    You should have received a copy of the GNU AFFERO GENERAL PUBLIC LICENSE
#    (AGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
#############################################################################
from odoo import models, fields
from odoo import tools


class SubscriptionReport(models.Model):
    _name = "subscription.report"
    _description = "Subscription Analysis"
    _auto = False

    total_recurring_price = fields.Float('Recurring Price', readonly=True,
                                         help='Total recurring price '
                                              'associated with this '
                                              'subscription analysis.')
    quantity = fields.Float('Quantity', readonly=True,
                            help='The quantity associated with this '
                                 'subscription analysis.')
    user_id = fields.Many2one('res.users', 'Salesperson', readonly=True,
                              help='The salesperson associated with'
                                   ' this record.')
    plan_id = fields.Many2one('subscription.package.plan',
                              'Subscription Template', readonly=True,
                              help='The subscription template '
                                   'associated with this record.')

    def _query(self):
        select_ = """
            SELECT min(sl.id) as id,
                    sl.product_qty as quantity,
                    sub.total_recurring_price as total_recurring_price,
                    sub.user_id as user_id,
                    sub.plan_id as plan_id,
                    sub.name as name
        """
        from_ = """
            subscription_package_product_line sl
                  join subscription_package sub on (sl.subscription_id = sub.id)
        """
        groupby_ = """
            GROUP BY sl.product_qty,
                    sub.total_recurring_price,
                    sub.user_id,
                    sub.plan_id,
                    sub.name
        """
        return '%s FROM ( %s ) %s' % (select_, from_, groupby_)

    def init(self):
        tools.drop_view_if_exists(self.env.cr, self._table)
        self.env.cr.execute("""CREATE or REPLACE VIEW %s as (%s)""" % (
            self._table, self._query()))
