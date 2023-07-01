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
