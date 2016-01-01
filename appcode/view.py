__author__ = 'aub3'
#!/usr/bin/env python
from flask import render_template, redirect, request, abort,jsonify
import base64
from inception_indexer import *
png_data = load_network(True)
sess = tf.InteractiveSession()

def home():
    payload = {'gae_mode':True}
    return render_template('editor.html',payload = payload)

def search():
    image_url = request.form['image_url']
    image_data = base64.decodestring(image_url[22:])
    pool3 = sess.graph.get_tensor_by_name('pool_3:0')
    pool3_features = sess.run(pool3,{png_data: image_data})
    print np.squeeze(pool3_features)
    return jsonify(test=True)


def add_views(app):
    app.add_url_rule('/',view_func=home)
    app.add_url_rule('/Search',view_func=search,methods=['POST'])


