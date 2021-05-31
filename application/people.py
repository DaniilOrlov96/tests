people = [{'name': 'One', 'position_id': 1},
          {'name': 'Two', 'position_id': 2},
          {'name': 'Three', 'position_id': 3},
          {'name': 'Four', 'position_id': 2},
          {'name': 'Five', 'position_id': 4}]

positions = [{'id': 1, 'name': 'repairman', 'salary': 2000},
             {'id': 2, 'name': 'stripper', 'salary': 3000},
             {'id': 3, 'name': 'postman', 'salary': 4000},
             {'id': 4, 'name': 'sniper', 'salary': 66666666}]


def get_employees():
    return [{'name': p['name'],
             'position': next(i['name'] for i in positions if i['id'] == p['position_id']),
             'id': p['position_id'],
             'salary': next(i['salary'] for i in positions if i['id'] == p['position_id'])} for p in people]