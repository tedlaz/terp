import sqlite3
from collections import namedtuple


def _dict_factory(cursor, row):
    dictionary = {}
    for idx, col in enumerate(cursor.description):
        dictionary[col[0]] = row[idx]
    return dictionary


def _get_dict(sql, db_file):
    # res = None
    with sqlite3.connect(db_file) as con:
        con.row_factory = _dict_factory
        cur = con.cursor()
        cur.execute(sql)
        res = cur.fetchall()
        cur.close()
    return res


def _namedtuple_factory(cursor, row):
    """Returns sqlite rows as named tuples."""
    fields = [col[0] for col in cursor.description]
    Row = namedtuple("Row", fields)
    return Row(*row)


def _get_namedtuple(sql, db_file):
    with sqlite3.connect(db_file) as con:
        con.row_factory = _namedtuple_factory
        cur = con.cursor()
        cur.execute(sql)
        res = cur.fetchall()
        cur.close()
    return res


def run_sql(db, sql, as_dict=False):
    """Run SQL on db"""
    if not as_dict:
        return _get_namedtuple(sql, db)
    return _get_dict(sql, db)


def select_table(db, table, as_dict=False):
    """Select all records from a table/view"""
    sql = f'SELECT * FROM {table}'
    return run_sql(db, sql, as_dict)


def select_one(db, table, idv, as_dict=False):
    """Select one record by id from a table/view"""
    sql = f'SELECT * FROM {table} WHERE id={idv}'
    return run_sql(db, sql, as_dict)[0]


def select_master_detail(db, master, detail, idv):
    sq1 = f'SELECT * FROM {master} WHERE id={idv}'
    sq2 = f'SELECT * FROM {detail} WHERE {master}_id={idv}'
    rec = run_sql(db, sq1, as_dict=True)[0]
    det = run_sql(db, sq2, as_dict=True)
    rec['_z'] = det
    return rec


def select_master_detail_all(db, master, detail):
    sq1 = f'SELECT * FROM {master}'
    rec = run_sql(db, sq1, as_dict=True)
    for elm in rec:
        idv = elm['id']
        sq2 = f'SELECT * FROM {detail} WHERE {master}_id={idv}'
        det = run_sql(db, sq2, as_dict=True)
        elm['_z'] = det
    return rec


if __name__ == '__main__':
    db = "/home/ted/Documents/pelates/spartiotis/apotelesmata/gasbah2.sql3"
    print(select_one(db, 'logistiki_lmo', 8, as_dict=True))
    print(select_master_detail(db, 'tran', 'tran_d', 7906))
    print(select_master_detail_all(db, 'tran', 'tran_d'))
