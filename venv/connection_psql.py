import psycopg2

#create connection
conn = psycopg2.connect(host='localhost', dbname='PIBLT92', user='marcos', password='seg4marcos')
cur = conn.cursor()
print ("connection database successful")

#construtor de consulta

print

#consulta
cur.execute('select count(*) from membros')
row_id = cur.fetchall()
transf_id = str(row_id).strip('[]')
id_gerador_id=str(transf_id)[1]
id_id = int(id_gerador_id)

"""tabela = input('Tabela: ')
new_id = id_id+1
nome = "'" + input('Nome: ') + "'"
endereco = "'" + input('Endereço: ') + "'"
cep = "'" + input('CEP: ') + "'"
data_nasc = "'" + input('data(yyyy-mm-dd): ') + "'"
cpf = "'" + input('CPF: ') + "'"
celular = "'" + input('Celular: ') + "'"
statement = "'" + input('Estado Civil: ') + "'"""""

tabela = 'membros'
new_id = "'5'"
nome = "'marcos'"
endereco = "'rua'"
cep = "'vao'"
data_nasc ="'15-12-1998'"
cpf = "'10000000000'"
celular = "'00000000000'"
statement = "'casado'"

cons = ('insert into' + ' ' + str(tabela) + ' ' + 'values ('  + str(new_id) + ',' + str(nome) + ',' + str(endereco) + ',' + str(cep) + ',' + str(data_nasc) + ',' + str(cpf) + ',' + str(celular) + ',' + str(statement) + ');')

cur.execute(str(cons))
conn.commit()
cur.execute('select * from membros')
row = cur.fetchall()


for linha in row:
    print(str(linha))

cur.close()