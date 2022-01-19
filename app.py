from flask import Flask,render_template
import corona_data
from datetime import date, timedelta




app=Flask(__name__)


@app.route('/')
def index():

    now=date.today()
    now_str=now.strftime("%Y%m%d")
    print(now_str)

    data=corona_data.get_corona_data(now_str,now_str)
    #없으면 어제 날짜로 요청
    if not data:
        yesterday=now-timedelta(days=1)
        yesterday_str=yesterday.strftime("%Y%m%d")
        print(yesterday_str)

        data=corona_data.get_corona_data(now_str,now_str)
        print(data)
    return render_template('index.html',data=data)

if __name__=="__main__":
    app.run(debug=True)