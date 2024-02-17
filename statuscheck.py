import pymysql

class XenForoStatusBot:
    def __init__(self, db_host, db_user, db_password, db_name):
        self.db_connection = pymysql.connect(
            host=db_host,
            user=db_user,
            password=db_password,
            database=db_name
        )
        self.cursor = self.db_connection.cursor()

    def get_total_users(self):
        query = "SELECT COUNT(*) FROM xf_user"
        self.cursor.execute(query)
        result = self.cursor.fetchone()
        return result[0] if result else 0

    def get_total_threads(self):
        query = "SELECT COUNT(*) FROM xf_thread"
        self.cursor.execute(query)
        result = self.cursor.fetchone()
        return result[0] if result else 0

    def get_total_posts(self):
        query = "SELECT COUNT(*) FROM xf_post"
        self.cursor.execute(query)
        result = self.cursor.fetchone()
        return result[0] if result else 0

    def get_total_forums(self):
        query = "SELECT COUNT(*) FROM xf_forum"
        self.cursor.execute(query)
        result = self.cursor.fetchone()
        return result[0] if result else 0

if __name__ == "__main__":
    # XenForo veritabanı bağlantı bilgileri
    DB_HOST = 'localhost'
    DB_USER = 'berat'
    DB_PASSWORD = 'berat'
    DB_NAME = 'berat'

    # XenForo Status Bot oluştur
    status_bot = XenForoStatusBot(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME)

    # Genel durumu al
    total_users = status_bot.get_total_users()
    total_threads = status_bot.get_total_threads()
    total_posts = status_bot.get_total_posts()
    total_forums = status_bot.get_total_forums()

    print("XenForo Genel Durumu:")
    print(f"Toplam Kullanıcı Sayısı: {total_users}")
    print(f"Toplam Konu Sayısı: {total_threads}")
    print(f"Toplam Gönderi Sayısı: {total_posts}")
    print(f"Toplam Forum Sayısı: {total_forums}")
