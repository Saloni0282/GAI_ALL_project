36. -- SQL: Find the ride with the highest and lowest fare
SELECT *
FROM Rides
WHERE fare = (SELECT MAX(fare) FROM Rides)
   OR fare = (SELECT MIN(fare) FROM Rides);

// MongoDB: Find the ride with the highest and lowest fare
db.Rides.find({ $or: [{ fare: db.Rides.find().sort({ fare: -1 }).limit(1)[0].fare }, { fare: db.Rides.find().sort({ fare: 1 }).limit(1)[0].fare }] });

37. -- SQL: Find the average fare and distance for each driver_id
SELECT driver_id, AVG(fare) AS average_fare, AVG(distance) AS average_distance
FROM Rides
GROUP BY driver_id;

// MongoDB: Find the average fare and distance for each driver_id
db.Rides.aggregate([
    {
        $group: {
            _id: "$driver_id",
            average_fare: { $avg: "$fare" },
            average_distance: { $avg: "$distance" }
        }
    }
]);

38.-- SQL: Find driver_id that have completed more than 5 rides
SELECT driver_id
FROM Rides
GROUP BY driver_id
HAVING COUNT(*) > 5;

// MongoDB: Find driver_id that have completed more than 5 rides
db.Rides.aggregate([
    {
        $group: {
            _id: "$driver_id",
            ride_count: { $sum: 1 }
        }
    },
    {
        $match: { ride_count: { $gt: 5 } }
    }
]);

39. -- SQL: Find the name of the driver with the highest fare
SELECT Drivers.name
FROM Rides
INNER JOIN Drivers ON Rides.driver_id = Drivers.driver_id
WHERE Rides.fare = (SELECT MAX(fare) FROM Rides);

// MongoDB: Find the name of the driver with the highest fare
db.Rides.aggregate([
    {
        $sort: { fare: -1 }
    },
    {
        $limit: 1
    },
    {
        $lookup: {
            from: "Drivers",
            localField: "driver_id",
            foreignField: "driver_id",
            as: "driver"
        }
    },
    {
        $unwind: "$driver"
    },
    {
        $project: { "driver.name": 1, _id: 0 }
    }
]);

40. -- SQL: Find the top 3 drivers who have earned the most from fares
SELECT driver_id, SUM(fare) AS total_earnings
FROM Rides
GROUP BY driver_id
ORDER BY total_earnings DESC
LIMIT 3;

// MongoDB: Find the top 3 drivers who have earned the most from fares
db.Rides.aggregate([
    {
        $group: {
            _id: "$driver_id",
            total_earnings: { $sum: "$fare" }
        }
    },
    {
        $sort: { total_earnings: -1 }
    },
    {
        $limit: 3
    }
]);

41. -- SQL: Find all rides that happened in the last 7 days
SELECT *
FROM Rides
WHERE ride_date >= DATE_SUB(NOW(), INTERVAL 7 DAY);

// MongoDB: Find all rides that happened in the last 7 days
const sevenDaysAgo = new Date();
sevenDaysAgo.setDate(sevenDaysAgo.getDate() - 7);
db.Rides.find({ ride_date: { $gte: sevenDaysAgo } });

42. -- SQL: Find all rides where the end_location is not set
SELECT *
FROM Rides
WHERE end_location IS NULL;

// MongoDB: Find all rides where the end_location is not set
db.Rides.find({ end_location: { $exists: false } });

43. -- SQL: Calculate the fare per mile for each ride and order by fare per mile in descending order
SELECT id, fare / distance AS fare_per_mile
FROM Rides
ORDER BY fare_per_mile DESC;

// MongoDB: Calculate the fare per mile for each ride and order by fare per mile in descending order
db.Rides.aggregate([
    {
        $addFields: { fare_per_mile: { $divide: ["$fare", "$distance"] } }
    },
    {
        $sort: { fare_per_mile: -1 }
    },
    {
        $project: { id: 1, fare_per_mile: 1, _id: 0 }
    }
]);

44. -- SQL: Return a list of all rides including the driver's name and passenger's name
SELECT Rides.id, Drivers.name AS driver_name, Passengers.name AS passenger_name
FROM Rides
INNER JOIN Drivers ON Rides.driver_id = Drivers.driver_id
INNER JOIN Passengers ON Rides.passenger_id = Passengers.passenger_id;

// MongoDB: Return a list of all rides including the driver's name and passenger's name
db.Rides.aggregate([
    {
        $lookup: {
            from: "Drivers",
            localField: "driver_id",
            foreignField: "driver_id",
            as: "driver"
        }
    },
    {
        $unwind: "$driver"
    },
    {
        $lookup: {
            from: "Passengers",
            localField: "passenger_id",
            foreignField: "passenger_id",
            as: "passenger"
        }
    },
    {
        $unwind: "$passenger"
    },
    {
        $project: { id: 1, "driver.name": 1, "passenger.name": 1, _id: 0 }
    }
]);


45. -- SQL: Add a tip field to the Rides table
ALTER TABLE Rides
ADD COLUMN tip DECIMAL(6, 2);

// MongoDB: Add a tip field to the Rides collection
db.Rides.updateMany({}, { $set: { tip: 0 } });

