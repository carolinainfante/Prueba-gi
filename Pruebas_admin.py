
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


driver = webdriver.Chrome(executable_path = r"C:\Users\ASUS\Documents\Pruebas_Selenium\chromedriver.exe")
#driver = webdriver.Firefox(executable_path = r"C:\Users\ASUS\Documents\Pruebas_Selenium\geckodriver.exe")
urladmin = "https://app.portermetrics.com/login"
urlpoter = "https://portermetrics.com/en/home/"
driver.maximize_window()
sleep(10)
driver.get(urladmin)
#Accede a la cuenta de gmail
login = driver.find_element(by=By.XPATH, value="//button[@type='button'][contains(.,'Sign in with Google')]").click()
usercorreo = driver.find_element(by=By.XPATH, value="//input[contains(@id,'identifierId')]").send_keys("carolina@portermetrics.com")
siguiente = driver.find_element(by=By.XPATH, value="//span[@jsname='V67aGc'][contains(.,'Siguiente')]").click()
sleep(5)
userpass = driver.find_element(by=By.XPATH, value="//input[@type='password']").send_keys("Carito.22")
siguientepass = driver.find_element(by=By.XPATH, value="//span[@jsname='V67aGc'][contains(.,'Siguiente')]").click()
sleep(8)
"""
#modulo apps -----------------------------------------------------------------------
#abre ventana para una nueva conexion 
conectarnew = driver.find_element_by_xpath("//a[@class='btn btn-primary']").click()
sleep(5)
driver.switch_to.window(driver.window_handles[0])
sleep(3)
driver.execute_script("window.scrollTo(0,500)")
sleep(5)
driver.execute_script("window.scrollTo(500,0)")
#Evalua si existe la clase para ingresar a cada conector y evalua si esta o no habilitado
estado = driver.find_element(by=By.TAG_NAME, value="div")
tarjetaconector = driver.find_elements(by=By.CSS_SELECTOR, value=(".card-custom"))
listaapps = ["linkedin-pages-enabled","facebook-ads-enabled", "instagram-insights-enabled","facebook-insights-enabled", "hubspot-enabled", "shopify-enabled", "woocommerce-enabled", "facebook-public-data-enabled", "twitter-ads-enabled", "tiktok-ads-enabled", "google-my-business-enabled", "linkedin-ads-enabled", "twitter-organic-analytics-enabled"]
#Recorre cada conector habilitado y elimina una cuenta 
for listaapp in listaapps:
    print(f"Probando: {listaapp}")
    name=None
    sleep(7)
    try:
        name = driver.find_element(by=By.CSS_SELECTOR, value=f".{listaapp}")
    except  NoSuchElementException as e:
        print("no esta habilitado la app")
    if name:
        name.click()
        sleep(5)
        agrupar = driver.find_element_by_xpath("//*[@id='kt_content']/div/div/app-app-connector/div[2]/div/div/div[1]/div[2]/a").click()
        sleep(3)
        desagrupar = driver.find_element_by_xpath("//*[@id='kt_content']/div/div/app-app-connector/div[2]/div/div/div[1]/div[2]/a").click()
        eliminar = driver.find_elements(by=By.CLASS_NAME, value=("btn-light-danger"))
        cont = 0
        for borrar in eliminar:
            print(f"Probando el eliminar: {cont}") 
            cont +=1
            sleep(5)
            if cont > 2: 
                borrar.click() 
                driver.back()
                sleep(3)
                break
        driver.back()
     
#modulo de acceso a los template ----------------------------------------------------------------------
template = driver.find_element_by_xpath("//a[contains(@id,'use-template')]").click()
sleep(5)
driver.switch_to.window(driver.window_handles[0])
sleep(5)
#Modulo de acceso para hacer reportes -----------------------------------------------------------------
reportes = driver.find_element_by_xpath("//a[contains(@id,'make-report')]").click()
sleep(5)
#tab = driver.find_elements(by=By.CLASS_NAME, value="//div[@class='elementskit-infobox text-left text-left icon-lef-right-aligin elementor-animation- media gradient-active  hover_from_left'][contains(.,'Facebook Ads')]").click()
driver.switch_to.window(driver.window_handles[0])
sleep(3)
"""
#modulo de compra--------------------------------------------------------------------------------------
btnbuy = driver.find_element_by_xpath("//a[contains(@id,'buy_licence')]").click()
sleep(15)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
sleep(3)
#mes = driver.find_element(by=By.XPATH, value="/html/body/app-layout/div/div/div/div/div/div/app-buy/div[1]/div/span/label/input").click()
#mes_anual = driver.find_element(by=By.XPATH, value="//*[@id='monthly-checkbox']").click()
#realizar una compra plan solo---------------------
buysolo =  driver.find_element_by_xpath("(//button[contains(@type,'button')])[1]").click()
sleep(10)

