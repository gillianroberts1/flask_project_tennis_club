import pdb
from db.run_sql import run_sql
from models.member import Member


def delete_all():
    sql = "DELETE FROM members"
    run_sql(sql)


def save(member):
    
    sql = "INSERT INTO members (name, premium) VALUES (%s, %s) RETURNING *"
    values = [member.name, member.premium]
    results = run_sql(sql, values)
    member.id = results[0]['id']
    return member



def select_all():
    members = []
    sql = "SELECT * FROM members"
    results = run_sql(sql)
    for row in results:
        member = Member(row['name'], row['premium'], row['id'])
        members.append(member)
    return member
    


def select(id):
    member = []
    sql = "SELECT * FROM members WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        member = Member(result['name'], result['premium'], result['id'])
    return member





