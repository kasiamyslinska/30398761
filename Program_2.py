#!/usr/bin/env python
# coding: utf-8

# In[5]:


get_ipython().run_cell_magic('file', 'app.py', 'from flask import Flask, request, jsonify\nimport statistics\n\napp = Flask(__name__)\n\ndef stats_decorator(func):\n    def wrapper():\n        numbers = request.json["numbers"]\n        mean = statistics.mean(numbers)\n        median = statistics.median(numbers)\n        return func(mean, median)\n    return wrapper\n\n@app.route("/")\ndef home():\n    return "Welcome to the Stats API!"\n    \n@stats_decorator\ndef calculate(mean, median):\n    return jsonify({\n        "mean": mean,\n        "median": median\n    })\n\nif __name__ == "__main__":\n    app.run()\n')

