import mariadb
import dbcreds
#makes returned data look nicer
def convert_data(cursor, results):
    column_names = [i[0] for i in cursor.description]
    new_results = []
    for row in results:
        new_results.append(dict(zip(column_names, row)))
    return new_results

#function that gets called on each request using args based on which request was called
def run_proceedure(sql, args):
    try:
        #connecting to the DB/making results = None so if it does become defined by following code, it will end the connection.
        results = None
        conn = mariadb.connect(**dbcreds.conn_params)
        cursor = conn.cursor()
        cursor.execute(sql, args)
        results = cursor.fetchall()
        results = convert_data(cursor, results)
        #catching errors and diagnosing them
    except mariadb.ProgrammingError as error:
        print('There is an issue with the DB code: ', error)
    except mariadb.OperationalError as error:
        print('DB connection issue: ',error)
    except Exception as error:
        print('Unknown error: ', error)
    finally:
        if(cursor !=None):
            cursor.close()
        if(conn !=None):
            conn.close()
            #returing the results from cursor.fetchall()
        return results

