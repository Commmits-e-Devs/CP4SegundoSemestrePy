servicos = {
     "login": {
     "criticidade": 3,
     "descricao": "acesso ao sistema"
     },
     "pagamento": {
     "criticidade": 5,
     "descricao": "processamento de pagamentos"
     },
     "relatorio": {
     "criticidade": 2,
     "descricao": "geracao de relatorios"
     },
     "notificacoes": {
     "criticidade": 1,
     "descricao": "envio de avisos ao usuario"
     }
}

def exibir_perguntas():
     nome = input("Digite o serviço: ")
     sintomas = input("Digite os sintomas: ").split(", ")
     return nome, sintomas

def consultar_servico(servicos,nome,erro="Serviço não encontrado."):
     if nome in servicos:
          return servicos[nome]
     return erro

def consultar_sintomas(*sintomas):
     lista = []
     for sintoma in sintomas:
          lista.append(sintoma)
     return lista

nome, sintomas = exibir_perguntas()
resultado = consultar_servico(servicos, nome)
print(consultar_sintomas(*sintomas))