import streamlit as st

st.set_page_config(
    page_title="SQL Mastery Program", 
    page_icon="🗄️",
    layout="wide"
)

# --- Custom CSS for SQL/Database Branding ---
st.markdown("""
<style>
    .sql-header {
        background: linear-gradient(90deg, #00758F 0%, #F29111 100%);
        padding: 2rem;
        border-radius: 10px;
        color: white;
        text-align: center;
    }
    .sql-header h1 {
        color: #F29111;
        text-shadow: 2px 2px 4px #000000;
    }
    .highlight-box {
        background-color: #f0f2f6;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #F29111;
    }
    .module-card {
        background-color: white;
        padding: 1.2rem;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        margin-bottom: 1rem;
        border: 1px solid #e0e0e0;
        transition: transform 0.2s;
    }
    .module-card:hover {
        transform: scale(1.02);
        box-shadow: 0 4px 8px rgba(0,0,0,0.15);
        border-color: #F29111;
    }
    .career-badge {
        background-color: #00758F;
        color: #F29111;
        padding: 0.3rem 0.8rem;
        border-radius: 20px;
        font-weight: bold;
        display: inline-block;
    }
    .query-box {
        background-color: #1e1e1e;
        color: #F29111;
        padding: 0.5rem;
        border-radius: 5px;
        font-family: 'Courier New', monospace;
        border-left: 3px solid #F29111;
    }
    .note-box {
        background-color: #e7f3ff;
        padding: 1rem;
        border-radius: 5px;
        border-left: 5px solid #00758F;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# --- Header Section with SQL Branding ---
st.markdown("""
<div class="sql-header">
    <h1>🗄️ SQL Mastery Program</h1>
    <h3>From Zero to SQL Expert | Data Analysis • Database Management • Query Optimization</h3>
    <p style="font-size: 1.2rem;">Master MySQL, PostgreSQL, SQL Server • Complex Queries • Joins • Window Functions</p>
</div>
""", unsafe_allow_html=True)

# --- Quick Stats ---
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Duration", "2 Months", "Weekend/Hybrid")
with col2:
    st.metric("Level", "Beginner to Expert", "No Prior Experience")
with col3:
    st.metric("Projects", "6 Database Projects", "Portfolio Ready")
with col4:
    st.metric("Fee", "₹15,000", "EMI Available")

st.markdown("---")

# --- Why SQL? Section ---
st.markdown("## 🎯 Why SQL? The Language of Data")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="highlight-box">
        <h4>📈 Career Opportunities</h4>
        <ul>
            <li><strong>SQL Developer</strong> - ₹4-8 LPA</li>
            <li><strong>Data Analyst</strong> - ₹5-10 LPA</li>
            <li><strong>Database Administrator</strong> - ₹6-12 LPA</li>
            <li><strong>Business Intelligence Analyst</strong> - ₹5-9 LPA</li>
            <li><strong>Backend Developer</strong> - ₹6-15 LPA</li>
            <li><strong>Data Engineer</strong> - ₹8-18 LPA</li>
        </ul>
        <p><span class="career-badge">🔥 SQL is #1 Required Skill for Data Roles</span></p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="highlight-box">
        <h4>🏢 Top Hiring Companies</h4>
        <ul>
            <li>Google • Amazon • Microsoft</li>
            <li>JPMorgan • Goldman Sachs</li>
            <li>Deloitte • EY • KPMG • PwC</li>
            <li>Flipkart • Uber • Ola • Zomato</li>
            <li>Infosys • TCS • Wipro • Accenture</li>
            <li>And 10,000+ more companies</li>
        </ul>
        <p><span class="career-badge">🎯 100% of Companies Use SQL</span></p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# --- Comprehensive SQL Curriculum ---
st.markdown("## 📚 Complete SQL Mastery Curriculum")
st.markdown("### Structured Learning Path - From Zero to Hero")

# Create tabs for different levels
tab1, tab2, tab3, tab4, tab5 = st.tabs(["🔰 SQL Basics", "📊 Intermediate SQL", "🚀 Advanced SQL", "⚡ Expert SQL", "🏗️ Database Design"])

with tab1:
    st.markdown("### Module 01: SQL Fundamentals")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="module-card">
            <h4>📌 Introduction to Databases</h4>
            <ul>
                <li>What is SQL? Why SQL?</li>
                <li>RDBMS Concepts (Tables, Rows, Columns)</li>
                <li>Database Types (MySQL, PostgreSQL, SQL Server)</li>
                <li>Installing MySQL/PostgreSQL</li>
                <li>GUI Tools (Workbench, pgAdmin, DBeaver)</li>
                <li>Database vs Schema vs Tables</li>
            </ul>
            <div class="query-box">
                SHOW DATABASES;<br>
                USE database_name;<br>
                SELECT DATABASE();
            </div>
        </div>
        
        <div class="module-card">
            <h4>📋 Data Types in SQL</h4>
            <ul>
                <li>Numeric Types (INT, DECIMAL, FLOAT)</li>
                <li>String Types (CHAR, VARCHAR, TEXT)</li>
                <li>Date & Time (DATE, TIME, DATETIME, TIMESTAMP)</li>
                <li>Boolean & Binary Types</li>
                <li>Choosing Right Data Types</li>
                <li>Type Conversion (CAST, CONVERT)</li>
            </ul>
        </div>
        
        <div class="module-card">
            <h4>🆕 Creating Tables</h4>
            <ul>
                <li>CREATE TABLE Statement</li>
                <li>Column Constraints (NOT NULL, UNIQUE)</li>
                <li>DEFAULT Values</li>
                <li>AUTO_INCREMENT / SERIAL</li>
                <li>ALTER TABLE (ADD, MODIFY, DROP)</li>
                <li>DROP TABLE vs TRUNCATE vs DELETE</li>
            </ul>
            <div class="query-box">
                CREATE TABLE employees (<br>
                &nbsp;&nbsp;id INT PRIMARY KEY AUTO_INCREMENT,<br>
                &nbsp;&nbsp;name VARCHAR(100) NOT NULL,<br>
                &nbsp;&nbsp;salary DECIMAL(10,2) DEFAULT 0<br>
                );
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="module-card">
            <h4>🔍 Basic SELECT Queries</h4>
            <ul>
                <li>SELECT * FROM table</li>
                <li>SELECT Specific Columns</li>
                <li>SELECT DISTINCT (Unique Values)</li>
                <li>Aliases (AS) for Columns & Tables</li>
                <li>Comments in SQL</li>
                <li>LIMIT & OFFSET for Pagination</li>
            </ul>
            <div class="query-box">
                SELECT first_name, salary <br>
                FROM employees <br>
                LIMIT 10;
            </div>
        </div>
        
        <div class="module-card">
            <h4>🎯 Filtering Data (WHERE Clause)</h4>
            <ul>
                <li>WHERE Clause Syntax</li>
                <li>Comparison Operators (=, !=, >, <, >=, <=)</li>
                <li>Logical Operators (AND, OR, NOT)</li>
                <li>IN Operator (Multiple Values)</li>
                <li>BETWEEN (Range Filtering)</li>
                <li>LIKE & Wildcards (%, _)</li>
                <li>IS NULL / IS NOT NULL</li>
            </ul>
            <div class="query-box">
                SELECT * FROM employees <br>
                WHERE salary > 50000 <br>
                AND department = 'IT' <br>
                AND name LIKE 'A%';
            </div>
        </div>
        
        <div class="module-card">
            <h4>📊 Sorting & Ordering</h4>
            <ul>
                <li>ORDER BY (ASC, DESC)</li>
                <li>Sorting by Multiple Columns</li>
                <li>ORDER BY with Expressions</li>
                <li>Custom Sorting (FIELD())</li>
            </ul>
            <div class="query-box">
                SELECT * FROM employees <br>
                ORDER BY salary DESC, name ASC;
            </div>
        </div>
        """, unsafe_allow_html=True)

