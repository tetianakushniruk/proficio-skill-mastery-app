roadmap_prompt = '''
Generate a JSON roadmap for mastering Data Science. The roadmap should include key milestones with their respective names and descriptions.
{{
  \"roadmap\": [
    {{
      \"name\": \"Mathematics\",
      \"description\": \"Math skills are essential for understanding various machine learning algorithms. Topics include linear algebra, calculus, and probability theory.\"
    }},
    {{
      \"name\": \"Probability\",
      \"description\": \"Probability theory is a prerequisite for mastering machine learning. Topics include probability distributions, random variables, and statistical inference.\"
    }},
    {{
      \"name\": \"Statistics\",
      \"description\": \"Understanding statistics is crucial for data analysis. Topics include descriptive statistics, hypothesis testing, and regression analysis.\"
    }},
    {{
      \"name\": \"Programming\",
      \"description\": \"Good grasp of programming concepts is necessary. Languages commonly used are Python, R, Java, Scala, and C++. Skills include data structures, algorithms, and performance optimization.\"
    }},
    {{
      \"name\": \"Machine Learning\",
      \"description\": \"Mastering basic algorithms of supervised and unsupervised learning. Utilize Python and R libraries for implementation.\"
    }},
    {{
      \"name\": \"Deep Learning\",
      \"description\": \"Build and train neural networks using deep learning frameworks like TensorFlow and Keras.\"
    }},
    {{
      \"name\": \"Feature Engineering\",
      \"description\": \"Discover effective ways to improve model performance by manipulating and transforming input data.\"
    }},
    {{
      \"name\": \"Natural Language Processing\",
      \"description\": \"Learn techniques for working with text data, including sentiment analysis, named entity recognition, and text classification.\"
    }},
    {{
      \"name\": \"Data Visualization Tools\",
      \"description\": \"Develop skills in data visualization using tools like Matplotlib, Seaborn, and Tableau to create impactful visualizations.\"
    }},
    {{
      \"name\": \"Deployment\",
      \"description\": \"Learn how to deploy machine learning models into production systems and ensure scalability, reliability, and performance.\"
    }}
  ]
}}
##
Generate a JSON roadmap for mastering Web Development. The roadmap should include key milestones with their respective names and descriptions.
{{
  \"roadmap\": [
    {{
      \"name\": \"HTML and CSS Fundamentals\",
      \"description\": \"Master the basics of HTML markup and CSS styling to create static web pages.\"
    }},
    {{
      \"name\": \"JavaScript and Front-End Frameworks\",
      \"description\": \"Learn JavaScript programming and popular front-end frameworks like React or Vue.js for building interactive and dynamic web applications.\"
    }},
    {{
      \"name\": \"Back-End Development\",
      \"description\": \"Develop skills in server-side programming languages such as Node.js or Python to handle data, build APIs, and interact with databases.\"
    }},
    {{
      \"name\": \"Database Systems\",
      \"description\": \"Understand the fundamentals of database design and management, including SQL or NoSQL databases like MySQL or MongoDB.\"
    }},
    {{
      \"name\": \"Web Security\",
      \"description\": \"Learn about web security best practices, including authentication, authorization, and protection against common vulnerabilities like cross-site scripting (XSS) and SQL injection.\"
    }},
    {{
      \"name\": \"Responsive Web Design\",
      \"description\": \"Acquire knowledge of techniques and frameworks like Bootstrap or CSS Grid to create responsive and mobile-friendly web layouts.\"
    }},
    {{
      \"name\": \"Web Performance Optimization\",
      \"description\": \"Optimize website performance by understanding techniques like caching, minification, and image optimization.\"
    }},
    {{
      \"name\": \"Version Control and Collaboration\",
      \"description\": \"Master version control systems like Git and collaborate effectively with other developers using platforms like GitHub or GitLab.\"
    }},
    {{
      \"name\": \"Web Accessibility\",
      \"description\": \"Ensure your websites are accessible to users with disabilities by following web accessibility standards and guidelines.\"
    }},
    {{
      \"name\": \"Deployment and DevOps\",
      \"description\": \"Learn about deploying web applications, setting up continuous integration/continuous deployment (CI/CD), and utilizing cloud platforms like AWS or Azure.\"
    }}
  ]
}}
## 
Generate a JSON roadmap for mastering Graphic Design. The roadmap should include key milestones with their respective names and descriptions.
{{
  \"roadmap\": [
    {{
      \"name\": \"Design Principles and Elements\",
      \"description\": \"Gain a solid understanding of design principles, including color theory, typography, composition, and visual hierarchy.\"
    }},
    {{
      \"name\": \"Digital Design Tools\",
      \"description\": \"Master popular design software such as Adobe Photoshop, Illustrator, or Sketch for creating digital designs and graphics.\"
    }},
    {{
      \"name\": \"Layout and Composition\",
      \"description\": \"Develop skills in arranging visual elements, grids, and creating balanced compositions for various design projects.\"
    }},
    {{
      \"name\": \"Brand Identity Design\",
      \"description\": \"Learn how to create cohesive brand identities, including logos, brand guidelines, and visual branding assets.\"
    }},
    {{
      \"name\": \"Print Design and Production\",
      \"description\": \"Understand print design principles, prepare designs for print production, and work with print technologies and specifications.\"
    }},
    {{
      \"name\": \"User Interface (UI) Design\",
      \"description\": \"Focus on designing intuitive and visually appealing user interfaces for websites, applications, or digital products.\"
    }},
    {{
      \"name\": \"User Experience (UX) Design\",
      \"description\": \"Explore user-centered design methodologies, wireframing, prototyping, and conducting user research and testing.\"
    }},
    {{
      \"name\": \"Motion Graphics and Animation\",
      \"description\": \"Learn motion graphics techniques, including animation principles, creating dynamic visual experiences, and using tools like Adobe After Effects.\"
    }},
    {{
      \"name\": \"Typography and Type Design\",
      \"description\": \"Dive into the world of typography, including selecting appropriate typefaces, hierarchy, and even designing custom typefaces.\"
    }},
    {{
      \"name\": \"Portfolio Building and Presentation\",
      \"description\": \"Develop a strong portfolio showcasing your design projects and learn effective presentation skills to communicate your work.\"
    }}
  ]
}}
##
Generate a JSON roadmap for mastering {field}. The roadmap should include key milestones with their respective names and descriptions.

'''

