#! /bin/sh
PYTHON=/root/Env/odoo_league/bin/python3
ODOO=/var/www/html/odoo_league/odoo/odoo-bin
CONF=/var/www/html/odoo_league/odoorc

${PYTHON} ${ODOO} -c ${CONF} "$@"