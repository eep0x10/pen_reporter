<!--Matriz-->
## 8. Matriz Vulnerabilidade

Para o cálculo de criticidade foi utilizado a metodologia utilizada pelo NIST CVSS [https://nvd.nist.gov/vuln-metrics/cvss](https://nvd.nist.gov/vuln-metrics/cvss). Abaixo segue um informativo para cada criticidade.

<!--Cores Tabela-->
<style>
    .heatMapMatriz {
        width: 100%;
        text-align: center;
    }
    .heatMapMatriz th {
        background: grey;
        word-wrap: break-word;
        text-align: center;
    }
    .heatMapMatriz tr:nth-child(1) { background: BlueViolet; }
    .heatMapMatriz tr:nth-child(2) { background: red; }
    .heatMapMatriz tr:nth-child(3) { background: orange; }
    .heatMapMatriz tr:nth-child(4) { background: green; }
    .heatMapMatriz tr:nth-child(5) { background: Lightgrey; }
    .heatMapMatriz td:nth-child(2) { background: white; }
</style>

<div class="heatMapMatriz">

|Criticidade|Descrição|
|---|---|
|**Vulnerabilidade Criticidade Crítica<br/>CVSS: 9.0 \> 10.0<br/>Deadline: 14 dias**|Vulnerabilidades de criticidade "Crítica" são caracterizadas por comprometer completamente a confidencialidade, integridade e avaliabilidade da aplicação, por meio de ataques de baixa complexidade ou da falta de privilégios requeridos para realização do ataque.Exemplo: SQL Injection, RCE (Remote Control Execution).|
|**Vulnerabilidade Criticidade Alta<br/>CVSS: 7.0 \> 8.9<br/>Deadline: 1 mês**|Vulnerabilidades de criticidade "Alta" são caracterizadas por comprometer quase totalmente a confidencialidade, integridade e avaliabilidade da aplicação.Exemplo: SSRF, Broken Authentication.|
|**Vulnerabilidade Criticidade Média<br/>CVSS: 4.0 \> 6.9<br/>Deadline: 4 meses**|Vulnerabilidades de criticidade "Média" são caracterizadas por comprometer parcialmente a confidencialidade, integridade e avaliabilidade da aplicação, por meio de ataques de alta complexidade ou do excesso de privilégios requeridos para realização do ataque.Exemplo: Improper Input Validation, CSRF.|
|**Vulnerabilidade Criticidade Baixa<br/>CVSS: 0.1 \> 3.9<br/>Deadline: 6 meses**|Vulnerabilidades de criticidade "Baixa" são caracterizadas por comprometer parcialmente a confidencialidade, integridade ou avaliabilidade da aplicação, como vazamento de dados sensíveis e falhas de configuração.Exemplo: Uncaught Exception, Clickjacking.|
|**Vulnerabilidade Criticidade Informativa<br/>CVSS: 0.0<br/>Deadline: Á definir**|Vulnerabilidades de criticidade "Informativa" são caracterizadas por não comprometer a confidencialidade, integridade e avaliabilidade da aplicação, são apenas recomendações de segurança.|
</div>