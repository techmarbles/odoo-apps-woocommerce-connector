# TechMarbles Odoo Apps — WooCommerce Connector

Source repository for [apps.odoo.com](https://apps.odoo.com) submissions.

Each branch targets one Odoo series (`16.0`, `17.0`, `18.0`, `19.0`); the
module `woocommerce_connector/` sits at the branch root, as the store scanner
requires. The module is a store-listing package (manifest + description page);
the sync itself runs in the OdooConnector cloud service and the WordPress
plugin: https://wordpress.org/plugins/erp7-solutions-sync-for-odoo-and-woocommerce
