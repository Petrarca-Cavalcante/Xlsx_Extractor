# Xlsx_Extractor

#### O projeto Xlsx_Extractor é uma aplicação desenvolvida em Python que coleta dados de funcionários a partir de uma planilha de uma empresa e os prepara para envio a uma API. Esses dados serão usados para a integração de planos de saúde.

---
### Instalando dependências 

Após extrair o .zip do projeto e acessar a pasta Xlsx_Extractor é necessário:

* Criar um ambiente virtual (venv) - ``` python3 -m venv venv```
* Acessar o ambiente virtual ( linux / windows )
  
   ``` source venv/bin/activate ```
  
   ``` source venv/scripts/activate ```

* Instalar as dependências - ``` pip install -r requirements.txt"  ```
* Rodar o projeto - ``` python3 main.py ```
  
---
#### A API deve estar ativa antes de rodar esta aplicação. Quando a aplicação está funcionando normalmente, cada registro de funcionário coletado da planilha e enviado para a API será exibido no terminal junto com o código de status retornado.
