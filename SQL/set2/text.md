16.-- Create a Restaurants table in SQL
CREATE TABLE Restaurants (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    cuisine_type VARCHAR(100),
    location VARCHAR(255),
    average_rating DECIMAL(3,2),
    delivery_available BOOLEAN
);

17.-- Insert data into the Restaurants table in SQL
INSERT INTO Restaurants (id, name, cuisine_type, location, average_rating, delivery_available)
VALUES
  (1, 'Italian Delight', 'Italian', '123 Main St', 4.5, true),
  (2, 'Chinese Garden', 'Chinese', '456 Elm St', 3.8, true),
  (3, 'Mediterranean Breeze', 'Mediterranean', '789 Oak St', 4.0, true),
  (4, 'Sushi House', 'Japanese', '321 Maple St', 4.2, false),
  (5, 'Mexican Fiesta', 'Mexican', '567 Pine St', 4.7, true);


// Insert data into the Restaurants collection in MongoDB
db.Restaurants.insertMany([
  {
    id: 1,
    name: 'Italian Delight',
    cuisine_type: 'Italian',
    location: '123 Main St',
    average_rating: 4.5,
    delivery_available: true
  },
  {
    id: 2,
    name: 'Chinese Garden',
    cuisine_type: 'Chinese',
    location: '456 Elm St',
    average_rating: 3.8,
    delivery_available: true
  },
  {
    id: 3,
    name: 'Mediterranean Breeze',
    cuisine_type: 'Mediterranean',
    location: '789 Oak St',
    average_rating: 4.0,
    delivery_available: true
  },
  {
    id: 4,
    name: 'Sushi House',
    cuisine_type: 'Japanese',
    location: '321 Maple St',
    average_rating: 4.2,
    delivery_available: false
  },
  {
    id: 5,
    name: 'Mexican Fiesta',
    cuisine_type: 'Mexican',
    location: '567 Pine St',
    average_rating: 4.7,
    delivery_available: true
  }
]);

18.-- Fetch all restaurants ordered by average_rating in descending order in SQL
SELECT * FROM Restaurants
ORDER BY average_rating DESC;


// Fetch all restaurants ordered by average_rating in descending order in MongoDB
db.Restaurants.find().sort({ average_rating: -1 });

19.-- Fetch restaurants with delivery_available and average_rating > 4 in SQL
SELECT * FROM Restaurants
WHERE delivery_available = true AND average_rating > 4;


// Fetch restaurants with delivery_available and average_rating > 4 in MongoDB
db.Restaurants.find({
  delivery_available: true,
  average_rating: { $gt: 4 }
});

20.-- Fetch restaurants where cuisine_type is not set or is null in SQL
SELECT * FROM Restaurants
WHERE cuisine_type IS NULL OR cuisine_type = '';

// Fetch restaurants where cuisine_type is not set or is null in MongoDB
db.Restaurants.find({
  $or: [
    { cuisine_type: null },
    { cuisine_type: "" }
  ]
});

21.-- Count the number of restaurants with delivery_available in SQL
SELECT COUNT(*) AS delivery_count FROM Restaurants
WHERE delivery_available = true;

// Count the number of restaurants with delivery_available in MongoDB
db.Restaurants.countDocuments({ delivery_available: true });

22.-- Fetch restaurants with location containing 'New York' in SQL
SELECT * FROM Restaurants
WHERE location LIKE '%New York%';

// Fetch restaurants with location containing 'New York' in MongoDB
db.Restaurants.find({
  location: /New York/
});

23.-- Calculate the average average_rating of all restaurants in SQL
SELECT AVG(average_rating) AS average_rating_avg FROM Restaurants;

// Calculate the average average_rating of all restaurants in MongoDB
db.Restaurants.aggregate([
  {
    $group: {
      _id: null,
      average_rating_avg: { $avg: "$average_rating" }
    }
  }
]);


24.-- Fetch the top 5 restaurants ordered by average_rating in descending order in SQL
SELECT * FROM Restaurants
ORDER BY average_rating DESC
LIMIT 5;

// Fetch the top 5 restaurants ordered by average_rating in descending order in MongoDB
db.Restaurants.find().sort({ average_rating: -1 }).limit(5);


25.-- Delete the restaurant with id 3 in SQL
DELETE FROM Restaurants
WHERE id = 3;

// Delete the restaurant with id 3 in MongoDB
db.Restaurants.deleteOne({ id: 3 });


