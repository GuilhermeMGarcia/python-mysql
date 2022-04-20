import pymysql.cursors


host = 'localhost'
user = 'udemy'
password = '123456'
db = 'escola_curso'
port = 3306

connection = pymysql.connect(host=host,
                             user=user,
                             password=password,
                             database=db,
                             port=port,
                             cursorclass=pymysql.cursors.DictCursor)

# Formacto para Pymysql
'''with connection:
    with connection.cursor() as cursor:
        sql = "SELECT `*` FROM `alunos` "
        cursor.execute(sql)
        result = cursor.fetchone()
        print(result)'''


def select(fields, tables, where=None):
    with connection:
        with connection.cursor() as cursor:
            sql = "SELECT {} FROM {} ".format(fields, tables)
            if where:
                sql = "{} WHERE {} ".format(sql, where)

            cursor.execute(sql)
            return cursor.fetchall()


def insert(values, table, fields=None):
    with connection:
        with connection.cursor() as cursor:
            sql = "INSERT INTO {}".format(table)
            if fields:
                sql = "{} ({})".format(sql, fields)
            sql = sql + " VALUES " + ",".join(["(" + v + ")" for v in values])

            cursor.execute(sql)
            connection.commit()


def update(sets, table, where=None):
    with connection:
        with connection.cursor() as cursor:
            sql = "UPDATE {}".format(table)
            sql = sql + " SET " + ", ".join([
                field + " = " + f"'{value}'"
                for field, value in sets.items()
            ])
            if where:
                sql = "{} WHERE {}".format(sql, where)

            cursor.execute(sql)
            connection.commit()


def delete(table, where):
    with connection:
        with connection.cursor() as cursor:
            sql = f"DELETE FROM {table} WHERE {where}"

            cursor.execute(sql)
            connection.commit()


values = [
    "DEFAULT, 'Gustavo', '2000-10-10', 'Av da pedras, 123', 'Betim', 'MG', '12855678922'",
    "DEFAULT, 'Guilherme', '2000-10-10', 'Av da pedras, 123', 'Betim', 'MG', '12345688942'"
          ]

#insert(values, 'alunos')
#update({"nome": "Thiago", "cidade": "Paicandu"}, "alunos", "id_aluno = 2")
#delete('alunos', 'nome = "Guilherme" or nome = "Gustavo"')

nomes = (select('nome', 'alunos'))
for nome in nomes:
    print(nome)