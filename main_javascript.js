const { Builder, By, until } = require('selenium-webdriver');
const chrome = require('selenium-webdriver/chrome');
const path = require('path');

let webdriver;
const url = 'https://onfly-rpa-forms-62njbv2kbq-uc.a.run.app/';

async function instancia_webdriver() {
    webdriver = await new Builder().forBrowser('chrome').setChromeOptions(new chrome.Options()).build();
}

async function cadastrarInformacoes() {
    try {
        await webdriver.get(url);

        // Tarefa 1: Identificar o formulário
        let formulario = await webdriver.wait(until.elementLocated(By.xpath('//*[@id="payment-form"]')), 10000);
        console.log('O formulário foi identificado na página, prosseguindo...');

        // Dados fictícios
        let dados = {
            nome: 'Marcos dos Santos Moreira',
            endereco: 'Rua Alvorada 876',
            cidade: 'Belo Horizonte',
            estado: 'Minas Gerais',
            cep: '30541228',
            telefone: '31999274853',
            email: 'marcos_santos@gmail.com',
            num_cartao_credito: '1457986523154789',
            dta_val_cartao: '05/2032',
            cvv_cartao: '542'
        };

        // Inserção dos dados nos inputs
        async function preencherCampo(labelText, valor) {
            let label = await webdriver.wait(until.elementLocated(By.xpath(`//label[contains(text(), '${labelText}')]`)), 10000);
            let inputId = await label.getAttribute('for');
            let input = await webdriver.findElement(By.id(inputId));
            await input.sendKeys(valor);
        }

        // Verificar e preencher os campos
        await preencherCampo('Nome Completo', dados.nome);
        await preencherCampo('Telefone', dados.telefone);
        await preencherCampo('E-mail', dados.email);

        // Validação do e-mail
        let emailRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
        if (!emailRegex.test(dados.email)) {
            return 'O email inserido é inválido :(';
        } else {
            console.log('Email válido! :)');
        }

        // Clicar no botão "Próximo"
        let btnProx = await webdriver.wait(until.elementLocated(By.xpath('//*[@id="next-btn"]')), 10000);
        await btnProx.click();

        // Continuar preenchendo os outros campos
        await preencherCampo('CEP', dados.cep);
        await preencherCampo('Endereço', dados.endereco);
        await preencherCampo('Cidade', dados.cidade);
        await preencherCampo('Estado', dados.estado);

        await btnProx.click();

        // Preencher informações do cartão de crédito
        await preencherCampo('Nome do Titular', dados.nome);
        await preencherCampo('Número do Cartão', dados.num_cartao_credito);
        await preencherCampo('Data de Validade', dados.dta_val_cartao);
        await preencherCampo('CVV', dados.cvv_cartao);

        await btnProx.click();

        // Verificar se a mensagem de sucesso apareceu
        let msgSucesso = await webdriver.wait(until.elementLocated(By.className('congrats-wrapper')), 10000);
        let displayMsgSucesso = await webdriver.executeScript("return window.getComputedStyle(arguments[0]).display;", msgSucesso);

        if (displayMsgSucesso === 'block') {
            return 'Formulário preenchido e enviado com sucesso!';
        } else {
            return 'A mensagem de sucesso foi localizada, mas não está visível na tela.';
        }

    } catch (error) {
        console.error('Erro:', error);
        return 'Erro ao preencher o formulário.';
    } finally {
        //await webdriver.quit();
    }
}

async function alterarTextos() {
    try {
        // Identificar todos os <p> na página
        let ps = await webdriver.findElements(By.tagName('p'));
        for (let p of ps) {
            await webdriver.executeScript("arguments[0].innerText = arguments[1];", p, 'Texto alterado');
        }
        return 'Todos os <p> foram alterados para "Texto alterado"!';

    } catch (error) {
        console.error('Erro:', error);
        return 'Erro ao alterar os <p> para "Texto alterado"';
    } finally {
        //await webdriver.quit();
    }
}

(async function main() {
    await instancia_webdriver();

    let resultadoCadastrarInfos = await cadastrarInformacoes();
    console.log(resultadoCadastrarInfos);

    let resultadoAlterarTextos = await alterarTextos();
    console.log(resultadoAlterarTextos);
})();
