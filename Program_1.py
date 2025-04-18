#!/usr/bin/env python
# coding: utf-8

# In[6]:


get_ipython().run_cell_magic('file', 'app.py', 'from flask import Flask, jsonify\n\napp = Flask(__name__)\n\n@app.route(\'/\')\ndef home():\n    return jsonify({"message": "Witaj w moim API!"})\n\n')

