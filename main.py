from flask import Flask, render_template, request, jsonify
import pymysql
import json

app = Flask(__name__)


# route
@app.route('/')
def root():
    return render_template('home.html')


# post
@app.route('/problem', methods=['POST'])
def save_problems():
    db = pymysql.connect(host='hjdb.cmux79u98wpg.us-east-1.rds.amazonaws.com', user='master', db='hjdb', password='Abcd!234', charset='utf8')
    curs = db.cursor()

    title = request.form['title_give']
    comment = request.form['comment_give']
    user_unique_id = 1

    sql = """insert into problem (problem_title, problem_comment, user_unique_id)
         values (%s,%s,%s)
        """
    curs.execute(sql, (title, comment, user_unique_id))

    rows = curs.fetchall()

    json_str = json.dumps(rows, indent=4, sort_keys=True, default=str)
    db.commit()
    db.close()
    return json_str, 200


# GET
@app.route('/problem', methods=['GET'])
def get_problems():
    db = pymysql.connect(host='hjdb.cmux79u98wpg.us-east-1.rds.amazonaws.com', user='master', db='hjdb', password='Abcd!234', charset='utf8')
    curs = db.cursor()

    sql = """
    SELECT *
    FROM problem
    """

    curs.execute(sql)

    rows = curs.fetchall()

    json_str = json.dumps(rows, indent=4, sort_keys=True, default=str, ensure_ascii=False)
    db.commit()
    db.close()
    return json_str, 200


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000)
