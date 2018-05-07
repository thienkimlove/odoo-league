Odoo Project for League
=======================

### Prepare

```
mkvirtualenv odoo_league
mkdir -p /var/www/html/odoo_league
cd /var/www/html/odoo_league
git clone https://github.com/odoo/odoo.git -b 11.0 --depth=1

# Create project data dir
mkdir -p ~/.local/share/odoo_league

# Create configration file
cp .odoorc.example .odoorc
# Install requirements
pip3 install -r odoo/requirements.txt

# creates a PostgreSQL user
su - postgres
psql
CREATE USER tieungao;
alter user tieungao with encrypted password 'tieungao123';
ALTER USER tieungao WITH SUPERUSER;
\q
exit
```

Make `odoo` directory as source in PyCharm

Run Odoo 11 first time `./odoo/odoo-bin -c .odoorc` and access `http://192.168.99.100:9160/web` with credentials `admin/admin`.

### Start developing modules

#### Create module

```
./odoo/odoo-bin scaffold generation /var/www/html/odoo_league/custom_addons/
```

Add `'application' : True` to end of file `/var/www/html/odoo_league/custom_addons/generation/__manifest__.py`

Run `./odoo/odoo-bin -c .odoorc -u generation` and go to Admin to install `genration` app