#driver.SwitchTo().Window(<windowname>)
cerrar = driver.find_element(by=By.XPATH, value="(//button[contains(@type,'button')])[4]").click()
##driver.switch_to.window(driver.window_handles[0])
#driver.switch_to().alert()
#cerrar = driver.find_element(by=By.XPATH, value="//button[@type='button'][contains(.,'x')]").click()
"""
driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
sleep(3)
gotopaysolo = driver.find_element(by=By.XPATH, value="//button[@type='button'][contains(.,'Go to pay')]").click()
sleep(5)
codpromo = driver.find_element(by=By.XPATH, value="//input[contains(@name,'promotionCode')]").click()
sleep(5)
codigo = driver.find_element(by=By.XPATH, value="(//input[contains(@type,'text')])[1]").send_keys("100PORTEROFF45")
sleep(5)
aplicar = driver.find_element_by_xpath("//span[contains(.,'Aplicar')]").click()
sleep(6)
numtarjeta = driver.find_element(by=By.XPATH, value="//input[contains(@id,'cardNumber')]").click()
sleep(5)
numero = driver.find_element(by=By.XPATH, value="//input[contains(@name,'cardNumber')]").send_keys("4859 5303 3623 4950")
sleep(3)
fechavencimiento = driver.find_element(by=By.XPATH, value="//input[contains(@name,'cardExpiry')]").click()
sleep(3)
fecha = driver.find_element(by=By.XPATH, value="//input[contains(@name,'cardExpiry')]").send_keys("0225")
sleep(3)
cvc = driver.find_element(by=By.XPATH, value="//input[contains(@name,'cardCvc')]").click()
sleep(3)
numcvc = driver.find_element(by=By.XPATH, value="//input[contains(@name,'cardCvc')]").send_keys("278")
sleep(3)
nombre = driver.find_element(by=By.XPATH, value="//input[contains(@autocomplete,'ccname')]").click()
sleep(3)
nombrecompleto = driver.find_element(by=By.XPATH, value="//input[contains(@autocomplete,'ccname')]").send_keys("Juan Jose Bello")
sleep(5)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
sleep(5)
suscribirse = driver.find_element(by=By.XPATH, value="//div[contains(@class,'SubmitButton-IconContainer')]").click()

sleep(15)
confirmacion = driver.find_element(by=By.XPATH, value="//a[contains(.,'Return to billing page')]").click()

btnbuy = driver.find_element_by_xpath("//a[contains(@id,'buy_licence')]").click()
sleep(5)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
sleep(3)             
#cerrarventan = driver.find_element(by=By.XPATH, value="(//button[contains(@type,'button')])[4]").click()
#driver.switch_to.window(driver.window_handles[0])
#cerrr =  driver.find_element_by_xpath("button[@type='button'][contains(.,'x')]").click()
#cer = driver.find_element(by=By.CSS_SELECTOR, value=".button[@type='button'][contains(.,'x')]")
#cerrar = driver.find_element_by_xpath("//button[contains(@class,'close')]").click()
#paysolo = driver.find_element_by_xpath("(//button[contains(@type,'button')])[1]").click()

#Aumentar el numero de cuentas adicionales team
contadicion = 0
for mas in range (8):
    sleep(3)
    if mas <= 8:
        aumentar = driver.find_element_by_xpath("//*[@id='kt_content']/div/div/app-buy/div[2]/div[2]/div/div/div[14]/div/button[2]").click()
        print(f"incremento:{contadicion}")
        contadicion +=1
#Disminuir la cantidad de cuentas  team
for mas in range (8):
    sleep(3)
    if mas <= 8:
        disminuir = driver.find_element_by_xpath("//*[@id='kt_content']/div/div/app-buy/div[2]/div[2]/div/div/div[14]/div/button[1]").click()
        print(f"disminuye:{contadicion}")
        contadicion -=1
#pagar el plan team
sleep(10)
btnnowteam = driver.find_element(by=By.XPATH, value="(//button[@type='button'][contains(.,'Pay now')])[2]").click()
sleep(3)
gotopayteam = driver.find_element(by=By.XPATH, value="//button[@type='button'][contains(.,'Go to pay')]").click()
sleep(10)
codpromo = driver.find_element(by=By.XPATH, value="//input[contains(@name,'promotionCode')]").click()
sleep(5)
codigo = driver.find_element(by=By.XPATH, value="(//input[contains(@type,'text')])[1]").send_keys("100PORTEROFF45")
sleep(5)
aplicar = driver.find_element_by_xpath("//span[contains(.,'Aplicar')]").click()
sleep(6)
numtarjeta = driver.find_element(by=By.XPATH, value="//input[contains(@id,'cardNumber')]").click()
sleep(5)
numero = driver.find_element(by=By.XPATH, value="//input[contains(@name,'cardNumber')]").send_keys("4859 5303 3623 4950")
sleep(3)
fechavencimiento = driver.find_element(by=By.XPATH, value="//input[contains(@name,'cardExpiry')]").click()
sleep(3)
fecha = driver.find_element(by=By.XPATH, value="//input[contains(@name,'cardExpiry')]").send_keys("0225")
sleep(3)
cvc = driver.find_element(by=By.XPATH, value="//input[contains(@name,'cardCvc')]").click()
sleep(3)
numcvc = driver.find_element(by=By.XPATH, value="//input[contains(@name,'cardCvc')]").send_keys("278")
sleep(3)
nombre = driver.find_element(by=By.XPATH, value="//input[contains(@autocomplete,'ccname')]").click()
sleep(3)
nombrecompleto = driver.find_element(by=By.XPATH, value="//input[contains(@autocomplete,'ccname')]").send_keys("Juan Jose Bello")
sleep(5)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
sleep(5)
suscribirse = driver.find_element(by=By.XPATH, value="//div[contains(@class,'SubmitButton-IconContainer')]").click()

sleep(15)
confirmacion = driver.find_element(by=By.XPATH, value="//a[contains(.,'Return to billing page')]").click()

btnbuy = driver.find_element_by_xpath("//a[contains(@id,'buy_licence')]").click()
sleep(5)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
sleep(3)             
"""
"""
#Aumentar la cantidad de cuentas agency
contadicion = 0

for mas in range (11):
    sleep(3)
    if mas < 11:
        aumentaragency = driver.find_element_by_xpath("//*[@id='kt_content']/div/div/app-buy/div[2]/div[3]/div/div/div[14]/div/button[2]").click()
        print(f"incremento:{contadicion}")
        contadicion +=1
        if mas == 10:
            sleep(3)
            call = driver.find_element(by=By.XPATH, value="//button[contains(@class,'btn btn-success')]").click()
            sleep(3)
            handles = driver.window_handles 
            for i in handles:       
                driver.switch_to.window(i) 
                print(driver.title)  
            sleep(3)               
            agendar = driver.find_element(by=By.XPATH, value="//div[contains(@class,'DKTIFpsb_BvUKsL5bGP2 Ycu0Thh4F4paU6_41lGw')]").click()  
            sleep(5)
            driver.switch_to.window(driver.window_handles[0])         
        
#Disminuir la cantidad de cuentas agency
for mas in range (10):
    sleep(3)
    if mas < 10:
        disminuiragency = driver.find_element_by_xpath("//*[@id='kt_content']/div/div/app-buy/div[2]/div[3]/div/div/div[14]/div/button[1]").click()
        print(f"disminuye:{contadicion}")
        contadicion -=1

buyagency = driver.find_element(by=By.XPATH, value="(//button[contains(@type,'button')])[3]").click() 
driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
payagency = driver.find_element(by=By.XPATH, value="//button[@type='button'][contains(.,'Go to pay')]").click()
#realizar una compra
sleep(5)
codpromo = driver.find_element(by=By.XPATH, value="//input[contains(@name,'promotionCode')]").click()
sleep(5)
codigo = driver.find_element(by=By.XPATH, value="(//input[contains(@type,'text')])[1]").send_keys("100PORTEROFF45")
sleep(5)
aplicar = driver.find_element_by_xpath("//span[contains(.,'Aplicar')]").click()
sleep(6)
numtarjeta = driver.find_element(by=By.XPATH, value="//input[contains(@id,'cardNumber')]").click()
sleep(5)
numero = driver.find_element(by=By.XPATH, value="//input[contains(@name,'cardNumber')]").send_keys("4859 5303 3623 4950")
sleep(3)
fechavencimiento = driver.find_element(by=By.XPATH, value="//input[contains(@name,'cardExpiry')]").click()
sleep(3)
fecha = driver.find_element(by=By.XPATH, value="//input[contains(@name,'cardExpiry')]").send_keys("0225")
sleep(3)
cvc = driver.find_element(by=By.XPATH, value="//input[contains(@name,'cardCvc')]").click()
sleep(3)
numcvc = driver.find_element(by=By.XPATH, value="//input[contains(@name,'cardCvc')]").send_keys("278")
sleep(3)
nombre = driver.find_element(by=By.XPATH, value="//input[contains(@autocomplete,'ccname')]").click()
sleep(3)
nombrecompleto = driver.find_element(by=By.XPATH, value="//input[contains(@autocomplete,'ccname')]").send_keys("Juan Jose Bello")
sleep(5)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
sleep(5)
suscribirse = driver.find_element(by=By.XPATH, value="//div[contains(@class,'SubmitButton-IconContainer')]").click()

sleep(15)
confirmacion = driver.find_element(by=By.XPATH, value="//a[contains(.,'Return to billing page')]").click()

#agendar = driver.find_element_by_xpath("//div[contains(@class,'DKTIFpsb_BvUKsL5bGP2 Ycu0Thh4F4paU6_41lGw')]").click()
#atras = driver.find_element(by=By.XPATH, value="//span[contains(.,'Atrás')]").click()


#driver.switch_to.window(driver.window_handles[0])
sleep(5)
#Modulo de acceso para hacer reportes 
#reportes = driver.find_element_by_xpath("//a[contains(@id,'make-report')]").click()
#sleep(5)
"""
"""

#linea para  hacer el for para los conectores hover_from_left
#Evalua si existe la clase para ingresar a cada conector y evalua si esta o no habilitado
estado = driver.find_element(by=By.TAG_NAME, value="div")
tarjetaconector = driver.find_elements(by=By.CSS_SELECTOR, value=(".card-custom"))
listaapps = ["linkedin-pages-enabled","facebook-ads-enabled", "instagram-insights-enabled","facebook-insights-enabled", "hubspot-enabled", "shopify-enabled", "woocommerce-enabled", "facebook-public-data-enabled", "twitter-ads-enabled", "tiktok-ads-enabled", "google-my-business-enabled", "linkedin-ads-enabled", "twitter-organic-analytics-enabled"]
#Recorre cada conector habilitado y elimina una cuenta 
for listaapp in listaapps:
    print(f"Probando: {listaapp}")
    name=None
    sleep(10)
    try:
        name = driver.find_element(by=By.CSS_SELECTOR, value=f".{listaapp}")
    except  NoSuchElementException as e:
        print("no esta habilitado la app")
    if name:
        name.click()
        sleep(5)
        agrupar = driver.find_element_by_xpath("//*[@id='kt_content']/div/div/app-app-connector/div[2]/div/div/div[1]/div[2]/a").click()
        sleep(3)
        desagrupar = driver.find_element_by_xpath("//*[@id='kt_content']/div/div/app-app-connector/div[2]/div/div/div[1]/div[2]/a").click()
        eliminar = driver.find_elements(by=By.CLASS_NAME, value=("btn-light-danger"))
        cont = 0
        for borrar in eliminar:
            print(f"Probando el eliminar: {cont}") 
            cont +=1
            sleep(5)
            if cont > 2: 
                borrar.click() 
                driver.back()
                sleep(3)
                break
        driver.back()
        
#modulo de acceso a los template
template = driver.find_element_by_xpath("//a[contains(@id,'use-template')]").click()
sleep(5)
driver.switch_to.window(driver.window_handles[0])
sleep(5)
#Modulo de acceso para hacer reportes 
reportes = driver.find_element_by_xpath("//a[contains(@id,'make-report')]").click()
sleep(5)
tab = driver.find_elements(by=By.CLASS_NAME, value="//div[@class='elementskit-infobox text-left text-left icon-lef-right-aligin elementor-animation- media gradient-active  hover_from_left'][contains(.,'Facebook Ads')]").click()
"""
print("Bienvenidos terricolas")
print(driver.title)
sleep(10)