from pipeline.extract.extract_bcb import buscar_selic

dados = buscar_selic("https://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados?formato=json&dataInicial=01/01/2023&dataFinal=07/07/2026")

print(dados[:3])