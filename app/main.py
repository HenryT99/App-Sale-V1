from app import app
from flask import render_template
from app import dao



@app.route('/')
def to_home():
    return render_template('index.html')

@app.route('/products')
def to_products():
    return render_template('products.html', products = dao.read_data(app.root_path))

@app.route('/products/<int:category_id>')
def to_products_by_category(category_id):
    return render_template('products.html', products = dao.read_data(app.root_path,category_id))

if __name__ == '__main__':
    app.run(debug=True)