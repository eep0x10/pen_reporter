<!--Checklist-->
## 5. Checklist

Tópico checklist tem a função de informar quais testes foram ou não realizados referente a aplicação em questão, tendo 3 possíveis respostas:

- "**Realizado**" o qual informa que foram feitos testes referentes ao tópico.
- "**Não realizado**" o qual informa que não foram feitos testes em relação ao tópico, e o mesmo existe na aplicação, porém por questões externas (como limitação de escopo ou tempo) o mesmo não foi realizado.
- "**Não se aplica**" o qual informa que o teste não foi realizado, pois não faz sentido para a aplicação em questão, por conta de funcionalidades as quais estão atreladas ao teste não existirem na mesma, ou estar fora do escopo solicitado de testes.

<!--Cores Tabela-->
<style>
    .heatMapCheck {
        width: 100%;
        text-align: center;
    }
    .heatMapCheck th {
        background: grey;
        word-wrap: break-word;
        text-align: center;
    }
    .heatMapCheck tr:nth-child(1) { background: green; }
    .heatMapCheck tr:nth-child(2) { background: red; }
    .heatMapCheck tr:nth-child(3) { background: orange; }
    .heatMapCheck td:nth-child(1) { background: white; }
</style>

<div class="heatMapCheck">

<!--Preencher Checklist, e alterar cores equivalentes-->
| Teste realizado | Check |
| --- | --- |
| Testes de Privilégio (ex: Escalação de Privilégio Horizontal ou Vertical) | Realizado |
| Testes de Autorização (ex: IDOR) | Não realizado |
| Testes de Autenticação (ex: Bypass Login, Weak Password, CAPTCHA) | Não se aplica |
| Testes de Token (ex: JWT, JWE) |?|
| Testes de Cookie (ex: Flag Secure, Flag HTTPOnly) |?|
| Testes Lógicos (ex: Alteração do Fluxo lógico) |?|
| Testes de Input de Dados (ex: Injections, SSRF) |? |
| Testes de Envio de Arquivos (ex: Bypass File Upload, Envio de N Arquivos) |?|
| Teste de Carga (ex: Brute Force, Limite Requisição, DOS) |?|
| Testes HTTP Header (ex: CRLF, Open Redirect) |?|
| Security Misconfiguration (ex: robots.txt, Information Exposure) |?|
| Enumeração |?|
| Componentes Desatualizados |?|
| Criptografía/Canal de Comunicacao (ex: Uso de SSL/criptografía) |?|
</div>

<div style="page-break-after: always; visibility: hidden"> 
</div>