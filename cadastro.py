#O nome deve ter no mínimo 3 letras
#Variavel para alocar o nome
nome = str(input("Digite seu nome completo: "))

#Função de formatação do nome
def formatar_nome(nome):

    nome = nome.strip()     #Remover espaços desnecessários
    nome = nome.title()     #Capitalizar cada nome

    #Retornar o nome formatado
    return nome

#Formatar nome
nome = formatar_nome(nome)

#Atualizar o primeiro nome
nome_separado = nome.split()        #Dividir o nome, sobrenome e etc.
primeiro_nome = nome_separado[0]    #Pegar o primeiro nome

#Nome deve ter no mínimo 3 letras
#Enquanto o nome tiver menos que 3 letras, executar esse código
while len(primeiro_nome) < 3:

    #Pedir nome novamente
    nome = str(input("Seu primeiro nome deve ter no mínimo 3 letras! Digite novamente seu nome completo: "))

    #Formatar nome
    nome = formatar_nome(nome)

    #Atualizar o primeiro nome
    nome_separado = nome.split()        #Dividir o nome, sobrenome e etc.
    primeiro_nome = nome_separado[0]    #Pegar o primeiro nome

#O Email é divido em 2 partes, o "prefixo" (antes do "@") e "sufixo" (depois do "@")
#O prefixo não pode conter caracteres especiais
#O sufixo deve terminar em algum dos seguintes domínios: "gmail.com", "hotmail.com", "yahoo.com"
#Input email
email = str(input(f"Perfeito, {primeiro_nome}, agora, digite seu email: "))

#Formatação do email
caracteres_especiais = ("#", "!", "$", "%", "&", "¨", "(", ")", "-", "+", "£", "{", "}", "@")   #caracteres especiais que não são permitidos no email
dominios = ("gmail.com","hotmail.com", "yahoo.com")     #Domínios aceitos
arroba = email.find("@")                                #achar o arroba
prefixo_email = email[:arroba]                          #parte antes do arroba
sufixo_email = email[arroba+1:]                         #parte depois do arroba
prefixo_valido = True                                   #prefixo válido
dominio_aceito = False                                  #dominio aceito
prefixo_dominio = [prefixo_valido, dominio_aceito]      #lista para o all

#Função para verificar se o email é valido
def verificar_email(caracteres_especiais, prefixo_email, sufixo_email):

    #Pegar cada caractere especial da lista "caracteres_especiais" e alocar na variavel "caractere especial"
    for caractere_especial in caracteres_especiais:

        #Se o caractere especial escolhido estiver no prefixo email o prefixo vai ser inválido e o for vai ser parado
        if caractere_especial in prefixo_email:

            #Prefixo inválido e break for
            prefixo_valido = False
            break

        else:

            #Caso não tenha nenhum caractere especial, o prefixo válido
            prefixo_valido = True

    #Verificar se o dominio é aceitavel
    if sufixo_email in dominios: dominio_aceito = True
    else: dominio_aceito = False

    #Lista para o all
    prefixo_dominio = [prefixo_valido, dominio_aceito]

    #Retornar o valor de all
    return all(prefixo_dominio)

#Se tudo estiver correto, o email é valido
email_valido = verificar_email(caracteres_especiais, prefixo_email, sufixo_email)

#Enquanto o email for inválido, pedir outro email
while email_valido == False:

    #Mensagem de Email não encontrado
    print("Email não encontrado! Verifique se digitou corretamente. O email não pode conter caracteres especiais e deve ser 'gmail.com','hotmail.com' ou 'yahoo.com'. ")

    #Pedir outro email
    email = str(input("Digite novamente seu email: "))

    #Dados para formatar
    arroba = email.find("@")                                #achar o arroba
    prefixo_email = email[:arroba]                          #parte antes do arroba
    sufixo_email = email[arroba+1:]                         #parte depois do arroba

    email_valido = verificar_email(caracteres_especiais, prefixo_email, sufixo_email)

#Mensagem de registro final
mensagem_registro = f"Olá, {primeiro_nome}! Seu email: {email} foi registrado com sucesso!"
print(mensagem_registro)