with tab2:
    st.markdown("### Module 02: Intermediate SQL")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="module-card">
            <h4>📊 Aggregate Functions</h4>
            <ul>
                <li>COUNT() - Count Rows</li>
                <li>SUM() - Total of Column</li>
                <li>AVG() - Average Value</li>
                <li>MIN() & MAX() - Minimum & Maximum</li>
                <li>COUNT(DISTINCT) - Unique Count</li>
                <li>Aggregate with Filtering</li>
            </ul>
            <div class="query-box">
                SELECT <br>
                &nbsp;&nbsp;COUNT(*) as total_employees,<br>
                &nbsp;&nbsp;AVG(salary) as avg_salary,<br>
                &nbsp;&nbsp;MAX(salary) as max_salary<br>
                FROM employees;
            </div>
        </div>
        
        <div class="module-card">
            <h4>📑 GROUP BY & HAVING</h4>
            <ul>
                <li>GROUP BY Fundamentals</li>
                <li>Grouping by Single Column</li>
                <li>Grouping by Multiple Columns</li>
                <li>HAVING vs WHERE</li>
                <li>Filtering Groups with HAVING</li>
                <li>Grouping with Aggregates</li>
            </ul>
            <div class="query-box">
                SELECT department, AVG(salary) as avg_salary<br>
                FROM employees<br>
                GROUP BY department<br>
                HAVING AVG(salary) > 60000;
            </div>
        </div>
        
        <div class="module-card">
            <h4>➕ INSERT, UPDATE, DELETE</h4>
            <ul>
                <li>INSERT INTO (Single Row)</li>
                <li>INSERT Multiple Rows</li>
                <li>INSERT INTO SELECT</li>
                <li>UPDATE Statement</li>
                <li>DELETE Statement</li>
                <li>ON DELETE CASCADE/SET NULL</li>
            </ul>
            <div class="query-box">
                INSERT INTO employees (name, salary, department)<br>
                VALUES ('John', 55000, 'IT');<br><br>
                UPDATE employees SET salary = 60000<br>
                WHERE name = 'John';
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="module-card">
            <h4>🔗 Joins - Combining Tables</h4>
            <ul>
                <li>INNER JOIN (Matching Records)</li>
                <li>LEFT JOIN (All from Left)</li>
                <li>RIGHT JOIN (All from Right)</li>
                <li>FULL OUTER JOIN (All Records)</li>
                <li>CROSS JOIN (Cartesian Product)</li>
                <li>SELF JOIN (Table with Itself)</li>
                <li>NATURAL JOIN</li>
            </ul>
            <div class="query-box">
                SELECT e.name, d.department_name<br>
                FROM employees e<br>
                INNER JOIN departments d<br>
                ON e.dept_id = d.dept_id;
            </div>
        </div>
        
        <div class="module-card">
            <h4>🔄 Joins with Multiple Tables</h4>
            <ul>
                <li>Joining 3+ Tables</li>
                <li>Join with WHERE Conditions</li>
                <li>Join with Aggregate Functions</li>
                <li>Join with GROUP BY</li>
                <li>Join Best Practices</li>
                <li>Performance Considerations</li>
            </ul>
            <div class="query-box">
                SELECT o.order_id, c.name, p.product_name<br>
                FROM orders o<br>
                JOIN customers c ON o.customer_id = c.id<br>
                JOIN products p ON o.product_id = p.id;
            </div>
        </div>
        
        <div class="module-card">
            <h4>📝 String & Date Functions</h4>
            <ul>
                <li>String Functions (CONCAT, UPPER, LOWER)</li>
                <li>SUBSTRING, REPLACE, TRIM</li>
                <li>LENGTH, POSITION, LEFT/RIGHT</li>
                <li>Date Functions (NOW, CURDATE, YEAR, MONTH)</li>
                <li>DATEDIFF, DATE_ADD, DATE_SUB</li>
                <li>EXTRACT, DATE_FORMAT</li>
            </ul>
            <div class="query-box">
                SELECT CONCAT(first_name, ' ', last_name) as full_name,<br>
                &nbsp;&nbsp;DATEDIFF(NOW(), hire_date) as days_worked<br>
                FROM employees;
            </div>
        </div>
        """, unsafe_allow_html=True)

with tab3:
    st.markdown("### Module 03: Advanced SQL")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="module-card">
            <h4>🔍 Subqueries</h4>
            <ul>
                <li>Single-Row Subqueries</li>
                <li>Multi-Row Subqueries (IN, ANY, ALL)</li>
                <li>Correlated Subqueries</li>
                <li>Subqueries in SELECT</li>
                <li>Subqueries in FROM (Derived Tables)</li>
                <li>Subqueries in WHERE</li>
                <li>EXISTS & NOT EXISTS</li>
            </ul>
            <div class="query-box">
                SELECT name, salary<br>
                FROM employees<br>
                WHERE salary > (SELECT AVG(salary) FROM employees);
            </div>
        </div>
        
        <div class="module-card">
            <h4>🔄 Set Operations</h4>
            <ul>
                <li>UNION & UNION ALL</li>
                <li>INTERSECT</li>
                <li>EXCEPT / MINUS</li>
                <li>Set Operation Rules</li>
                <li>Combining with ORDER BY</li>
            </ul>
            <div class="query-box">
                SELECT name FROM employees<br>
                UNION<br>
                SELECT name FROM contractors;
            </div>
        </div>
        
        <div class="module-card">
            <h4>📊 Window Functions - Part 1</h4>
            <ul>
                <li>Introduction to Window Functions</li>
                <li>OVER() Clause</li>
                <li>PARTITION BY</li>
                <li>ORDER BY in Windows</li>
                <li>ROW_NUMBER()</li>
                <li>RANK() & DENSE_RANK()</li>
            </ul>
            <div class="query-box">
                SELECT name, department, salary,<br>
                &nbsp;&nbsp;ROW_NUMBER() OVER(PARTITION BY department ORDER BY salary DESC) as rank<br>
                FROM employees;
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="module-card">
            <h4>📈 Window Functions - Part 2</h4>
            <ul>
                <li>LAG() & LEAD() - Previous/Next Values</li>
                <li>FIRST_VALUE() & LAST_VALUE()</li>
                <li>NTILE() - Bucketing</li>
                <li>Running Totals</li>
                <li>Moving Averages</li>
                <li>Window Frames (ROWS/RANGE)</li>
            </ul>
            <div class="query-box">
                SELECT name, salary,<br>
                &nbsp;&nbsp;LAG(salary, 1) OVER(ORDER BY salary) as prev_salary<br>
                FROM employees;
            </div>
        </div>
        
        <div class="module-card">
            <h4>📋 Common Table Expressions (CTEs)</h4>
            <ul>
                <li>WITH Clause Basics</li>
                <li>Simple CTEs</li>
                <li>Multiple CTEs</li>
                <li>Recursive CTEs</li>
                <li>CTEs vs Subqueries</li>
                <li>CTEs with Window Functions</li>
            </ul>
            <div class="query-box">
                WITH high_earners AS (<br>
                &nbsp;&nbsp;SELECT * FROM employees WHERE salary > 70000<br>
                )<br>
                SELECT * FROM high_earners;
            </div>
        </div>
        
        <div class="module-card">
            <h4>📊 CASE Statements & Conditional Logic</h4>
            <ul>
                <li>CASE WHEN THEN</li>
                <li>Simple CASE vs Searched CASE</li>
                <li>Nested CASE Statements</li>
                <li>IF() and IFNULL()</li>
                <li>COALESCE() for NULL Handling</li>
                <li>Conditional Aggregation</li>
            </ul>
            <div class="query-box">
                SELECT name, salary,<br>
                &nbsp;&nbsp;CASE <br>
                &nbsp;&nbsp;&nbsp;&nbsp;WHEN salary > 70000 THEN 'High'<br>
                &nbsp;&nbsp;&nbsp;&nbsp;WHEN salary > 40000 THEN 'Medium'<br>
                &nbsp;&nbsp;&nbsp;&nbsp;ELSE 'Low'<br>
                &nbsp;&nbsp;END as salary_category<br>
                FROM employees;
            </div>
        </div>
        """, unsafe_allow_html=True)

