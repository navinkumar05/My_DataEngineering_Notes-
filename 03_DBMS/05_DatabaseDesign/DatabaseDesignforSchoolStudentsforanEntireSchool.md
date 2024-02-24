This summary is for [this video](https://www.youtube.com/watch?v=1YPT6VH256w&list=PLZDOU071E4v6epq3GS0IqZicZc3xwwBN_&index=20)

Database Design for School Students for an Entire School

1. The school stores information about students: their name (first, middle, last), gender, date of birth, and when they enrolled at the school.<br>
2.	Information about parents, grandparents, and other carers of students can be stored. A student can have many of these. Each of them has a name and contact information, such as email and phone.<br>
3.	Schools operate based on school years. A year has a start date and end date, and can be in a single calendar year or multiple calendar years.<br>
4.	A year has multiple terms, which have start and end dates. There is no specific number of terms that are required for a year.<br>
5.	Students are enrolled in one year level at a time, and can move up to the next year level in the future. A year level could be kinder, grade 1, 2, 3, and so on.<br>
6.	Students are part of classes, and can be in more than one class at a time.<br>
7.	A class has a subject, such as Sport, or Physics. A class subject may be a more general name for the junior years.<br>
8.	Subjects belong to departments. For example, Physics and Chemistry belong to the Science department.<br>
9.	A class is taught by a teacher.<br>
10.	Teachers are stored in our system, and have names, genders, and contact information.<br>
11.	A class exists for a term. There can be multiple classes in a year, and multiple classes within the same term (e.g. if there is a large number of English students and they need to split the class into two). A class can have a name to help describe it.<br>
12.	The time that a class occurs is called a period. There are a certain number of periods per day, and the periods are set for the entire school each year.<br>
13.	A class can occur over multiple periods, which could be two periods or up to the entire day.<br>
14.	Students are graded based on their work in each class and given a score between 0 and 100. This score is stored for each class and a calculation is done to determine their overall score for the year.<br>
15.	Classes are held in a classroom. A classroom can be a certain type of room, such as a gymnasium or computer room or regular classroom. A classroom has a name that could include the location, and the capacity or number of students it can hold.<br>
16.	The scores can be matched to a letter grade. For example, a score of 0-50 means an "F", from 51 to 60 means a "D", and so on, up to 100.<br>

<img src ="attachment\erd_school.png">

[00:00-18:32](https://www.youtube.com/watch?v=1YPT6VH256w&t=0) 
 # Designing a School Management System Database

## Introduction
Designing a database for a school involves careful consideration of various aspects such as students, teachers, classes, and more. In this article, we'll go through the step-by-step process of designing a comprehensive database for a school management system. The goal is to meet the requirements and create a flexible and efficient database structure.

## Requirements Analysis
Let's start with a blank page and outline the requirements for our school database. We'll break down the design process by addressing each requirement systematically.

### 1. Student Information
The first requirement is to store information about students, including their name, gender, date of birth, and enrollment date. We'll create a table named `student` to capture this data.

```markdown
### Student Table
-  ID (Primary Key)
-  Name (First, Middle, Last)
-  Gender
-  Date of Birth
-  Enrollment Date
```

### 2. Guardians
The database should store information about parents, grandparents, and other carers. We'll create a table named `guardian` and introduce a joining table `student_guardian` to handle the many-to-many relationship.

```markdown
### Guardian Table
-  ID (Primary Key)
-  Given Name
-  Surname
-  Email Address
-  Phone Number

### Student_Guardian Table (Joining Table)
-  Student ID (Foreign Key)
-  Guardian ID (Foreign Key)
-  Guardian Type (e.g., Mother, Father)
```

### 3. School Years
To represent school years with start and end dates, we'll create a table named `school_year`.

```markdown
### School Year Table
-  ID (Primary Key)
-  Start Date
-  End Date
-  Name
```

### 4. Terms
The requirement is to have multiple terms within a year. We'll create a table named `term` to capture this information.

```markdown
### Term Table
-  ID (Primary Key)
-  Year ID (Foreign Key)
-  Term Number
-  Start Date
-  End Date
```

### 5. Year Levels
To represent different levels or grades in the school, we'll create a table named `year_level`.

```markdown
### Year Level Table
-  ID (Primary Key)
-  Name
-  Level Order
```

### 6. Student-Year Level Relationship
As students move across different levels, we'll introduce a joining table `student_year_level`.

```markdown
### Student_Year_Level Table (Joining Table)
-  Student ID (Foreign Key)
-  Year Level ID (Foreign Key)
-  School Year ID (Foreign Key)
```

### 7. Classes
Classes are introduced as entities, and we create a basic table named `class`.

```markdown
### Class Table
-  ID (Primary Key)
```

### 8. Subjects
Each class is associated with subjects, and we'll create a `subject` table.

```markdown
### Subject Table
-  ID (Primary Key)
-  Subject Name
```

### 9. Departments
Subjects belong to departments, and we'll create a `department` table.

```markdown
### Department Table
-  ID (Primary Key)
-  Name
```

### 10. Teachers
Teachers are introduced as entities, and we create a `teacher` table.

```markdown
### Teacher Table
-  ID (Primary Key)
-  Given Name
-  Surname
-  Gender
-  Email Address
-  Phone Number
```

### 11. Class-Subject Relationship
We establish a relationship between classes and subjects using a joining table `class_subject`.

```markdown
### Class_Subject Table (Joining Table)
-  Class ID (Foreign Key)
-  Subject ID (Foreign Key)
```

### 12. Class-Teacher Relationship
We link classes and teachers using a joining table `class_teacher`.

```markdown
### Class_Teacher Table (Joining Table)
-  Class ID (Foreign Key)
-  Teacher ID (Foreign Key)
```

### 13. Class-Term Relationship
Classes are related to terms through a joining table `class_term`.

```markdown
### Class_Term Table (Joining Table)
-  Class ID (Foreign Key)
-  Term ID (Foreign Key)
```

### 14. Class-Period Relationship
The requirement is that a class can occur over multiple periods. We enhance the `class` table.

```markdown
### Class Table (Enhanced)
-  ID (Primary Key)
-  Name
-  Start Period ID (Foreign Key)
-  End Period ID (Foreign Key)
```

### 15. Class-Period Relationship
We create a joining table `class_period` to establish a relationship between classes and periods.

```markdown
### Class_Period Table (Joining Table)
-  Class ID (Foreign Key)
-  Period ID (Foreign Key)
```

### 16. Student Grades
Students are graded based on their work, and we enhance the `student_class` table.

```markdown
### Student_Class Table (Enhanced)
-  Student ID (Foreign Key)
-  Class ID (Foreign Key)
-  Score
```

### 17. Score Ranges
We introduce a `score_range` table to map scores to letter grades.

```markdown
### Score_Range Table
-  ID (Primary Key)
-  Grade (Letter)
-  Min Score
-  Max Score
```

## Conclusion
This comprehensive database design captures various aspects of a school management system, including students, teachers, classes, terms, and grading. The design can be further enhanced to meet additional requirements. Refer to the database diagram(link_to_diagram) for a visual representation of the structure.

In summary, a well-designed school management system database provides a solid foundation for efficient data management and retrieval, meeting the diverse needs of educational institutions.