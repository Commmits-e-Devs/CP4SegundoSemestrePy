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

equipes = {
    "login": "Equipe de Identidade",
    "pagamento": "Equipe de Pagamentos",
    "relatorio": "Equipe de Dados",
    "notificacoes": "Equipe de Comunicação"
}

def exibir_perguntas():
     nome = input("Digite o serviço: ")
     sintomas = input("Digite os sintomas: ").split(", ")
     quantidadeDePessoasAfetadas = int(input("Digite a quantidade de pessoas afetadas: "))
     caiu = input("O sistema caiu, Digite S/N :")
     return nome, sintomas, quantidadeDePessoasAfetadas, caiu

def consultar_equipe(nome, equipes):
     if nome in equipes:
          return equipes[nome]

def consultar_servico(servicos, nome, erro="Serviço não encontrado."):
     if nome in servicos:
          return servicos[nome]
     return erro

def consultar_sintomas(*sintomas):
     lista = []
     for sintoma in sintomas:
          lista.append(sintoma)
     return lista

# Validação de entrada inválida
def validar_entrada(nome, servicos, quantidadeDePessoasAfetadas, caiu):
     if nome not in servicos:
          return False, f"Erro: serviço '{nome}' não está cadastrado."

     if quantidadeDePessoasAfetadas < 0:
          return False, "Erro: a quantidade de pessoas afetadas não pode ser negativa."

     if caiu.strip().upper() not in ("S", "N"):
          return False, "Erro: resposta inválida para indisponibilidade. Use apenas S ou N."

     return True, "Entrada válida."

def verificarPontos(quantidadeDePessoasAfetadas, caiu, criticidade=0, qtd_sintomas=0):
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

     ponts += criticidade
     if qtd_sintomas >= 3:
          ponts += 3
     elif qtd_sintomas == 2:
          ponts += 2
     elif qtd_sintomas == 1:
          ponts += 1

     return ponts, f"Pontuação baseada em {quantidadeDePessoasAfetadas} usuários e criticidade {criticidade}"

calculo_prioridade = lambda ponts: f"Prioridade alta: {ponts}" if ponts >= 7 else f"prioridade normal: {ponts}"

def definir_prazo(prioridade):
     if "Prioridade alta" in prioridade:
          return "Ate 30 minutos"
     return "Ate 4 horas"

def processar_incidente(nome, sintomas, quantidadeDePessoasAfetadas, caiu):
     valido, mensagem_validacao = validar_entrada(
          nome=nome,
          servicos=servicos,
          quantidadeDePessoasAfetadas=quantidadeDePessoasAfetadas,
          caiu=caiu
     )

     if not valido:
          print(mensagem_validacao)
          return

     resultado = consultar_servico(servicos, nome)
     criticidade = resultado["criticidade"] if isinstance(resultado, dict) else 0
     lista_sintomas = consultar_sintomas(*sintomas)

     ponts, mensagem = verificarPontos(
          quantidadeDePessoasAfetadas=quantidadeDePessoasAfetadas,
          caiu=caiu,
          criticidade=criticidade,
          qtd_sintomas=len(lista_sintomas)
     )
     prioridade = calculo_prioridade(ponts)

     print(consultar_equipe(nome, equipes))
     print(resultado)
     print(lista_sintomas)
     print(mensagem)
     print(prioridade)
     print(definir_prazo(prioridade))

def executar_casos_de_teste():
     print("=" * 50)
     print("CASOS DE TESTE OBRIGATÓRIOS")
     print("=" * 50)

     print("\n--- Caso A ---")
     processar_incidente(
          "login",
          ["senha rejeitada", "tela retorna ao início"],
          20,
          "N",
     )

     print("\n--- Caso B ---")
     processar_incidente(
          "pagamento",
          ["checkout falha", "PIX indisponível", "cartão recusado"],
          250,
          "S"
     )

     print("\n" + "=" * 50)
     print("FIM DOS CASOS DE TESTE")
     print("=" * 50 + "\n")


executar_casos_de_teste()

nome, sintomas, quantidadeDePessoasAfetadas, caiu = exibir_perguntas()
processar_incidente(nome, sintomas, quantidadeDePessoasAfetadas, caiu)

