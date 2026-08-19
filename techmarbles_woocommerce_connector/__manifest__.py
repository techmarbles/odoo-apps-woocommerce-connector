# -*- coding: utf-8 -*-
{
    'name': "WooCommerce Connector",

    'summary': """
        Real-time two-way sync between WooCommerce and Odoo.
        Orders, products, customers, stock, invoices and payments.
    """,

    'description': """
WooCommerce Integration for Odoo
=================================

Connect your WooCommerce store to Odoo with a managed cloud sync service.
No CSV exports, no cron scripts, no server maintenance.

Key Features:
- Real-time two-way order synchronisation
- Product and variant sync, including pricing and images
- Live inventory levels pushed from Odoo to WooCommerce
- Customer records and addresses
- Invoices, payments and refunds
- Taxes, discounts and shipping mapped to the correct Odoo accounts
- Fulfilment and tracking numbers pushed back to WooCommerce
- Automatic retry and replay of failed syncs
- Full audit log of every record synchronised

Compatibility:
- Odoo 16, 17, 18 and 19+
- Automatic protocol selection: XML-RPC on Odoo 16-18, JSON-2 on Odoo 19+
- WooCommerce HPOS (High Performance Order Storage)
- Classic and block checkout

How It Works:
1. Install the free WooCommerce plugin on your WordPress site
2. Connect your Odoo instance
3. Choose what to sync and in which direction
4. Data flows automatically - first sync in minutes

Data Processing Notice:
This connector transmits store and Odoo record data to the OdooConnector
cloud service in order to perform synchronisation. Data is processed only
to provide the sync service. See the privacy policy at
https://odooconnector.cloud for full details.

Support:
support@odooconnector.cloud
Documentation: https://odooconnector.cloud/docs
    """,

    'author': "TechMarbles",
    'website': "https://wordpress.org/plugins/erp7-solutions-sync-for-odoo-and-woocommerce",
    'support': "support@odooconnector.cloud",
    'live_test_url': "https://wordpress.org/plugins/erp7-solutions-sync-for-odoo-and-woocommerce",
    'category': 'Sales/Sales',
    'version': '18.0.1.0.3',

    'depends': ['base', 'stock', 'sale_management', 'account'],

    'data': [],

    'images': ['static/description/banner.png'],

    'license': 'OPL-1',
    'price': 0.0,
    'currency': 'EUR',

    'installable': True,
    'application': True,
    'auto_install': False,
}
