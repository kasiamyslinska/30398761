#!/usr/bin/env python
# coding: utf-8

# In[3]:


get_ipython().run_cell_magic('file', 'app.py', "\nfrom flask import Flask, jsonify\n\napp = Flask(__name__)\n\n@app.route('/')\ndef home():\n    return jsonify('My second API')\n")

