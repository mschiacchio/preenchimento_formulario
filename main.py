from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import re


webdriver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

#Tarefa 1
def cadastrarInformacoes():

    url = 'https://onfly-rpa-forms-62njbv2kbq-uc.a.run.app/'

    webdriver.get(url)

    try:
        formulario = WebDriverWait(webdriver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="payment-form"]')))
        print('O formulário foi identificado na página, prosseguindo...')
    except:
        print('O formulário não foi identificado na página.')

    #Dados fictícios
    nome = 'Marcos dos Santos Moreira'
    endereco = 'Rua Alvorada 876'
    cidade = 'Belo Horizonte'
    estado = 'Minas Gerais'
    cep = '30541228'
    telefone = '31999274853'
    email = 'marcos_santos@gmail.com'
    num_cartao_credito = '1457986523154789'
    dta_val_cartao = '05/2032'
    cvv_cartao = '542'

    #Inserção dos dados nos inputs
    #Nome
    label_nome = WebDriverWait(webdriver, 10).until(EC.presence_of_element_located((By.XPATH, "//label[contains(text(), 'Nome Completo')]")))
    input_nome = webdriver.find_element(By.ID, label_nome.get_attribute("for"))
    input_nome.send_keys(nome)
    #Telefone
    label_telefone = WebDriverWait(webdriver, 10).until(EC.presence_of_element_located((By.XPATH, "//label[contains(text(), 'Telefone')]")))
    input_telefone = webdriver.find_element(By.ID, label_telefone.get_attribute("for"))
    input_telefone.send_keys(telefone)
    #Email
    label_email = WebDriverWait(webdriver, 10).until(EC.presence_of_element_located((By.XPATH, "//label[contains(text(), 'E-mail')]")))
    input_email = webdriver.find_element(By.ID, label_email.get_attribute("for"))
    validacao_email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(validacao_email, email):
        return 'O email inserido é inválido :('
    else:
        print('Email válido! :)')
        input_email.send_keys(email)

    btnProx = WebDriverWait(webdriver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="next-btn"]')))
    btnProx.click()

    #CEP
    label_cep = WebDriverWait(webdriver, 10).until(EC.presence_of_element_located((By.XPATH, "//label[contains(text(), 'CEP')]")))
    input_cep = webdriver.find_element(By.ID, label_cep.get_attribute("for"))
    input_cep.send_keys(cep)
    #Endereço
    label_endereco = WebDriverWait(webdriver, 10).until(EC.presence_of_element_located((By.XPATH, "//label[contains(text(), 'Endereço')]")))
    input_endereco = webdriver.find_element(By.ID, label_endereco.get_attribute("for"))
    input_endereco.send_keys(endereco)
    #Cidade
    label_cidade = WebDriverWait(webdriver, 10).until(EC.presence_of_element_located((By.XPATH, "//label[contains(text(), 'Cidade')]")))
    input_cidade = webdriver.find_element(By.ID, label_cidade.get_attribute("for"))
    input_cidade.send_keys(cidade)
    #Estado
    label_estado = WebDriverWait(webdriver, 10).until(EC.presence_of_element_located((By.XPATH, "//label[contains(text(), 'Estado')]")))
    input_estado = webdriver.find_element(By.ID, label_estado.get_attribute("for"))
    input_estado.send_keys(estado)

    btnProx.click()

    #Nome
    label_titular = WebDriverWait(webdriver, 10).until(EC.presence_of_element_located((By.XPATH, "//label[contains(text(), 'Nome do Titular')]")))
    input_nome = webdriver.find_element(By.ID, label_titular.get_attribute("for"))
    input_nome.send_keys(nome)
    #Número do cartão de crédito
    label_num_cartao = WebDriverWait(webdriver, 10).until(EC.presence_of_element_located((By.XPATH, "//label[contains(text(), 'Número do Cartão')]")))
    input_num_cartao = webdriver.find_element(By.ID, label_num_cartao.get_attribute("for"))
    input_num_cartao.send_keys(num_cartao_credito)
    #Data de validade do cartão de crédito
    label_val_cartao = WebDriverWait(webdriver, 10).until(EC.presence_of_element_located((By.XPATH, "//label[contains(text(), 'Data de Validade')]")))
    input_val_cartao = webdriver.find_element(By.ID, label_val_cartao.get_attribute("for"))
    input_val_cartao.send_keys(dta_val_cartao)
    #CVV do cartão de crédito
    label_cvv_cartao = WebDriverWait(webdriver, 10).until(EC.presence_of_element_located((By.XPATH, "//label[contains(text(), 'CVV')]")))
    input_cvv_cartao = webdriver.find_element(By.ID, label_cvv_cartao.get_attribute("for"))
    input_cvv_cartao.send_keys(cvv_cartao)

    btnProx.click()

    #Verificando se a mensagem de sucesso apareceu
    try:
        msg_sucesso = WebDriverWait(webdriver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "congrats-wrapper")))
        display_msg_sucesso = msg_sucesso.value_of_css_property("display")
        if display_msg_sucesso == "block":
            return 'Formulário preenchido e enviado com sucesso!'
        else:
            print(f"A mensagem de sucesso foi localizada, mas não está visível na tela.")
    except:
        print('Não identificou a mensagem de formulário concluído.')

    #webdriver.quit()

#Tarefa 2
def alterarTextos():
    try:
        ps = webdriver.find_elements(By.TAG_NAME, 'p')
        for p in ps:
            webdriver.execute_script("arguments[0].innerText = arguments[1];", p, 'Texto alterado')
        return 'Todos os <p> foram alterados para "Texto alterado"!'
    except:
        return 'Erro ao alterar os <p> para "Texto alterado"'

if __name__ == '__main__':
    resultado_cadastrar_infos = cadastrarInformacoes()
    print(resultado_cadastrar_infos)
    resultado_alterar_textos = alterarTextos()
    print(resultado_alterar_textos)
