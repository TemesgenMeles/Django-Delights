# Django-Delights Project

## Table of Contents
- [Overview](#overview)
- [Built With](#built-with)
- [File Structure](#file-structure)
- [Usage](#usage)
- [Contact](#contact)

## Overview

- Welcome to my Django project, This project is an Inventory project that provides a platform for individuals to manage inventorys, deliver menus, and calculate profits.

## Built With

- The project website is built using
    - **Python**
    - **Django**
    - **HTML**
    - **CSS**

## File structure

    .
    │   db.sqlite3
    │   manage.py
    │
    ├───DjangoDelights
    │   │   asgi.py
    │   │   settings.py
    │   │   urls.py
    │   │   wsgi.py
    │   │   __init__.py
    │   │
    │   └───__pycache__
    │           settings.cpython-312.pyc
    │           urls.cpython-312.pyc
    │           wsgi.cpython-312.pyc
    │           __init__.cpython-312.pyc
    │
    └───inventory
        │   admin.py
        │   apps.py
        │   models.py
        │   tests.py
        │   urls.py
        │   views.py
        │   __init__.py
        │
        ├───migrations
        │   │   0001_initial.py
        │   │   0002_alter_reciperequirement_ingradint.py
        │   │   0003_alter_purchase_menu_item.py
        │   │   0004_profit_purcahsehistory_alter_purchase_menu_item.py
        │   │   0005_menuitem_reating.py
        │   │   0006_alter_reciperequirement_unit.py
        │   │   0007_alter_profit_timestamp_end_and_more.py
        │   │   __init__.py
        │   │
        │   └───__pycache__
        │           0001_initial.cpython-312.pyc
        │           0002_alter_ingradient_unit_price.cpython-312.pyc
        │           0002_alter_reciperequirement_ingradint.cpython-312.pyc
        │           0003_alter_ingradient_unit_price.cpython-312.pyc
        │           0003_alter_purchase_menu_item.cpython-312.pyc
        │           0004_profit_purcahsehistory_alter_purchase_menu_item.cpython-312.pyc
        │           0005_menuitem_reating.cpython-312.pyc
        │           0006_alter_reciperequirement_unit.cpython-312.pyc
        │           0007_alter_profit_timestamp_end_and_more.cpython-312.pyc
        │           __init__.cpython-312.pyc
        │
        ├───static
        │   └───inventory
        │       ├───css
        │       │       add_ingradient.css
        │       │       add_ingradient_quantity.css
        │       │       add_menu.css
        │       │       all_profit.css
        │       │       base.css
        │       │       conformation.css
        │       │       edit_ingradient.css
        │       │       menu.css
        │       │       purchase.css
        │       │       purchase_history.css
        │       │       recipe.css
        │       │       recipe_edit.css
        │       │       stock.css
        │       │       style.css
        │       │       update_requirement.css
        │       │
        │       ├───font-awesome
        │       │   │   HELP-US-OUT.txt
        │       │   │
        │       │   ├───css
        │       │   │       font-awesome.css
        │       │   │       font-awesome.min.css
        │       │   │
        │       │   ├───fonts
        │       │   │       fontawesome-webfont.eot
        │       │   │       fontawesome-webfont.svg
        │       │   │       fontawesome-webfont.ttf
        │       │   │       fontawesome-webfont.woff
        │       │   │       fontawesome-webfont.woff2
        │       │   │       FontAwesome.otf
        │       │   │
        │       │   ├───less
        │       │   │       animated.less
        │       │   │       bordered-pulled.less
        │       │   │       core.less
        │       │   │       fixed-width.less
        │       │   │       font-awesome.less
        │       │   │       icons.less
        │       │   │       larger.less
        │       │   │       list.less
        │       │   │       mixins.less
        │       │   │       path.less
        │       │   │       rotated-flipped.less
        │       │   │       screen-reader.less
        │       │   │       stacked.less
        │       │   │       variables.less
        │       │   │
        │       │   └───scss
        │       │           font-awesome.scss
        │       │           _animated.scss
        │       │           _bordered-pulled.scss
        │       │           _core.scss
        │       │           _fixed-width.scss
        │       │           _icons.scss
        │       │           _larger.scss
        │       │           _list.scss
        │       │           _mixins.scss
        │       │           _path.scss
        │       │           _rotated-flipped.scss
        │       │           _screen-reader.scss
        │       │           _stacked.scss
        │       │           _variables.scss
        │       │
        │       ├───fonts
        │       │       acorn bold.ttf
        │       │
        │       └───images
        │           │   background.jpg
        │           │   background2.jpg
        │           │   background3.jpg
        │           │   background4.jpg
        │           │   background5.jpg
        │           │   background6.jpg
        │           │   logo vertical.png
        │           │   logo.png
        │           │   logo_name.png
        │           │
        │           ├───green
        │           └───red
        │                   logo vertical.png
        │                   logo.png
        │                   logo_name.png
        │
        ├───templates
        │   └───inventory
        │           add_ingradient.html
        │           add_ingradient_quantity.html
        │           Add_menu.html
        │           all_profit.html
        │           base.html
        │           edit_ingradient.html
        │           edit_menu.html
        │           index.html
        │           ingradients.html
        │           menus.html
        │           purchase.html
        │           purchase_conformation.html
        │           purchase_history.html
        │           recipe.html
        │           recipe_edit.html
        │           update_requirement.html
        │
        ├───templatetags
        │   │   my_filters.py
        │   │   __init__.py
        │   │
        │   └───__pycache__
        │           my_filters.cpython-312.pyc
        │           __init__.cpython-312.pyc
        │
        └───__pycache__
                admin.cpython-312.pyc
                apps.cpython-312.pyc
                models.cpython-312.pyc
                urls.cpython-312.pyc
                views.cpython-312.pyc
                __init__.cpython-312.pyc


## Usage

First clone the repository from Github and switch to the new directory:

    $ git clone https://github.com/TemesgenMeles/Django-Delights
    $ cd Django-Delights


Then simply apply the migrations:

    $ python manage.py migrate


You can now run the development server:

    $ python manage.py runserver

## Contact
[![LinkedIn](https://img.shields.io/badge/LinkedIn-%230077B5.svg?logo=linkedin&logoColor=white)](https://linkedin.com/in/temesgen-meles)
