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

tabela = input('Tabela: ')
new_id = id_id+1
nome = "'" + input('Nome: ') + "'"
endereco = "'" + input('Endereço: ') + "'"
cep = "'" + input('CEP: ') + "'"
data_nasc = "'" + input('data(yyyy-mm-dd): ') + "'"
cpf = "'" + input('CPF: ') + "'"
celular = "'" + input('Celular: ') + "'"
statement = "'" + input('Estado Civil: ') + "'"

cons = ('insert into' + ' ' + str(tabela) + ' ' + 'values ('  + str(new_id) + ',' + str(nome) + ',' + str(endereco) + ',' + str(cep) + ',' + str(data_nasc) + ',' + str(cpf) + ',' + str(celular) + ',' + str(statement) + ');')

cur.execute(str(cons))
conn.commit()
cur.execute('select * from membros')
row = cur.fetchall()
transf = row

print(row)
print(transf)

cur.close()


#cur.execute('''insert into membros values (03, 'Marcos Barboza Silva ','Rua Papa Pio XII nº 49, Vila Rica - Lote 92, Jaboatão dos Guararapes-PE','54090415','1968-02-02','50128990406','81985455346','casado');''')

