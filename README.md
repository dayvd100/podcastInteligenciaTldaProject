Projeto de Extração e Visualização de Visualizações do YouTube
Descrição
Este projeto extrai o número de visualizações de vídeos de várias playlists do YouTube e gera um gráfico de barras mostrando o total de visualizações por playlist.

Dependências
Certifique-se de ter as seguintes dependências instaladas:

BeautifulSoup
Selenium
Pandas
Matplotlib
Você pode instalá-las usando os comandos abaixo:

bash
Copiar código
pip install beautifulsoup4
pip install selenium
pip install pandas
pip install matplotlib
Como Rodar o Projeto
Passo 1: Configurar o Selenium
Você precisará do ChromeDriver para rodar o Selenium com o Google Chrome. Baixe o ChromeDriver compatível com a versão do seu Chrome (ou com o navegador que você usa) e coloque-o no seu PATH.

Passo 2: Executar o Script de Extração de Dados
Execute o script inteligencia_ltda_proj.py para extrair os dados das playlists do YouTube.

bash
Copiar código
python inteligencia_ltda_proj.py
Passo 3: Executar o Script de Visualização de Dados
Execute o script show_graphic.py para gerar e visualizar o gráfico de barras com o número de visualizações por playlist.

bash
Copiar código
python show_graphic.py
Considerações Finais
Validação dos Dados: Você pode adicionar verificações para garantir que os dados foram extraídos corretamente, como verificar se há duplicatas ou entradas vazias.
Otimização: Se a extração dos dados for lenta, considere otimizar a espera dos elementos ou aumentar o tempo de espera no WebDriverWait.
