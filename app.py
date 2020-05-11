import otter
import time
import os
from flask import Flask, render_template, request, json, jsonify, send_from_directory

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
	if request.method == 'POST':
		# check if the post request has the file part
		
		if 'file' not in request.files:
			return "Incomplete Request"
		
		# if user does not select file, browser also
		# submit an empty part without filename
		file = request.files['file']
		if file.filename == '':
			return 'No selected file'
		s = "\t\t\t\t\t".join(map(lambda x: x.decode('utf-8'), file.readlines()))
		s = "\t\t\t\t\t{}".format(s)
		n = '''test = gfh
	"name": "{}",
	"points": {},
	"hidden": True,
	"suites": [
		gfh
			"cases": [
				gfh
					"code": r"""\n'''
		n = n.format(request.form['uname'], request.form['points']).replace("gfh", "{")
		s = n + s
		p = '''\t\t\t\t\t""",
					"hidden": False,
					"locked": False,
				},
			],
			"scored": False,
			"setup": "",
			"teardown": "",
			"type": "doctest"
		}
	]
}'''
		s += p
		name = request.form['uname'] + ".py"
		with open(name, "w+") as f:
			f.write(s)
			f.close()
		return send_from_directory("./", name)
	
	return '''
	<!doctype html>
	<title>Upload new File</title>
	<h1>Upload new File</h1>
	<form method=post enctype=multipart/form-data>
	  <input type=file name=file>
	  <input type=text name=uname placeholder="new File name e.g test9/test7/etc">
	  <input type=number name=points placeholder="points carried by the test case e.g 6/2/3/etc">
	  <input type=submit value=Upload>
	</form>
	'''

if __name__ == '__main__':
    app.run(threaded=True, debug=True)
