#NOT:Chrome versiyonu 92.0.4515.159 ile çalışır durumdadır. Eğer sizin Chrome unuzun versiyonu farklı ise dosyadaki chromedriver.exe dosyasını güncelleyiniz!!!
from selenium import webdriver
import time
from InstagramBilgi import kullanici_adi,sifre
from selenium.webdriver.common.keys import Keys

class Instagram:
    def __init__(self,kullanici_adi,sifre):
        self.tarayici=webdriver.Chrome()
        self.kullanici_adi=kullanici_adi
        self.sifre=sifre
    def GirisYap(self):
        self.tarayici.get("https://www.instagram.com/accounts/login/")
        time.sleep(3)
        kullanici_adi_giris=self.tarayici.find_element_by_name("username")
        sifre_giris = self.tarayici.find_element_by_name("password")

        kullanici_adi_giris.send_keys(self.kullanici_adi)
        sifre_giris.send_keys(self.sifre)
        sifre_giris.send_keys(Keys.ENTER)
        time.sleep(5)
    def Takip(self):
        self.tarayici.get("https://www.instagram.com/tayfunozcan14")
        time.sleep(2)
        self.tarayici.find_element_by_xpath("//*[@id ='react-root']/section/main/div/header/section/ul/li[3]/a").click()
        time.sleep(2)
        dialog = self.tarayici.find_element_by_css_selector("div[role=dialog] ul")
        takipci_sayisi = len(dialog.find_elements_by_css_selector("li"))
        print("first count: {0}".format(takipci_sayisi))
        action = webdriver.ActionChains(self.tarayici)
        while True:
            dialog.click()
            action.key_down(Keys.SPACE).key_up(Keys.UP).perform()
            time.sleep(2)
            duzenlenmis_sayi = len(dialog.find_elements_by_css_selector("li"))
            if takipci_sayisi != duzenlenmis_sayi:
                takipci_sayisi = duzenlenmis_sayi
                print("second count: {0}".format(duzenlenmis_sayi))
                time.sleep(2)
            else:
                break
        takipciler = dialog.find_elements_by_css_selector("li")
        hesaplayici = 0
        for user in takipciler:
            takip_tusu = user.find_element_by_css_selector('button')
            if (takip_tusu.text != 'Following'):
                takip_tusu.click()
                hesaplayici = hesaplayici + 1
                time.sleep(2)
            else:
                pass
        print(str(hesaplayici) + " kişi takip edildi.")
    def Takipten_Cik(self):
        self.tarayici.get("https://www.instagram.com/tayfunozcan14/")
        time.sleep(2)
        self.tarayici.find_element_by_xpath("//*[@id ='react-root']/section/main/div/header/section/ul/li[3]/a").click()
        time.sleep(2)
        dialog = self.tarayici.find_element_by_css_selector("div[role=dialog] ul")
        takipci_sayisi = len(dialog.find_elements_by_css_selector("li"))
        print("first count: {0}".format(takipci_sayisi))
        action = webdriver.ActionChains(self.tarayici)
        while True:
            dialog.click()
            action.key_down(Keys.SPACE).key_up(Keys.UP).perform()
            time.sleep(2)
            duzenlenmis_sayi = len(dialog.find_elements_by_css_selector("li"))
            if takipci_sayisi != duzenlenmis_sayi:
                takipci_sayisi = duzenlenmis_sayi
                print("second count: {0}".format(duzenlenmis_sayi))
                time.sleep(2)
            else:
                break
        takipciler = dialog.find_elements_by_css_selector("li")
        TakipciListesi = []
        for kullanici in takipciler:
            takipten_cik_tusu = kullanici.find_element_by_css_selector('button')
            if (takipten_cik_tusu.text == 'Following' or takipten_cik_tusu.text == 'Requested'):
                takipten_cik_tusu.click()
                time.sleep(2)
                confirmButton = self.tarayici.find_element_by_xpath('//button[text() = "Unfollow"]')
                confirmButton.click()
            else:
                pass
    def ResimBegen(self):
        self.tarayici.get("https://www.instagram.com/p/...")
        resim = self.tarayici.find_element_by_xpath(" //button[normalize-space(class)='wpO6b']/*[name()='svg']")
        print(resim.get_attribute('aria-label'))
        if (resim.get_attribute('aria-label') == 'Like'):
            begen_tusu = self.tarayici.find_element_by_xpath("//*[name()='svg'][aria-label='Like']/parent::button")
            self.tarayici.execute_script("arguments[0].click()", begen_tusu)
        else:
            pass
    def Cikis(self):
        self.tarayici.get("https://www.instagram.com/{0}".format(self.kullanici_adi))
        self.tarayici.find_element_by_xpath("// *[ @ id = 'react-root'] / section / main / div / header / section / div[1] / div / button").click()
        self.tarayici.find_element_by_xpath("/ html / body / div[4] / div / div / div / button[9]").click()
instagram=Instagram(kullanici_adi,sifre)
instagram.GirisYap()
instagram.Takip()
instagram.Takipten_Cik()
instagram.ResimBegen()
instagram.Cikis()