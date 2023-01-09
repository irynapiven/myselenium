import time
import pytest

from homepage_nav.Homepage_nav import HomepageNav


@pytest.mark.usefixture('setup')
class TestForField():
  
    def test_for_field(self):
        driver = HomepageNav(self.driver)
        name_field = driver.find_full_name_field()
        name_field.send_keys('Google')
        time.sleep(5)