with tab4:
    st.markdown("### Module 04: Expert SQL")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="module-card">
            <h4>⚡ Query Optimization</h4>
            <ul>
                <li>Understanding EXPLAIN / Execution Plan</li>
                <li>Identifying Slow Queries</li>
                <li>Indexing Strategies</li>
                <li>Avoiding SELECT *</li>
                <li>Optimizing JOINs</li>
                <li>Query Rewriting Techniques</li>
            </ul>
        </div>
        
        <div class="module-card">
            <h4>📑 Indexes for Performance</h4>
            <ul>
                <li>CREATE INDEX</li>
                <li>Single-Column vs Composite Indexes</li>
                <li>UNIQUE Indexes</li>
                <li>FULLTEXT Indexes for Search</li>
                <li>When to Use/Not Use Indexes</li>
                <li>Index Maintenance</li>
            </ul>
            <div class="query-box">
                CREATE INDEX idx_salary ON employees(salary);<br>
                CREATE INDEX idx_dept_salary ON employees(department, salary);
            </div>
        </div>
        
        <div class="module-card">
            <h4>🔒 Views & Materialized Views</h4>
            <ul>
                <li>Creating Views</li>
                <li>Updatable Views</li>
                <li>WITH CHECK OPTION</li>
                <li>Materialized Views (PostgreSQL)</li>
                <li>View vs Table</li>
                <li>Security with Views</li>
            </ul>
            <div class="query-box">
                CREATE VIEW high_salary_employees AS<br>
                SELECT name, salary FROM employees<br>
                WHERE salary > 70000;
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="module-card">
            <h4>💼 Stored Procedures & Functions</h4>
            <ul>
                <li>CREATE PROCEDURE</li>
                <li>Parameters (IN, OUT, INOUT)</li>
                <li>CREATE FUNCTION</li>
                <li>Function vs Procedure</li>
                <li>Variables & Control Flow</li>
                <li>Error Handling</li>
            </ul>
        </div>
        
        <div class="module-card">
            <h4>⚙️ Triggers & Events</h4>
            <ul>
                <li>CREATE TRIGGER</li>
                <li>BEFORE/AFTER INSERT, UPDATE, DELETE</li>
                <li>Row-Level Triggers</li>
                <li>Trigger Use Cases (Audit, Validation)</li>
                <li>Scheduled Events</li>
            </ul>
        </div>
        
        <div class="module-card">
            <h4>📊 Pivot Tables & Dynamic SQL</h4>
            <ul>
                <li>Pivoting Data (CASE + Aggregation)</li>
                <li>Dynamic SQL Generation</li>
                <li>PREPARE & EXECUTE</li>
                <li>Cross-tab Reports</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

