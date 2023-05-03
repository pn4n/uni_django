import sqlite3

DBFILE = 'db.sqlite3'

def execute_sql(query: str, args: tuple):
    con = sqlite3.connect(DBFILE)
    cur = con.cursor()
    res = cur.execute(query, args)
    result = res.fetchone()
    con.commit()
    con.close()
    return result

def execute_non_sql(query: str):
    con = sqlite3.connect(DBFILE)
    cur = con.cursor()
    res = cur.execute(query)
    result = res.fetchall()
    con.commit()
    con.close()
    return result

# execute_sql("UPDATE articles_article SET title=? WHERE id=?", tuple(("[0] Жареный суп (рецепт от бати)", 1)))

# new_text = "♒️Водолей: Вы можете стать статным и элегантным борцом с комодами. Так же не следует играть с свиньями, так как они могут стать опасными людьми. Полоумный дед Ленин может ворваться в вашу комнату и сломать шкаф. Во второй половине дня думайте о том, что вы сошли с ума."

# execute_sql("UPDATE articles_article SET text=? WHERE id=?", tuple((new_text, 2)))

# new_record_title = '[3] ChatGPT'
# new_record_text = "Необходимо использовать нейросети с осторожностью и осознанием потенциальных рисков, а не полностью отказываться от их использования. Нейросети могут быть полезными в различных областях, таких как медицина, наука, технологии и другие, и могут привести к значительному прогрессу в этих областях. Однако, важно убедиться в том, что они используются правильно и не представляют угрозу для общества и личной безопасности."

# execute_sql("INSERT INTO articles_article VALUES (4, ?, ?, DATE(), 1)", tuple((new_record_title, new_record_text)))

# new_record_title = '[4] The Psychedelic Furs - President Gas (1982) Lyrics'
# new_record_text = "Don't cry, don't do anything. No lies, back in the government. No tears, party time is here again. President gas is up for president. Line up, put your kisses down. Say yeah, say yes again. Stand up, there's a head count. President gas on everything but roller skates"

# execute_sql("INSERT INTO articles_article VALUES (5, ?, ?, DATE(), 1)", tuple((new_record_title, new_record_text)))

new_text = """You have to have a party
When you're in a state like this
You can really move it all
You have to vote and change

You have to get right out of it
Like out of all this mess
You'll say yeah to anything
If you believe all this, but

Don't cry, don't do anything
No lies, back in the government
No tears, party time is here again
President gas is up for president

Line up, put your kisses down
Say yeah, say yes again
Stand up, there's a head count
President gas on everything but roller skates

It's sick the price of medicine
Stand up, we'll put you on your feet again
Open up your eyes
Just to check that your asleep again
President gas is president gas again

He comes in from the left sometimes
He comes in from the right
It's so heavily advertised that he wants you and I

It's a real cowboy set your electric company
Every day is "Happy Days"
It's hell without the sin, but

Don't cry, don't do anything
No lies, back in the government
No tears, party time is here again
President gas is up for president

Line up, put your kisses down
Say yeah, say yes again
Stand up, there's a head count
President gas on everything but roller skates

It's sick the price of medicine
Stand up, we'll put you on your feet again
Open up your eyes just to check that you're asleep again
President gas is president gas again"""

execute_sql("UPDATE articles2_article SET text=? WHERE id=?", tuple((new_text, 5)))