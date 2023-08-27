from db.run_sql import run_sql
from models.member import Member
from models.court import Court




def save(member):
    sql = "INSERT INTO members (name, address, postcode, tel_no, email, dob, premium, win, loss) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING id"
    values = [member.name, member.address, member.postcode, member.tel_no, member.email, member.dob, member.premium, member.win, member.loss]
    results = run_sql(sql, values)
    member.id = results[0]['id']
    return member



def select_all():
    members = []
    sql = "SELECT * FROM members"
    results = run_sql(sql)
    for row in results:
        member = Member(row['name'], row['address'], row['postcode'], row['tel_no'], row['email'], row['dob'], row['premium'], row['win'], row['loss'], row['id'])
        members.append(member)
    return members
    


def select(id):
    member = []
    sql = "SELECT * FROM members WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        member = Member(result['name'], result['address'], result['postcode'], result['tel_no'], result['email'], result['dob'], result['premium'], result['win'], result['loss'], result['id'])
    return member


def update(member):
    sql = "UPDATE members SET (name, address, postcode, tel_no, email, dob, premium, win, loss) = (%s, %s, %s, %s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [member.name, member.address, member.postcode, member.tel_no, member.email, member.dob, member.premium, member.win, member.loss, member.id]
    run_sql(sql, values)

def delete(member):
    sql = "DELETE FROM members WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def delete_all():
    sql = "DELETE FROM members"
    run_sql(sql)


