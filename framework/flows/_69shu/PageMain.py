from elements._69shu.PageMain import PageMain as PageMainElements
from common.Driver import Driver as D
class PageMain(PageMainElements):

    def goTo(self):
        Driver = D()
        Driver.goTo(f'https://www.69shu.pro/book/{Driver.get_novel_id()}.htm')

    def get_title():
        pass
    