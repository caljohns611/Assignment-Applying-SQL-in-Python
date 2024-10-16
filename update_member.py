from connect_sql import connect_database
# task 3

def update_member_age(member_id, new_age):
    query = "UPDATE Members SET age = (age) WHERE member_id = (member_id) VALUES (%s, %s)"
    cursor.execute(query(member_id, new_age))


conn = connect_database()
if conn is not None:
    try:
        cursor = conn.cursor()

        update_member_age(1, 25)

        conn.commit()
        print("Member updated")
    
    except Exception as e:
        print(f"Error: {e}")
    
    finally:
        cursor.close()
        conn.close()