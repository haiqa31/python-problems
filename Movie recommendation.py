movies_name = (input("Enter the name of Movie:"))
movie_name1 = "Beauty and the beast"
movie_name2 = "The Portable Door"
movie_name3 = "Three Idiots"
movie_name4 = "Bahubali"

store_genre = ["musical romantic fantasy" , "magical" , "funny" , "historical"]
ratings = [10 , 9.0 , 6.7 , 5]
release_year = [ 2017, 2023 , 2009, 2015]

if movies_name == 'Beauty and the beast':
    print("fully recommended you will love this movie")
elif movies_name =='The portable Door':
        print("if you love magics must watch this movie")
elif movies_name == 'Three_Idiots':
    print("Recommended for which have good sense of humour")
elif movies_name == "Bahubali" :
     print("The history lovers should must watch this movie")    
else:
    print("opps ! this movie is Not Recommended to you from me")