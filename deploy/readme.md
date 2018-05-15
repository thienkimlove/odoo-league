# Deploy

`cd /var/www/html/ && git clone git@github.com:thienkimlove/odoo-league.git odoo_league`

`cd /var/www/html/odoo_league/ && git clone https://github.com/odoo/odoo.git -b 11.0 --depth=1`

`cp odoorc.example odoorc`

`su - postgres`

`psql`

`\list` for database checking

`mkvirtualenv odoo_league`

`pip install -r odoo/requirements.txt`

`pip install -r watchdog`

`pip3 install Babel decorator docutils ebaysdk feedparser gevent greenlet html2text Jinja2 lxml Mako MarkupSafe mock num2words ofxparse passlib Pillow psutil psycogreen psycopg2 pydot pyparsing PyPDF2 pyserial python-dateutil python-openid pytz pyusb PyYAML qrcode reportlab requests six suds-jurko vatnumber vobject Werkzeug XlsxWriter xlwt xlrd`

`npm -v` for checking `npm` is installed.

`sudo npm install -g less less-plugin-clean-css`

`sudo apt-get install node-less`

`sudo wget https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.1/wkhtmltox-0.12.1_linux-trusty-amd64.deb`

`sudo dpkg -i wkhtmltox-0.12.1_linux-trusty-amd64.deb`

`rm -rf wkhtmltox-0.12.1_linux-trusty-amd64.deb`

`sudo cp /usr/local/bin/wkhtmltoimage /usr/bin/wkhtmltoimage`

`sudo cp /usr/local/bin/wkhtmltopdf /usr/bin/wkhtmltopdf`

`find /etc/postgresql -name "pg_hba.conf"` and check if `local` Unix user change from `peer` to `md5`.

`service postgresql restart`

`./odoo/odoo-bin -c odoorc` for checking first time.

`ln -s /var/www/html/odoo_league/deploy/odoo.service /lib/systemd/system/odoo.service`

`chmod +x /var/www/html/odoo_league/deploy/start-odoo`

`systemctl enable odoo.service`

`service odoo start`

`service odoo status` to check

`ln -s /var/www/html/odoo_league/deploy/odoo.antim.vn /etc/nginx/sites-enabled/odoo.antim.vn`

