import pdb

from db.run_sql import run_sql
from models.slot import Slot

import repositories.member_repository as member_repository
import repositories.court_repository as court_repository


def save(slot):
    sql = "INSERT INTO slots ( court_id, start_time, end_time, available ) VALUES (%s, %s, %s, %s) RETURNING id"  
    values = [slot.court.id, slot.start_time, slot.end_time, slot.available]
    results = run_sql(sql, values)
    slot.id = results[0]['id']  
    return slot

def select_all():
    slots = []
    sql = "SELECT * FROM slots"
    results = run_sql(sql)
    for row in results:
        court = court_repository.select(row['court_id'])
        slot = Slot(court, row['start_time'], row['end_time'], row['available'])
        slots.append(slot)
        return slots
    
def select(id):
    slot = []
    sql = "SELECT * FROM slots WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        court = court_repository.select(result['court_id'])
        slot = Slot(court, result['court'], result['start_time'], result['end_time'], result['available'], result['id'])
    return slot



def delete_all():
    sql = "DELETE FROM slots"
    run_sql(sql)