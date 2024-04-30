from definitions._69shu.PageMain import PageMain as PageMainDefinitions
from common.Driver import Driver as D

class PageMain(PageMainDefinitions):

    def get_title():
        Driver = D()
        D.find_element(super.title)

    