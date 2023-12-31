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

interview_q_prompt = '''
Generate a JSON list of interview questions and answers for Data Science. Each question should have the properties question and answer.
{{
  \"interview_questions\": [
    {{
      \"question\": \"What is the Central Limit Theorem?\",
      \"answer\": \"The Central Limit Theorem states that when independent random variables are added, their sum tends toward a normal distribution.\"
    }},
    {{
      \"question\": \"Explain the difference between supervised and unsupervised learning.\",
      \"answer\": \"Supervised learning involves training a model using labeled data, while unsupervised learning involves finding patterns and relationships in unlabeled data.\"
    }},
    {{
      \"question\": \"What is regularization in machine learning?\",
      \"answer\": \"Regularization is a technique used to prevent overfitting in machine learning models by adding a penalty term to the loss function.\"
    }},
    {{
      \"question\": \"What is the difference between precision and recall?\",
      \"answer\": \"Precision is the ratio of true positives to the sum of true positives and false positives, while recall is the ratio of true positives to the sum of true positives and false negatives.\"
    }},
    {{
      \"question\": \"What is feature selection in machine learning?\",
      \"answer\": \"Feature selection is the process of selecting the most relevant and informative features from a dataset to improve model performance and reduce complexity.\"
    }}
  ]
}}
##
Generate a JSON list of interview questions and answers for Web Development. Each question should have the properties question and answer.
{{
  \"interview_questions\": [
    {{
      \"question\": \"What is the difference between HTML and HTML5?\",
      \"answer\": \"HTML5 introduces new elements, attributes, and APIs, providing enhanced semantic markup, better support for multimedia, and improved accessibility.\"
    }},
    {{
      \"question\": \"Explain the box model in CSS.\",
      \"answer\": \"The box model in CSS describes the rectangular boxes that surround elements, consisting of content, padding, border, and margin.\"
    }},
    {{
      \"question\": \"What is the difference between a block-level element and an inline element?\",
      \"answer\": \"Block-level elements start on a new line and take up the full width available, while inline elements do not start on a new line and only take up as much width as necessary.\"
    }},
    {{
      \"question\": \"What is the purpose of media queries in responsive web design?\",
      \"answer\": \"Media queries in CSS allow developers to apply different styles and layouts based on various device characteristics, such as screen size, resolution, or orientation.\"
    }},
    {{
      \"question\": \"What is the role of JavaScript in web development?\",
      \"answer\": \"JavaScript is a programming language that enables interactive and dynamic features on web pages, such as form validation, DOM manipulation, and AJAX requests.\"
    }}
  ]
}}
##
Generate a JSON list of interview questions and answers for Graphic Design. Each question should have the properties question and answer.
{{
  \"interview_questions\": [
    {{
      \"question\": \"What is the principle of contrast in design?\",
      \"answer\": \"Contrast is the juxtaposition of different elements to create visual interest, highlight important information, and create a sense of hierarchy.\"
    }},
    {{
      \"question\": \"Explain the RGB and CMYK color models.\",
      \"answer\": \"The RGB color model is used for digital displays and combines red, green, and blue to create a wide range of colors. The CMYK color model is used for print and combines cyan, magenta, yellow, and black.\"
    }},
    {{
      \"question\": \"What is the role of typography in graphic design?\",
      \"answer\": \"Typography plays a crucial role in graphic design by enhancing readability, setting the tone, and conveying messages effectively through the use of fonts, sizes, spacing, and hierarchy.\"
    }},
    {{
      \"question\": \"What is the golden ratio in design?\",
      \"answer\": \"The golden ratio is a mathematical ratio of approximately 1.618 that is believed to create aesthetically pleasing proportions. It is often used in design compositions and layouts.\"
    }},
    {{
      \"question\": \"What are the key principles of good logo design?\",
      \"answer\": \"Good logo design should be memorable, scalable, versatile, appropriate for the brand, and communicate the brand's values or unique attributes effectively.\"
    }}
  ]
}} 
##
Generate a JSON list of interview questions and answers for {field}. Each question should have the properties question and answer.
'''

tip_prompt = '''
Generate a useful tip for Data Science. 
{{ "tip": "Spend more time cleaning your data than analyzing it." }}
##
Generate a useful tip for Web Development.
{{ "tip": "Make sure to test your web application thoroughly before releasing it to the public." }}
##
Generate a useful tip for Graphic Design.
{{ "tip": "Use the rule of thirds to create a balanced and visually appealing layout." }}
##
Generate a useful tip for {field}.
'''

