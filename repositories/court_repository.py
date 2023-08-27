import pdb
from db.run_sql import run_sql
from models.court import Court
from models.member import Member



def save(court):
    
    sql = "INSERT INTO courts ( court_no, surface) VALUES ( %s, %s ) RETURNING id"
    values = [court.court_no, court.surface]
    results = run_sql(sql, values)
    court.id = results[0]['id']
    return court


def select_all():
    courts = []
    sql = "SELECT * FROM courts"
    results = run_sql(sql)
    for row in results:
        court = Court(row['court_no'], row['surface'], row['id'])
        courts.append(court)
    return courts

def select(id):
    
    court = None
    sql = " SELECT * FROM courts WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        court = Court(result['court_no'], result['surface'], result['id'])
    return court

def update(court):
    sql = "UPDATE courts SET (court_no, surface) = (%s, %s) WHERE id = %s"
    values = [court.court_no, court.surface, court.id]
    run_sql(sql, values)


def delete(id):
    sql = "DELETE FROM courts WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM courts"
    run_sql(sql)

def court_for_member(member):
    courts = []
    sql = "SELECT courts.* FROM courts INNER JOIN bookings ON bookings.court_id = courts.id WHERE member_id = %s"
    values = [member.id]
    results = run_sql(sql, values)

    for row in results:
        court = Court(row['court_no'], row['surface'], row['id'])
        courts.append(court)

    return courts



