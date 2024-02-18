# Flask API

**HTTP (Hypertext Transfer Protocol):** protocolo de comunicação utilizado na web para transferir dados entre um cliente e um servidor.

**HTTPS (Hypertext Transfer Protocol Secure):** protocolo de comunicação utilizado na web para transferir dados entre um cliente e um servidor seguro. Encriptado.

**Métodos de requisição HTTP**

- GET: faz uma consulta a um registro ou uma coleção de registros do servidor.
- POST: envia dados para criar um 'novo registro' no servidor.
- PUT: envia dados para atualizar um 'registro existente' no servidor.
- DELETE: excluir registros do servidor
- PATCH: envia dados para atualizar parcialmente um registro existente no servidor.

Todo método passa por 4 elementos:

- CONNECT: é usado para abrir uma conexão de com o servidor remoto.
- OPTIONS: é usado para descrever asopções de comunicação para um recurso específico.
- TRACE: foi projetado parafins de diagnósticodurante o desenvolvimento.
- HEAD: recupera os cabeçalhos do recurso específico do próprio recurso.

Certificado de segurança SSL (Secure Sockets Layer) é um protocolo de segurança da Internet baseado em criptografia.
Empresas precisam de certificados para garantir que o site é seguro, um comum é o letsencrypt.

** API (Application Programming Interface):** são interfaces que permitem a counicação e a integração entre diferentes aplicações desoftware (sites, aplicativos e dispositivos).

Mais conhecidas: REST and SOAP

- _SOAP_ é como um envelope.
  é um protocolo oficial mantido pela World Wide Web Consortium (W3C).
- _REST_ é como um cartão postal.
  é um conjunto de diretrizes que oferece uma implementação mais flexível.

**CRUD:** create (POST), read (GET), update (PUT), delete (DELETE).

**Estrutura de uma REST API com JSON**

Representational State Transfer.
**endpoint:** é um URL (Uniform Resource Locator) específico em um servidor que aguarda para receber uma requisição.
headers: são informações adicionais incluídas na requisição e na resposta HTTP.
**body:** é a parte da requisição ou resposta que contém os dados propriamente ditos.
response: formato JSON, XML.

Exemplo resposta JSON:
´´´
{
"employee": "Max Mustermann", "items": [
{
"name": "TestData", "quantity": "2"
},
{
"name": "Test2", "quantity": "3"
},
{
"name": "Test3", "quantity": "4"
}
],
"table": "Tisch 5"
}
´´´

**FLASK**<br>
Flask é um micro framework escrito em Python que permite criar aplicativos web de forma ágil e flexível.
Ele é ideal para quem busca: simplicidade, rapidez, soluções para projetos pequenos e aplicações robustas.

o Flask é baseado no kit de ferramentas WSGI (Web Server Gateway Interface) e na biblioteca Jinja2.
WSGI é uma especificação para uma interface simples e universal entre servidores web e aplicações web ou frameworks escritos em Python. O WSGI é uma camada intermediária que fica entre o servidor web e a sua aplicação Python.

Etapas para criação da primeira aplicação Flask:
1- criar um ambiente virtual (py -3 -m venv .venv)
2- entrar no ambiente virtual (.\.venv\Scripts\activate)
3- instalar o Flask (pip install flask)
4- desenvolve aplicação
5- testa (flask --app app run)