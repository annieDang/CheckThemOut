# Checkout System

## Overview

This project implements a flexible checkout system for a computer store, incorporating various pricing rules. The system is designed to handle different types of promotions and pricing strategies while ensuring scalability and maintainability. The implementation is done in Python using object-oriented programming principles.

## Design Pattern

The system is built using the Strategy Design Pattern. This pattern is used to define a family of algorithms, encapsulate each one, and make them interchangeable. Strategy allows the algorithm to vary independently from clients that use it.

## Why Strategy Pattern?

Flexibility: Different pricing rules can be applied to different products without changing the core logic of the checkout process.
Scalability: New pricing rules can be added easily without modifying existing code.
Maintainability: Encapsulating the pricing rules into separate classes makes the codebase cleaner and easier to manage.

## Components

- Product: Represents a product in the store.
- Item: Represents an item with a status that tracks its state (e.g., "in store", "scanned", "payed").
- Pricing Rules: Different pricing rules are implemented as separate classes, inheriting from a common interface.

  ```
  Example pricing rules:

  ThreeForTwoDeal: Buy 3, pay for 2.
  BulkDiscount: Discount for buying in bulk.
  FreeBundle: Free item with the purchase of another item.
  ```

- Inventory: Manages the stock of items.
- Checkout: Handles the scanning of items and calculates the total cost, applying any relevant pricing rules.

## Testing

Testing is implemented using pytest. Test files are located in the tests directory and include tests for the checkout process, inventory management, and pricing rules.

### Running Tests

`make test`
