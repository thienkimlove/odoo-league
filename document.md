

<!-- toc -->

- [Attributes](#attributes)
  * [`_name`](#_name)
  * [`_description`](#_description)
  * [`_order`](#_order)
  * [`_rec_name`](#_rec_name)
  * [`_table`](#_table)
  * [`_inherit`](#_inherit)
  * [`_inherits`](#_inherits)
- [Transient and Abstract models](#transient-and-abstract-models)
- [Fields](#fields)
  * [`Char(string)`](#charstring)
  * [`Text(string)`](#textstring)
  * [`Selection(selection, string)`](#selectionselection-string)
  * [`Html(string)`](#htmlstring)
  * [`Integer(string)`](#integerstring)
  * [`Float(string, digits)`](#floatstring-digits)
  * [`Monetary(string, currency_field)`](#monetarystring-currency_field)
  * [`Date(string)` and `Datetime(string)`](#datestring-and-datetimestring)
  * [`Boolean(string)`](#booleanstring)
  * [`Binary(string)`](#binarystring)
  * [`Relation` fields](#relation-fields)
  * [Many-to-many relationships](#many-to-many-relationships)
  * [One-to-Many Relationship](#one-to-many-relationship)
  * [Hierarchical relationships](#hierarchical-relationships)
  * [Dynamic relationships using Reference fields](#dynamic-relationships-using-reference-fields)
  * [`Related fields`](#related-fields)
  * [Model constraints](#model-constraints)
  * [Models inherit](#models-inherit)
- [Special field names](#special-field-names)
  * [`id`](#id)
  * [`create_uid`](#create_uid)
  * [`create_date`](#create_date)
  * [`write_uid`](#write_uid)
  * [`write_date`](#write_date)
  * [`name`](#name)
  * [`active`](#active)
  * [`sequence`](#sequence)
  * [`state`](#state)
  * [`parent_id`, `parent_left`, and `parent_right`](#parent_id-parent_left-and-parent_right)
- [ORM decorators](#orm-decorators)
  * [`@api.multi`](#apimulti)
  * [`@api.one`](#apione)
  * [`@api.model`](#apimodel)
  * [`@api.depends(fld1,...)`](#apidependsfld1)
  * [`@api.constrains(fld1,...)`](#apiconstrainsfld1)
  * [`@api.onchange(fld1,...)`](#apionchangefld1)
- [Field Attributes](#field-attributes)
  * [`string`](#string)
  * [`default`](#default)
  * [`size`](#size)
  * [`translate`](#translate)
  * [`help`](#help)
  * [`readonly=True`](#readonlytrue)
  * [`index=True`](#indextrue)
  * [`copy=False`](#copyfalse)
  * [`groups`](#groups)
  * [`states`](#states)
  * [`deprecated=True`](#deprecatedtrue)
  * [`oldname='field'`](#oldnamefield)
- [Adding/Modify fields to Existed Model](#addingmodify-fields-to-existed-model)
- [Many-to-one relationships](#many-to-one-relationships)
  * [`ondelete`](#ondelete)
  * [`context`](#context)
  * [`domain`](#domain)
  * [`auto_join=True`](#auto_jointrue)
- [Many-to-many relationships](#many-to-many-relationships-1)
- [One-to-Many Relationship](#one-to-many-relationship-1)
- [Hierarchical relationships](#hierarchical-relationships-1)
- [Dynamic relationships using Reference fields](#dynamic-relationships-using-reference-fields-1)
- [Model constraints](#model-constraints-1)
- [Models inherit](#models-inherit-1)
  * [`prototype inheritance`](#prototype-inheritance)
  * [`delegation inheritance`](#delegation-inheritance)
- [Views](#views)
  * [Field Dynamic attributes](#field-dynamic-attributes)
    + [`groups`](#groups-1)
    + [`states`](#states-1)
    + [`attrs`](#attrs)
  * [Field Widgets](#field-widgets)
    + [`email`](#email)
    + [`url`](#url)
    + [`html`](#html)
    + [`handle`](#handle)
    + [`float_time`](#float_time)
    + [`monetary`](#monetary)
    + [`progressbar`](#progressbar)
    + [`many2many_tags`](#many2many_tags)
    + [`selection`](#selection)
    + [`radio`](#radio)
    + [`priority`](#priority)
    + [`state_selection`](#state_selection)
  * [Tree Attributes](#tree-attributes)
    + [`decoration–NAME`](#decoration%E2%80%93name)
    + [`default_order`](#default_order)
    + [`create`, `delete`, and `edit`,](#create-delete-and-edit)
    + [`editable`](#editable)
  * [Buttons](#buttons)
    + [`string`](#string-1)
    + [`type`](#type)
    + [`name`](#name-1)
    + [`args`](#args)
    + [`context`](#context-1)
    + [`confirm`](#confirm)
    + [`special="cancel"`](#specialcancel)
    + [`icon`](#icon)
  * [Smart buttons](#smart-buttons)
    + [`class="oe_stat_button"`](#classoe_stat_button)
    + [`icon`](#icon-1)
    + [`type` and `name`](#type-and-name)
    + [`string`](#string-2)
    + [`context`](#context-2)
    + [`help`](#help-1)
- [ORM built-in methods](#orm-built-in-methods)
  * [Read using `search()` and `browse()`.](#read-using-search-and-browse)
    + [RPC method](#rpc-method)
      - [`read([fields])`](#readfields)
      - [`search_read([domain], [fields], offset=0, limit=None, order=None)`](#search_readdomain-fields-offset0-limitnone-ordernone)
    + [Import and Export method](#import-and-export-method)
      - [`load([fields], [data])`](#loadfields-data)
      - [`export_data([fields], raw_data=False)`](#export_datafields-raw_datafalse)
    + [Methods for the user interface](#methods-for-the-user-interface)
      - [`name_get()`](#name_get)
      - [`name_search(name='', args=None, limit=100)`](#name_searchname-argsnone-limit100)
      - [`name_create(name)`](#name_createname)
      - [`default_get([fields])`](#default_getfields)
      - [`fields_get()`](#fields_get)
      - [`fields_view_get()`](#fields_view_get)
  * [Write](#write)
    + [create](#create)
    + [write](#write)
    + [unlink](#unlink)
  * [Example ORM](#example-orm)
    + [`search_count`](#search_count)
    + [Customize `create` and `write` in models.](#customize-create-and-write-in-models)
    + [Continue..](#continue)

<!-- tocstop -->

### Attributes

#### `_name` 

is the internal identifier for the Odoo model we are creating. 

Mandatory when creating a new model.

#### `_description` 

is a user-friendly title for the model's records, shown when the model is viewed in the user interface. 

Optional but recommended.

#### `_order` 

sets the default order to use when the model's records are browsed, or shown in a list view.

It is a text string to be used as the SQL order by clause, so it can be anything you could use there, although it has smart behavior and supports translatable and many-to-one field names.

#### `_rec_name` 

indicates the field to use as the record description when referenced from related fields, such as a many-to-one relationship.

By default, it uses the name field, which is a common field in models.

But this attribute allows us to use any other field for that purpose.

#### `_table` 

is the name of the database table supporting the model. Usually, it is left to be calculated automatically, and is the model name with the dots replaced by underscores.

But it's possible to set it to indicate a specific table name.

#### `_inherit`

#### `_inherits`

### Transient and Abstract models

`Transient models` are based on the `models.TransientModel` class and are used for wizard-style user interaction.

Their data is still stored in the database, but it is expected to be temporary.

A vacuum job periodically clears old data from these tables. 

For example, the `Load a Language` dialog window, found in the `Settings | Translations` menu, uses a `Transient model` to store user selections and implement wizard logic.

An example of using a Transient model is discussed in Chapter 7, Business Logic - Supporting Business Processes.

`Abstract models` are based on the `models.AbstractModel` class and have no data storage attached to them.

They act as reusable feature sets to be mixed in with other models, using the Odoo inheritance capabilities.

For example, `mail.thread` is an Abstract model provided by the Discuss addon, used to add message and follower features to other models.

This particular example is discussed later in this chapter.

### Fields

#### `Char(string)` 

is a basic string field, presented as a single line. 

The only positional argument expected is the string title.

#### `Text(string)` 

differs from Char in that it can hold multiline text content, but also one positional argument for the string title.

#### `Selection(selection, string)` 

is a drop-down selection list.

The first argument is the list of selectable options and the second is the string title.

The selection item is a list of `('value', 'Title')` tuples, for the value stored in the database and the corresponding user interface description.

When extending through inheritance, the `selection_add` argument is available to append new items to an existing selection list.


#### `Html(string)` 

is stored as a text field, but has specific handling of the user interface for HTML content presentation.

For security reasons, it is sanitized by default, but this behavior can be overridden.

#### `Integer(string)` 

just expects a string argument for the field title.

#### `Float(string, digits)` 

has a second optional argument, an `(x,y)` tuple with the field's precision.

`x` is the total number of digits; of those, `y` are decimal digits.


#### `Monetary(string, currency_field)` 

is similar to a float field, but has specific handling for currency. 

It needs a helper field to set the currency being used.

By default, that field is expected to be named `currency_id`, but it has a different name we can use for the second positional argument to declare it.

#### `Date(string)` and `Datetime(string)` 

fields expect only the string text as a positional argument.

For historical reasons, the ORM handles their values in the UTC timezone represented as a string format. 

Helper functions should be used to convert them to actual date objects.

This is discussed in more detail in Chapter 7, Business Logic - Supporting Business Processes.

#### `Boolean(string)` 

holds `True` or `False` values, as you might expect, and only has one positional argument for the string text.


#### `Binary(string)`
 
stores file-like binary data, and also expects only the string argument.

It can be handled by Python code using base64 encoded strings.

#### `Relation` fields

Example:  `Post` is in `Category` and have many `Tags`

```
category_id = fields.Many2one('generation.category', 'Category')
tag_ids = fields.Many2many('generation.tag', string='Tags')

```
#### [Many-to-many relationships](#many-to-many-relationships) 
####  [One-to-Many Relationship](#one-to-many-relationship) 
####  [Hierarchical relationships](#hierarchical-relationships) 
#### [Dynamic relationships using Reference fields](#dynamic-relationships-using-reference-fields) 


#### `Related fields` 

Instead of  add new field to `post` which change when this parent category name change as below:


```
class Post(models.Model):
    direct_category_name = fields.Char(
        'Direct Category Name',     
        compute='_compute_direct_category_name', 
        store=False, # the default
        search='_search_direct_category_name',
        inverse='_write_direct_category_name')
    
    @api_depends('category_id.name')
    def _compute_direct_category_name(self):
        for post in self:
           post.direct_category_name = post.category_id.name  
           
    def _search_direct_category_name(self, operator, value):
            return [('category_id.name', operator, value)]
    
        def _write_direct_category_name(self):
            for post in self:
                post.direct_category_name = post.category_id.name  

```

We can using : 

```text
class Post(models.Model):
    category_name = fields.Char(
    string='Category Name',
    related='category_id.name')
```

Or 

 ```text
# Related fields:
    category_status = fields.Selection(
        related='category_id.status',
        string='Category Status',
        store=True,  # optional
    )
```

Behind the scenes, `related fields` are just computed fields that conveniently implement `search` and `inverse` methods. 

This means that we can search and write to them out of the box, without having to write any additional code. 

It's also worth noting that these `Related` fields can also be stored in a database, using `store=True`, just like any other computed
field.

#### [Model constraints](#model-constraints)

#### [Models inherit](#models-inherit)

### Special field names

A few field names are reserved for use by the ORM.

#### `id` 

field is an automatic number uniquely identifying each record, and used as the database primary key.

It's automatically added to every model.

The following fields are automatically created on new models, unless the `_log_access=False` model attribute is set:

#### `create_uid` 

is for the user that created the record
#### `create_date` 

is for the date and time when the record is created
#### `write_uid` 

is for the last user to modify the record
#### `write_date` 

is for the last date and time when the record was modified

The information in these fields is available in the web client, in the `Developer Mode` menu, by selecting the `View Metadata` option.

#### `name` 

is used by default as the display name for the record.

Usually, it is a `Char`, but can also be a `Text` or a `Many2one` field type.

We can choose another field to be used for the display name, using the `_rec_name` model attribute.

#### `active`

, of type Boolean, allows us to inactivate records.

Records with `active==False` will automatically be excluded from queries.

To access them, an `('active','=',False)` condition must be added to the search domain, or the `'active_test': False` key should be set on the current context.

#### `sequence`

, of type Integer, if present in a list view, allows us to manually drag records to define the order of the records.

For it to work properly, you should not forget to include it in the model's `_order` attribute.

#### `state`

, of type Selection, represents basic states of the record's life cycle and can be used by the state's field attribute to dynamically modify the view; some form fields can be made `readonly`, `required`, or `invisible` in specific record states.

#### `parent_id`, `parent_left`, and `parent_right`

, of type Integer, have special meaning for parent/child hierarchical relations.
We will discuss them in detail later in this chapter.
    
### ORM decorators

Allow us to add certain features to our models, such as implementing validations and automatic computations.

If no decorator is used on a model method, it will default to `@api.multi` behavior.

#### `@api.multi` 

We want a custom method to perform some actions on a recordset. For this, we should use `@api.multi`, and in that case, the self argument will be the recordset to work with. 

The method's logic will usually include a `for` loop iterating on it. 

This is surely the most frequently used decorator.

#### `@api.one` 

The method is prepared to work with a single record (a singleton).

Because it would be deprecated and may be removed in the future so we using `@api.multi` with `self.ensure_one()`.

to ensure it is a singleton as expected.

Example 

```text
@api.multi
    def do_populate_tasks(self):
        self.ensure_one()
        Task = self.env['todo.task']
        all_tasks = Task.search([('is_done', '=', False)])
        # Fill the wizard Task list with all tasks
        self.task_ids = all_tasks
        # reopen wizard form on same wizard record
        return self._reopen_form()
```

#### `@api.model`

In some cases, the method is expected to work at the class level, and not on particular records. 

In some object-oriented languages this would be called a static method. 

These class-level static methods should be decorated with `@api.model`. 

In these cases, `self` should be used as a reference for the model, without expecting it to contain actual records.

Example

```text
@api.model
    def default_get(self, field_names):
        defaults = super(
            TodoWizard, self).default_get(field_names)
        defaults['task_ids'] = self.env.context['active_ids']
        return defaults
```

Methods decorated with `@api.model` cannot be used with user interface buttons. 

In those cases, `@api.multi` should be used instead.

Mostly, method with `@api.model` using for another model calling to.

Example in one class `SupplierModel` we have

```text
@api.model
 def upsert_supplier(self, supplier_info, address_info, account_info, msg_id):
  
```

In Class `Expert` we call `self.env['generation.supplier'].upsert_supplier`.


#### `@api.depends(fld1,...)` 

is used for computed field functions, to identify on what changes the (re)calculation should be triggered. 

It must set values on the computed fields, otherwise it will error.

Example


```text
@api.depends('category_id.name')
    def _compute_direct_category_name(self):
        for post in self:
            post.category_name = post.category_id.name
```

#### `@api.constrains(fld1,...)` 

is used for validation functions, and performs checks for when any of the mentioned fields are changed. 

It should not write changes in the data. 

If the checks fail, an exception should be raised.   

Example

```text
 @api.constrains('name')
    def _check_name_size(self):
        for todo in self:
            if len(todo.name) < 5:
                raise ValidationError('Title must have 5 chars!')
                
``` 

#### `@api.onchange(fld1,...)` 

is used in the user interface, to automatically change some field values when other fields are changed. 

The self argument is a singleton with the current form data, and the method should set values on it for the changes that should happen in the form.


It doesn't actually write to database records, instead it provides information to change the data in the UI form.

Example 

```text
@api.onchange('user_id')
    def onchange_user_id(self):
        if not self.user_id:
            self.team_ids = None
            return {
                'warning': {
                    'title': 'Responsible User Reset',
                    'message': 'Please choose a new Team.',
                }
            }
            
```


Here, we are using the `@api.onchange` decorator to attach some logic to any changes in the `user_id` field, when done through the user interface. 

Note that the actual method name is not relevant, but the convention is for its name to begin with `onchange_`.

Inside an `onchange` method, `self` represents a single virtual record containing all the fields currently set in the record being edited, and we can interact with them. 

Most of the time, this is what we want to do: to automatically fill values in other fields, depending on the value set to the changed field. 

In this case, we are setting the `team_ids` field to an empty value base on change from `user_id` field.

The `onchange` methods don't need to return anything, but they can return a dictionary containing a `warning` or a `domain` key:

The `warning` key should describe a message to show in a dialogue window, such as: `{'title': 'Message Title', 'message': 'Message Body'}`.

The `domain` key can set or change the domain attribute of other fields. 

This allows you to build more user-friendly interfaces, by having to-many fields list only the selection option that make sense for this case. 

The value for the domain key looks like this: `{'team_ids': [('is_author', '=', True)]}`



When using the preceding decorators, no return value is needed. Except for `onchange` methods that can optionally return a dict with a warning message to display in the user
interface.


### Field Attributes

#### `string` 

is the field default label, to be used in the user interface.

Except for `Selection` and `Relational` fields, it is the first positional argument, so most of the time it is not used as a keyword argument.

If not provided, it is automatically generated from the field name.

#### `default` 

sets a default value for the field.

It can be a static value, such as a string,  or a callable reference, either a named function or an anonymous function (a lambda expression).

In the stage model,  we can see an example of a default value on the `date_created` field that uses a lambda expression to set the current date  and time when a new record is created.

#### `size` 

applies only to `Char` fields, and can set a maximum size allowed.

It's  recommended to not use it unless there is a business requirement for it, for example, a social security number with a maximum length allowed.

#### `translate` 

applies only to `Char`, `Text`, and `Html` fields, and makes the field contents translatable, holding different values for different languages.

#### `help` 

provides the text for tooltips displayed to users.

#### `readonly=True` 

makes the field not editable in the user interface by default.

This is not enforced at the API level; code in model methods will still be capable of writing to it.

It is only a user interface setting.

####`required=True` 

makes the field mandatory in the user interface by default.

This is enforced at the database level by adding a `NOT NULL` constraint on the column.

#### `index=True` 


adds a database index on the field, for faster search operations at the expense of slower write operations.

#### `copy=False` 


has the field ignored when using the duplicate record feature - the `copy()` ORM method.

The non-relational fields are copyable by default.

#### `groups` 

allows limiting the field's access and visibility to only some groups.

It expects a comma-separated list of XML IDs for security groups, such as `groups='base.group_user,base.group_system'`.

#### `states` 

expects dictionary mapping values for UI attributes depending on values of the state field.

The attributes that can be used are `readonly`, `required`, and  `invisible`, for example: `states={'done':[('readonly',True)]}`.

Note that the states field attribute is equivalent to the `attrs` attribute in views.

Example

```
<field name="state" invisible="True" />

<button name="do_clear_done"
        type="object"
        string="Clear Done"
        attrs="{'invisible':[('state', 'in', ['draft'])]}"
        class="oe_highlight" />
```

In this example

```
The Fields used in a domain or attrs expression must be loaded into the
view, and there must be a <field> element for them.

If the field is not supposed to be seen by the users, we then have them loaded with an invisible field element.
```

Note : views support a `states` attribute, but it has a different usage: it accepts a comma-separated list of states to control when the element should be visible

#### `deprecated=True` 

logs a warning whenever the field is being used

#### `oldname='field'` 

is used when a field is renamed in a newer version, enabling the data in the old field to be automatically copied into the new field.

### Adding/Modify fields to Existed Model

```
class TodoTask(models.Model):
    _name = 'todo.task'
    _inherit = ['todo.task', 'mail.thread']

    name = fields.Char(help="What needs to be done?") # modify
    effort_estimate = fields.Integer() # add
```

### Many-to-one relationships

Example:  `Post` is in `Category` and have many `Tags`

```
category_id = fields.Many2one('generation.category', 'Category')
tag_ids = fields.Many2many('generation.tag', string='Tags')

```
The `Many2one` relationship accepts two positional arguments: the `related model` (corresponding to the comodel keyword argument) and the `title` string.

It creates a field in the database table with a foreign key to the related table.

Some additional named arguments are also available to use with this type of field:

#### `ondelete` 

defines what happens when the related record is deleted.

Its default is `set null`, meaning that an empty value is set when the related record is deleted.

Other possible values are `restricted`, raising an error preventing the deletion, and `cascade`, which also deletes this record.


#### `context` 

is a dictionary of data, meaningful for the web client views, to carry information when navigating through the relationship, for example, to set default
values.

It will be better explained in Chapter 7, Business Logic - Supporting business processes.

#### `domain` 

is a domain expression; a list of tuples used to filter the records made available for selection on the relation field.

See Chapter 7, Business Logic Supporting Business Processes for more details.

#### `auto_join=True` 

allows the ORM to use SQL joins when doing searches using this relationship.

If used, the access security rules will be bypassed, and the user could have access to related records the security rules wouldn't allow, but the SQL queries will be more efficient and run faster.

### Many-to-many relationships

Example:  `Post` have many `Tags`

```
tag_ids = fields.Many2many('generation.tag', string='Tags')
```

The `Many2many` minimal signature accepts one argument for the related model, and it is recommended to also provide the string argument with the field title.

At the database level, it does not add any columns to the existing tables. 

Instead, it automatically creates a new relationship table that has only two ID fields with foreign keys to the related tables. 

If not provided, the relationship table name and the field names are
automatically generated. 

By default, the relationship table name is the two table names joined with an underscore and `_rel` appended at the end.

We can customize as below

```
# Post <-> Tag relation (positional args)
tag_ids = fields.Many2many(
    'generation.post', # related model
    'generation_post_tag_rel', # relation table name
    'post_id', # field for "this" record
    'tag_id', # field for "other" record
    'Tags') # string label text

```
Just like `many-to-one` fields, `many-to-many` fields also support the `domain` and `context` keyword attributes.

There is a limitation in the ORM design regarding `Abstract models`. 

When you force the names of the relationship table and columns, they cannot be cleanly inherited anymore. 

So this should not be done in `Abstract models`.

The inverse of the Many2many relationship is also a Many2many field. 

If we also add a Many2many field to the `Tags` model, Odoo infers that this many-to-many relationship is the inverse of the one in the `Post` model.


`post_ids = fields.Many2many(
        'generation.post',
        string='Posts')
        `


### One-to-Many Relationship

An inverse of a `Many2one` can be added to the other end of the relationship. 

This has no impact on the actual database structure, but allows us to easily browse from the one side of the many related records. 

A typical use case is the relationship between a document header
and its lines.

```
# One2many inverse relation:
class Category(models.Models):
    post_ids = fields.One2many(
        'generation.posts',
        'category_id',
        'Posts in this category')
```

One2many accepts three positional arguments: the `related model`, the `field name` in that model referring to this record, and the title string. 

The first two positional arguments correspond to the `comodel_name` and `inverse_name` keyword arguments.

The additional keyword parameters available are the same as for Many2one: `context`, `domain`, and `ondelete` (here acting on the many side of the relationship).


### Hierarchical relationships

```class GenerationCategory(models.Model):
    # Hierarchic relationships:
    _parent_store = True
    _parent_name = 'parent_id'  # the default
    
     parent_id = fields.Many2one(
            'generation.category',
            'Parent Category',
            ondelete='restrict')
        parent_left = fields.Integer('Parent Left', index=True)
        parent_right = fields.Integer('Parent Right', index=True)
        child_ids = fields.One2many(
            'generation.category',
            'parent_id',
            'Child Category')
```

### Dynamic relationships using Reference fields

Regular relational fields reference one fixed `comodel`. 

The `Reference` field type does not have this limitation and supports dynamic relationships, so that the same field is able to
refer to more than one model.

For example, we can use it to add a `Refers` to field to To-Do tasks that can either refer to a `User` or a `Partner`:

```text

 # Dynamic Reference fields:
    refers_to = fields.Reference(
        # Set a Selection list, such as:
        # [('res.user', 'User'), ('res.partner', 'Partner')],
        # Or use standard "Referencable Models":
        referenceable_models,
        'Refers to',  # string= (title)
    )

```

### Model constraints

To enforce data integrity, models also support two types of constraints: SQL and Python.

A common use case is to add unique constraints to models. 

Suppose we don't want to allow two active tasks with the same title, as follows:

```text
 _sql_constraints = [(
        'generation_post_name_unique',
        'UNIQUE (name, active)',
        'Post title must be unique!'
    )]
```

```text
 # Chapter 04 - ORM Constraints
    @api.constrains('name')
    def _check_name_size(self):
        for todo in self:
            if len(todo.name) < 5:
                raise ValidationError('Title must have 5 chars!')
                
```

### Models inherit

#### `prototype inheritance` 

If `_inherit` without `_name`. It will add to existed model.


If, along with `_inherit`, we also use the `_name` attribute with a value different from the parent model, we get a new model reusing the features from the inherited one, with its own database table and data. 

Here, you take a model and create a brand new one that is a copy of the original one. 

As you add new features to it, they will be added only to the new model, and the original model isn't changed.

Example `we can use this to add messaging features to our Posts`. 

Must add in `__manifest__.py` :      

```text
class TodoTask(models.Model):
    _name = 'todo.task'
    _inherit = ['todo.task', 'mail.thread']
```
Copying means that the inherited methods and fields will also be available in the inheriting
model. 

The inherited fields will be created and stored in the target model's database tables.


The data records of the original (inherited) and the new (inheriting) models are kept
unrelated. Only the definitions are shared.

In practice, this type of inheritance is usually used with abstract mixin classes. It is rarely
used to inherit from regular models because it duplicates data structures.

#### `delegation inheritance`

by using the `_inherits` attribute. It allows us to create a new model that contains and extends an existing model.


When a new record is created for the new model, a new record in the original model is also created and linked, using a `many-to-one` field. 

Observers of the new model see all the fields, both from the original and new models, although behind the scenes each model handles its
own data.

Example

```text
from odoo import fields, models
class User(models.Model):
_name = 'res.users'
_inherits = {'res.partner': 'partner_id')
partner_id = fields.Many2one('res.partner')
```
With `delegation inheritance`, the `res.users` model embeds the inherited model, `res.partner`, so that when a new User class is created, a partner is also created and a reference to it is kept in the `partner_id` field of the User class.
 
 It has some similarities with the polymorphism concept in object-oriented programming.
  
Through the delegation mechanism, all fields from the inherited model and partner are available as if they were User fields.
 
 For example, the partner name and address fields are exposed as User fields, but in fact they are being stored in the linked partner model and no data duplication occurs.
 
 The advantage of this, compared to prototype inheritance, is that there is no need to repeat data structures, such as addresses, across several tables. 
 
 Any new model that needs to include an address can delegate that to an embedded partner model.
  
 If modifications are introduced in partner address fields, these are immediately available to all the models embedding them!
 
 Note that with delegation inheritance, fields are inherited but methods are not.

### Views

#### Field Dynamic attributes
Some attributes allow us to dynamically change the display of view elements, depending on
the record's values.

##### `groups` 
can make an element visible depending on the security groups the current user belongs to. 

Only the members of the specified groups will see it. It expects a comma-separated list of Group XML IDs.

##### `states` 

can make an element visible depending on the record's State field. It expects a comma-separated list of State values, and only works on models with an actual state field.

##### `attrs` 
special attribute, expecting as a value a dictionary that maps the value of the invisible attribute to the result of an expression.

For example, to have the `date_deadline` field visible in all states except `draft`, use the
following code:

`<field name="date_deadline" attrs="{'invisible':[('state', '=', ['draft'])]}"/>`

* `invisible` 
attribute is available in any element, not only fields. 
For example, we can use it on notebook pages and in `group` elements.

* `readonly` and `required`. 
These only make sense for data fields to make them not editable or mandatory. This allows us to implement some basic client-side logic, such as making a field mandatory depending on other record values, such as the State.

#### Field Widgets
For text fields, we have the following widgets:

##### `email` 
is used to make the email text an actionable "mail-to" address.
##### `url` 
is used to format the text as a clickable URL.
##### `html` 
is used to render the text as HTML content; in edit mode, it features a WYSIWYG editor to allow for the formatting of the content without the need for using the HTML syntax.

For numeric fields, we have the following widgets :

##### `handle` 
is specifically designed for sequence fields in list views and displays a handle that allows you to drag lines to a custom order.
##### `float_time`
formats a float field with time quantities as hours and minutes.
##### `monetary`
displays a float field as the currency amount. 
It expects a `currency_id` companion field, but another field name can be provided with `options="{'currency_field': 'currency_id'}"`.
##### `progressbar`
presents a float as a progress percentage and can be useful for fields representing a completion rate.

For relational and selection fields, we have these additional widgets:

##### `many2many_tags`
displays values as a list of button-like labels.

##### `selection`
uses the selection field widget for a many-to-one field.

##### `radio`
displays the selection field options using radio buttons.

##### `priority`
represents the selection field as a list of clickable stars. The selection options are usually numeric digits.

##### `state_selection`
shows a semaphore light for the kanban state selection list.
The normal state is represented in gray, done is represented in green, and any other state is represented in red.

The `state_selection` widget was introduced in Odoo 11, and replaces
the former `kanban_state_selection`. The later one is deprecated, but for backward compatibility it is still supported.

#### Tree Attributes

##### `decoration–NAME`

The row text color and font can change dynamically depending on the results of a Python
expression evaluation.

The `NAME` part can be `bf` or `it`, for bold and italic fonts, or any Bootstrap text contextual colors: `danger`, `info`, `muted`, `primary`, `success`, or `warning`. The Bootstrap  documentation has examples of how these are presented: `http://getbootstrap.com/css/#helper-classes-colors`.

Remember that fields used in expressions must be declared in a `<field>` element, so that
the web client knows that that column needs to be retrieved from the server. 
If we don't want to have it displayed to the user, we should use the `invisible="1"` attribute on it.

In this example below we using expression from field `state` so this field must be present on views but invisible.

```textmate
<tree decoration-muted="is_done"
      decoration-bf="state=='open'"
      delete="false">
      <field name="name"/>
      <field name="user_id"/>
      <field name="is_done"/>
      <field name="state" invisible="1"/>
    </tree>
```

Other relevant attributes of the tree element are:

##### `default_order` 
allows us to override the model's default `sort` order, and its value follows the same format as an order attribute used in model definitions.

##### `create`, `delete`, and `edit`,
if set to `false` (in lowercase), disable the corresponding action on the list view.

##### `editable`
makes records editable directly on the list view. 

Possible values are `top` and `bottom`, the location where the new records will be added.

A list view can contain fields and buttons, and most of their attributes for forms are also
valid here.


#### Buttons

Buttons support these attributes:

##### `string`
is the button text label, or the HTML alt text when an icon is used.
##### `type`
is the type of the action to perform. Possible values are:
* `object` is used for calling a Python method 
* `action` is used to run a window action 

##### `name` 
identifies the specific action to perform, according to the chosen type: either a model method name or the database ID of window action to run. 

The `%(xmlid)d` formula can be used to translate the XML ID into the required Database ID when the view is being loaded.

##### `args` 
is used when the `type` is `object`, to pass additional parameters to the method, which must be purely static JSON parameters appended to the record ID to form the arguments of the method call.

##### `context`
adds values to the context, which can have an effect after the windows action is run, or in the Python code methods called.

##### `confirm`
displays a confirmation message box before running the related action, displaying the text assigned to this attribute.

##### `special="cancel"`
is used on wizard form, to add a Cancel button.

##### `icon`
is for the icon image to be shown in the button. The icons available are from the Font Awesome set and should be specified using the corresponding CSS class, such as `icon="fa-question"`. For more information, refer to `http://fontawesome.io`.

#### Smart buttons

When designing the form structure, we included a top-right area to contain smart buttons.

Let's now add a button inside it.

Example : button displaying the total number of To-Do tasks for the  owner of the current To-Do task, and clicking on it will navigate to the list of those items.

In views we have code

```text
<sheet>
        <!-- To add form content -->
        <div name="button_box" class="oe_button_box">
          <!-- Smart buttons will go here... -->
            <div name="button_box" class="oe_button_box">
            <button class="oe_stat_button"
                type="action" icon="fa-tasks"
                name="%(action_todo_task_button)d"
                context="{'default_user_id': user_id}"
                help="All to-dos for this user" >
                <field string="To-Dos" name="user_todo_count"
                widget="statinfo"/>
            </button>
            </div>
        </div>
```

In models, we have code 

```text
# Ch09 Views - Smart Buttons
    def _compute_user_todo_count(self):
        for task in self:
            task.user_todo_count = task.search_count(
                [('user_id', '=', task.user_id.id)])

    user_todo_count = fields.Integer(
        'User To-Do Count',
        compute='_compute_user_todo_count')
```
This button displays the total number of To-Do Tasks for the person responsible for this To-Do task, computed by the `user_todo_count` field.


The button element above itself is a container, with fields displaying statistics. 
These statistics are regular fields using the widget `statinfo`. 
The field is usually a computed field defined in the underlying model. 

Other than fields, inside a button we can also use static text, such as `<div>User's To-dos</div>`.

When clicking on the button,we want to see a list with only the Tasks for the current
responsible user. 
For that, we use the button's context attribute to store that value.

That will be done via the `action_todo_task_button` action. But it needs to know the current responsible user to be able to perform the filtering. 

The Action used must be defined before the Form, so we should add it at the top of the
XML file:

```textmate
<act_window id="action_todo_task_button"
  name="To-Do Tasks"
  res_model="todo.task"
  view_mode="tree,form,calendar,graph,pivot"
  domain="[('user_id','=',default_user_id)]" />  
```

Notice how we use the `default_user_id` context key for the domain filter. This particular key will also set the default value on the `user_id` field when creating new Tasks after following the button link.



These are the attributes that we can use when adding smart buttons:

##### `class="oe_stat_button"`
renders a rectangle instead of a regular button.

##### `icon`
sets the icon to use, chosen from the Font Awesome set. Visit `http://fontawesome.io` to browse the available icons.

##### `type` and `name`
are the button type and the name of the action to trigger. 
For smart buttons, the type will usually be action for a window action, and name will be the ID of the action to execute.
 It expects an actual database ID, so we have to use a formula to convert an XML ID into a database ID: "`%(actionxmlid)d`". 
 This action should open a view with the related records.
 
##### `string`
adds label text to the button. 
We have not used it here because the contained field already provides a text for it.

##### `context` 
should be used to set default values on the target view, to be used on new records created on the view after clicking on the button.

##### `help`
adds a help tooltip displayed when the mouse pointer is over the button.


### ORM built-in methods

Basic methods provided by the ORM, used mainly to perform CRUD(create, read, update and delete) operations on our model data.

#### Read using `search()` and `browse()`.

##### RPC method
    
###### `read([fields])` 

is similar to the `browse` method, but, instead of a recordset, it returns a list of rows of data with the fields given as its argument. 
    
Each row is a dictionary. 

It provides a serialized representation of the data that can be sent through RPC protocols and is intended to be used by client programs and not in server logic.
    
###### `search_read([domain], [fields], offset=0, limit=None, order=None)` 

performs a search operation followed by a read on the resulting record list. 
    
It is intended to be used by RPC clients and saves them the extra round trip needed when doing a search followed by a read on the results.

##### Import and Export method    
    
###### `load([fields], [data])` 

is used to import data acquired from a CSV file. 
    
The first argument is the list of fields to import, and it maps directly to a CSV top row.

The second argument is a list of records, where each record is a list of string values to parse and import, and it maps directly to the CSV data rows and columns.
     
It implements the features of CSV data import, such as the external identifiers support. 
 
It is used by the web client `Import` feature.
     
###### `export_data([fields], raw_data=False)` 

is used by the web client Export function. 
    
It returns a dictionary with a data key containing the data: a list of rows.

The field names can use the `.id` and `/id` suffixes used in CSV files, and the data is in a format compatible with an importable CSV file.

The optional `raw_data` argument allows for data values to be exported with their Python types, instead
of the string representation used in CSV.

##### Methods for the user interface

###### `name_get()` 

returns a list of (ID, name) tuples with the text representing each record. 
    
It is used by default for computing the `display_name` value, providing the text representation of relation fields. 
    
It can be extended to implement custom display representations, such as displaying the record code and name instead of only the name.
    
###### `name_search(name='', args=None, limit=100)` 

returns a list of `(ID, name)` tuples, where the display name matches the text in the `name` argument. 
    
It is used in the UI while typing in a relation field to produce the list with the suggested records matching the typed text. 

For example, it is used to implement product lookup both by name and by reference, while typing in a field to pick a product.
    
###### `name_create(name)` 

creates a new record with only the title name to use for it.
    
It is used in the UI for the "quick-create" feature, where you can quickly create a related record by just providing its name. 

It can be extended to provide specific defaults for the new records created through this feature.
    
###### `default_get([fields])` 

returns a dictionary with the default values for a new record to be created. 
    
The default values may depend on variables such as the current user or the session context.
    
###### `fields_get()` 

is used to describe the model's field definitions, as seen in the `View Fields` option of the developer menu.
    
###### `fields_view_get()` 

is used by the web client to retrieve the structure of the UI view to render. 
    
It can be given the ID of the view as an argument or the type of view we want using `view_type='form'`.
 
For example, you may try this:  `self.fields_view_get(view_type='tree')`. 
 
#### Write

The ORM provides three methods for the three basic write operations:

##### create
 
 `<Model>.create(values)` creates a new record on the model. Returns the created record.
    
##### write

`<Recordset>.write(values)` updates field values on the recordset. Returns nothing.
    
##### unlink

`<Recordset>.unlink()` deletes the records from the database. Returns nothing.

The `values` argument is a dictionary, mapping field names to values to write.

In some cases, we need to extend these methods to add some business logic to be triggered whenever these actions are executed. 

By placing our logic in the appropriate section of the custom method, we can have the code run before or after the main operations are executed.

```text
@api.model
    def create(self, vals):
        # Code before create: should use the `vals` dict
        new_record = super(TodoTask, self).create(vals)
        # Code after create: can use the `new_record` created
        return new_record
```

A custom `write()` would follow this structure:

```text
@api.multi
def write(self, vals): 
    #can use `self`, with the old values
    super(TodoTask, self).write(vals)
    # Code after write: can use `self`, with the updated values
    return True
```
While extending `create()` and `write()` opens up a lot of possibilities, remember in many
cases we don't need to do that, since there are tools also available that may be better suited:

For field values that are automatically calculated based on other fields, we should use computed fields. 

An example of this is to calculate a header total when the values of the lines are changed.

- To have field default values calculated dynamically, we can use a field default bound to a function instead of a fixed value.

- To have values set on other fields when a field is changed, we can use `onchange` functions.

An example of this is when picking a customer, setting their currency as the document's currency that can later be manually changed by the user. 
Keep in mind that `onchange` only works on form view interaction and not on direct write calls.

- For validations, we should use constraint functions decorated with `@api.constraints(fld1,fld2,...)`. 

These are like computed fields but, instead of computing values, they are expected to raise errors.

Consider carefully if you really need to use extensions to the `create` or `write` methods.

In most cases, we just need to perform some validation or automatically compute some value, when the record is saved. 

But we have better tools for this: validations are best implemented with `@api.constrains` methods, and automatic calculations are better implemented as computed fields. 

In this case, we need to compute field values when saving.

If, for some reason, computed fields are not a valid solution, the best approach is to have our logic at the top of the method, accumulating the changes needed into the `vals` dictionary that will be passed to the final `super()` call.


For the `write()` method, having further write operations on the same model will lead to a recursion loop and end with an error when the worker process resources are exhausted.

Please consider if this is really needed. 

If it is, a technique to avoid the recursion loop is to set a flag in the context. 

For example, we could add code such as the following:

```text
if not self.env.context.get('todo_task_writing'):
    self.with_context(todo_task_writing=True).write(some_values)
```
    
With this technique, our specific logic is guarded by an `if` statement, and runs only if a specific marker is not found in the context. 

Furthermore, our `self.write()` operations should use `with_context` to set that marker. 

This combination ensures that the custom login inside the `if` statement runs only once, and is not triggered on further `write()` calls, avoiding the infinite loop.

#### Example ORM


##### `search_count`

return total.

```textmate
def _compute_user_todo_count(self):
        for task in self:
            task.user_todo_count = task.search_count(
                [('user_id', '=', task.user_id.id)])

    user_todo_count = fields.Integer(
        'User To-Do Count',
        compute='_compute_user_todo_count')
```

##### Customize `create` and `write` in models.

```textmate
    @api.model
    def create(self, vals):
        vals['history_ids'] = [(6, 0, [vals.get('club_id')])]
        record = super(Player, self).create(vals)
        return record

    @api.multi
    def write(self, vals):
        vals['history_ids'] = [(4, vals.get('club_id'), 0)]
        super(Player, self).write(vals)
        return True
```
##### Continue..



