from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from homework6.page_objects.BasePage import BasePage


class DesktopsPage(BasePage):
    TIMEOUT = 10

    BREADCRUMPS =   (By.CLASS_NAME, "breadcrumb")
    LIST_GROUP =    (By.CLASS_NAME, "list-group")
    CONTENT =       (By.ID, "content")
    COMPARE_TOTAL = (By.ID, "compare-total")
    FOOTER =        (By.CSS_SELECTOR, "footer")

    def check_elements(self):
        self.wait.until(EC.visibility_of_element_located(self.BREADCRUMPS), "Breadcrumb loading error")
        self.wait.until(EC.visibility_of_element_located(self.LIST_GROUP), "List group loading error")
        self.wait.until(EC.visibility_of_element_located(self.CONTENT), "Content loading error")
        self.wait.until(EC.visibility_of_element_located(self.COMPARE_TOTAL), "Compare element loading error")
        self.wait.until(EC.visibility_of_element_located(self.FOOTER), "Footer loading error")
