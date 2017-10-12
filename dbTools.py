import psycopg2
from settings import db_url

class Connection:
	def __new__(cls, db_url):
		try:
			connection = psycopg2.connect(
				database = db_url[0],
				user = db_url[0], 
				password = db_url[1],
				host = db_url[2],
				port = db_url[3]
			)
			cursor = connection.cursor()
			return connection, cursor

		except psycopg2.OperationalError:
			return False
		

class UserPosition:
	def __init__(self, db_url):
		connect = Connection(db_url)
		self.connection, self.cursor = connect

	def set_getting_position(self, user_id):
		self.cursor.execute("INSERT INTO user_position (user_id, faculty, course, group_name) VALUES (%s, %s, %s, %s)", (user_id, 'empty', 'empty', 'empty'))
		self.connection.commit()

	def set_faculty_position(self, user_id, faculty):
		self.cursor.execute("UPDATE user_position SET faculty = (%s) WHERE id IN (SELECT max(id) FROM user_position WHERE user_id = (%s)) AND course = (%s) AND group_name = (%s)", (faculty, user_id, 'empty', 'empty'))
		self.connection.commit()

	def set_course_position(self, user_id, course):
		self.cursor.execute("UPDATE user_position SET course = (%s) WHERE id IN (SELECT max(id) FROM user_position WHERE user_id = (%s)) AND group_name = (%s)", (course, user_id, 'empty'))
		self.connection.commit()

	def set_group_position(self, user_id, group_name):
		self.cursor.execute("UPDATE user_position SET group_name = (%s) WHERE id IN (SELECT max(id) FROM user_position WHERE user_id = (%s)) AND group_name = (%s)", (group_name, user_id, 'empty'))
		self.connection.commit()

	def get_faculty_and_course(self, user_id):
		self.cursor.execute("SELECT * FROM user_position WHERE id IN (SELECT max(id) FROM user_position WHERE user_id = (%s))", (user_id, ))
		return tuple([element for index, element in enumerate(self.cursor.fetchone()) if index == 2 or index == 3])

	def verification(self, user_id):
		self.cursor.execute("SELECT group_name FROM user_position WHERE id IN (SELECT max(id) FROM user_position WHERE user_id = (%s))", (user_id, ))
		return self.cursor.fetchone()[0]

	def cancel_getting_started(self, user_id):
		self.cursor.execute("DELETE FROM user_position WHERE user_id=%s", (user_id,))
		self.connection.commit()

	def cancel_faculty(self, user_id):
		self.cursor.execute("UPDATE user_position SET faculty = (%s) WHERE id IN (SELECT max(id) FROM user_position WHERE user_id = (%s))", ('empty', user_id))
		self.connection.commit()

	def cancel_course(self, user_id):
		self.cursor.execute("UPDATE user_position SET course = (%s) WHERE id IN (SELECT max(id) FROM user_position WHERE user_id = (%s) AND faculty != (%s))", ('empty', user_id, 'empty'))
		self.connection.commit()

	def cancel_group(self, user_id):
		self.cursor.execute("UPDATE user_position SET group_name = (%s) WHERE id IN (SELECT max(id) FROM user_position WHERE user_id = (%s) AND faculty != (%s))", ('empty', user_id, 'empty'))
		self.connection.commit() 

	def back_keyboard(self, user_id):
		self.cursor.execute("SELECT * FROM user_position WHERE id IN (SELECT max(id) FROM user_position WHERE user_id = (%s))", (user_id, ))

		count = -1
		for index, field in enumerate(self.cursor.fetchone()):
			if field != 'empty':
				count += 1
		return count