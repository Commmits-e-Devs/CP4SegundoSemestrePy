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
     quantidadeDePessoasAfetadas = int(input("Digite a quantidade de pessoas afetadas: "))
     caiu = input("O sistema caiu, Digite S/N :")
     return nome, sintomas, quantidadeDePessoasAfetadas, caiu

def consultar_servico(servicos, nome, erro="Serviço não encontrado."):
     if nome in servicos:
          return servicos[nome]
     return erro

def consultar_sintomas(*sintomas):
     lista = []
     for sintoma in sintomas:
          lista.append(sintoma)
     return lista

def verificarPontos(quantidadeDePessoasAfetadas, caiu):
     ponts = 0
     caiu_bool = caiu.strip().upper() == "S"

     if caiu_bool and quantidadeDePessoasAfetadas >= 200:
          ponts += 14
     elif caiu_bool and quantidadeDePessoasAfetadas >= 100:
          ponts += 10
     elif quantidadeDePessoasAfetadas >= 200:
          ponts += 7
     elif quantidadeDePessoasAfetadas >= 100:
          ponts += 5
     return ponts

calculo_prioridade = lambda ponts: f"Prioridade alta: {ponts}" if ponts >= 7 else f"prioridade normal: {ponts}"

nome, sintomas, quantidadeDePessoasAfetadas, caiu = exibir_perguntas()
resultado = consultar_servico(servicos, nome)

ponts = verificarPontos(quantidadeDePessoasAfetadas, caiu)

print(resultado)
print(consultar_sintomas(*sintomas))
print(calculo_prioridade(ponts))

