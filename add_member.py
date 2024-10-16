from connect_sql import connect_database

# task 1
def add_member(id, name, phone, age):
    query = "INSERT INTO Members (id, name, phone, age) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (id, name, phone, age))

# task 2
def add_workout_session(date, member_id, duration_minutes, calories_burned):
    query = "INSERT INTO Workout_sessions (date, member_id, duration_minutes, calories_burned) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (date, member_id, duration_minutes, calories_burned))

conn = connect_database()
if conn is not None:
    try:
        cursor = conn.cursor()

        add_member(2, "John Doe", 123-456-7890, 23)

        add_workout_session("2024-10-26", 2, 40, 100)

        conn.commit()
        print("Member and workout session added.")
    
    except Exception as e:
        print(f"Error: {e}")
    
    finally:
        cursor.close()
        conn.close()