with tab5:
    st.markdown("### Module 05: Database Design & Modeling")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="module-card">
            <h4>🏗️ Database Normalization</h4>
            <ul>
                <li>1NF (First Normal Form)</li>
                <li>2NF (Second Normal Form)</li>
                <li>3NF (Third Normal Form)</li>
                <li>BCNF (Boyce-Codd Normal Form)</li>
                <li>Denormalization Trade-offs</li>
                <li>Real-World Normalization Examples</li>
            </ul>
        </div>
        
        <div class="module-card">
            <h4>🔑 Keys & Constraints</h4>
            <ul>
                <li>Primary Key Strategies</li>
                <li>Foreign Key Relationships</li>
                <li>Composite Keys</li>
                <li>Unique Constraints</li>
                <li>Check Constraints</li>
                <li>Default Constraints</li>
                <li>Referential Integrity</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="module-card">
            <h4>📊 Entity-Relationship Diagrams (ERD)</h4>
            <ul>
                <li>Entities & Attributes</li>
                <li>Relationships (1:1, 1:M, M:N)</li>
                <li>Cardinality & Modality</li>
                <li>Designing ERDs</li>
                <li>Converting ERD to Tables</li>
                <li>Tools for ERD (MySQL Workbench, draw.io)</li>
            </ul>
        </div>
        
        <div class="module-card">
            <h4>🔄 Transactions & ACID</h4>
            <ul>
                <li>ACID Properties</li>
                <li>BEGIN TRANSACTION / COMMIT / ROLLBACK</li>
                <li>SAVEPOINT</li>
                <li>Transaction Isolation Levels</li>
                <li>READ COMMITTED, REPEATABLE READ</li>
                <li>Deadlocks & Resolution</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

