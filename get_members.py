from connect_sql import Error


def get_members_in_age_range(start_age, end_age, connection):
    try:
        cursor = connection.cursor()
        query = "SELEC * FROM Members WHERE age BETWEEN %s AND %s"
        cursor.excute(query, (start_age, end_age))

        members = cursor.fethcall()

        for member in members:
            print(member)

    except Error as e:
        print(f"Error: {e}")

    finally:
        cursor.close() 