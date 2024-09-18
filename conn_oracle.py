import oracledb, os
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env (do not overver already defined vars)

print('DATABASE_USER', os.getenv('DATABASE_USER'))
#print('DATABASE_PASSWORD', os.getenv('DATABASE_PASSWORD'))
print('DATABASE_DSN', os.getenv('DATABASE_DSN'))

# Connexion à la base de données Oracle
conn = oracledb.connect(user=os.getenv('DATABASE_USER'),
                        password=os.getenv('DATABASE_PASSWORD'),
                        dsn=os.getenv('DATABASE_DSN'))

# Création d'un curseur pour exécuter une requête
cur = conn.cursor()

# Exécution d'une requête SELECT
DATABASE_TABLE=os.getenv('DATABASE_TABLE')
cur.execute(f"SELECT * FROM {DATABASE_TABLE}")

# Récupération des résultats
for row in cur:
    print(row)

# Fermeture de la connexion
cur.close()
conn.close()

