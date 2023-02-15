from flask import Flask, request, jsonify

app = Flask(__name__)

# Define an empty leaderboard
leaderboard = {}

@app.route('/leaderboard/add', methods=['POST'])
def add_score():
    data = request.get_json()
    name = data['name']
    score = data['score']
    
    # Add the score to the leaderboard or update it if the user already exists
    if name in leaderboard:
        leaderboard[name] = max(leaderboard[name], score)
    else:
        leaderboard[name] = score
    
    # Return a success message
    return jsonify({'message': 'Score added successfully'})

@app.route('/leaderboard/get', methods=['GET'])
def get_leaderboard():
    # Sort the leaderboard by descending score and convert it to a list of dictionaries
    sorted_leaderboard = [{'name': k, 'score': v} for k, v in sorted(leaderboard.items(), key=lambda item: item[1], reverse=True)]
    
    # Return the sorted leaderboard
    return jsonify(sorted_leaderboard)

if __name__ == '__main__':
    app.run()
