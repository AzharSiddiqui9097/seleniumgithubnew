import pytest
from BaseTest import BaseTest
from ConfigPage import ConfigPage
from config import ConfigData


class TestAutomation(BaseTest):
    def test_title(self):
        self.admin_page_title = ConfigPage(self.driver)
        title_name = self.admin_page_title.perform_login(ConfigData.company_key,ConfigData.username,ConfigData.password
                                                    ,ConfigData.page_title)
        assert title_name == "Replicon - Administration"
