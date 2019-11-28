import os
from flask import Flask, render_template, redirect, request, url_for, request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

app.config["MONGO_URI"] = os.getenv("MONGO_URI")

mongo = PyMongo(app)



@app.route('/')
@app.route('/create_team')
def view_team():
    return render_template("team.html",
                            first_players_collection=mongo.db.players.find(),
                            second_players_collection = mongo.db.players.find(),
                            third_players_collection = mongo.db.players.find(),
                            fourth_players_collection = mongo.db.players.find(),
                            fith_players_collection = mongo.db.players.find(),
                            sixth_players_collection = mongo.db.players.find(),
                            seventh_players_collection = mongo.db.players.find(),
                            eighth_players_collection = mongo.db.players.find(),
                            ninth_players_collection = mongo.db.players.find(),
                            tenth_players_collection = mongo.db.players.find(),
                            eleventh_players_collection = mongo.db.players.find(),
                            twelth_players_collection = mongo.db.players.find(),
                            thirteenth_players_collection = mongo.db.players.find(),
                            fourteenth_players_collection = mongo.db.players.find(),
                            fithteenth_players_collection = mongo.db.players.find())

                            
@app.route('/new_team')
def new_team():
    return render_template("addplayers.html",
                            addplayers=mongo.db.players.find())

@app.route('/add_player', methods=['POST'])
def add_player():
    addplayers = mongo.db.players
    addplayers.insert_one(request.form.to_dict())
    return redirect(url_for('create_team'))
    
@app.route('/create_team')
def create_team():
    return render_template("team.html",
                            first_players_collection=mongo.db.players.find())
                            
@app.route('/add_team', methods=['POST'])
def add_team():
    team =  mongo.db.team
    team.insert_one(request.form.to_dict())
    return redirect(url_for('manage_team'))
    
@app.route('/manage_team')
def manage_team():
    return render_template("manageteam.html",
                            team=mongo.db.team.find())

@app.route('/delete_team/<team_id>')
def delete_team(team_id):
    mongo.db.team.remove({'_id': ObjectId(team_id)})
    return redirect(url_for('manage_team'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)