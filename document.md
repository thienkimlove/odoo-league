### Models

#### Attributes

* `_name` is the internal identifier for the Odoo model we are creating. Mandatory
when creating a new model.

* `_description` is a user-friendly title for the model's records, shown when the
model is viewed in the user interface. Optional but recommended.

* `_order` sets the default order to use when the model's records are browsed, or shown in a list view.

    It is a text string to be used as the SQL order by clause, so
it can be anything you could use there, although it has smart behavior and supports translatable and many-to-one field names.

* `_rec_name` indicates the field to use as the record description when referenced from related fields, such as a many-to-one relationship.

    By default, it uses the name field, which is a common field in models.

    But this attribute allows us to use any other field for that purpose.

* `_table` is the name of the database table supporting the model. Usually, it is left to be calculated automatically, and is the model name with the dots replaced by underscores.

    But it's possible to set it to indicate a specific table name.

* `_inherit`

* `_inherits`

#### Transient and Abstract models

`Transient models` are based on the `models.TransientModel` class and are used for wizard-style user interaction.

Their data is still stored in the database, but it is expected to
be temporary.

A vacuum job periodically clears old data from these tables. For example, the `Load a Language` dialog window, found in the `Settings | Translations` menu, uses a `Transient model` to store user selections and implement wizard logic.

An example of using a Transient model is discussed in Chapter 7, Business Logic - Supporting Business Processes.

`Abstract models` are based on the `models.AbstractModel` class and have no data storage attached to them.

They act as reusable feature sets to be mixed in with other models, using the Odoo inheritance capabilities.

For example, `mail.thread` is an Abstract model provided by
the Discuss addon, used to add message and follower features to other
models.

This particular example is discussed later in this chapter.

#### Fields

* `Char(string)` is a basic string field, presented as a single line. The only positional argument expected is the string title.

* `Text(string)` differs from Char in that it can hold multiline text content, but also one positional argument for the string title.

* `Selection(selection, string)` is a drop-down selection list.

    The first argument is the list of selectable options and the second is the string title.

    The selection item is a list of `('value', 'Title')` tuples, for the value stored in the database and the corresponding user interface description.

    When extending through inheritance, the `selection_add` argument is available to append new items to an existing selection list.


* `Html(string)` is stored as a text field, but has specific handling of the user interface for HTML content presentation.

    For security reasons, it is sanitized by default, but this behavior can be overridden.

* `Integer(string)` just expects a string argument for the field title.

* `Float(string, digits)` has a second optional argument, an `(x,y)` tuple with the field's precision.

    `x` is the total number of digits; of those, `y` are decimal digits.


* `Monetary(string, currency_field)` is similar to a float field, but has specific handling for currency. It needs a helper field to
set the currency being used.

    By default, that field is expected to be named `currency_id`, but it has a different name we can use for the second positional argument to declare it.

* `Date(string)` and `Datetime(string)` fields expect only the string text as a positional argument.

    For historical reasons, the ORM handles their values in the UTC timezone represented as a string format. Helper functions should
be used to convert them to actual date objects.

This is discussed in more detail in Chapter 7, Business Logic - Supporting Business Processes.

* `Boolean(string)` holds `True` or `False` values, as you might expect, and only has one positional argument for the string text.


* `Binary(string)` stores file-like binary data, and also expects only the string argument.

    It can be handled by Python code using base64 encoded strings.

* Relation fields

Example:  `Post` is in `Category` and have many `Tags`

