
#adicionar um contato na agenda
def adicionar_contato(contatos, nome_contato, telefone_contato, email_contato, contato_favorito):
  if not nome_contato or not telefone_contato or not email_contato:
    print("\nO contato não foi salvo na sua agenda :/ \nTodos os campos são obrigatórios!")
    return

  if not telefone_contato.isdigit() or len(telefone_contato) < 10:
    print("\nO número que você digitou não é válido!")
    return

  if "@" not in email_contato or ".com" not in email_contato:
    print("\nO endereço de e-mail que digitou é inválido!")
    return
  
  
  contato = {"Nome": nome_contato, "Telefone": telefone_contato, "E-mail": email_contato, "Contato favorito": contato_favorito}
  contatos.append(contato)
  print(f"\nO contato de {nome_contato} foi adicionado à sua agenda!")
  return

#visualizar os contatos existentes
def ver_contatos(contatos):
  if not contatos:
        print("\nVocê ainda não adicionou um contato em sua agenda. Adicione utilizando a opção 1.")
  else:         
    print("\nAqui estão os contatos salvos em sua agenda:")
    for indice, contato in enumerate(contatos, start=1):
      nome_contato = contato["Nome"]
      telefone_contato = contato["Telefone"]
      email_contato = contato["E-mail"]
      contato_favorito = "✔" if contato["Contato favorito"] == 'S' else "✘"
      print(f"\n{indice}. \nNome: {nome_contato} \nTelefone: {telefone_contato} \nE-mail: {email_contato} \nContato favorito? {contato_favorito}")
    return

#editar a lista de contatos
def editar_contato(contatos, indice_contato, novo_nome_contato, novo_telefone_contato, novo_email_contato, novo_contato_favorito):
  indice_contato_ajustado = int(indice_contato) - 1
  if 0 <= indice_contato_ajustado < len(contatos):
    if not novo_nome_contato or not novo_telefone_contato or not novo_email_contato:
      print("\nTodos os campos são obrigatórios!")
      return
    if not novo_telefone_contato.isdigit() or len(novo_telefone_contato) < 11:
      print("\nO número que você digitou não é válido!")
      return
    if "@" not in novo_email_contato or ".com" not in novo_email_contato:
      print("\nO endereço de e-mail que digitou é inválido!")
      return

    contato = contatos[indice_contato_ajustado]
    contato["Nome"] = novo_nome_contato
    contato["Telefone"] = novo_telefone_contato
    contato["E-mail"] = novo_email_contato
    contato["Contato favorito"] = novo_contato_favorito
    print(f"\nContato {novo_nome_contato} atualizado com sucesso!")
  else:
    print("\nNão foi possível localizar o contato indicado :/ ")

#adicionar ou remover um favorito com base na lista de contatos
def editar_favorito(contatos, indice_contato):
  indice_contato_favorito = int(indice_contato) - 1
  if 0 <= indice_contato_favorito < len(contatos):
    contato = contatos[indice_contato_favorito]
    if contato["Contato favorito"].upper() == 'S':
      contato["Contato favorito"] = 'N'
      print(f"\nO contato {contato['Nome']} foi removido dos favoritos.")
    else:
      contato["Contato favorito"] = 'S'
      print(f"\nO contato {contato['Nome']} foi marcado como favorito.")
  else:
      print("\nNão foi possível localizar o contato indicado.")
  return

#lista de contatos favoritos
def lista_contatos_favoritos(contatos):
  favoritos = []
  for contato in contatos:
    if contato["Contato favorito"].upper() == 'S':
      favoritos.append(contato)
          
  if favoritos:
    print("\nAqui estão seus contatos favoritos:")
    for indice, contato in enumerate(favoritos, start=1):
      print(f"\n{indice}. \nNome: {contato['Nome']} \nTelefone: {contato['Telefone']} \nE-mail: {contato['E-mail']}")
  else:
      print("\nVocê ainda não possui contatos marcados como favoritos.")
  return

#apagar um contato da agenda
def apagar_contato(contatos, indice_contato):
  ver_contatos(contatos)
  indice_contato_ajustado = int(indice_contato) - 1
  if 0 <= indice_contato_ajustado < len(contatos):
      confirmar = input(f"Você tem certeza que deseja remover o contato {contatos[indice_contato_ajustado]['Nome']} da sua agenda? (S/N): ").upper()
      if confirmar == 'S':
        contato = contatos.pop(indice_contato_ajustado)
        print(f"\nO contato {contato['Nome']} foi removido da sua agenda com sucesso!")
      else:
        print("\nO contato não foi apagado de sua agenda.")
  else:
    print("\nNão foi possível localizar o contato que você indicou.")


contatos = []

while True:
  print("\nMenu da agenda de contatos:")
  print("1. Adicionar um contato")
  print("2. Seus contatos cadastrados")
  print("3. Editar um contato")
  print("4. Adicionar ou remover um contato favorito")
  print("5. Seus contatos favoritos")
  print("6. Apagar um contato")
  print("0. Sair")
  

  escolha = input("\nDigite a opção desejada: ")

  if escolha == "1":
    nome_contato = input("Digite o nome do contato : ")
    telefone_contato = input("Digite o número de telefone do contato : ")
    email_contato = input ("Digite o e-mail do contato: ")
    contato_favorito = input ("Deseja marcar esse contato como favorito? (S/N):")
    adicionar_contato(contatos, nome_contato, telefone_contato, email_contato, contato_favorito.upper())
  
  elif escolha == "2":
    ver_contatos(contatos)

  elif escolha == "3":
    ver_contatos(contatos)
    indice_contato = input("\nDigite o número do contato que deseja atualizar: ")
    novo_nome_contato = input("Digite o novo nome do contato : ")
    novo_telefone_contato = input("Digite o novo número de telefone do contato : ")
    novo_email_contato = input ("Digite o novo e-mail do contato: ")
    novo_contato_favorito = input ("Deseja marcar esse contato como favorito? (S/N):")
    editar_contato(contatos, indice_contato, novo_nome_contato, novo_telefone_contato, novo_email_contato, novo_contato_favorito.upper())
  
  elif escolha == "4":
    ver_contatos(contatos)
    indice_contato = input("\nDigite o número do contato que deseja adicionar ou remover dos seus favoritos: ")
    editar_favorito(contatos, indice_contato)

  elif escolha == "5":
    lista_contatos_favoritos(contatos)   

  elif escolha == "6":
    ver_contatos(contatos)
    indice_contato = input("\nDigite o número do contato que deseja apagar: ")
    apagar_contato(contatos, indice_contato)

  elif escolha == "0":
    print("\nSaindo da agenda de contatos. Até a próxima!")
    break

  else:
     print("\nOpção inválida! Tente novamente.")
 