profession_prompt = '''
Generate a list of suggested professions based on my skills, education, and experiences: I know Python programming and Statistics. I have Bachelor's degree in Computer Science. 
{{
  \"suggested_professions\": [
    \"Data Scientist\",
    \"Machine Learning Engineer\",
    \"Data Analyst\",
    \"Quantitative Analyst\",
    \"Business Intelligence Analyst\"
  ]
}}
##
Generate a list of suggested professions based on my skills, education, and experiences: I'm passionate about drawing. I am familiar with Adobe photoshop and illustrator. I've exhibited my artworks at local galleries.
{{
  \"suggested_professions\": [
    \"Graphic Designer\",
    \"Illustrator\",
    \"Visual Development Artist\",
    \"Concept Artist\"
  ]
}}
##
Generate a list of suggested professions based on my skills, education, and experiences: I love gardening and plant care.
{{
  \"suggested_professions\": [
    \"Landscaper\",
    \"Gardener\",
    \"Horticulturist\",
    \"Landscape Designer\",
    \"Groundskeeper\"
  ]
}}
##
Generate a list of suggested professions based on my skills, education, and experiences: {input}. 
'''

valid_profession_prompt = '''
Check if user input is a valid job, profession, field or area of interest. If valid return 'True', if no return error message.
User input: data science 
{{ \"valid\": \"True\", \"message\": \"\" }}
## 
Check if user input is a valid job, profession, field or area of interest. If yes - return 'True', if no - return error message.
User input: Journalism 
{{ \"valid\": \"True\", \"message\": \"\" }}
## 
Check if user input is a valid job, profession, field or area of interest. If yes - return 'True', if no - return error message.
User input: teaching
{{ \"valid\": \"True\", \"message\": \"\" }}
## 
Check if user input is a valid job, profession, field or area of interest. If yes - return 'True', if no - return error message.
User input: Medicine
{{ \"valid\": \"True\", \"message\": \"\" }}
## 
Check if user input is a valid job, profession, field or area of interest. If yes - return 'True', if no - return error message.
User input: music
{{ \"valid\": \"True\", \"message\": \"\" }}
## 
Check if user input is a valid job, profession, field or area of interest. If yes - return 'True', if no - return error message.
User input: Engineering
{{ \"valid\": \"True\", \"message\": \"\" }}
## 
Check if user input is a valid job, profession, field or area of interest. If yes - return 'True', if no - return error message.
User input: Law
{{ \"valid\": \"True\", \"message\": \"\" }}
## 
Check if user input is a valid job, profession, field or area of interest. If yes - return 'True', if no - return error message.
User input: finance
{{ \"valid\": \"True\", \"message\": \"\" }}
## 
Check if user input is a valid job, profession, field or area of interest. If yes - return 'True', if no - return error message.
User input: electrics
{{ \"valid\": \"True\", \"message\": \"\" }}
## 
Check if user input is a valid job, profession, field or area of interest. If yes - return 'True', if no - return error message.
User input: nail services
{{ \"valid\": \"True\", \"message\": \"\" }}
## 
Check if user input is a valid job, profession, field or area of interest. If yes - return 'True', if no - return error message.
User input: linguistics
{{ \"valid\": \"True\", \"message\": \"\" }}
## 
Check if user input is a valid job, profession, field or area of interest. If yes - return 'True', if no - return error message.
User input: actor
{{ \"valid\": \"True\", \"message\": \"\" }}
## 
Check if user input is a valid job, profession, field or area of interest. If yes - return 'True', if no - return error message.
User input: design
{{ \"valid\": \"True\", \"message\": \"\" }}
## 
Check if user input is a valid job, profession, field or area of interest. If yes - return 'True', if no - return error message.
User input: movie director
{{ \"valid\": \"True\", \"message\": \"\" }}
## 
Check if user input is a valid job, profession, field or area of interest. If yes - return 'True', if no - return error message.
User input: repair work
{{ \"valid\": \"True\", \"message\": \"\" }}
## 
Check if user input is a valid job, profession, field  or area of interest. If yes - return 'True', if no - return error message.
User input: metallurgy
{{ \"valid\": \"True\", \"message\": \"\" }}
## 
Check if user input is a valid job, profession, field or area of interest. If yes - return 'True', if no - return error message.
User input: plumber
{{ \"valid\": \"True\", \"message\": \"\" }}
## 
Check if user input is a valid job, profession, field or area of interest. If yes - return 'True', if no - return error message.
User input: foundry
{{ \"valid\": \"True\", \"message\": \"\" }}
## 
Check if user input is a valid job, profession, field or area of interest. If yes - return 'True', if no - return error message.
User input: qwerty 
{{ \"valid\": \"False\", \"message\": \"Please provide a valid profession. For example, \"Artificial Intelligence\"\" }}
##
Check if user input is a valid job, profession, field or area of interest. If yes - return 'True', if no - return error message.
User input: IT 
{{ \"valid\": \"False\", \"message\": \"IT is a very broad concept. Input a specific field or area you're interested in, such as \"AI\"\" }}
## 
Check if user input is a valid job, profession, field or area of interest. If yes - return 'True', if no - return error message.
User input: dog 
{{ \"valid\": \"False\", \"message\": \"What you entered doesn't seem to match any known profession.\" }}
## 
Check if user input is a valid job, profession, field or area of interest. If yes - return 'True', if no - return error message.
User input: {field}
'''
