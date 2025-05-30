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
from odoo import api, fields, models


class SubscriptionPackagePlan(models.Model):
    _name = 'subscription.package.plan'
    _description = 'Subscription Package Plan'

    name = fields.Char(string='Plan Name', required=True,
                       help='The name of the subscription plan.')
    renewal_value = fields.Char(string='Renewal',
                                help='A descriptive value indicating the '
                                     'renewal status or details for the '
                                     'subscription plan.')
    renewal_period = fields.Selection([('days', 'Day(s)'),
                                       ('weeks', 'Week(s)'),
                                       ('months', 'Month(s)'),
                                       ('years', 'Year(s)')],
                                      default='months',
                                      help='Select the unit of time for the '
                                           'renewal period of the '
                                           'subscription plan.')
    renewal_time = fields.Integer(string='Renewal Time Interval',
                                  compute='_compute_renewal_time',
                                  store=True,
                                  help='The computed renewal time interval '
                                       'for the subscription plan, based on '
                                       'the selected renewal period.')
    limit_choice = fields.Selection([('ones', 'Ones'),
                                     ('manual', 'Until Closed Manually'),
                                     ('custom', 'Custom')],
                                    default='ones',
                                    help='Select the limit choice for the '
                                         'subscription plan, specifying how '
                                         'long it will be active.')
    limit_count = fields.Integer(string='Custom Renewal Limit',
                                 help='Specify the custom renewal limit for '
                                      'the subscription plan. This field is '
                                      'relevant when the "Limit Choice" is '
                                      'set to "Custom".')
    days_to_end = fields.Integer(string='Days End', readonly=True,
                                 compute='_compute_days_to_end', store=True,
                                 help="Subscription ending date")
    invoice_mode = fields.Selection([('manual', 'Manually'),
                                     ('draft_invoice', 'Draft')],
                                    default='draft_invoice',
                                    help='Select the invoice mode for the '
                                         'subscription plan, specifying '
                                         'whether invoices are generated '
                                         'manually or in draft state.')
    journal_id = fields.Many2one('account.journal', string='Journal',
                                 domain="[('type', '=', 'sale')]")
    company_id = fields.Many2one('res.company', string='Company', store=True,
                                 default=lambda self: self.env.company)
    short_code = fields.Char(string='Short Code')
    terms_and_conditions = fields.Text(string='Terms and Conditions')
    product_count = fields.Integer(string='Products',
                                   compute='_compute_product_count')
    subscription_count = fields.Integer(string='Subscriptions',
                                        compute='_compute_subscription_count')

    @api.depends('product_count')
    def _compute_product_count(self):
        """ Calculate product count based on subscription plan """
        self.product_count = self.env['product.product'].search_count(
            [('subscription_plan_id', '=', self.id)])

    @api.depends('subscription_count')
    def _compute_subscription_count(self):
        """ Calculate subscription count based on subscription plan """
        self.subscription_count = self.env[
            'subscription.package'].search_count([('plan_id', '=', self.id)])

    @api.depends('renewal_value', 'renewal_period')
    def _compute_renewal_time(self):
        """ This method calculate renewal time based on renewal value """
        for rec in self:
            if int(rec.renewal_value) == 0 or int(rec.renewal_value) < 0:
                rec.renewal_value = 1
            if rec.renewal_period == 'days':
                rec.renewal_time = int(rec.renewal_value)
            elif rec.renewal_period == 'weeks':
                rec.renewal_time = int(rec.renewal_value) * 7
            elif rec.renewal_period == 'months':
                rec.renewal_time = int(rec.renewal_value) * 28
            elif rec.renewal_period == 'years':
                rec.renewal_time = int(rec.renewal_value) * 364
            if rec.name:
                rec.short_code = str(rec.name[0:3]).upper()

    @api.depends('renewal_time', 'limit_count')
    def _compute_days_to_end(self):
        """ This method calculate days to end for subscription plan based on
        limit count """
        for rec in self:
            if rec.limit_count == 0 or rec.limit_count < 0:
                rec.limit_count = 1
            if rec.limit_choice == 'ones':
                rec.days_to_end = rec.renewal_time
            if rec.limit_choice == 'manual':
                rec.days_to_end = False
            if rec.limit_choice == 'custom':
                rec.days_to_end = rec.renewal_time * rec.limit_count

    def button_product_count(self):
        """ It displays products based on subscription plan """
        return {
            'name': 'Products',
            'res_model': 'product.product',
            'domain': [('subscription_plan_id', '=', self.id)],
            'view_type': 'form',
            'view_mode': 'list,form',
            'type': 'ir.actions.act_window',
            'context': {
                'default_is_subscription': True,
            },
        }

    def button_sub_count(self):
        """ It displays subscriptions based on subscription plan """
        return {
            'name': 'Subscriptions',
            'domain': [('plan_id', '=', self.id)],
            'view_type': 'form',
            'res_model': 'subscription.package',
            'view_mode': 'list,form',
            'type': 'ir.actions.act_window',
        }

    def name_get(self):
        """ It displays record name as combination of short code and
        plan name """
        res = []
        for rec in self:
            res.append((rec.id, '%s - %s' % (rec.short_code, rec.name)))
        return res
