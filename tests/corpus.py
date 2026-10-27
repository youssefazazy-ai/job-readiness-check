# Test corpus: realistic job posts in the formats people actually paste, with what a careful human expects.
# req / pref: skills that must be detected with that priority. absent: skills that must NOT be detected.
# years: expected minimum-years note (0 = no note). scope: expect the "not a tech role" warning. max_unmapped: noise ceiling.
import pathlib
Q = pathlib.Path(__file__).parent

POSTS = [
dict(name="wuzzuf_frontend", text="""Junior Front-End Developer
Giza, Egypt
Full Time

Job Details
Experience Needed: 1 to 3 years
Career Level: Entry Level (Junior Level / Fresh Grad)
Education Level: Bachelor's Degree
Salary: Confidential
Job Categories: IT/Software Development Engineering - Telecom/Technology

Skills And Tools:
Information Technology (IT)
Computer Science
JavaScript
React

Job Description
Develop new user-facing features using React.js
Build reusable components and front-end libraries for future use
Translate designs and wireframes into high quality code
Optimize components for maximum performance across devices and browsers

Job Requirements
Strong proficiency in JavaScript, including DOM manipulation
Thorough understanding of React.js and its core principles
Experience with popular React.js workflows (such as Redux)
Familiarity with RESTful APIs
Knowledge of modern authorization mechanisms, such as JSON Web Token
Familiarity with code versioning tools such as Git
Experience with TypeScript is a plus""",
 req=["JavaScript","React","Redux","REST APIs","Git & GitHub","Authentication (JWT/OAuth)"], pref=["TypeScript"], absent=["Java"], years=1, max_unmapped=4),

dict(name="linkedin_about_the_job", text="""About the job
We are looking for a Junior Backend Engineer to join our growing fintech team in Cairo. You will design and build APIs used by thousands of merchants. You should have hands-on experience with Node.js and Express, a solid understanding of PostgreSQL and SQL, and be comfortable writing unit tests with Jest. Experience with Docker or AWS is a big plus. We value clear communication and teamwork.

About Paymob
Paymob is a leading payments company founded 10 years ago with over 500 employees.

Benefits
Medical insurance, flexible hours, and a modern office.""",
 req=["Node.js","Express","PostgreSQL","SQL","Unit testing","Jest","Communication","Teamwork"], pref=["Docker","AWS"], absent=[], years=0, max_unmapped=2),

dict(name="arabic_full", text="""مطلوب مطور Flutter جونيور للعمل في شركة ناشئة بالقاهرة

المهام:
- تطوير تطبيقات موبايل باستخدام Flutter و Dart
- ربط التطبيق بـ REST APIs و Firebase
- العمل مع فريق التصميم لتنفيذ الواجهات من Figma

المتطلبات:
- خبرة لا تقل عن سنة في تطوير تطبيقات Flutter
- فهم جيد لـ State Management مثل Bloc أو Provider
- معرفة بـ Git
- إجادة اللغة الإنجليزية قراءة وكتابة

يفضل:
- خبرة في نشر التطبيقات على Google Play و App Store
- معرفة بـ Kotlin أو Swift

المزايا:
- تأمين طبي
- مرتب مجزي""",
 req=["Flutter","Dart","REST APIs","Firebase","Figma","Git & GitHub","English","State management"], pref=["Kotlin","Swift","App store publishing"], absent=[], years=1, max_unmapped=3),

dict(name="emoji_linkedin", text="""🚀 We're Hiring: Junior Python Developer (Remote, Egypt) 🚀

📌 Responsibilities
✅ Build data pipelines and REST APIs with Python and FastAPI
✅ Write clean, tested code
✅ Collaborate with the data team

📌 Requirements
🔹 0-2 years of experience with Python
🔹 Good knowledge of SQL and PostgreSQL
🔹 Familiar with Docker and Linux
🔹 Strong problem-solving skills

📌 Nice to have
⭐ Experience with Airflow or ETL pipelines
⭐ Basic knowledge of AWS

📩 Send your CV to careers@example.com""",
 req=["Python","FastAPI","REST APIs","SQL","PostgreSQL","Docker","Linux","Problem solving","Teamwork","Data engineering (ETL)"], pref=["AWS"], absent=[], years=0, max_unmapped=2),

dict(name="caps_headings", text="""JUNIOR .NET DEVELOPER

RESPONSIBILITIES:
* Develop and maintain web applications using ASP.NET Core MVC
* Write clean code following SOLID principles and design patterns

REQUIREMENTS:
* B.Sc. in Computer Science or related field
* 1+ years of experience with C# and .NET Core
* Good knowledge of SQL Server, Entity Framework and LINQ
* Understanding of OOP concepts
* Familiarity with HTML, CSS, JavaScript and jQuery

NICE TO HAVE:
* Angular
* Azure DevOps""",
 req=[".NET / ASP.NET","MVC","SOLID","Design patterns","Education (degree)","C#","SQL Server","Entity Framework","LINQ","OOP","HTML","CSS","JavaScript","jQuery"], pref=["Angular","Azure"], absent=["SQL"], years=1, max_unmapped=1),

dict(name="paragraph_only", text="""We are hiring a Junior Frontend Developer to join our product team in New Cairo. You will build user interfaces with React and TypeScript, consume REST APIs and work closely with designers using Figma. You should have 1+ years of experience with HTML, CSS and JavaScript and be comfortable with Git. Experience with Next.js or Tailwind CSS is a plus. Good communication skills in English are required.""",
 req=["React","TypeScript","REST APIs","Figma","HTML","CSS","JavaScript","Git & GitHub","Communication","English"], pref=["Next.js","Tailwind CSS"], absent=[], years=1, max_unmapped=0),

dict(name="trap_words", text="""Customer Success Associate

We need someone who can react quickly to customer issues and express empathy. You will work with the rest of the team to resolve tickets, and you should excel at written communication. Solid organizational skills and a go-getter attitude are required. Node of our network: Cairo office. Strong English is a must.""",
 req=["Communication","English"], pref=[], absent=["React","Express","REST APIs","Excel / spreadsheets","SOLID","Go","Node.js"], years=0, scope=True, max_unmapped=1),

dict(name="java_spring", text="""Junior Java Developer - Alexandria

Requirements:
- Bachelor's degree in Computer Engineering
- Good knowledge of Java 8+ and Spring Boot
- Experience building RESTful web services
- Knowledge of Hibernate/JPA and MySQL
- Understanding of data structures and algorithms
- Familiarity with Maven and JUnit

Preferred:
- Microservices architecture
- Kafka or RabbitMQ""",
 req=["Education (degree)","Java","Spring Boot","REST APIs","ORM","MySQL","Data structures & algorithms","JUnit"], pref=["Microservices","Async jobs & queues"], absent=["JavaScript"], years=0, max_unmapped=2),

dict(name="php_laravel", text="""Junior PHP / Laravel Developer

What you'll do:
- Build and maintain web applications using PHP and Laravel
- Write MySQL queries and design database schemas
- Integrate third-party APIs

What we're looking for:
- At least two years of experience with Laravel
- Good understanding of MVC architecture
- Experience with Vue.js or React is a plus
- Git""",
 req=["PHP","Laravel","MySQL","MVC","Git & GitHub"], pref=["Vue.js","React"], absent=[], years=2, max_unmapped=2),

dict(name="mern_internship", text="""MERN Stack Internship (3 months, paid)

Who you are:
- A fresh graduate or final-year student
- You know MongoDB, Express.js, React and Node.js basics
- You have built at least one project and can show it on GitHub
- Good English communication

What we offer:
- Mentorship from senior engineers
- Possibility of full-time employment
- 5,000 EGP monthly stipend""",
 req=["MongoDB","Express","React","Node.js","Git & GitHub","English","Communication"], pref=[], absent=[], years=0, max_unmapped=2),

dict(name="data_analyst", text="""Junior Data Analyst

Key Responsibilities:
- Build dashboards and reports in Power BI
- Clean and analyze data using Excel, SQL and Python (Pandas)
- Present insights to stakeholders

Qualifications:
- 0–2 years of experience in data analysis
- Strong Excel skills (pivot tables, VLOOKUP)
- Solid SQL
- Knowledge of statistics
- Tableau is a plus""",
 req=["Power BI","Dashboards & metrics","Excel / spreadsheets","SQL","Python","Pandas","Data analysis","Statistics"], pref=["Tableau"], absent=["SOLID"], years=0, max_unmapped=2),

dict(name="ml_engineer", text="""Junior Machine Learning Engineer

Requirements
- Strong Python skills
- Hands-on experience with scikit-learn, TensorFlow or PyTorch
- Understanding of deep learning and NLP
- Experience with LLMs, RAG and vector databases
- Familiarity with Docker and Git

Bonus points
- Computer vision with OpenCV
- MLOps experience""",
 req=["Python","Scikit-learn","TensorFlow","PyTorch","Deep learning","NLP","LLMs / Generative AI","Embeddings & vector databases","Docker","Git & GitHub"], pref=["Computer vision"], absent=[], years=0, max_unmapped=2),

dict(name="android_kotlin", text="""Android Developer (Junior)

Must have:
- Kotlin and Android SDK
- MVVM, Jetpack Compose
- Retrofit and REST APIs
- Unit testing

Good to have:
- Java
- CI/CD with GitHub Actions""",
 req=["Kotlin","Android","REST APIs","Unit testing"], pref=["Java","CI/CD"], absent=["Git & GitHub"], years=0, max_unmapped=3),

dict(name="ios_swift", text="""Junior iOS Developer

Requirements:
1. 1+ year building iOS apps with Swift and SwiftUI
2. Experience with REST APIs and JSON
3. Familiarity with Git
4. Good English

Nice-to-have:
1. Firebase
2. Experience publishing apps on the App Store""",
 req=["iOS","Swift","REST APIs","Git & GitHub","English"], pref=["Firebase","App store publishing"], absent=["JavaScript"], years=1, max_unmapped=0),

dict(name="qa_tester", text="""Junior Software Tester (QA)

Responsibilities
- Write test cases and test plans
- Perform manual testing and report bugs in Jira
- Automate tests with Selenium
- Test APIs using Postman

Requirements
- Understanding of the software testing life cycle
- Basic SQL
- Attention to detail and good communication""",
 req=["Manual testing / QA","Agile / Scrum","Selenium","Postman","SQL","Communication"], pref=[], absent=[], years=0, max_unmapped=2),

dict(name="devops", text="""Junior DevOps Engineer

You will:
- Maintain CI/CD pipelines in GitLab CI and Jenkins
- Manage infrastructure on AWS using Terraform
- Run containers with Docker and Kubernetes
- Set up monitoring with Prometheus and Grafana

You have:
- Linux and Bash scripting
- Networking fundamentals (TCP/IP, DNS)
- Python scripting is an advantage""",
 req=["CI/CD","AWS","Terraform / IaC","Docker","Kubernetes","Logging & monitoring","Linux","Networking","Git & GitHub"], pref=["Python"], absent=[], years=0, max_unmapped=1),

dict(name="uiux", text="""Junior UI/UX Designer

Requirements:
- Portfolio showing UI/UX design work
- Proficiency in Figma and Adobe XD
- Understanding of user research, wireframes and prototyping
- Basic HTML/CSS knowledge is a plus""",
 req=["UI/UX design","Figma","Adobe XD"], pref=["HTML","CSS"], absent=[], years=0, max_unmapped=1),

dict(name="cyber", text="""Junior SOC Analyst

Requirements:
- Bachelor's in Computer Science or Cyber Security
- Knowledge of networking and TCP/IP
- Familiarity with SIEM tools
- Linux basics
- CCNA or Security+ is a plus""",
 req=["Education (degree)","Cybersecurity","Networking","Linux"], pref=[], absent=[], years=0, max_unmapped=1),

dict(name="embedded", text="""Junior Embedded Software Engineer

Requirements:
- Strong C and C++ programming
- Experience with microcontrollers (STM32, Arduino) and RTOS
- Understanding of embedded systems and communication protocols (UART, SPI, I2C)
- Git

Nice to have: Python for test automation""",
 req=["C","C++","Embedded systems","Git & GitHub"], pref=["Python"], absent=["C#","Communication"], years=0, max_unmapped=1),

dict(name="odoo", text="""Odoo Developer (Fresh Graduates Welcome)

Requirements:
- Python
- Odoo framework (ORM, views, reports)
- PostgreSQL
- XML and JavaScript basics""",
 req=["Python","Odoo","ORM","PostgreSQL","JavaScript"], pref=[], absent=[], years=0, max_unmapped=1),

dict(name="gulf_inline", text="""Junior Full Stack Developer - Riyadh, KSA (Relocation)
Must have: Angular, .NET Core, SQL Server, Git. Nice to have: Azure, Docker. Minimum 2 years of experience. Arabic and English required.""",
 req=["Angular",".NET / ASP.NET","SQL Server","Git & GitHub","English"], pref=["Azure","Docker"], absent=[], years=2, max_unmapped=1),

dict(name="years_company_trap", text="""About us
We have been building software for 25 years and serve 300 clients.

Requirements
- 0-1 years of experience
- React and Node.js""",
 req=["React","Node.js"], pref=[], absent=[], years=0, max_unmapped=0),

dict(name="years_upto", text="""Requirements
- Up to 2 years of experience in backend development with Go (Golang)
- PostgreSQL""",
 req=["Go","PostgreSQL"], pref=[], absent=[], years=0, max_unmapped=0),

dict(name="years_minimum_words", text="""Requirements:
- Minimum of three years of professional experience with Python and Django
- REST APIs""",
 req=["Python","Django","REST APIs"], pref=[], absent=[], years=3, max_unmapped=0),

dict(name="arabic_years", text="""المتطلبات:
- خبرة من سنتين إلى ٣ سنوات في PHP
- معرفة بـ Laravel""",
 req=["PHP","Laravel"], pref=[], absent=[], years=2, max_unmapped=0),

dict(name="mixed_ar_en", text="""مطلوب Junior React Developer
Requirements:
- خبرة في React و JavaScript
- معرفة بـ Redux و TypeScript
- Git
يفضل معرفة بـ Next.js""",
 req=["React","JavaScript","Redux","TypeScript","Git & GitHub"], pref=["Next.js"], absent=[], years=0, max_unmapped=0),

dict(name="html_paste", text="""<h3>Requirements</h3><ul><li>Strong <b>JavaScript</b> &amp; <b>React</b></li><li>Experience with Node.js</li></ul><h3>Nice to have</h3><ul><li>GraphQL</li></ul>""",
 req=["JavaScript","React","Node.js"], pref=["GraphQL"], absent=[], years=0, max_unmapped=0),

dict(name="crlf_bullets", text="Requirements:\r\n• Vue.js\r\n• Nuxt or Vite\r\n• Sass\r\n\r\nPreferred qualifications:\r\n• Cypress testing\r\n",
 req=["Vue.js","Sass/SCSS"], pref=["Cypress"], absent=[], years=0, max_unmapped=1),

dict(name="lettered_list", text="""Qualifications:
a) Bachelor's degree in Information Systems
b) Experience with Ruby on Rails
c) PostgreSQL and Redis
d) Knowledge of Agile/Scrum""",
 req=["Education (degree)","Ruby on Rails","PostgreSQL","Redis","Agile / Scrum"], pref=[], absent=[], years=0, max_unmapped=0),

dict(name="preferred_vs_basic", text="""Basic Qualifications
- Experience with Python or Java
- Understanding of object-oriented design

Preferred Qualifications
- Experience with AWS
- Knowledge of distributed systems and microservices""",
 req=["Python","Java","OOP"], pref=["AWS","Microservices"], absent=["JavaScript"], years=0, max_unmapped=0),

dict(name="non_job_text", text="""Grandma's lentil soup recipe: wash two cups of lentils, add onions and carrots, boil for 30 minutes, then blend and season with cumin. Serve hot with lemon and toasted bread.""",
 req=[], pref=[], absent=["React","Node.js"], years=0, scope=False, max_unmapped=0),

dict(name="one_liner", text="Looking for a React Native developer with Expo experience.",
 req=["React Native"], pref=[], absent=["React"], years=0, max_unmapped=0),

dict(name="json_not_js", text="""Requirements:
- Comfortable reading JSON and XML
- Java Script (ES6) fundamentals""",
 req=["JavaScript"], pref=[], absent=["Java"], years=0, max_unmapped=1),

dict(name="responsive_trap", text="""Requirements:
- Responsive to feedback and deadlines
- Build responsive web design layouts with CSS Grid and Flexbox""",
 req=["Responsive design","CSS"], pref=[], absent=[], years=0, max_unmapped=1),

dict(name="ecom_research", text=(Q/"ecom2.txt").read_text(),
 req=["E-commerce","Market & product research","Supply chain / sourcing","Analytical thinking","Communication"], pref=["Shopify"], absent=[], years=0, scope=True, max_unmapped=2),

dict(name="ai_engineer", text=(Q/"ai.txt").read_text(),
 req=["Python","FastAPI","Node.js","TypeScript","LLMs / Generative AI","AI agents & tool calling","Webhooks","REST APIs","PostgreSQL","Docker","CI/CD","Git & GitHub","Automated testing","Authentication (JWT/OAuth)"], pref=["Embeddings & vector databases"], absent=[], years=0, max_unmapped=4),

dict(name="huge_repeat", text=("Requirements:\n- React and Node.js\n- Strong communication\n" * 200),
 req=["React","Node.js","Communication"], pref=[], absent=[], years=0, max_unmapped=0),
]
