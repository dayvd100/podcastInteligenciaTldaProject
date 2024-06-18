# Projeto de Extração e Visualização de Visualizações do YouTube 

## Descrição 

Este projeto extrai o número de visualizações de vídeos de várias playlists do YouTube e gera um gráfico de barras mostrando o total de visualizações por playlist. 

## Como Rodar o Projeto

## Passo 1: Configurar o Selenium

Você precisará do ChromeDriver para rodar o Selenium com o Google Chrome. Baixe o ChromeDriver compatível com a versão do seu Chrome (ou com o browser que você usa) e coloque-o no seu PATH. 

Passo 2: Executar o Script de Extração de Dados 
Passo 3: Executar o Script de Visualização de Dados 

### Considerações Finais

**Validação dos Dados:** Você pode adicionar verificações para garantir que os dados foram extraídos corretamente, como verificar se há duplicatas ou entradas vazias. 
**Otimização:** Se a extração dos dados for lenta, considere otimizar a espera dos elementos ou aumentar o tempo de espera no `WebDriverWait`.

## Dependências 

Certifique-se de ter as seguintes dependências instaladas:

- BeautifulSoup 
- Selenium 
- Pandas 
- Matplotlib
  
Você pode instalá-las usando os comandos abaixo:

```bash
pip install beautifulsoup4
pip install selenium
pip install pandas
pip install matplotlib