st.markdown("---")

# --- 6 Real-World SQL Projects ---
st.markdown("## 🏆 6 Portfolio-Ready SQL Projects")
st.markdown("### Build These Real-World Database Projects")

project_cols = st.columns(2)

projects = [
    {
        "title": "🏪 E-Commerce Database",
        "description": "Complete database for online store - customers, products, orders, payments",
        "skills": "Tables, Relationships, Joins, Aggregations",
        "queries": "Sales reports, customer analysis, inventory management"
    },
    {
        "title": "🏥 Hospital Management System",
        "description": "Database for patients, doctors, appointments, prescriptions",
        "skills": "Normalization, Foreign Keys, Complex Joins",
        "queries": "Doctor schedules, patient history, revenue reports"
    },
    {
        "title": "📚 Library Management System",
        "description": "Track books, members, borrowing, returns, fines",
        "skills": "Constraints, Date Functions, Subqueries",
        "queries": "Overdue books, popular titles, member activity"
    },
    {
        "title": "🎓 Student Database",
        "description": "University database - students, courses, enrollments, grades",
        "skills": "Many-to-Many, Aggregate Functions, Window Functions",
        "queries": "Grade analysis, student performance, course popularity"
    },
    {
        "title": "🏦 Banking System",
        "description": "Accounts, transactions, customers, branches",
        "skills": "Transactions, Stored Procedures, Triggers",
        "queries": "Account statements, transaction history, balance checks"
    },
    {
        "title": "📦 Employee Management",
        "description": "Employees, departments, salaries, attendance, performance",
        "skills": "Self-Joins, Hierarchical Queries, CTEs",
        "queries": "Salary analysis, manager hierarchy, attendance reports"
    }
]

