import mysql.connector
import difflib
from difflib import get_close_matches

con = mysql.connector.connect(
user = "ardit700_student",
password = "ardit700_student",
host = "108.167.140.122",
database = "ardit700_pm1database"
)

cursor = con.cursor()

query = cursor.execute('SELECT Expression FROM Dictionary')
all_results = cursor.fetchall()
expressions = []
for x in range(len(all_results)):
    expressions.append(all_results[x][0])

def translate(word):
    query = cursor.execute("SELECT Definition FROM Dictionary WHERE Expression = '%s'" % word)
    results = cursor.fetchall()
    if results:
        for result in results:
            print(result[0])
    elif len(get_close_matches(word, expressions)) > 0:
        while True:
            update = input(f"Do you mean the word: {get_close_matches(word, expressions)[0]}? If yes, enter 'Y', otherwise, enter 'N': ")
            if update.upper() == 'Y':
                query = cursor.execute(f"SELECT Definition FROM Dictionary WHERE Expression = '{get_close_matches(word, expressions)[0]}'")
                update_results = cursor.fetchall()
                for definition in update_results:
                    print(definition[0])
                break
            elif update.upper() == 'N':
                print('The word does not exist. Please double check it!')
                break
            else:
                print("Looks like you did not enter 'Y' or 'N'.")
                continue
    else:
        print("No word found!")

word = input("Enter the word: ")

translate(word)
