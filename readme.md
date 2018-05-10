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
cp odoorc.example odoorc
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

Run Odoo 11 first time `./odoo/odoo-bin -c odoorc` and access `http://192.168.99.100:9160/web` with credentials `admin/admin`.

### Start developing modules

#### Create module

```
./odoo/odoo-bin scaffold generation /var/www/html/odoo_league/custom_addons/
```

Add `'application' : True` to end of file `/var/www/html/odoo_league/custom_addons/generation/__manifest__.py`

Run `./odoo/odoo-bin -c odoorc -u generation` and go to Admin to install `genration` app

#### Tip and Tricks

* Always check for example at `odoo/addons`

* For override `<models>.create`

```text
@api.model
    def create(self, vals):
        vals['history_ids'] = [(6, 0, [vals.get('club_id')])]
        record = super(Player, self).create(vals)
        return record
```

* For override `<models>.write`

```text
@api.multi
    def write(self, vals):
        vals['history_ids'] = [(4, vals.get('club_id'), 0)]
        super(Player, self).write(vals)
        return True
```

* How to manually fill the `Many2many` fields

```text
(0, 0,  { values }) link to a new record that needs to be created with the given values dictionary

(1, ID, { values }) update the linked record with id = ID (write values on it)

(2, ID) remove and delete the linked record with id = ID (calls unlink on ID, that will delete the object completely, and the link to it as well)

(3, ID) cut the link to the linked record with id = ID (delete the relationship between the two objects but does not delete the target object itself)

(4, ID) link to existing record with id = ID (adds a relationship)

(5) unlink all (like using (3,ID) for all linked records)

(6, 0, [IDs]) replace the list of linked IDs (like using (5) then (4,ID) for each ID
```

