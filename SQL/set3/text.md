26.CREATE TABLE Rides (
    id INT PRIMARY KEY,
    driver_id INT,
    passenger_id INT,
    start_location VARCHAR(255),
    end_location VARCHAR(255),
    distance DECIMAL(5,2),
    ride_time DECIMAL(5,2),
    fare DECIMAL(6,2)
);

// Use the MongoDB shell or a MongoDB driver in your preferred programming language.
// Make sure you are connected to the appropriate database.

// Create the Rides collection and insert a document.
db.createCollection("Rides");

// Insert a document with the specified fields.
db.Rides.insertOne({
    "driver_id": ObjectId(),
    "passenger_id": ObjectId(),
    "start_location": "Start City",
    "end_location": "End City",
    "distance": 10.5,
    "ride_time": 25.5,
    "fare": 15.00
});



27. -- Inserting five rows into the Rides table in SQL
INSERT INTO Rides (driver_id, passenger_id, start_location, end_location, distance, ride_time, fare)
VALUES
    (1, 101, 'Start City 1', 'End City 1', 5.5, 15.0, 10.00),
    (2, 102, 'Start City 2', 'End City 2', 7.2, 20.5, 12.50),
    (3, 103, 'Start City 3', 'End City 3', 3.8, 10.5, 8.75),
    (4, 104, 'Start City 4', 'End City 4', 8.0, 22.0, 14.00),
    (5, 105, 'Start City 5', 'End City 5', 6.5, 18.5, 11.25);


// Inserting five documents into the Rides collection in MongoDB
db.Rides.insertMany([
    {
        "driver_id": ObjectId(),
        "passenger_id": ObjectId(),
        "start_location": "Start City 1",
        "end_location": "End City 1",
        "distance": 5.5,
        "ride_time": 15.0,
        "fare": 10.00
    },
    {
        "driver_id": ObjectId(),
        "passenger_id": ObjectId(),
        "start_location": "Start City 2",
        "end_location": "End City 2",
        "distance": 7.2,
        "ride_time": 20.5,
        "fare": 12.50
    },
    {
        "driver_id": ObjectId(),
        "passenger_id": ObjectId(),
        "start_location": "Start City 3",
        "end_location": "End City 3",
        "distance": 3.8,
        "ride_time": 10.5,
        "fare": 8.75
    },
    {
        "driver_id": ObjectId(),
        "passenger_id": ObjectId(),
        "start_location": "Start City 4",
        "end_location": "End City 4",
        "distance": 8.0,
        "ride_time": 22.0,
        "fare": 14.00
    },
    {
        "driver_id": ObjectId(),
        "passenger_id": ObjectId(),
        "start_location": "Start City 5",
        "end_location": "End City 5",
        "distance": 6.5,
        "ride_time": 18.5,
        "fare": 11.25
    }
]);

28.-- Fetch all rides ordered by fare in descending order in SQL
SELECT * FROM Rides
ORDER BY fare DESC;

// Fetch all rides ordered by fare in descending order in MongoDB
db.Rides.find().sort({ fare: -1 });


29.-- Calculate total distance and total fare for all rides in SQL
SELECT SUM(distance) AS total_distance, SUM(fare) AS total_fare
FROM Rides;

// Calculate total distance and total fare for all rides in MongoDB
db.Rides.aggregate([
    {
        $group: {
            _id: null,
            total_distance: { $sum: "$distance" },
            total_fare: { $sum: "$fare" }
        }
    }
]);

30.-- Calculate the average ride_time of all rides in SQL
SELECT AVG(ride_time) AS average_ride_time
FROM Rides;


// Calculate the average ride_time of all rides in MongoDB
db.Rides.aggregate([
    {
        $group: {
            _id: null,
            average_ride_time: { $avg: "$ride_time" }
        }
    }
]);


31.-- Fetch all rides with start_location or end_location containing 'Downtown' in SQL
SELECT *
FROM Rides
WHERE start_location LIKE '%Downtown%' OR end_location LIKE '%Downtown%';


// Fetch all rides with start_location or end_location containing 'Downtown' in MongoDB
db.Rides.find({
    $or: [
        { start_location: { $regex: /Downtown/ } },
        { end_location: { $regex: /Downtown/ } }
    ]
});

32.-- Count the number of rides for a given driver_id in SQL
SELECT COUNT(*) AS ride_count
FROM Rides
WHERE driver_id = <your_driver_id>;

// Count the number of rides for a given driver_id in MongoDB
db.Rides.aggregate([
    {
        $match: { driver_id: <your_driver_id> }
    },
    {
        $group: {
            _id: null,
            ride_count: { $sum: 1 }
        }
    }
]);

33.-- Update the fare of the ride with id 4 in SQL
UPDATE Rides
SET fare = <new_fare_value>
WHERE id = 4;

// Update the fare of the ride with id 4 in MongoDB
db.Rides.updateOne(
    { _id: ObjectId("id_of_ride_4") }, // Replace with the actual ObjectId of the ride
    { $set: { fare: <new_fare_value> } } // Replace with the desired fare value
);


34.-- Calculate the total fare for each driver_id in SQL
SELECT driver_id, SUM(fare) AS total_fare
FROM Rides
GROUP BY driver_id;

// Calculate the total fare for each driver_id in MongoDB
db.Rides.aggregate([
    {
        $group: {
            _id: "$driver_id",
            total_fare: { $sum: "$fare" }
        }
    }
]);


35.-- Delete the ride with id 2 in SQL
DELETE FROM Rides
WHERE id = 2;

// Delete the ride with id 2 in MongoDB
db.Rides.deleteOne({ _id: ObjectId("id_of_ride_2") });



