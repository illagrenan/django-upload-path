==================
Django Upload Path
==================

.. image:: https://img.shields.io/pypi/v/django-upload-path.svg
    :target: https://pypi.python.org/pypi/django-upload-path
    :alt: PyPi

.. image:: https://img.shields.io/badge/license-MIT-blue.svg
    :target: https://pypi.python.org/pypi/django-upload-path/
    :alt: MIT

.. image:: https://img.shields.io/travis/illagrenan/django-upload-path.svg
    :target: https://travis-ci.org/illagrenan/django-upload-path
    :alt: TravisCI

.. image:: https://img.shields.io/coveralls/illagrenan/django-upload-path.svg
    :target: https://coveralls.io/github/illagrenan/django-upload-path?branch=master
    :alt: Coverage

.. image:: https://img.shields.io/pypi/implementation/django-upload-path.svg
    :target: https://pypi.python.org/pypi/django_brotli/
    :alt: Supported Python implementations

.. image:: https://img.shields.io/pypi/pyversions/django-upload-path.svg
    :target: https://pypi.python.org/pypi/django_brotli/
    :alt: Supported Python versions

Introduction
------------

This application provides various implementations for the ``FileField/ImageField.upload_to`` attribute (`https://docs.djangoproject.com/en/dev/ref/models/fields/#django.db.models.FileField.upload_to <https://docs.djangoproject.com/en/dev/ref/models/fields/#django.db.models.FileField.upload_to>`_) (``upload_to`` attribute accepts callable).

These implementations are:

- ``auto_cleaned_path`` will generate ``{MODEL_NAME}/{SAFE_UPLOADED_FILENAME}{SUFFIX}``
- ``auto_cleaned_path_uuid4`` will generate ``{MODEL_NAME}/{SAFE_UPLOADED_FILENAME}{SEPARATOR}{UUID4}{SUFFIX}``
- ``auto_cleaned_path_stripped_uuid4`` will generate ``{MODEL_NAME}/{UUID4}{SUFFIX}``


Example
=======

For example, how ``auto_cleaned_path`` works: First, the original file name (typically from the user) is always cleaned (using ``django.utils.text.slugify``). Then, a new path is generated that contains the model name.

If you have a ``MyModel`` model and the user uploads a ``foo-bar.txt`` file, the resulting path will be ``mymodel/foo-bar.txt``.

.. code:: python

    from django.db import models
    from django_upload_path import auto_cleaned_path


    class MyModel(models.Model):
        file = models.FileField(upload_to=auto_cleaned_path)


Installation
------------

- Supported Python versions are: ``3.4.``, ``3.5``, ``3.6`` and ``3.7-dev``.
- Supported Django versions are: ``1.8.x`` (LTS), ``1.9.x``, ``1.10.x`` and ``1.11.x`` (LTS).

.. code:: shell

    pip install django-upload-path

**Do not** add the app to ``INSTALLED_APPS`` (it is useless).

Usage
-----

.. code:: python

    from django.db import models
    from django_upload_path.upload_path import auto_cleaned_path, auto_cleaned_path_stripped_uuid4, auto_cleaned_path_uuid4


    class MyModel(models.Model):
        file1 = models.FileField(upload_to=auto_cleaned_path)
        file2 = models.FileField(upload_to=auto_cleaned_path_stripped_uuid4)
        file3 = models.FileField(upload_to=auto_cleaned_path_uuid4)


Note: ``ImageField`` (`https://docs.djangoproject.com/en/dev/ref/models/fields/#django.db.models.ImageField <https://docs.djangoproject.com/en/dev/ref/models/fields/#django.db.models.ImageField>`_) is also supported.


License
-------

The MIT License (MIT)

Copyright (c) 2017 Vašek Dohnal (@illagrenan)

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be included
in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
