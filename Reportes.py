from cmath import e
from pickle import FALSE, TRUE
from tkinter.messagebox import NO
from webbrowser import get
from selenium.webdriver.common.by import By
from time import sleep, time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome(executable_path = r"C:\Users\ASUS\Documents\Proyectos\Pruebas_Selenium\nueva version de chrome\chromedriver.exe")
#driver = webdriver.Firefox(executable_path = r"C:\Users\ASUS\Documents\Proyectos\Pruebas_Selenium\geckodriver.exe")
datastudio = "https://datastudio.google.com/"
urladmin = "https://app.portermetrics.com/login"
urlpoter = "https://portermetrics.com/en/home/"
fbads = "https://account.portermetrics.com/templates-hub/facebook-ads"
instagram ="https://account.portermetrics.com/templates-hub/instagram-insights"              
fbinsights = "https://account.portermetrics.com/templates-hub/facebook-insights"
publicdata ="https://account.portermetrics.com/templates-hub/facebook-competitors"
twitterads = "https://account.portermetrics.com/templates-hub/twitter-ads"
twitteranalytic = "https://portermetrics.com/en/connectors/twitter-analytics/"
linkedinpages = "https://account.portermetrics.com/templates-hub/linkedin-pages"
linkedinads = "https://account.portermetrics.com/templates-hub/linkedin-ads"
gmb = "https://account.portermetrics.com/templates-hub/gmb"
tiktok = "https://account.portermetrics.com/templates-hub/tiktok-ads"
hubspot = "https://account.portermetrics.com/templates-hub/hubspot"
shopify = "https://account.portermetrics.com/templates-hub/shopify"
woo = "https://account.portermetrics.com/templates-hub/woocommerce"
driver.maximize_window()
sleep(5)

"""
#Revocar cuentas desde data studio
driver.get(datastudio)
inicio = driver.find_element(by=By.XPATH, value="//a[@class='freeButton'][contains(.,'use it for free')]").click()
sleep(5)
handles = driver.window_handles
driver.switch_to.window(handles[-1])
sleep(3)  
usercorreo = driver.find_element(by=By.XPATH, value="//input[contains(@id,'identifierId')]").send_keys("carolina@portermetrics.com")
siguiente = driver.find_element(by=By.XPATH, value="//span[@jsname='V67aGc'][contains(.,'Siguiente')]").click()
sleep(5)
userpass = driver.find_element(by=By.XPATH, value="//input[@type='password']").send_keys("Carito.22")
siguientepass = driver.find_element(by=By.XPATH, value="//span[@jsname='V67aGc'][contains(.,'Siguiente')]").click()
sleep(5)
handles = driver.window_handles
driver.switch_to.window(handles[-1])
sleep(5) 
crear = driver.find_element(by=By.XPATH, value="/html/body/app-bootstrap/ng2-bootstrap/lego-router-outlet/navigation-page/nav-sidebar/create-button/button/span").click()
datos = driver.find_element(by=By.XPATH, value="//*[@id='mat-menu-panel-0']/div/button[2]").click()
sleep(10)
buscar = driver.find_element(by=By.XPATH, value="//*[@id='mat-input-0']").send_keys("Porter Metrics")
sleep(5)
#etiquetatwitter = driver.find_element(by=By.XPATH, value="(//div[contains(.,'Twitter Ads De Porter Metrics  Automate your Twitter Ads reporting on Google Data Studio')])[17]")
referencias = driver.find_elements(by=By.XPATH, value="(//p[contains(@class,'sub-title')])")
conectores=[]
cant_cone=0
for referencia in referencias:
    if referencia.text not in conectores:
        conectores.append(referencia.text)
        cant_cone+=1


if referencia.text is 'Twitter Ads':  
    opciones = driver.find_element(by=By.XPATH, value="//*[@id='body']/div/div/shade/div/div[3]/div/div/detail/div/div[2]/connector-picker/div/connector-gallery/div[2]/div/connector-gallery-category[2]/div/div[2]/connector-gallery-card[1]/gmat-card/div[3]/button/span[1]/mat-icon").click()
    sleep(5)   
    revocar = driver.find_element(by=By.XPATH, value="//*[@id='mat-menu-panel-637']/div/button").click()
    quitar = driver.find_element(by=By.XPATH, value="/html/body/div[5]/md-dialog/md-dialog-actions/button[2]").click()
    sleep(7)
    uitardos = driver.find_element(by=By.XPATH, value="/html/body/div[5]/md-dialog/md-dialog-actions/button[2]").click()


"""   
driver.get(urladmin)
#Accede a la cuenta de gmail
login = driver.find_element(by=By.XPATH, value="//button[@type='button'][contains(.,'Sign in with Google')]").click()
usercorreo = driver.find_element(by=By.XPATH, value="//input[contains(@id,'identifierId')]").send_keys("carolina@portermetrics.com")
siguiente = driver.find_element(by=By.XPATH, value="//span[@jsname='V67aGc'][contains(.,'Siguiente')]").click()
sleep(5)
userpass = driver.find_element(by=By.XPATH, value="//input[@type='password']").send_keys("Carito.22")
siguientepass = driver.find_element(by=By.XPATH, value="//span[@jsname='V67aGc'][contains(.,'Siguiente')]").click()
sleep(8)



