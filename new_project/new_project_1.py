from rr_connection_manager import PostgresConnection

conn = PostgresConnection(app='radar_live', tunnel=True)
conn.connection_check()