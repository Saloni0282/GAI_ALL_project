1. -- Create a Customers table in SQL
CREATE TABLE Customers (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    address VARCHAR(255),
    phone_number VARCHAR(50)
);

2. -- Insert data into the Customers table in SQL
INSERT INTO Customers (id, name, email, address, phone_number)
VALUES
  (1, 'John Smith', 'john@example.com', '123 Main St', '555-123-4567'),
  (2, 'Alice Johnson', 'alice@example.com', '456 Elm St', '555-987-6543'),
  (3, 'Bob Brown', 'bob@example.com', '789 Oak St', '555-567-8901'),
  (4, 'Eva Davis', 'eva@example.com', '321 Maple St', '555-234-5678'),
  (5, 'Michael Wilson', 'michael@example.com', '567 Pine St', '555-678-9012');

// Insert data into the Customers collection in MongoDB
db.Customers.insertMany([
  {
    id: 1,
    name: 'John Smith',
    email: 'john@example.com',
    address: '123 Main St',
    phone_number: '555-123-4567'
  },
  {
    id: 2,
    name: 'Alice Johnson',
    email: 'alice@example.com',
    address: '456 Elm St',
    phone_number: '555-987-6543'
  },
  {
    id: 3,
    name: 'Bob Brown',
    email: 'bob@example.com',
    address: '789 Oak St',
    phone_number: '555-567-8901'
  },
  {
    id: 4,
    name: 'Eva Davis',
    email: 'eva@example.com',
    address: '321 Maple St',
    phone_number: '555-234-5678'
  },
  {
    id: 5,
    name: 'Michael Wilson',
    email: 'michael@example.com',
    address: '567 Pine St',
    phone_number: '555-678-9012'
  }
]);

3. -- Fetch all data from the Customers table in SQL
SELECT * FROM Customers;

// Fetch all data from the Customers collection in MongoDB
db.Customers.find({});

4. -- Select only the name and email fields from the Customers table in SQL
SELECT name, email FROM Customers;

// Select only the name and email fields from the Customers collection in MongoDB
db.Customers.find({}, { name: 1, email: 1, _id: 0 });


5. -- Fetch the customer with id = 3 from the Customers table in SQL
SELECT * FROM Customers WHERE id = 3;


-- Fetch the customer with id = 3 from the Customers table in SQL
SELECT * FROM Customers WHERE id = 3;

6. -- Fetch customers whose name starts with 'A' in SQL
SELECT * FROM Customers WHERE name LIKE 'A%';
 
 // Fetch customers whose name starts with 'A' in MongoDB
db.Customers.find({ name: /^A/ });

7. -- Fetch all customers ordered by name in descending order in SQL
SELECT * FROM Customers
ORDER BY name DESC;

// Fetch all customers ordered by name in descending order in MongoDB
db.Customers.find().sort({ name: -1 });

8.-- Update the address of the customer with id = 4 in SQL
UPDATE Customers
SET address = '789 New Address St'
WHERE id = 4;


// Update the address of the customer with id = 4 in MongoDB
db.Customers.updateOne(
   { id: 4 },
   {
     $set: {
       address: '789 New Address St'
     }
   }
);

9. -- Fetch the top 3 customers ordered by id in ascending order in SQL
SELECT * FROM Customers
ORDER BY id ASC
LIMIT 3;


// Fetch the top 3 customers ordered by id in ascending order in MongoDB
db.Customers.find().sort({ id: 1 }).limit(3);

10. -- Delete the customer with id = 2 in SQL
DELETE FROM Customers
WHERE id = 2;


// Delete the customer with id = 2 in MongoDB
db.Customers.deleteOne({ id: 2 });

11.-- Count the number of customers in SQL
SELECT COUNT(*) AS customer_count FROM Customers;


// Count the number of customers in MongoDB
db.Customers.countDocuments();

12.-- Fetch all customers except the first two ordered by id in ascending order in SQL
SELECT * FROM Customers
ORDER BY id ASC
OFFSET 2;

// Fetch all customers except the first two ordered by id in ascending order in MongoDB
db.Customers.find().sort({ id: 1 }).skip(2);


13.-- Fetch customers whose id is greater than 2 and name starts with 'B' in SQL
SELECT * FROM Customers
WHERE id > 2 AND name LIKE 'B%';

// Fetch customers whose id is greater than 2 and name starts with 'B' in MongoDB
db.Customers.find({
  $and: [
    { id: { $gt: 2 } },
    { name: /^B/ }
  ]
});

14.-- Fetch customers whose id is less than 3 or name ends with 's' in SQL
SELECT * FROM Customers
WHERE id < 3 OR name LIKE '%s';

// Fetch customers whose id is less than 3 or name ends with 's' in MongoDB
db.Customers.find({
  $or: [
    { id: { $lt: 3 } },
    { name: /s$/ }
  ]
});

15.-- Fetch customers where phone_number is not set or is null in SQL
SELECT * FROM Customers
WHERE phone_number IS NULL OR phone_number = '';

// Fetch customers where phone_number is not set or is null in MongoDB
db.Customers.find({
  $or: [
    { phone_number: null },
    { phone_number: '' }
  ]
});
