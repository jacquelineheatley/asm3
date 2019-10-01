#!/usr/bin/python env

import unittest
import base

import asm3.onlineform
import asm3.utils

class TestOnlineForm(unittest.TestCase):

    nformid = 0
    nfieldid = 0
    collationid = 0

    def setUp(self):
        data = {
            "name": "Test Form",
            "header": "HEADER",
            "footer": "FOOTER"
        }
        post = asm3.utils.PostedData(data, "en")
        self.nformid = asm3.onlineform.insert_onlineform_from_form(base.get_dbo(), "test", post)
        data = {
            "fieldname": "testfield",
            "formid":    str(self.nformid),
            "fieldtype": "1", # TEXT
            "label":     "Test Field",
            "displayindex": "1"
        }
        post = asm3.utils.PostedData(data, "en")
        self.nfieldid = asm3.onlineform.insert_onlineformfield_from_form(base.get_dbo(), "test", post)
        data = {
            "formname":     "Test Form",
            asm3.onlineform.JSKEY_NAME: asm3.onlineform.JSKEY_VALUE,
            "testfield_%s" % self.nfieldid: "Test Value"
        }
        post = asm3.utils.PostedData(data, "en")
        self.collationid = asm3.onlineform.insert_onlineformincoming_from_form(base.get_dbo(), post, "0.0.0.0")

    def tearDown(self):
        asm3.onlineform.delete_onlineform(base.get_dbo(), "test", self.nformid)
        asm3.onlineform.delete_onlineformincoming(base.get_dbo(), "test", self.collationid)

    def test_get_onlineform(self):
        assert asm3.onlineform.get_onlineform(base.get_dbo(), self.nformid) is not None

    def test_get_onlineforms(self):
        assert len(asm3.onlineform.get_onlineforms(base.get_dbo())) > 0

    def test_get_onlineform_html(self):
        assert asm3.onlineform.get_onlineform_html(base.get_dbo(), self.nformid) != ""

    def test_get_onlineform_json(self):
        assert asm3.onlineform.get_onlineform_json(base.get_dbo(), self.nformid) != ""

    def test_get_onlineform_name(self):
        assert asm3.onlineform.get_onlineform_name(base.get_dbo(), self.nformid) != ""

    def test_get_onlineformfields(self):
        assert len(asm3.onlineform.get_onlineformfields(base.get_dbo(), self.nformid)) > 0

    def test_get_onlineformincoming_formheader(self):
        asm3.onlineform.get_onlineformincoming_formheader(base.get_dbo(), self.nformid)

    def test_get_onlineformincoming_formfooter(self):
        asm3.onlineform.get_onlineformincoming_formfooter(base.get_dbo(), self.nformid)

    def test_get_onlineformincoming_headers(self):
        assert len(asm3.onlineform.get_onlineformincoming_headers(base.get_dbo())) > 0

    def test_get_onlineformincoming_detail(self):
        assert len(asm3.onlineform.get_onlineformincoming_detail(base.get_dbo(), self.collationid)) > 0

    def test_get_onlineformincoming_html(self):
        assert asm3.onlineform.get_onlineformincoming_html(base.get_dbo(), self.collationid) != ""

    def test_get_onlineformincoming_plain(self):
        assert asm3.onlineform.get_onlineformincoming_plain(base.get_dbo(), self.collationid) != ""

    def test_get_onlineformincoming_html_print(self):
        assert asm3.onlineform.get_onlineformincoming_html_print(base.get_dbo(), [self.collationid]) != ""

    def test_get_onlineformincoming_name(self):
        assert asm3.onlineform.get_onlineformincoming_name(base.get_dbo(), self.collationid) != ""

    def test_auto_remove_old_incoming_forms(self):
        asm3.onlineform.auto_remove_old_incoming_forms(base.get_dbo())

    # TODO: Test create_RECORD methods - requires a more detailed form



