import requests
import logging
import time

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[logging.FileHandler('C:/Pipeline de Dados Econômicos do Brasil/logs/extract.log', encoding='utf-8'),
                               logging.StreamHandler()])

url_selic = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados?formato=json&dataInicial=01/01/2023&dataFinal=31/12/2023"
def buscar_selic(url, headers=None, params=None):
    MAX_TENTATIVAS = 3
    TIMEOUT = 10


    for tentantiva in range(1, MAX_TENTATIVAS + 1):
        logging.info(f"Tentativa {tentantiva}/{MAX_TENTATIVAS} - acessando a url {url}")
        try:

            response = requests.get(url=url, params=params, headers=headers, timeout=TIMEOUT)
            response.raise_for_status()
            dados = response.json()

            if not dados:
                logging.warning("Nenhum dado foi encontrado.")
                return None
            logging.info("Extração concluida!")
            return dados
        # Tratamento de erros
        except requests.exceptions.HTTPError as errh:
            logging.error(f"Erro de HTTP (Servidor recusou): {errh}")
        
            if response.status_code == 429:
                logging.warning("Ocorreu erro por muita tentativa de request. Tente novament em 10 segundos.")
                time.sleep(10)
                continue
            if response.status_code in [401, 403, 404]:
                logging.critical(f"Erro critico ao fazer request. Não Autorizado ou Não existe.")
                break
        except requests.exceptions.ConnectionError as errc:
            logging.error(f'Erro de conexão. {errc}')
        except requests.exceptions.Timeout as errt:
            logging.error(f'Timeout. A APi demorou mais de {TIMEOUT} pra responder.')
        except Exception as e:
            logging.critical(f"Erro inesperado. {e}")
            break
    if tentantiva < MAX_TENTATIVAS:
        logging.info("Aguardando 3 segundos pra tentar novamente.")
        time.sleep(3)
    logging.error("Todas tentativas falharam")
    return None

