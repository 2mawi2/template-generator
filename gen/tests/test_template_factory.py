from unittest import TestCase

from assertpy import assert_that

from gen.application.template_factory import TemplateFactory
from gen.application.template_type import TemplateType
from gen.application.wawi_uri_factory import WaWiUriFactory
from gen.file_generator.template import Template
from gen.utils import values


class TestTemplateFactory(TestCase):
    def test_create_crud(self):
        uri_fac = WaWiUriFactory(values.default_base_uri)
        fac = TemplateFactory(TemplateType.CRUD, values.default_base_uri)
        expected = [
            Template(values.crud_controller_template,
                     uri_fac.controller("ERP", "ProductElementPrice"),
                     values.default_replacers("ProductElementPrice", "ERP")),
            Template(values.icrud_controller_template,
                     uri_fac.i_controller("ERP", "ProductElementPrice"),
                     values.default_replacers("ProductElementPrice", "ERP")),
            Template(values.crud_repository_template,
                     uri_fac.repo("ERP", "ProductElementPrice"),
                     values.default_replacers("ProductElementPrice", "ERP")),
            Template(values.icrud_repository_template,
                     uri_fac.i_repo("ERP", "ProductElementPrice"),
                     values.default_replacers("ProductElementPrice", "ERP")),
            Template(values.crud_api_controller_template,
                     uri_fac.admin_api_controller("ProductElementPrice"),
                     values.default_replacers("ProductElementPrice", "ERP")),
        ]
        assert_that(fac.create("ERP", "ProductElementPrice")).is_equal_to(expected)

    def test_create_crud(self):
        uri_fac = WaWiUriFactory(values.default_base_uri)
        fac = TemplateFactory(TemplateType.SEARCHABLE, values.default_base_uri)
        expected = [
            Template(values.searchable_controller_template,
                     uri_fac.controller("ERP", "ProductElementPrice"),
                     values.default_replacers("ProductElementPrice", "ERP")),
            Template(values.isearchable_controller_template,
                     uri_fac.i_controller("ERP", "ProductElementPrice"),
                     values.default_replacers("ProductElementPrice", "ERP")),
            Template(values.searchable_repository_template,
                     uri_fac.repo("ERP", "ProductElementPrice"),
                     values.default_replacers("ProductElementPrice", "ERP")),
            Template(values.isearchable_repository_template,
                     uri_fac.i_repo("ERP", "ProductElementPrice"),
                     values.default_replacers("ProductElementPrice", "ERP")),
            Template(values.searchable_api_controller_template,
                     uri_fac.admin_api_controller("ProductElementPrice"),
                     values.default_replacers("ProductElementPrice", "ERP")),
        ]
        assert_that(fac.create("ERP", "ProductElementPrice")).is_equal_to(expected)
