from Recommendation import Recommendation


from flask import Flask
from flask_restful import Api, Resource
import json

app = Flask(__name__)
api = Api(app)

class GetRecommendationEndPoint(Resource):
    def post(self, favMoviesList):
        if(len(favMoviesList) < 1 or favMoviesList ):
            raise ValueError('Cannot make recommendation for 0 movies')
            return favMoviesList
        r = Recommendation()
        predictedMoviesList = r.make_recommendation(["shawshank redemption", 'the matrix', 'inception', 'dark Knight'])
        #print(predictedMoviesList.values.tolist()[0][1])

        response = json.dumps(predictedMoviesList.values.tolist())
        return response




api.add_resource(GetRecommendationEndPoint, '/recommend/<favMoviesList>')
if __name__ == "__main__":
    app.run(debug=True)






