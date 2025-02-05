from mongodb_connect import client

db = client.td01b

db.authors.insert_one({
    "name": "Nicolas Sarkozy",
    "birth_date": "1955-01-28",
    "books": [
        {
            "id": "984021984032198726219841",
            "title": "Le temps des tempêtes",
            "publication_year": 1951
        }
    ]
})
db.borrowers.insert_one({
    "name": "Rémi Neveu",
    "borrow_date": "2024-09-04",
    "book_id": "984021984032198726219841"
})

print([i for i in db.authors.find()])
print([i for i in db.authors.find({"birthdate": {"$gt": "1980-12-31"}})])
db.authors.update_many({}, [{ "$set": { "name": { "$concat": [ "$name", "BD5" ] } } }])

# Auteurs avec livres empruntés
borrowed_book_ids = [i["book_id"] for i in db.borrowers.find()]
print([i for i in db.authors.find({"books": {"$elemMatch": { "id": {"$in": borrowed_book_ids}}}})])
