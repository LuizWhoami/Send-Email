import email.mime
import smtplib
import email.message
import requests

def enviar():
    corpo = """
    <!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Variáveis e Funções em Python</title>
    <style>
        .Sletter{
            color: #333;                
        }
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            background-color: #f9f9f9;
            color: #333;
            margin: 20px;
        }
        h1, h2 {
            color: #0078D7;
        }
        code {
            background-color: #f4f4f4;
            padding: 2px 4px;
            border-radius: 4px;
            font-family: monospace;
            font-size: 14px;
        }
        pre {
            background-color: #f4f4f4;
            padding: 10px;
            border-radius: 4px;
            overflow-x: auto;
            font-size: 14px;
        }
        .example {
            background-color: #e7f3ff;
            border-left: 4px solid #0078D7;
            padding: 10px;
            margin: 20px 0;
        }
    </style>
</head>
<body>
    <h1 class="Sletter">SL LETTER NEWS</h1>
    <h1>Variáveis e Funções em Python</h1>
    <p>Veja abaixo uma explicação didática e simples sobre variáveis e funções em Python.</p>

    <h2>1. Variáveis</h2>
    <p>Uma <strong>variável</strong> é como uma "caixa" onde você pode guardar um valor para usar mais tarde. Cada variável tem um <strong>nome</strong> e pode armazenar diferentes tipos de dados, como números, textos ou listas.</p>

    <h3>Como criar uma variável:</h3>
    <pre><code># Exemplos de variáveis
nome = "João"           # Texto (string)
idade = 25              # Número inteiro (int)
altura = 1.75           # Número decimal (float)
eh_estudante = True     # Verdadeiro/Falso (booleano)

# Imprimindo os valores
print(nome)             # Resultado: João
print(idade)            # Resultado: 25</code></pre>

    <h3>Dicas:</h3>
    <ul>
        <li>O nome da variável não pode começar com número.</li>
        <li>Evite usar caracteres especiais ou espaços.</li>
        <li>Use nomes descritivos, como <code>preco_produto</code> em vez de <code>x</code>.</li>
    </ul>

    <h2>2. Funções</h2>
    <p>Uma <strong>função</strong> é um conjunto de comandos que você pode reutilizar sempre que quiser. É como uma "receita" para executar uma tarefa específica.</p>

    <h3>Como criar uma função:</h3>
    <pre><code># Criando uma função simples
def saudacao():
    print("Olá! Seja bem-vindo!")

# Chamando a função
saudacao()  # Resultado: Olá! Seja bem-vindo!</code></pre>

    <h3>Funções com parâmetros:</h3>
    <pre><code># Função com parâmetros
def saudacao_personalizada(nome):
    print(f"Olá, {nome}! Seja bem-vindo!")

# Chamando a função com diferentes valores
saudacao_personalizada("Maria")  # Resultado: Olá, Maria! Seja bem-vindo!
saudacao_personalizada("Carlos")  # Resultado: Olá, Carlos! Seja bem-vindo!</code></pre>

    <h3>Funções que retornam valores:</h3>
    <pre><code># Função que soma dois números
def somar(a, b):
    return a + b

# Usando o retorno da função
resultado = somar(3, 5)
print(f"A soma é: {resultado}")  # Resultado: A soma é: 8</code></pre>

    <h2>Resumo</h2>
    <ul>
        <li><strong>Variáveis</strong>: guardam informações para serem usadas no programa.</li>
        <li><strong>Funções</strong>: ajudam a organizar o código e permitem reutilizar tarefas.</li>
    </ul>

    <div class="example">
        <h3>Exemplo final juntando variáveis e funções:</h3>
        <pre><code># Variáveis
nome = "Ana"
idade = 30

# Função para mostrar informações
def apresentar_pessoa(nome, idade):
    print(f"Essa é {nome}, que tem {idade} anos.")

# Chamando a função
apresentar_pessoa(nome, idade)</code></pre>
        <p><strong>Resultado:</strong></p>
        <p>Essa é Ana, que tem 30 anos.</p>
    </div>

</body>
</html>

    """
    banco = 'Email a enviar'
    msg = email.message.Message()
    msg['Subject'] = 'SLLATTER - Boas Práticas Com Python'
    msg['From'] = 'Seu Email'    
    msg['To'] = banco[0]
    passw = 'SUA KEY'
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo)


    envia = smtplib.SMTP('smtp.gmail.com: 587')
    envia.starttls()

    envia.login(msg['From'], passw)
    envia.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')

enviar()