```
category_id = fields.Many2one('generation.category', 'Category')
tag_ids = fields.Many2many('generation.tag', string='Tags')

```
-  [Many-to-many relationships](#many-to-many-relationships) 
-  [One-to-Many Relationship](#one-to-many-relationship) 
-  [Hierarchical relationships](#hierarchical-relationships) 
-  [Dynamic relationships using Reference fields](#dynamic-relationships-using-reference-fields) 



#### Field Attributes

* `string` is the field default label, to be used in the user interface.

    Except for `Selection` and `Relational` fields, it is the first positional argument, so most of the time it is not used as a keyword argument.

    If not provided, it is automatically generated from the field name.

* `default` sets a default value for the field.

    It can be a static value, such as a string,  or a callable reference, either a named function or an anonymous function (a lambda expression).

    In the stage model,  we can see an example of a default value on the `date_created` field that uses a lambda expression to set the current date  and time when a new record is created.

* `size` applies only to `Char` fields, and can set a maximum size allowed.

    It's  recommended to not use it unless there is a business requirement for it, for example, a social security number with a maximum length allowed.

* `translate` applies only to `Char`, `Text`, and `Html` fields, and makes the field contents translatable, holding different values for different languages.

* `help` provides the text for tooltips displayed to users.

* `readonly=True` makes the field not editable in the user interface by default.

    This is not enforced at the API level; code in model methods will still be capable of writing to it.

    It is only a user interface setting.

* `required=True` makes the field mandatory in the user interface by default.

    This is enforced at the database level by adding a `NOT NULL` constraint on the column.

* `index=True` adds a database index on the field, for faster search operations at the expense of slower write operations.

* `copy=False` has the field ignored when using the duplicate record feature - the `copy()` ORM method.

    The non-relational fields are copyable by default.

* `groups` allows limiting the field's access and visibility to only some groups.

    It expects a comma-separated list of XML IDs for security groups, such as `groups='base.group_user,base.group_system'`.

* `states` expects dictionary mapping values for UI attributes depending on values of the state field.

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

* `deprecated=True` logs a warning whenever the field is being used

* `oldname='field'` is used when a field is renamed in a newer version, enabling the data in the old field to be automatically copied into the new field.

#### Special field names

A few field names are reserved for use by the ORM.

* `id` field is an automatic number uniquely identifying each record, and used as the database primary key.

    It's automatically added to every model.

    The following fields are automatically created on new models, unless the `_log_access=False` model attribute is set:

* `create_uid` is for the user that created the record
* `create_date` is for the date and time when the record is created
* `write_uid` is for the last user to modify the record
* `write_date` is for the last date and time when the record was modified

    The information in these fields is available in the web client, in the `Developer Mode` menu, by selecting the `View Metadata` option.

* `name` is used by default as the display name for the record.

    Usually, it is a `Char`, but can also be a `Text` or a `Many2one` field type.

    We can choose another field to be used for the display name, using the `_rec_name` model attribute.

* `active`, of type Boolean, allows us to inactivate records.

    Records with `active==False` will automatically be excluded from queries.

    To access them, an `('active','=',False)` condition must be added to the search domain, or the `'active_test': False` key should
be set on the current context.

* `sequence`, of type Integer, if present in a list view, allows
  us to manually drag records to define the order of the records.

    For it to work properly, you should not forget to include it in the model's `_order` attribute.

* `state`, of type Selection, represents basic states of the record's life cycle and can be used by the state's field attribute to dynamically modify the view; some form fields can be made `readonly`, `required`, or `invisible` in specific record states.

* `parent_id`, `parent_left`, and `parent_right`, of type Integer, have special meaning for parent/child hierarchical relations.

    We will discuss them in detail later in this chapter.

### Extending models

#### Adding/Modify fields to Existed Model

```
class TodoTask(models.Model):
    _name = 'todo.task'
    _inherit = ['todo.task', 'mail.thread']

    name = fields.Char(help="What needs to be done?") # modify
    effort_estimate = fields.Integer() # add
```

#### Many-to-one relationships

Example:  `Post` is in `Category` and have many `Tags`

```
category_id = fields.Many2one('generation.category', 'Category')
tag_ids = fields.Many2many('generation.tag', string='Tags')

```
The `Many2one` relationship accepts two positional arguments: the `related model` (corresponding to the comodel keyword argument) and the `title` string.

It creates a field in the database table with a foreign key to the related table.

Some additional named arguments are also available to use with this type of field:

* `ondelete` defines what happens when the related record is deleted.

    Its default is `set null`, meaning that an empty value is set when the related record is deleted.

    Other possible values are `restricted`, raising an error preventing the deletion, and `cascade`, which also deletes this record.


* `context` is a dictionary of data, meaningful for the web client views, to carry information when navigating through the relationship, for example, to set default
values.

    It will be better explained in Chapter 7, Business Logic - Supporting business processes.

* `domain` is a domain expression; a list of tuples used to filter the records made available for selection on the relation field.

    See Chapter 7, Business Logic Supporting Business Processes for more details.
* `auto_join=True` allows the ORM to use SQL joins when doing searches using this relationship.

    If used, the access security rules will be bypassed, and the user
could have access to related records the security rules wouldn't allow, but the SQL queries will be more efficient and run faster.

#### Many-to-many relationships

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


#### One-to-Many Relationship

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


#### Hierarchical relationships

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

#### Dynamic relationships using Reference fields

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

The `@api.depends` decorator is needed when the computation depends on other fields, as it usually does. 

It lets the server know when to recompute stored or cached values. One or more field names are accepted as arguments and dot-notation can be used to follow field relationships.

For example we will add new field to `post` which change when this parent category name change as below:


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




    