books_prompt = '''
Generate a JSON list of recommended books for Data Science. Each book should have the properties name, description, and author.
{{
  \"books\": [
    {{
      \"name\": \"Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow\",
      \"description\": \"This book provides a comprehensive introduction to machine learning, covering essential algorithms and practical examples. It's authored by Aurélien Géron.\",
      \"author\": \"Aurélien Géron\"
    }},
    {{
      \"name\": \"Python for Data Analysis\",
      \"description\": \"Written by Wes McKinney, the creator of the pandas library, this book offers a practical guide to data manipulation and analysis using Python.\",
      \"author\": \"Wes McKinney\"
    }},
    {{
      \"name\": \"The Elements of Statistical Learning\",
      \"description\": \"This influential book by Trevor Hastie, Robert Tibshirani, and Jerome Friedman covers statistical learning methods, including regression, classification, and clustering.\",
      \"author\": \"Trevor Hastie, Robert Tibshirani, Jerome Friedman\"
    }},
    {{
      \"name\": \"Deep Learning\",
      \"description\": \"Authored by Ian Goodfellow, Yoshua Bengio, and Aaron Courville, this book is a comprehensive guide to deep learning techniques, covering theory and practical applications.\",
      \"author\": \"Ian Goodfellow, Yoshua Bengio, Aaron Courville\"
    }},
    {{
      \"name\": \"Data Science for Business\",
      \"description\": \"This book by Foster Provost and Tom Fawcett explores the application of data science in business contexts, providing insights on data-driven decision-making.\",
      \"author\": \"Foster Provost, Tom Fawcett\"
    }}
  ]
}}
## 
Generate a JSON list of recommended books for Web Development. Each book should have the properties name, description, and author.
{{ 
  \"books\": [ 
    {{ 
      \"name\": \"Eloquent JavaScript\", 
      \"description\": \"This book by Marijn Haverbeke is an in-depth guide to JavaScript programming, covering fundamental concepts and advanced techniques.\", 
      \"author\": \"Marijn Haverbeke\" 
    }}, 
    {{ 
      \"name\": \"HTML and CSS: Design and Build Websites\", 
      \"description\": \"Authored by Jon Duckett, this book provides a beginner-friendly introduction to HTML and CSS, with practical examples and visually appealing design.\", 
      \"author\": \"Jon Duckett\" 
    }}, 
    {{ 
      \"name\": \"JavaScript: The Good Parts\", 
      \"description\": \"Written by Douglas Crockford, this book focuses on the good parts of JavaScript and provides valuable insights for writing clean and maintainable code.\", 
      \"author\": \"Douglas Crockford\" 
    }}, 
    {{ 
      \"name\": \"Learning Web Design\", 
      \"description\": \"This book by Jennifer Robbins is a beginner's guide to web design, covering HTML, CSS, responsive design, and web graphics.\", 
      \"author\": \"Jennifer Robbins\" 
    }}, 
    {{ 
      \"name\": \"CSS Secrets\", 
      \"description\": \"Lea Verou's book explores lesser-known CSS techniques, tips, and tricks to enhance your web designs and solve common challenges.\", 
      \"author\": \"Lea Verou\" 
    }} 
  ] 
}} 
##
Generate a JSON list of recommended books for Graphic Design. Each book should have the properties name, description, and author.
{{ 
  \"books\": [ 
    {{ 
      \"name\": \"Thinking with Type\", 
      \"description\": \"This book by Ellen Lupton is a comprehensive guide to typography, covering principles, history, and practical applications in design.\", 
      \"author\": \"Ellen Lupton\" 
    }}, 
    {{ 
      \"name\": \"The Non-Designer's Design Book\", 
      \"description\": \"Robin Williams' book provides an introduction to design principles and techniques for non-designers, helping them create visually appealing designs.\", 
      \"author\": \"Robin Williams\" 
    }}, 
    {{ 
      \"name\": \"Graphic Design School\", 
      \"description\": \"Dabner, Stewart, and Zempol's book is a comprehensive introduction to graphic design, covering design fundamentals, techniques, and practical projects.\", 
      \"author\": \"David Dabner, Sandra Stewart, Eric Zempol\" 
    }}, 
    {{ 
      \"name\": \"Color Design Workbook\", 
      \"description\": \"This book by Terry Stone and Sean Adams explores the use of color in design, providing insights, examples, and exercises to develop color skills.\", 
      \"author\": \"Terry Stone, Sean Adams\" 
    }}, 
    {{ 
      \"name\": \"Logo Design Love\", 
      \"description\": \"Authored by David Airey, this book focuses on the process and principles of logo design, showcasing inspiring case studies and practical advice.\", 
      \"author\": \"David Airey\" 
    }} 
  ] 
}} 
##
Generate a JSON list of recommended books for {field}. Each book should have the properties name, description, and author.
'''