#Modulo de acceso para hacer reportes -----------------------------------------------------------------
reportes = driver.find_element(by=By.XPATH, value="//a[contains(@id,'make-report')]").click()
sleep(10)



"""
driver.switch_to.new_window()
#Reportes con Facebook Ads
driver.get(fbads)
sleep(10)

autorizacion = driver.find_element(by=By.XPATH, value="//button[contains(.,'Authorize')]").click()
sleep(5)
autorizaciongmail = driver.find_element(by=By.XPATH, value="//div[contains(@data-email,'carolina@portermetrics.com')]").click()
sleep(5)
permitir = driver.find_element(by=By.XPATH, value="(//div[contains(@class,'VfPpkd-RLmnJb')])[2]").click()
sleep(5)
autorizacionconector = driver.find_element(by=By.XPATH, value="//span[contains(@ng-if,'!$ctrl.isAuthorizing')]").click()
sleep(10)
handles = driver.window_handles
driver.switch_to.window(handles[-1])
sleep(3)               
validacionfb = driver.find_element(by=By.XPATH, value="//input[contains(@id,'email')]").send_keys("master@portermetrics.com")
sleep(10)
contraseñafb = driver.find_element(by=By.XPATH, value="//input[contains(@type,'password')]").send_keys("321654987Abc***.")
vpermitirfb = driver.find_element(by=By.XPATH, value="//input[contains(@value,'Entrar')]").click()
driver.find_element(By.CSS_SELECTOR("a[title=\"Go to Facebook home\"]")).click();  
driver.implicitly_wait(30)
fbads = driver.find_element(by=By.LINK_TEXT, value="//a[@href='https://account.portermetrics.com/templates-hub/facebook-ads'][contains(.,'Facebook Ads')]").click()
driver.find_element(By)
ads = driver.find_element(by=By.CLASS_NAME, value="//div[contains(@class,'elementor-element elementor-element-583237b Facebook-Ads ekit-equal-height-disable elementor-widget elementor-widget-elementskit-icon-box')]").click()
#WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='FbAds']/div/div/a/div")))
#WebDriverWait(driver, 10).until(EC.presence_of_element_located(By.XPATH, "//*[@id='FbAds']/div/div/a/div")).click()
"""
#Reportes de Twitter Ads
driver.switch_to.new_window()
driver.get(twitterads)
sleep(10)
"""
autorizar= driver.find_element(by=By.XPATH, value="//button[contains(.,'Authorize')]").click()
sleep(5)
handles = driver.window_handles
driver.switch_to.window(handles[-1])
sleep(3)
gmailregistrado =  driver.find_element(by=By.XPATH, value="//*[@id='view_container']/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div/div/ul/li[1]/div/div[1]/div/div[2]").click()
sleep(3)
permitir = driver.find_element(by=By.XPATH, value="(//span[contains(@jsname,'V67aGc')])[2]").click()
sleep(5)

autorizaciongmail = driver.find_element(by=By.XPATH, value="//div[contains(@data-email,'carolina@portermetrics.com')]").click()
sleep(5)
permitir = driver.find_element(by=By.XPATH, value="(//div[contains(@class,'VfPpkd-RLmnJb')])[2]").click()
sleep(5)
"""
autorizacionconectortw = driver.find_element(by=By.XPATH, value="//span[contains(@ng-if,'!$ctrl.isAuthorizing')]").click()
sleep(5)
handles = driver.window_handles
driver.switch_to.window(handles[-1])
sleep(3)               
validaciontw = driver.find_element(by=By.XPATH, value="//*[@id='username_or_email']").send_keys("PaulaMVelandia")
sleep(5)
contraseñatw = driver.find_element(by=By.XPATH, value="//input[contains(@type,'password')]").send_keys("Mainz1905!")
permitirtw = driver.find_element(by=By.XPATH, value="(//input[contains(@type,'submit')])[1]").click()
driver.close()
driver.switch_to.window(driver.window_handles[1])
#enlacehelp = driver.find_element(by=By.XPATH, value="//a[contains(.,'http://help.portermetrics.com/en/articles/5845795-how-to-set-up-a-twitter-ads-report-on-google-data-studio')]").click()
#handles = driver.window_handles
#driver.switch_to.window(handles[-1])
#driver.switch_to.window(driver.window_handles[1])
#selecuenta = driver.find_element(by=By.XPATH, value="//md-select[contains(@id,'select_6')]").click()
"""
#Reportes de Twitter Analityc
driver.switch_to.new_window()
driver.get(twitteranalytic)
sleep(8)

autorizar= driver.find_element(by=By.XPATH, value="//button[contains(.,'Authorize')]").click()
sleep(5)
handles = driver.window_handles
driver.switch_to.window(handles[-1])
sleep(3)
gmailregistrado =  driver.find_element(by=By.XPATH, value="//*[@id='view_container']/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div/div/ul/li[1]/div/div[1]/div/div[2]").click()
sleep(3)
permitir = driver.find_element(by=By.XPATH, value="(//span[contains(@jsname,'V67aGc')])[2]").click()
sleep(5)

autorizaciongmail = driver.find_element(by=By.XPATH, value="//div[contains(@data-email,'carolina@portermetrics.com')]").click()
sleep(5)
permitir = driver.find_element(by=By.XPATH, value="(//div[contains(@class,'VfPpkd-RLmnJb')])[2]").click()
sleep(5)

autorizacionconectortw = driver.find_element(by=By.XPATH, value="//span[contains(@ng-if,'!$ctrl.isAuthorizing')]").click()
sleep(5)
handles = driver.window_handles
driver.switch_to.window(handles[-1])
sleep(3)               
validaciontw = driver.find_element(by=By.XPATH, value="//*[@id='username_or_email']").send_keys("PaulaMVelandia")
sleep(5)
contraseñatw = driver.find_element(by=By.XPATH, value="//input[contains(@type,'password')]").send_keys("Mainz1905!")
permitirtw = driver.find_element(by=By.XPATH, value="(//input[contains(@type,'submit')])[1]").click()
driver.close()
sleep(3)
"""
#Validación al momento de seleccionar cuentas
sleep(15)
#sincuenta = driver.find_element(by=By.XPATH, value="//*[@id="body"]/div/div/shade/div/embedded-header/div/div/div/button").click()
conectarsincuenta = driver.find_element(by=By.XPATH, value="//*[@id='body']/div/div/shade/div/embedded-header/div/div/div/button").click()
sleep(5)
seleccionarcuenta = driver.find_element(by=By.XPATH, value="/html/body/div[4]/md-dialog/md-dialog-actions/button").click()
sleep(4)
#handles = driver.window_handles
#driver.switch_to.window(handles[-1])
#driver.execute_script("window.scrollTo(0, 300)")
cuentas = driver.find_element(by=By.XPATH, value="//md-select[contains(@role,'listbox')]").click()
#handles = driver.window_handles
#driver.switch_to.window(handles[-1])
#driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
seleccionarcuenta = driver.find_element(by=By.XPATH, value="seleccionarcuenta = driver.find_element(by=By.XPATH, value="")").click()
seleccionarcuenta = driver.find_element(by=By.XPATH, value="(//div[contains(@class,'md-container md-ink-ripple')])[1]").click()

"""seleccionarcuenta = driver.find_element(by=By.XPATH, value="")
seleccionarcuenta = driver.find_element(by=By.XPATH, value="")
seleccionarcuenta = driver.find_element(by=By.XPATH, value="")
seleccionarcuenta = driver.find_element(by=By.XPATH, value="")
seleccionarcuenta = driver.find_element(by=By.XPATH, value="")"""

  