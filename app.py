from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home_page():
	favorite_foods = ["fettucine alfredo", "mansaf", "maklouba eggplant", "cheeseburgers"]
	return render_template("index.html", favorite_foods = favorite_foods, opposite_day = True)
	
'''
def opposite_day():
	least_favorite_foods = ["maklouba coliflower", "IASA food", "idra"]
	return render_template("index.html", least_favorite_foods = least_favorite_foods)
'''

if __name__ == '__main__':
   app.run(debug = True)
