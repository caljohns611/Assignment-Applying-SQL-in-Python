from connect_sql import connect_database

# task 4

def delete_workout_session(session_id):
    query = "DELETE FROM workout_sessions WHERE session_id = (session_id) VALUES (%s)"
    cursor.execute(query, (session_id))


conn = connect_database()
if conn is not None:
    try:
        cursor = conn.cursor()

        delete_workout_session(3)

        conn.commit()
        print("Session has been deleted.")
    
    except Exception as e:
        print(f"Error: {e}")
    
    finally:
        cursor.close()
        conn.close()