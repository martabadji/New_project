from new_project.new_project_1 import conn

cur = conn.cursor()

query = """
SELECT * FROM codes LIMIT(10)
"""
print('hello')