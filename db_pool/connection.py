from mysql import connector

connect=connector.connect(
    user="root",
    password="root",
    host="localhost",
    database="management_db"
)
cursor = connect.cursor()
# if connect.is_connected():
#     print("sucessful")
# else:
#     print("not connected")