for i, project in enumerate(projects):
    if i % 2 == 0:
        cols = st.columns(2)
    with cols[i % 2]:
        st.markdown(f"""
        <div class="module-card">
            <h4>{project['title']}</h4>
            <p>{project['description']}</p>
            <p><strong>Skills:</strong> {project['skills']}</p>
            <p><strong>Key Queries:</strong> {project['queries']}</p>
            <p><span class="career-badge">Portfolio Project</span></p>
        </div>
        """, unsafe_allow_html=True)

st.markdown("---")

# --- SQL Interview Preparation ---
st.markdown("## 🎯 SQL Interview Preparation")
st.markdown("### Crack Data Analyst & Database Interviews")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="highlight-box">
        <h4>📋 Interview Topics Covered</h4>
        <ul>
            <li>✅ 100+ SQL Interview Questions</li>
            <li>✅ Complex Query Solving Techniques</li>
            <li>✅ Optimization & Performance Tuning</li>
            <li>✅ Real-World Problem Solving</li>
            <li>✅ Mock Interviews</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="highlight-box">
        <h4>📚 Companies Targeting</h4>
        <ul>
            <li>FAANG (Google, Amazon, Meta)</li>
            <li>Top Banks & Financial Firms</li>
            <li>Consulting Companies (Deloitte, EY)</li>
            <li>Product-Based Companies</li>
            <li>Startups & MNCs</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# --- Bonus Section ---
