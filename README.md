<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <title>Projeto Final de POO – Gerenciamento de Voos</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      line-height: 1.6;
      max-width: 900px;
      margin: 40px auto;
      padding: 0 20px;
      background-color: #f9f9f9;
      color: #333;
    }
    h1, h2, h3 {
      color: #005f73;
    }
    code {
      background-color: #eee;
      padding: 2px 6px;
      border-radius: 4px;
      font-size: 0.95em;
    }
    table {
      width: 100%;
      border-collapse: collapse;
      margin-top: 20px;
    }
    th, td {
      border: 1px solid #ddd;
      padding: 10px;
      text-align: left;
    }
    th {
      background-color: #e0f7fa;
    }
    pre {
      background-color: #f4f4f4;
      padding: 10px;
      overflow-x: auto;
      border-left: 4px solid #005f73;
    }
  </style>
</head>
<body>

  <h1>✈️ Projeto Final de Programação Orientada a Objetos – Gerenciamento de Voos</h1>

  <p>Este projeto foi desenvolvido como trabalho final da disciplina <strong>Programação Orientada a Objetos (POO)</strong>, sob orientação do professor <strong>Demetrios</strong>, no curso <strong>Técnico Integrado em Informática</strong> do <strong>IFRN – Campus Pau dos Ferros</strong>.</p>

  <h2>👨‍💻 Desenvolvedores</h2>
  <ul>
    <li><strong>Heitor Ferreira</strong></li>
    <li><strong>Robson Junior</strong></li>
    <li><strong>Fabricio Osorio</strong></li>
  </ul>

  <h2>🧠 Objetivo do Projeto</h2>
  <p>O objetivo do projeto é simular um <strong>Sistema de Gerenciamento de Voos</strong>, utilizando os princípios da Programação Orientada a Objetos. O sistema é composto por diversas classes que representam os diferentes componentes de uma companhia aérea, como passageiros, funcionários, voos, aeronaves e bagagens.</p>

  <h2>🧩 Estrutura de Classes</h2>
  <p>O projeto foi modelado com várias classes interligadas, utilizando conceitos de <em>composição</em>, <em>herança</em>, <em>métodos abstratos</em>, <em>mixins</em>, e <em>encapsulamento</em>.</p>

  <h3>📦 Classes criadas:</h3>
  <table>
    <thead>
      <tr>
        <th>Classe</th>
        <th>Descrição</th>
      </tr>
    </thead>
    <tbody>
      <tr><td>Logavel (ABC)</td><td>Interface para qualquer entidade que deva registrar entradas (logar).</td></tr>
      <tr><td>IdentificavelMixin</td><td>Geração automática de ID único (UUID).</td></tr>
      <tr><td>AuditavelMixin</td><td>Registra ações para auditoria (logs com carimbo de tempo).</td></tr>
      <tr><td>Pessoa</td><td>Classe base com informações genéricas de uma pessoa (nome, CPF, etc).</td></tr>
      <tr><td>Bagagem</td><td>Representa uma bagagem vinculada a um passageiro.</td></tr>
      <tr><td>Passageiro</td><td>Herda de Pessoa e representa passageiros em voos.</td></tr>
      <tr><td>Funcionario</td><td>Herda de Pessoa, Logavel, IdentificavelMixin e AuditavelMixin.</td></tr>
      <tr><td>MiniAeronave</td><td>Contém dados técnicos de aeronaves pequenas utilizadas nos voos.</td></tr>
      <tr><td>Voo</td><td>Representa um voo específico com data, rota, passageiros, tripulação, etc.</td></tr>
      <tr><td>CompanhiaAerea</td><td>Classe agregadora de voos, representando a companhia aérea.</td></tr>
    </tbody>
  </table>

  <h2>💻 Tecnologias Utilizadas</h2>
  <ul>
    <li>Python 3.10+</li>
    <li>Programação Orientada a Objetos (POO)</li>
    <li>abc (Abstract Base Classes)</li>
    <li>uuid</li>
    <li>datetime</li>
  </ul>

  <h2>🧪 Exemplos de Funcionalidades</h2>
  <ul>
    <li>Cadastro e autenticação de funcionários</li>
    <li>Criação e atribuição de voos</li>
    <li>Registro de bagagens por passageiro</li>
    <li>Identificação única de todas as entidades</li>
    <li>Logs e auditoria de ações do sistema</li>
  </ul>

  <h2>🚀 Como Executar o Projeto</h2>
  <pre>
1. Clone este repositório:
git clone https://github.com/seu-usuario/seu-repositorio.git

2. Acesse o diretório do projeto:
cd gerenciamento-de-voos

3. Execute o script principal:
python main.py
  </pre>

  <h2>📚 Aprendizados</h2>
  <p>Durante o desenvolvimento, foram aplicados e consolidados os principais conceitos da Programação Orientada a Objetos em Python, como:</p>
  <ul>
    <li>Herança múltipla com mixins</li>
    <li>Classes abstratas e polimorfismo</li>
    <li>Encapsulamento e validação</li>
    <li>Composição entre objetos</li>
    <li>Projeto modular e reutilizável</li>
  </ul>

  <h2>🏁 Considerações Finais</h2>
  <p>Este projeto representa o encerramento da disciplina de POO e a consolidação de conhecimentos importantes para o desenvolvimento de sistemas orientados a objetos no mundo real. Agradecemos ao professor <strong>Demetrios</strong> pela orientação e ao IFRN pelo suporte técnico e educacional.</p>

  <hr>

  <p><em>IFRN – Instituto Federal do Rio Grande do Norte<br>
  Campus Pau dos Ferros<br>
  Curso Técnico Integrado em Informática</em></p>

</body>
</html>
