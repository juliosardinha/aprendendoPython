import datetime

def calcula_idade(nome, data_nascimento):
  hoje = datetime.date.today()
  ano_nascimento = data_nascimento.year
  mes_nascimento = data_nascimento.month
  dia_nascimento = data_nascimento.day

  idade = hoje.year - ano_nascimento
  if hoje.month < mes_nascimento or (hoje.month == mes_nascimento and hoje.day < dia_nascimento):
    idade -= 1

  return f'{nome} tem {idade} anos.'

nome = input('Informe seu nome: ')
data_nascimento = input('Informe sua data de nascimento (no formato dd/mm/aaaa): ')
data_nascimento = datetime.datetime.strptime(data_nascimento, '%d/%m/%Y')

print(calcula_idade(nome, data_nascimento))
