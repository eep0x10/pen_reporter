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
<table>
    <tr>
        <td>Teste realizado</td>
        <td>Check</td>
    </tr>
    <tr>
        <td>Testes de Privilégio (ex: Escalação de Privilégio Horizontal ou Vertical)</td>
        <td>Realizado</td>
    </tr>
    <tr>
        <td>Testes de Autorização (ex: IDOR)</td>
        <td>Não realizado</td>
    </tr>
    <tr>
        <td>Testes de Autenticação (ex: Bypass Login, Weak Password, CAPTCHA)</td>
        <td>Não se aplica</td>
    </tr>
    <tr>
        <td>Testes de Token (ex: JWT, JWE)</td>
        <td>?</td>
    </tr>
    <tr>
        <td>Testes de Cookie (ex: Flag Secure, Flag HTTPOnly)</td>
        <td>?</td>
    </tr>
    <tr>
        <td>Testes Lógicos (ex: Alteração do Fluxo lógico)</td>
        <td>?</td>
    </tr>
    <tr>
        <td>Testes de Input de Dados (ex: Injections, SSRF)</td>
        <td>?</td>
    </tr>
    <tr>
        <td>Testes de Envio de Arquivos (ex: Bypass File Upload, Envio de N Arquivos)</td>
        <td>?</td>
    </tr>
    <tr>
        <td>Teste de Carga (ex: Brute Force, Limite Requisição, DOS)</td>
        <td>?</td>
    </tr>
    <tr>
        <td>Testes HTTP Header (ex: CRLF, Open Redirect)</td>
        <td>?</td>
    </tr>
    <tr>
        <td>Security Misconfiguration (ex: robots.txt, Information Exposure)</td>
        <td>?</td>
    </tr>
    <tr>
        <td>Enumeração</td>
        <td>?</td>
    </tr>
    <tr>
        <td>Componentes Desatualizados</td>
        <td>?</td>
    </tr>
    <tr>
        <td>Criptografía/Canal de Comunicacao (ex: Uso de SSL/criptografía)</td>
        <td>?</td>
    </tr>
</table>
</div>

<!--Fim da Página-->
<div style="page-break-after: always; visibility: hidden"> 
</div>
<div style="background-color: #01ff5f;height: 20px;width: 900px;margin-bottom: 15px;border: 1px solid black;position: vertical-align: top;"></div>
<br>