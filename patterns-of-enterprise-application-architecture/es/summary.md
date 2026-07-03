1. Copyright

2. The Addison-Wesley Signature Series

3. Preface
  3.1 - Who This Book Is For
  3.2 - Acknowledgements
  3.3 - Colophon

4. Introduction
  4.1 - Architecture
  4.2 - Enterprise Applications
  4.3 - Kinds of Enterprise Application
  4.4 - Thinking About Performance
  4.5 - Patterns

5. Part 1. The Narratives
  5.1 - Chapter 1. Layering
    5.1.1 - The Evolution of Layers in Enterprise Application
    5.1.2 - The Three Principal Layers
    5.1.3 - Choosing Where to Run Your Layers
  5.2 - Chapter 2. Organizing Domain Logic
    5.2.1 - Making a Choice
    5.2.2 - Service Layer
  5.3 - Chapter 3. Mapping to Relational Databases
    5.3.1 - Architectural Patterns
    5.3.2 - The Behavioral Patterns
    5.3.3 - Reading in Data
    5.3.4 - Structural Mapping Patterns
    5.3.5 - Building the Mapping
    5.3.6 - Using Metadata
    5.3.7 - Database Connections
    5.3.8 - Some Miscellaneous Points
    5.3.9 - Further Reading
  5.4 - Chapter 4. Web Presentation
    5.4.1 - View Patterns
    5.4.2 - Input Controller Patterns
    5.4.3 - Further Reading
  5.5 - Chapter 5. Concurrency
    5.5.1 - Concurrency Problems
    5.5.2 - Execution Contexts
    5.5.3 - Isolation and Immutability
    5.5.4 - Optimistic and Pessimistic concurrency Control
    5.5.5 - Transactions
    5.5.6 - Patterns for Offline Concurrency Control
    5.5.7 - Application Server Concurrency
    5.5.8 - Further Reading
  5.6 - Chapter 6. Session State
    5.6.1 - The Value of Statelessness
    5.6.2 - Session State
  5.7 - Chapter 7. Distribution Strategies
    5.7.1 - The Allure of Distributed Objects
    5.7.2 - Remote and Local Interfaces
    5.7.3 - Where You Have to Distribute
    5.7.4 - Working with the Distribution Boundary
    5.7.5 - Interfaces for Distribution
  5.8 - Chapter 8. Putting It All Together
    5.8.1 - Starting with the Domain Layer
    5.8.2 - Down to the Data Source Layer
    5.8.3 - Some Technology-Specific Advice
    5.8.4 - Other Layering Schemes

6. Part 2. The Patterns
  6.1 - Chapter 9. Domain Logic Patterns
    6.1.1 - Transaction Script
    6.1.2 - Domain Model
    6.1.3 - Table Module
    6.1.4 - Service Layer
  6.2 - Chapter 10. Data Source Architectural Patterns
    6.2.1 - Table Data Gateway
    6.2.2 - Row Data Gateway
    6.2.3 - Active Record
    6.2.4 - Data Mapper
  6.3 - Chapter 11. Object-Relational Behavioral Patterns
    6.3.1 - Unit of Work
    6.3.2 - Identity Map
    6.3.3 - Lazy Load
  6.4 - Chapter 12. Object-Relational Structural Patterns
    6.4.1 - Identity Field
    6.4.2 - Foreign Key Mapping
    6.4.3 - Association Table Mapping
    6.4.4 - Dependent Mapping
    6.4.5 - Embedded Value
    6.4.6 - Serialized LOB
    6.4.7 - Single Table Inheritance
    6.4.8 - Class Table Inheritance
    6.4.9 - Concrete Table Inheritance
    6.4.10 - Inheritance Mappers
  6.5 - Chapter 13. Object-Relational Metadata Mapping Patterns
    6.5.1 - Metadata Mapping
    6.5.2 - Query Object
    6.5.3 - Repository
  6.6 - Chapter 14. Web Presentation Patterns
    6.6.1 - Model View Controller
    6.6.2 - Page Controller
    6.6.3 - Front Controller
    6.6.4 - Template View
    6.6.5 - Transform View
    6.6.6 - Two Step View
    6.6.7 - Application Controller
  6.7 - Chapter 15. Distribution Patterns
    6.7.1 - Remote Facade
    6.7.2 - Data Transfer Object
  6.8 - Chapter 16. Offline Concurrency Patterns
    6.8.1 - Optimistic Offline Lock
    6.8.2 - Pessimistic Offline Lock
    6.8.3 - Coarse-Grained Lock
    6.8.4 - Implicit Lock
  6.9 - Chapter 17. Session State Patterns
    6.9.1 - Client Session State
    6.9.2 - Server Session State
    6.9.3 - Database Session State
  6.10 - Chapter 18. Base Patterns
    6.10.1 - Gateway
    6.10.2 - Mapper
    6.10.3 - Layer Supertype
    6.10.4 - Separated Interface
    6.10.5 - Registry
    6.10.6 - Value Object
    6.10.7 - Money
    6.10.8 - Special Case
    6.10.9 - Plugin
    6.10.10 - Service Stub
    6.10.11 - Record Set

7. References