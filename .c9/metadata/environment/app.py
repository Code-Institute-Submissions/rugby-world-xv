{"filter":false,"title":"app.py","tooltip":"/app.py","undoManager":{"mark":100,"position":100,"stack":[[{"start":{"row":18,"column":36},"end":{"row":18,"column":37},"action":"insert","lines":["g"],"id":149},{"start":{"row":18,"column":37},"end":{"row":18,"column":38},"action":"insert","lines":["e"]},{"start":{"row":18,"column":38},"end":{"row":18,"column":39},"action":"insert","lines":["t"]},{"start":{"row":18,"column":39},"end":{"row":18,"column":40},"action":"insert","lines":["r"]},{"start":{"row":18,"column":40},"end":{"row":18,"column":41},"action":"insert","lines":["e"]}],[{"start":{"row":18,"column":40},"end":{"row":18,"column":41},"action":"remove","lines":["e"],"id":150},{"start":{"row":18,"column":39},"end":{"row":18,"column":40},"action":"remove","lines":["r"]}],[{"start":{"row":18,"column":39},"end":{"row":18,"column":40},"action":"insert","lines":["e"],"id":151},{"start":{"row":18,"column":40},"end":{"row":18,"column":41},"action":"insert","lines":["a"]},{"start":{"row":18,"column":41},"end":{"row":18,"column":42},"action":"insert","lines":["m"]}],[{"start":{"row":18,"column":32},"end":{"row":18,"column":42},"action":"remove","lines":["manageteam"],"id":152}],[{"start":{"row":18,"column":32},"end":{"row":18,"column":33},"action":"insert","lines":["i"],"id":153},{"start":{"row":18,"column":33},"end":{"row":18,"column":34},"action":"insert","lines":["n"]}],[{"start":{"row":18,"column":32},"end":{"row":18,"column":34},"action":"remove","lines":["in"],"id":154},{"start":{"row":18,"column":32},"end":{"row":18,"column":37},"action":"insert","lines":["index"]}],[{"start":{"row":26,"column":48},"end":{"row":26,"column":49},"action":"insert","lines":[","],"id":155}],[{"start":{"row":26,"column":49},"end":{"row":27,"column":0},"action":"insert","lines":["",""],"id":156},{"start":{"row":27,"column":0},"end":{"row":27,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":27,"column":8},"end":{"row":27,"column":12},"action":"insert","lines":["    "],"id":157}],[{"start":{"row":27,"column":12},"end":{"row":27,"column":16},"action":"insert","lines":["    "],"id":158}],[{"start":{"row":27,"column":16},"end":{"row":27,"column":20},"action":"insert","lines":["    "],"id":159}],[{"start":{"row":27,"column":20},"end":{"row":27,"column":24},"action":"insert","lines":["    "],"id":160}],[{"start":{"row":27,"column":24},"end":{"row":27,"column":28},"action":"insert","lines":["    "],"id":161}],[{"start":{"row":27,"column":28},"end":{"row":27,"column":32},"action":"insert","lines":["    "],"id":162}],[{"start":{"row":27,"column":32},"end":{"row":27,"column":57},"action":"insert","lines":["team=mongo.db.team.find()"],"id":163}],[{"start":{"row":26,"column":15},"end":{"row":27,"column":58},"action":"remove","lines":["render_template('manageteam.html',","                                team=mongo.db.team.find())"],"id":164}],[{"start":{"row":26,"column":15},"end":{"row":26,"column":16},"action":"insert","lines":["r"],"id":165},{"start":{"row":26,"column":16},"end":{"row":26,"column":17},"action":"insert","lines":["e"]},{"start":{"row":26,"column":17},"end":{"row":26,"column":18},"action":"insert","lines":["d"]},{"start":{"row":26,"column":18},"end":{"row":26,"column":19},"action":"insert","lines":["i"]},{"start":{"row":26,"column":19},"end":{"row":26,"column":20},"action":"insert","lines":["r"]},{"start":{"row":26,"column":20},"end":{"row":26,"column":21},"action":"insert","lines":["e"]},{"start":{"row":26,"column":21},"end":{"row":26,"column":22},"action":"insert","lines":["c"]},{"start":{"row":26,"column":22},"end":{"row":26,"column":23},"action":"insert","lines":["t"]}],[{"start":{"row":26,"column":23},"end":{"row":26,"column":25},"action":"insert","lines":["()"],"id":166}],[{"start":{"row":26,"column":24},"end":{"row":26,"column":25},"action":"insert","lines":["u"],"id":167},{"start":{"row":26,"column":25},"end":{"row":26,"column":26},"action":"insert","lines":["r"]},{"start":{"row":26,"column":26},"end":{"row":26,"column":27},"action":"insert","lines":["l"]},{"start":{"row":26,"column":27},"end":{"row":26,"column":28},"action":"insert","lines":["#"]}],[{"start":{"row":26,"column":27},"end":{"row":26,"column":28},"action":"remove","lines":["#"],"id":168},{"start":{"row":26,"column":26},"end":{"row":26,"column":27},"action":"remove","lines":["l"]}],[{"start":{"row":26,"column":26},"end":{"row":26,"column":27},"action":"insert","lines":["l"],"id":169}],[{"start":{"row":26,"column":24},"end":{"row":26,"column":27},"action":"remove","lines":["url"],"id":170},{"start":{"row":26,"column":24},"end":{"row":26,"column":31},"action":"insert","lines":["url_for"]}],[{"start":{"row":26,"column":31},"end":{"row":26,"column":33},"action":"insert","lines":["()"],"id":171}],[{"start":{"row":26,"column":32},"end":{"row":26,"column":34},"action":"insert","lines":["''"],"id":172}],[{"start":{"row":26,"column":33},"end":{"row":26,"column":34},"action":"insert","lines":["i"],"id":173},{"start":{"row":26,"column":34},"end":{"row":26,"column":35},"action":"insert","lines":["n"]},{"start":{"row":26,"column":35},"end":{"row":26,"column":36},"action":"insert","lines":["d"]},{"start":{"row":26,"column":36},"end":{"row":26,"column":37},"action":"insert","lines":["e"]},{"start":{"row":26,"column":37},"end":{"row":26,"column":38},"action":"insert","lines":["x"]}],[{"start":{"row":16,"column":0},"end":{"row":27,"column":0},"action":"remove","lines":["def index():","    if 'username' in session:","        return render_template(\"index.html\")","    ","@app.route('/login', methods=['GET', 'POST'])","def login():","    user = mongo.db.users","    user.insert_one(request.form.to_dict())","    if request.method == 'POST':","        session['username'] = request.form['username']","        return redirect(url_for('index'))",""],"id":174}],[{"start":{"row":16,"column":0},"end":{"row":17,"column":0},"action":"remove","lines":["",""],"id":175}],[{"start":{"row":1,"column":32},"end":{"row":1,"column":33},"action":"remove","lines":[","],"id":176},{"start":{"row":1,"column":31},"end":{"row":1,"column":32},"action":"remove","lines":["n"]},{"start":{"row":1,"column":30},"end":{"row":1,"column":31},"action":"remove","lines":["o"]},{"start":{"row":1,"column":29},"end":{"row":1,"column":30},"action":"remove","lines":["i"]},{"start":{"row":1,"column":28},"end":{"row":1,"column":29},"action":"remove","lines":["s"]},{"start":{"row":1,"column":27},"end":{"row":1,"column":28},"action":"remove","lines":["s"]},{"start":{"row":1,"column":26},"end":{"row":1,"column":27},"action":"remove","lines":["e"]},{"start":{"row":1,"column":25},"end":{"row":1,"column":26},"action":"remove","lines":["s"]}],[{"start":{"row":1,"column":24},"end":{"row":1,"column":25},"action":"remove","lines":[" "],"id":177}],[{"start":{"row":36,"column":20},"end":{"row":36,"column":21},"action":"remove","lines":["m"],"id":178},{"start":{"row":36,"column":19},"end":{"row":36,"column":20},"action":"remove","lines":["a"]},{"start":{"row":36,"column":18},"end":{"row":36,"column":19},"action":"remove","lines":["e"]},{"start":{"row":36,"column":17},"end":{"row":36,"column":18},"action":"remove","lines":["t"]},{"start":{"row":36,"column":16},"end":{"row":36,"column":17},"action":"remove","lines":["_"]},{"start":{"row":36,"column":15},"end":{"row":36,"column":16},"action":"remove","lines":["w"]},{"start":{"row":36,"column":14},"end":{"row":36,"column":15},"action":"remove","lines":["e"]},{"start":{"row":36,"column":13},"end":{"row":36,"column":14},"action":"remove","lines":["n"]}],[{"start":{"row":36,"column":13},"end":{"row":36,"column":14},"action":"insert","lines":["p"],"id":179},{"start":{"row":36,"column":14},"end":{"row":36,"column":15},"action":"insert","lines":["l"]},{"start":{"row":36,"column":15},"end":{"row":36,"column":16},"action":"insert","lines":["a"]}],[{"start":{"row":36,"column":16},"end":{"row":36,"column":17},"action":"insert","lines":["y"],"id":180},{"start":{"row":36,"column":17},"end":{"row":36,"column":18},"action":"insert","lines":["w"]},{"start":{"row":36,"column":18},"end":{"row":36,"column":19},"action":"insert","lines":["e"]}],[{"start":{"row":36,"column":18},"end":{"row":36,"column":19},"action":"remove","lines":["e"],"id":181},{"start":{"row":36,"column":17},"end":{"row":36,"column":18},"action":"remove","lines":["w"]}],[{"start":{"row":36,"column":17},"end":{"row":36,"column":18},"action":"insert","lines":["w"],"id":182}],[{"start":{"row":36,"column":17},"end":{"row":36,"column":18},"action":"remove","lines":["w"],"id":183}],[{"start":{"row":36,"column":17},"end":{"row":36,"column":18},"action":"insert","lines":["e"],"id":184},{"start":{"row":36,"column":18},"end":{"row":36,"column":19},"action":"insert","lines":["r"]}],[{"start":{"row":36,"column":19},"end":{"row":36,"column":20},"action":"insert","lines":["/"],"id":185},{"start":{"row":36,"column":20},"end":{"row":36,"column":21},"action":"insert","lines":["n"]},{"start":{"row":36,"column":21},"end":{"row":36,"column":22},"action":"insert","lines":["e"]},{"start":{"row":36,"column":22},"end":{"row":36,"column":23},"action":"insert","lines":["w"]}],[{"start":{"row":36,"column":24},"end":{"row":36,"column":25},"action":"insert","lines":[","],"id":186}],[{"start":{"row":36,"column":25},"end":{"row":36,"column":26},"action":"insert","lines":[" "],"id":187},{"start":{"row":36,"column":26},"end":{"row":36,"column":27},"action":"insert","lines":["m"]},{"start":{"row":36,"column":27},"end":{"row":36,"column":28},"action":"insert","lines":["e"]},{"start":{"row":36,"column":28},"end":{"row":36,"column":29},"action":"insert","lines":["t"]},{"start":{"row":36,"column":29},"end":{"row":36,"column":30},"action":"insert","lines":["h"]},{"start":{"row":36,"column":30},"end":{"row":36,"column":31},"action":"insert","lines":["o"]},{"start":{"row":36,"column":31},"end":{"row":36,"column":32},"action":"insert","lines":["d"]}],[{"start":{"row":36,"column":32},"end":{"row":36,"column":33},"action":"insert","lines":["s"],"id":188},{"start":{"row":36,"column":33},"end":{"row":36,"column":34},"action":"insert","lines":["="]}],[{"start":{"row":36,"column":34},"end":{"row":36,"column":36},"action":"insert","lines":["[]"],"id":189}],[{"start":{"row":36,"column":35},"end":{"row":36,"column":37},"action":"insert","lines":["''"],"id":190}],[{"start":{"row":36,"column":36},"end":{"row":36,"column":37},"action":"insert","lines":["G"],"id":191},{"start":{"row":36,"column":37},"end":{"row":36,"column":38},"action":"insert","lines":["E"]},{"start":{"row":36,"column":38},"end":{"row":36,"column":39},"action":"insert","lines":["T"]}],[{"start":{"row":36,"column":40},"end":{"row":36,"column":41},"action":"insert","lines":[","],"id":192}],[{"start":{"row":36,"column":41},"end":{"row":36,"column":42},"action":"insert","lines":[" "],"id":193}],[{"start":{"row":36,"column":42},"end":{"row":36,"column":44},"action":"insert","lines":["''"],"id":194}],[{"start":{"row":36,"column":43},"end":{"row":36,"column":44},"action":"insert","lines":["P"],"id":195},{"start":{"row":36,"column":44},"end":{"row":36,"column":45},"action":"insert","lines":["O"]},{"start":{"row":36,"column":45},"end":{"row":36,"column":46},"action":"insert","lines":["S"]},{"start":{"row":36,"column":46},"end":{"row":36,"column":47},"action":"insert","lines":["T"]}],[{"start":{"row":37,"column":11},"end":{"row":37,"column":12},"action":"remove","lines":["m"],"id":196},{"start":{"row":37,"column":10},"end":{"row":37,"column":11},"action":"remove","lines":["a"]},{"start":{"row":37,"column":9},"end":{"row":37,"column":10},"action":"remove","lines":["e"]},{"start":{"row":37,"column":8},"end":{"row":37,"column":9},"action":"remove","lines":["t"]},{"start":{"row":37,"column":7},"end":{"row":37,"column":8},"action":"remove","lines":["_"]},{"start":{"row":37,"column":6},"end":{"row":37,"column":7},"action":"remove","lines":["w"]},{"start":{"row":37,"column":5},"end":{"row":37,"column":6},"action":"remove","lines":["e"]},{"start":{"row":37,"column":4},"end":{"row":37,"column":5},"action":"remove","lines":["n"]}],[{"start":{"row":37,"column":4},"end":{"row":37,"column":5},"action":"insert","lines":["c"],"id":197},{"start":{"row":37,"column":5},"end":{"row":37,"column":6},"action":"insert","lines":["r"]},{"start":{"row":37,"column":6},"end":{"row":37,"column":7},"action":"insert","lines":["e"]},{"start":{"row":37,"column":7},"end":{"row":37,"column":8},"action":"insert","lines":["a"]},{"start":{"row":37,"column":8},"end":{"row":37,"column":9},"action":"insert","lines":["t"]},{"start":{"row":37,"column":9},"end":{"row":37,"column":10},"action":"insert","lines":["e"]}],[{"start":{"row":37,"column":10},"end":{"row":37,"column":11},"action":"insert","lines":["_"],"id":198},{"start":{"row":37,"column":11},"end":{"row":37,"column":12},"action":"insert","lines":["p"]},{"start":{"row":37,"column":12},"end":{"row":37,"column":13},"action":"insert","lines":["l"]},{"start":{"row":37,"column":13},"end":{"row":37,"column":14},"action":"insert","lines":["a"]},{"start":{"row":37,"column":14},"end":{"row":37,"column":15},"action":"insert","lines":["y"]},{"start":{"row":37,"column":15},"end":{"row":37,"column":16},"action":"insert","lines":["e"]}],[{"start":{"row":37,"column":16},"end":{"row":37,"column":17},"action":"insert","lines":["r"],"id":199}],[{"start":{"row":37,"column":20},"end":{"row":38,"column":0},"action":"insert","lines":["",""],"id":200},{"start":{"row":38,"column":0},"end":{"row":38,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":38,"column":4},"end":{"row":38,"column":5},"action":"insert","lines":["i"],"id":201},{"start":{"row":38,"column":5},"end":{"row":38,"column":6},"action":"insert","lines":["f"]}],[{"start":{"row":38,"column":6},"end":{"row":38,"column":7},"action":"insert","lines":[" "],"id":202},{"start":{"row":38,"column":7},"end":{"row":38,"column":8},"action":"insert","lines":["r"]},{"start":{"row":38,"column":8},"end":{"row":38,"column":9},"action":"insert","lines":["e"]},{"start":{"row":38,"column":9},"end":{"row":38,"column":10},"action":"insert","lines":["q"]}],[{"start":{"row":38,"column":10},"end":{"row":38,"column":11},"action":"insert","lines":["u"],"id":203},{"start":{"row":38,"column":11},"end":{"row":38,"column":12},"action":"insert","lines":["e"]},{"start":{"row":38,"column":12},"end":{"row":38,"column":13},"action":"insert","lines":["s"]},{"start":{"row":38,"column":13},"end":{"row":38,"column":14},"action":"insert","lines":["t"]},{"start":{"row":38,"column":14},"end":{"row":38,"column":15},"action":"insert","lines":["."]}],[{"start":{"row":38,"column":15},"end":{"row":38,"column":16},"action":"insert","lines":["m"],"id":204},{"start":{"row":38,"column":16},"end":{"row":38,"column":17},"action":"insert","lines":["r"]}],[{"start":{"row":38,"column":16},"end":{"row":38,"column":17},"action":"remove","lines":["r"],"id":205}],[{"start":{"row":38,"column":16},"end":{"row":38,"column":17},"action":"insert","lines":["e"],"id":206},{"start":{"row":38,"column":17},"end":{"row":38,"column":18},"action":"insert","lines":["t"]},{"start":{"row":38,"column":18},"end":{"row":38,"column":19},"action":"insert","lines":["h"]},{"start":{"row":38,"column":19},"end":{"row":38,"column":20},"action":"insert","lines":["o"]},{"start":{"row":38,"column":20},"end":{"row":38,"column":21},"action":"insert","lines":["d"]}],[{"start":{"row":38,"column":21},"end":{"row":38,"column":22},"action":"insert","lines":[" "],"id":207},{"start":{"row":38,"column":22},"end":{"row":38,"column":23},"action":"insert","lines":["="]}],[{"start":{"row":38,"column":23},"end":{"row":38,"column":24},"action":"insert","lines":[" "],"id":208}],[{"start":{"row":38,"column":24},"end":{"row":38,"column":26},"action":"insert","lines":["''"],"id":209}],[{"start":{"row":38,"column":25},"end":{"row":38,"column":26},"action":"insert","lines":["P"],"id":210},{"start":{"row":38,"column":26},"end":{"row":38,"column":27},"action":"insert","lines":["O"]},{"start":{"row":38,"column":27},"end":{"row":38,"column":28},"action":"insert","lines":["S"]},{"start":{"row":38,"column":28},"end":{"row":38,"column":29},"action":"insert","lines":["T"]}],[{"start":{"row":38,"column":30},"end":{"row":38,"column":31},"action":"insert","lines":[":"],"id":211}],[{"start":{"row":38,"column":31},"end":{"row":39,"column":0},"action":"insert","lines":["",""],"id":212},{"start":{"row":39,"column":0},"end":{"row":39,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":39,"column":0},"end":{"row":39,"column":4},"action":"insert","lines":["    "],"id":213}],[{"start":{"row":39,"column":4},"end":{"row":39,"column":8},"action":"insert","lines":["    "],"id":214}],[{"start":{"row":39,"column":8},"end":{"row":41,"column":43},"action":"insert","lines":["addplayers = mongo.db.players","    addplayers.insert_one(request.form.to_dict())","    return redirect(url_for('create_team'))"],"id":215}],[{"start":{"row":41,"column":4},"end":{"row":41,"column":8},"action":"insert","lines":["    "],"id":216}],[{"start":{"row":40,"column":4},"end":{"row":40,"column":8},"action":"insert","lines":["    "],"id":217}],[{"start":{"row":38,"column":23},"end":{"row":38,"column":24},"action":"insert","lines":["="],"id":219}],[{"start":{"row":45,"column":0},"end":{"row":49,"column":43},"action":"remove","lines":["@app.route('/add_player', methods=['POST'])","def add_player():","    addplayers = mongo.db.players","    addplayers.insert_one(request.form.to_dict())","    return redirect(url_for('create_team'))"],"id":220},{"start":{"row":44,"column":0},"end":{"row":45,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":46,"column":23},"end":{"row":46,"column":24},"action":"remove","lines":["m"],"id":221},{"start":{"row":46,"column":22},"end":{"row":46,"column":23},"action":"remove","lines":["a"]},{"start":{"row":46,"column":21},"end":{"row":46,"column":22},"action":"remove","lines":["e"]},{"start":{"row":46,"column":20},"end":{"row":46,"column":21},"action":"remove","lines":["t"]},{"start":{"row":46,"column":19},"end":{"row":46,"column":20},"action":"remove","lines":["_"]},{"start":{"row":46,"column":18},"end":{"row":46,"column":19},"action":"remove","lines":["e"]},{"start":{"row":46,"column":17},"end":{"row":46,"column":18},"action":"remove","lines":["t"]},{"start":{"row":46,"column":16},"end":{"row":46,"column":17},"action":"remove","lines":["a"]},{"start":{"row":46,"column":15},"end":{"row":46,"column":16},"action":"remove","lines":["e"]},{"start":{"row":46,"column":14},"end":{"row":46,"column":15},"action":"remove","lines":["r"]}],[{"start":{"row":46,"column":13},"end":{"row":46,"column":14},"action":"remove","lines":["c"],"id":222}],[{"start":{"row":46,"column":13},"end":{"row":46,"column":14},"action":"insert","lines":["t"],"id":223},{"start":{"row":46,"column":14},"end":{"row":46,"column":15},"action":"insert","lines":["e"]},{"start":{"row":46,"column":15},"end":{"row":46,"column":16},"action":"insert","lines":["a"]}],[{"start":{"row":46,"column":16},"end":{"row":46,"column":17},"action":"insert","lines":["m"],"id":224}],[{"start":{"row":46,"column":17},"end":{"row":46,"column":18},"action":"insert","lines":["/"],"id":225},{"start":{"row":46,"column":18},"end":{"row":46,"column":19},"action":"insert","lines":["n"]},{"start":{"row":46,"column":19},"end":{"row":46,"column":20},"action":"insert","lines":["e"]},{"start":{"row":46,"column":20},"end":{"row":46,"column":21},"action":"insert","lines":["w"]}],[{"start":{"row":46,"column":22},"end":{"row":46,"column":23},"action":"insert","lines":[","],"id":226}],[{"start":{"row":46,"column":23},"end":{"row":46,"column":24},"action":"insert","lines":[" "],"id":227}],[{"start":{"row":46,"column":23},"end":{"row":46,"column":24},"action":"insert","lines":[" "],"id":228}],[{"start":{"row":46,"column":24},"end":{"row":46,"column":47},"action":"insert","lines":["methods=['GET', 'POST']"],"id":229}],[{"start":{"row":47,"column":18},"end":{"row":48,"column":0},"action":"insert","lines":["",""],"id":230},{"start":{"row":48,"column":0},"end":{"row":48,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":48,"column":4},"end":{"row":48,"column":32},"action":"insert","lines":["if request.method == 'POST':"],"id":231}],[{"start":{"row":48,"column":32},"end":{"row":49,"column":0},"action":"insert","lines":["",""],"id":232},{"start":{"row":49,"column":0},"end":{"row":49,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":49,"column":7},"end":{"row":51,"column":43},"action":"insert","lines":["team =  mongo.db.team","    team.insert_one(request.form.to_dict())","    return redirect(url_for('manage_team'))"],"id":233}],[{"start":{"row":50,"column":4},"end":{"row":50,"column":8},"action":"insert","lines":["    "],"id":234}],[{"start":{"row":51,"column":4},"end":{"row":51,"column":8},"action":"insert","lines":["    "],"id":235}],[{"start":{"row":50,"column":4},"end":{"row":50,"column":8},"action":"remove","lines":["    "],"id":236}],[{"start":{"row":50,"column":4},"end":{"row":50,"column":8},"action":"insert","lines":["    "],"id":237}],[{"start":{"row":50,"column":4},"end":{"row":50,"column":8},"action":"remove","lines":["    "],"id":238}],[{"start":{"row":50,"column":4},"end":{"row":50,"column":5},"action":"insert","lines":[" "],"id":239},{"start":{"row":50,"column":5},"end":{"row":50,"column":6},"action":"insert","lines":[" "]},{"start":{"row":50,"column":6},"end":{"row":50,"column":7},"action":"insert","lines":[" "]}],[{"start":{"row":51,"column":4},"end":{"row":51,"column":8},"action":"remove","lines":["    "],"id":240}],[{"start":{"row":51,"column":4},"end":{"row":51,"column":8},"action":"insert","lines":["    "],"id":241}],[{"start":{"row":51,"column":4},"end":{"row":51,"column":8},"action":"remove","lines":["    "],"id":242}],[{"start":{"row":51,"column":4},"end":{"row":51,"column":5},"action":"insert","lines":[" "],"id":243},{"start":{"row":51,"column":5},"end":{"row":51,"column":6},"action":"insert","lines":[" "]},{"start":{"row":51,"column":6},"end":{"row":51,"column":7},"action":"insert","lines":[" "]}],[{"start":{"row":55,"column":0},"end":{"row":59,"column":43},"action":"remove","lines":["@app.route('/add_team', methods=['POST'])","def add_team():","    team =  mongo.db.team","    team.insert_one(request.form.to_dict())","    return redirect(url_for('manage_team'))"],"id":244},{"start":{"row":54,"column":28},"end":{"row":55,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":52,"column":4},"end":{"row":53,"column":77},"action":"remove","lines":["return render_template(\"team.html\",","                            first_players_collection=mongo.db.players.find())"],"id":245}],[{"start":{"row":52,"column":4},"end":{"row":67,"column":84},"action":"insert","lines":["return render_template(\"team.html\",","                            first_players_collection=mongo.db.players.find(),","                            second_players_collection = mongo.db.players.find(),","                            third_players_collection = mongo.db.players.find(),","                            fourth_players_collection = mongo.db.players.find(),","                            fith_players_collection = mongo.db.players.find(),","                            sixth_players_collection = mongo.db.players.find(),","                            seventh_players_collection = mongo.db.players.find(),","                            eighth_players_collection = mongo.db.players.find(),","                            ninth_players_collection = mongo.db.players.find(),","                            tenth_players_collection = mongo.db.players.find(),","                            eleventh_players_collection = mongo.db.players.find(),","                            twelth_players_collection = mongo.db.players.find(),","                            thirteenth_players_collection = mongo.db.players.find(),","                            fourteenth_players_collection = mongo.db.players.find(),","                            fithteenth_players_collection = mongo.db.players.find())"],"id":246}],[{"start":{"row":70,"column":0},"end":{"row":73,"column":54},"action":"remove","lines":["@app.route('/manage_team')","def manage_team():","    return render_template(\"manageteam.html\",","                            team=mongo.db.team.find())"],"id":247},{"start":{"row":69,"column":4},"end":{"row":70,"column":0},"action":"remove","lines":["",""]},{"start":{"row":69,"column":0},"end":{"row":69,"column":4},"action":"remove","lines":["    "]},{"start":{"row":68,"column":28},"end":{"row":69,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":16,"column":0},"end":{"row":33,"column":84},"action":"remove","lines":["@app.route('/create_team')","def view_team():","    return render_template(\"team.html\",","                            first_players_collection=mongo.db.players.find(),","                            second_players_collection = mongo.db.players.find(),","                            third_players_collection = mongo.db.players.find(),","                            fourth_players_collection = mongo.db.players.find(),","                            fith_players_collection = mongo.db.players.find(),","                            sixth_players_collection = mongo.db.players.find(),","                            seventh_players_collection = mongo.db.players.find(),","                            eighth_players_collection = mongo.db.players.find(),","                            ninth_players_collection = mongo.db.players.find(),","                            tenth_players_collection = mongo.db.players.find(),","                            eleventh_players_collection = mongo.db.players.find(),","                            twelth_players_collection = mongo.db.players.find(),","                            thirteenth_players_collection = mongo.db.players.find(),","                            fourteenth_players_collection = mongo.db.players.find(),","                            fithteenth_players_collection = mongo.db.players.find())"],"id":248}],[{"start":{"row":16,"column":0},"end":{"row":19,"column":54},"action":"insert","lines":["@app.route('/manage_team')","def manage_team():","    return render_template(\"manageteam.html\",","                            team=mongo.db.team.find())"],"id":249}],[{"start":{"row":32,"column":47},"end":{"row":32,"column":48},"action":"remove","lines":[" "],"id":250}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":32,"column":48},"end":{"row":32,"column":48},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":13,"state":"start","mode":"ace/mode/python"}},"timestamp":1578258178568,"hash":"27217d6793bace970d3006f53b8eeba98b8d00f1"}