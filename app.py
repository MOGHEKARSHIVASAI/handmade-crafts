from flask import Flask, render_template, request, redirect, url_for, flash
from models import db, User, Product, Category, Order, OrderItem, Review, CustomRequest, FeaturedProduct
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

@app.route('/')
def index():
    featured_products = FeaturedProduct.query.all()
    return render_template('index.html', featured_products=featured_products)

@app.route('/shop')
def shop():
    categories = Category.query.all()
    products = Product.query.all()
    return render_template('shop.html', categories=categories, products=products)

@app.route('/product/<int:product_id>')
def product_detail(product_id):
    product = Product.query.get_or_404(product_id)
    reviews = Review.query.filter_by(product_id=product_id).all()
    artist = User.query.get(product.artist_id)
    return render_template('product_detail.html', product=product, reviews=reviews, artist=artist)

@app.route('/artist/<int:artist_id>')
def artist_profile(artist_id):
    artist = User.query.get_or_404(artist_id)
    products = Product.query.filter_by(artist_id=artist_id).all()
    return render_template('artist_profile.html', artist=artist, products=products)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Add login logic here
        pass
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Add registration logic here
        pass
    return render_template('register.html')

@app.route('/dashboard')
def user_dashboard():
    # User dashboard logic here
    return render_template('user_dashboard.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True,port=5002)
