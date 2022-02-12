movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

def is_IMDB_more_55(movie):
    return movie["imdb"] > 5.5

def sublist_with_high_IMDB():
    res = []
    for i in movies:
        if i["imdb"] > 5.5:
            res.append(i)
    return res

def sublist_category(categ: str):
    res = []
    for i in movies:
        if i["category"] == categ:
            res.append(i)
    return res

def average_IMDB(movies: list):
    score_sum = 0
    for i in movies:
        score_sum += i["imdb"]
    return score_sum/len(movies)

def average_IMDB_of_category(categ: str):
    score_sum = 0
    num = 0
    for i in movies:
        if i["category"] == categ:
            score_sum += i["imdb"]
            num += 1
    return score_sum/num

if __name__ == "__main__":
    print(is_IMDB_more_55(movies[0]))
    print(sublist_with_high_IMDB())
    print(sublist_category("Thriller"))
    print(average_IMDB(movies))
    print(average_IMDB_of_category("Thriller"))
