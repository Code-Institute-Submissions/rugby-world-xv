import os
from flask import Flask, render_template, redirect, request, url_for, request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

""" Secret key and Mongo URI which is hidden on github and linked to heroku """
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
app.config["MONGO_URI"] = os.getenv("MONGO_URI")

mongo = PyMongo(app)

""" Base route that loads the home page to show created teams """
@app.route('/')
@app.route('/created/teams')
def created_teams():
    return render_template("manageteam.html",
                            team=mongo.db.team.find())

""" Route and method that adds and saves to the player database and takes you to the
create team page """
@app.route('/player/new', methods=['GET', 'POST'])
def create_player():
    if request.method == 'POST':
        addplayers = mongo.db.players
        addplayers.insert_one(request.form.to_dict())
        return redirect(url_for('create_team'))        
    return render_template("addplayers.html",
                            addplayers=mongo.db.players.find())

""" Route and method that saves a team to the (team) database, which calls on players
that have been added from the add players page """
@app.route('/team/new', methods=['GET', 'POST'])
def create_team():
    if request.method == 'POST':
       team =  mongo.db.team
       team.insert_one(request.form.to_dict())
       return redirect(url_for('created_teams')) 
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
                            
""" Route and method that deletes a team from the database """
@app.route('/delete_team/<team_id>')
def delete_team(team_id):
    mongo.db.team.remove({'_id': ObjectId(team_id)})
    return redirect(url_for('created_teams'))

""" Route and method that calls on the created users team with the current players
selected """
@app.route('/edit_team/<team_id>')
def edit_team(team_id):
    the_team =  mongo.db.team.find_one({"_id": ObjectId(team_id)})
    all_positions =  mongo.db.team.find()
    return render_template('editteam.html', team=the_team,
                           positions=all_positions, 
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

""" Route and method that updates a users change of player/players and takes them back to the home
page to view the updated changes """
@app.route('/update_team/<team_id>', methods=["POST"])
def update_team(team_id):
    team = mongo.db.team
    team.update( {'_id': ObjectId(team_id)},
    {
        'team_name':request.form.get('team_name'),
        'loose_head_prop':request.form.get('loose_head_prop'),
        'hooker':request.form.get('hooker'),
        'tight_head_prop': request.form.get('tight_head_prop'),
        'blind_side_flanker': request.form.get('blind_side_flanker'),
        'second_row':request.form.get('second_row'),
        'second_row_2':request.form.get('second_row_2'),
        'open_side_flanker':request.form.get('open_side_flanker'),
        'number_eight':request.form.get('number_eight'),
        'scrum_half':request.form.get('scrum_half'),
        'fly_half':request.form.get('fly_half'),
        'inside_centre':request.form.get('inside_centre'),
        'outside_centre':request.form.get('outside_centre'),
        'left_wing':request.form.get('left_wing'),
        'full_back':request.form.get('full_back'),
        'right_wing':request.form.get('right_wing')
    })
    return redirect(url_for('created_teams'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)