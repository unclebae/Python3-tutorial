import pymysql

db = pymysql.connect("localhost", "kido", "1212", "boards")

cursor = db.cursor()
cursor.execute("DROP TABLE IF EXISTS BOARD")

SQL = """
CREATE TABLE `boards`.`board` (
  `id` BIGINT(10) NOT NULL AUTO_INCREMENT,
  `title` VARCHAR(200) NOT NULL,
  `content` VARCHAR(4000) NULL,
  `author` VARCHAR(45) NULL,
  `createAt` TIMESTAMP NOT NULL DEFAULT now(),
  `modifyAt` TIMESTAMP NULL,
  PRIMARY KEY (`id`));
"""
cursor.execute(SQL)

db.close()

