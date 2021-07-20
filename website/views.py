from flask import Blueprint, render_template,flash,request,jsonify
from flask_login import login_required,current_user
from .models import Note, PRODUCTS
from . import db
import json

views = Blueprint('views',__name__)

@views.route('/',methods = ['GET','POST'])
@login_required
def home():
    if request.method=='POST':
        note = request.form.get('note')
        if len(note)<1:
            flash('note is too short',category='error')
        else:
            new_note=Note(data=note,user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('note addeed',category='success')
    return render_template("home.html",user=current_user)


@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})

@views.route('/products',methods=['GET','POST'])
@login_required
def go_to_products():
    if request.method=='POST':
        print('adding product')
        prod = request.form.get('product')
        cal = request.form.get('calories')
        prot = request.form.get('protein')
        fat = request.form.get('fat')
        carb = request.form.get('carbohydrates')

        if len(prod)<1:
            flash('note is too short',category='error')
        elif len(cal)<1:
            pass
        elif len(prot)<1:
            pass
        elif len(fat)<1:
            pass
        elif len(carb)<1:
            pass
        else:
            new_product=PRODUCTS(USER_ID=current_user.id, PROD_NAME=prod,KCAL=cal,PROTEIN=prot, FAT=fat,CARB=carb)
            db.session.add(new_product)
            db.session.commit()
            flash('product addeed',category='success')
    return render_template("products.html",user=current_user)    