st.markdown("## 🎁 Exclusive Bonuses")

bonus_cols = st.columns(3)

bonuses = [
    {
        "icon": "📚",
        "title": "SQL Cheat Sheet",
        "desc": "Complete SQL syntax reference with examples"
    },
    {
        "icon": "📊",
        "title": "Practice Datasets",
        "desc": "20+ datasets with exercises"
    },
    {
        "icon": "📝",
        "title": "Interview Questions",
        "desc": "100+ real SQL interview questions"
    },
    {
        "icon": "🎥",
        "title": "Query Recordings",
        "desc": "Step-by-step query explanations"
    },
    {
        "icon": "🔧",
        "title": "Database Templates",
        "desc": "Ready-to-use database schemas"
    },
    {
        "icon": "📋",
        "title": "Resume Support",
        "desc": "SQL skills section optimization"
    }
]

for i, bonus in enumerate(bonuses):
    if i % 3 == 0:
        cols = st.columns(3)
    with cols[i % 3]:
        st.markdown(f"""
        <div class="module-card" style="text-align: center;">
            <h1>{bonus['icon']}</h1>
            <h4>{bonus['title']}</h4>
            <p>{bonus['desc']}</p>
        </div>
        """, unsafe_allow_html=True)

st.markdown("---")

# --- FAQ Section ---
st.markdown("## ❓ Frequently Asked Questions")

faq_col1, faq_col2 = st.columns(2)

with faq_col1:
    with st.expander("📌 Do I need any prior experience?"):
        st.write("No! We start from absolute basics. No coding or database experience required.")
    
    with st.expander("📌 Which SQL database will I learn?"):
        st.write("You'll learn MySQL/PostgreSQL (industry standard). Concepts apply to all databases.")
    
    with st.expander("📌 Is this enough for Data Analyst interviews?"):
        st.write("Absolutely! This covers everything asked in Data Analyst, BI, and SQL Developer interviews.")

with faq_col2:
    with st.expander("📌 Will I learn database design?"):
        st.write("Yes! Complete module on Database Design, Normalization, and ER Diagrams.")
    
    with st.expander("📌 Do you provide practice exercises?"):
        st.write("Yes! 100+ practice queries, 20+ datasets, and 6 complete projects.")
    
    with st.expander("📌 What if I miss a class?"):
        st.write("All sessions are recorded and available in your dashboard forever.")

st.markdown("---")

# --- Footer with CTA ---
st.markdown("""
<div style="background: linear-gradient(90deg, #00758F 0%, #F29111 100%); padding: 2.5rem; border-radius: 10px; text-align: center; color: white;">
    <h1 style="color: #F29111;">🚀 Ready to Master SQL?</h1>
    <h2>Join 4000+ Successful SQL Professionals</h2>
    <p style="font-size: 1.3rem;">Next Batch: Starting Soon | Limited to 8 Students Only</p>
    <p style="font-size: 2rem; font-weight: bold; color: #F29111;">Early Bird: ₹11,999 (Regular ₹15,000)</p>
    <p>✨ Includes 6 Projects + 100+ Queries + Interview Prep</p>
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# --- Apply Now Button ---
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.page_link("pages/Apply_Now.py", label="📩 APPLY NOW & GET FREE DEMO CLASS", icon="🎯")
    st.markdown("<p style='text-align: center;'>Limited Seats Available • Book Your Free Demo Today!</p>", unsafe_allow_html=True)

st.markdown("---")
st.caption("*Note: Clicking 'Apply Now' will work once the 'pages/Apply_Now.py' file is created.*")