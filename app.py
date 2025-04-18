#!/usr/bin/env python
# coding: utf-8

# In[7]:


get_ipython().run_cell_magic('file', 'app.py', 'from flask import Flask, request, jsonify\n\napp = Flask(__name__)\n\n@app.route(\'/\', methods=["GET"])\ndef check_pass():\n    score1 = float(request.args.get("score1"))\n    score2 = float(request.args.get("score2"))\n\n    avg = (score1 + score2) / 2\n\n    if avg >= 50:\n        result = "Zaliczono"\n    else:\n        result = "Nie zaliczono"\n\n    return jsonify({\n        "Średnia": avg,\n        "Wynik": result\n    })\n\nif __name__ == "__main__":\n    app.run()\n\n\n# run: http://127.0.0.1:5000/?score1=70&score2=60\n')

