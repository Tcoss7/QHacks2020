from flask import request, jsonify, render_template
import sys

@app.route("/receiver", methods=["GET", "POST"])
def my_function():
    if request.method == "POST":
        data = request.get_json()
		result = ''
		for item in data:
			result += str(item['url'])
			
		print(result)
		
        return result
    else:
        return render_template('popup.html')