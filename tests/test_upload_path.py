# -*- encoding: utf-8 -*-
# ! python3

import os
import re
from unittest import TestCase

from django_upload_path.upload_path import upload_path, get_safe_path_name, upload_path_strip_uuid4, upload_path_uuid4, get_base_dir_from_object, parse_filename

UUID_RAW_REGEX = "[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}"


class DummyModel:
    pass


class SafePathNameTestCase(TestCase):
    def test_get_safe_path_name(self):
        self.assertEqual('fooo', get_safe_path_name('   foOO   '))
        self.assertEqual('foo', get_safe_path_name('../foo'))
        self.assertEqual('foo', get_safe_path_name('.foo'))
        self.assertEqual('foo', get_safe_path_name('\.foo'))
        self.assertEqual('foo', get_safe_path_name('&foo'))
        self.assertEqual('foobar', get_safe_path_name('foo/bar'))
        self.assertEqual('root', get_safe_path_name('/root'))


class BaseDirTestCase(TestCase):
    def test_get_safe_path_name(self):
        self.assertEqual('dummymodel', get_base_dir_from_object(DummyModel))
        self.assertEqual('dummymodel', get_base_dir_from_object(DummyModel()))


class ParseFilenameTestCase(TestCase):
    def test_get_safe_path_name(self):
        self.assertTupleEqual(('foo', '.txt'), parse_filename('foo.txt'))
        self.assertTupleEqual(('foo', '.jpg'), parse_filename('foo.JPG'))
        self.assertTupleEqual(('foo', '.jpeg'), parse_filename('foo.JPEG'))
        self.assertTupleEqual(('foo', ''), parse_filename('foo'))


class UploadPathTestCase(TestCase):
    def test_get_safe_path_name(self):
        self.assertEqual(os.path.join('dummymodel', 'fooo-bar.txt'), upload_path(DummyModel(), 'fooo-bar.txt'))


class UploadPathUUID4TestCase(TestCase):
    def test_get_safe_path_name(self):
        self.assertRegex(upload_path_uuid4(DummyModel(), 'fooo-bar.txt'), r"dummymodel{}fooo-bar-{}.txt".format(re.escape(os.path.sep), UUID_RAW_REGEX))


class UploadPathStripUUID4TestCase(TestCase):
    def test_get_safe_path_name(self):
        self.assertRegex(upload_path_strip_uuid4(DummyModel(), 'fooo-bar.txt'), r"dummymodel{}{}.txt".format(re.escape(os.path.sep), UUID_RAW_REGEX))
