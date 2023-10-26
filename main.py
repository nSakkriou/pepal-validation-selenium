from seleniumScrapper import *

if __name__ == "__main__":
    root = logging.getLogger()
    root.setLevel(logging.INFO)

    aSeleniumScrapper = SeleniumScrapperPepal()
    aSeleniumScrapper.run()
