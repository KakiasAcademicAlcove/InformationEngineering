![image](https://github.com/kakiac/UoS_CloudComputing/assets/10551558/2f2841e7-043a-4d44-bcb6-e43eef1bc3b9)

## Information Engineering (Level 6 - 3rd year UG) (University of Suffolk)

### Welcome 👋

Welcome to your third year and the Information Engineering module! In this semester, we will get to know information systems and information engineering more closely.

![image](https://github.com/user-attachments/assets/c1a412f4-e0b5-4520-bc99-9f1d63e393c0)

Industry, commerce and research are being transformed by the potential to capture, store, manipulate, analyse and visualise data and information on a massive scale. Data-driven discovery and prediction are yielding new insights to businesses and academe in every domain, while information retrieval in the form of web search engines are the default mechanism by which most individuals prefer to find information.

<strong> Information Engineering </strong> is the engineering discipline that deals with the generation, distribution, analysis, and use of information, data, and knowledge in systems.

The components of information engineering include more theoretical fields such as <strong> machine learning, artificial intelligence and information theory</strong>, and more applied fields such as <strong> computer vision, natural language processing, bioinformatics, medical image computing,</strong> and <strong>robotics</strong>. Many of these originate from computer science, as well as other branches of engineering such as computer engineering, electrical engineering, and bioengineering.

"Big Data" in all its varied forms requires a set of statistical, analytical and programming skills, which are currently in short supply, and likely to remain so for the foreseeable future as this remains a bleeding edge growth area in terms of career opportunities. This module aims to provide students with the core skill set for information engineering, drawing across data science, artificial intelligence, operational research, information retrieval, and related technologies.

Join me in this module this semester where we will learn the basic principles and practice of information, information systems and develop the skills to generate, maintain and extract insights from data. Topics we will cover will include:


- History and context of data science and information engineering
- Technology landscape
- Parallel databases and query processing, and in-database analytics
- MapReduce and Hadoop
- Key-value stores and NoSQL, examples of NoSQL implementations
- Programming using Python and R
- Topics in information retrieval
- Topics in statistical modelling: statistics review, concepts, design, pitfalls
- Topics in machine learning: supervised learning, optimisation, unsupervised learning, classification, mining, forecasting
- Topics in reasoning with uncertainty
- Topics in visualisation and graph analytics
- Issues in privacy and ethics

### Learning Aims

By the end of this module, you should be able to:

1.  develop knowledge and understanding of the statistical, algorithmic, and analytical concepts and methods which underpin and embody the core of data science and information engineering
2.  develop the skills and intuitions necessary to select and design an information engineering solution to practical data and information problems
3.  develop skills to successfully apply statistical, algorithmic, and analytical techniques to implement an information engineering solution using appropriate programming languages and software packages and draw rational conclusions based on the results of the solution

### Learning Outcomes

By the end of this module, you will be able to:

1. Demonstrate a systematic understanding and knowledge of the statistical, algorithmic and analytical concepts and methods which form the core of data science and information engineering
2. Identify the most appropriate techniques and tools for a particular data or information problem, and be critically aware of the limitations on these methods
3. Design an information engineering solution to a particular data or information problem from a toolbox of appropriate techniques
4. Implement an information engineering solution, including such aspects as data modelling at scale, statistical modelling, programming and visualisation of results
5. Draw relevant and rational conclusions from the application of an information engineering solution to a particular data or information problem, and critically appreciate the uncertainties and limitations to the accuracy and/or applicability of these results

## Course Overview

| Module | Core Domain Focus | Included Units |
| :--- | :--- | :--- |
| **Module 1** | Foundations, Architectures & Modeling | Units 1–3: Systems theory, data modeling, ADRs, pipeline design patterns, backfilling & determinism. |
| **Module 2** | Storage, Ingestion & Data Warehousing | Units 4–7: Relational engines, APIs/CDC, NoSQL systems, and dimensional modeling. |
| **Module 3** | Modern Data Stack & Streaming Architectures | Units 8–11: Lakehouses, real-time event streaming, quality frameworks, DRE, and incident response. |
| **Module 4** | Orchestration, Distributed Computing & AI | Units 12–16: dbt, Docker, Spark tuning, networking, ML pipelines/MLOps, Vector search, and Agentic AI. |
| **Module 5** | Sustainability, Governance & Specialised Systems | Units 17–20: FinOps, green computing, privacy/AI regulations, network security, and domain systems. |
| **Module 6** | Careers & Professional Practice | Unit 21: Industry roles, certifications, portfolio development, and team dynamics. |


### Lecture 1
**Information Engineering Concepts**
<details>
<p>Welcome to the Information Engineering module 👋.</p>
<p>An overview of the module aims and objectives is available under Content &gt; Module Information. Please make sure you have a look at these pages before you proceed with the rest of the pages on this module. Make sure you have spotted the <strong>Readings</strong> page and that you have glanced through the other resources mentioned there.</p>
<p>We start this module by looking at the basics of <strong>information engineering</strong> and <strong>information systems engineering</strong>, including the history and the context of data science and information engineering and how it is being shaped by and has shaped the era of AI (and more recently Generative AI).</p>
<p>We will also be looking at what information, data and information engineering is,&nbsp;when they were first discussed in the computing world and their importance for businesses and society. We will also be&nbsp;discussing different ways information is understood across different fields of databases that you might come across (relational, non-relational, graph etc). Finally, we will be&nbsp;working in groups to discuss related issues and exchange ideas and experiences.</p>
<p>In the practical/lab, we will be refreshing our memory of programming basics and trying out some examples of information pipelines using open datasets and Python code in kaggle.com.</p>
<p>For the <em><strong>assessment</strong></em> on this module you will need to work on a fictional scenario of an organisation presented to you where you will need to identify and propose ways it could build or improve its data engineering architecture and data analytics pipelines. Assessment information will be made available under Content &gt; Module Assessment after Lecture 2. Don’t worry about what that will involve just yet. We will get there!</p>
<p>You should have everything you need to make a start on the assessment after Lecture 6 content is covered.</p>
<p><strong>Practicals/Labs</strong></p>
<p>All lectures are followed by an AWS Academy (or other cloud provider) training set of material - please make sure you gain access to AWS Academy training material (I will be providing details during class about how I will be adding you to these), and follow through the assigned module material (videos, labs and knowledge checks) to reinforce your knowledge of the contents covered.</p>
<p><strong>Readings for this Lecture</strong></p>
<p>Detailed information for today's key concepts can be found in the following readings:</p>
<ul>
<li>📘 Reading 1-1: <a rel="noopener" href="https://uos.on.worldcat.org/oclc/1351987584">Chapter 1 of Reis and Housley (2022) </a></li>
<li>📘 Reading 1-2: <a rel="noopener" href="https://uos.on.worldcat.org/oclc/1351987584" target="_self">Chapter 2 of Reis and Housley (2022)</a></li>
<li>📘 Reading 1-3: Chapter 1 of <a rel="noopener" href="https://uos.on.worldcat.org/oclc/320905871">Heijden (2009)</a></li>
<li>📘 Video Resource 1-4: What is information theory?</li>
</ul>
<div class="row">
<div class="col-xs-12 col-sm-8"><iframe width="560" height="315" src="https://www.youtube.com/embed/d9alWZRzBWk?wmode=opaque&amp;rel=0" title="YouTube video player?wmode=opaque" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="allowfullscreen"></iframe></div>
<ul>
<li>📘 Video Resource 1-5: IBM Cloud - what is data science?</li>
</ul>
<div class="col-xs-12 col-sm-8"><iframe width="560" height="315" src="https://www.youtube.com/embed/RBSUwFGa6Fk?wmode=opaque&amp;rel=0" title="YouTube video player?wmode=opaque" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="allowfullscreen"></iframe></div>
<div class="col-xs-12 col-sm-8">
<ul>
<li>📘 Video Resource 1-6: The Science of Information - a lecture by Professor Richard Harvey (23/10/2018)</li>
</ul>
</div>
<div class="col-xs-12 col-sm-8"><iframe width="560" height="315" src="https://www.youtube.com/embed/-_2qQpNH8BQ?wmode=opaque&amp;rel=0" title="YouTube video player?wmode=opaque" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="allowfullscreen"></iframe></div>
</div>
<p><strong>Case studies:</strong></p>
<ul>
<li>Stripe: <a rel="noopener" href="https://www.youtube.com/watch?v=O67TvnvKgic&amp;list=PL2yQDdvlhXf_22xqaqPb13gDRDOq2Sjg4&amp;index=9">AWS re:Invent 2022 - Modernize your data archive with Amazon S3, featuring Stripe (STG205) (youtube.com)</a>&nbsp;<strong></strong></li>
<li><a rel="noopener" href="https://www.youtube.com/watch?v=vDDJ9eWaUt0">AWS re:Invent 2022 - Achieving your modern data architecture (ANT205-R)</a></li>
</ul>
<p><strong>Labs:</strong></p>
<ul>
<li>Lab 1.1: Querying data using Athena (AWS Data Engineering &gt; Module 04)</li>
</ul>
<h3>Lecture 01 - recording (part 1)</h3>
<p><iframe src="https://uos.cloud.panopto.eu/Panopto/Pages/Embed.aspx?id=d9bcd8f7-6344-493d-b90b-b1fc008edfe7&amp;autoplay=false&amp;offerviewer=true&amp;showtitle=true&amp;showbrand=true&amp;captions=false&amp;interactivity=all" height="405" width="100%" style="border: 1px solid #464646;" allowfullscreen="allowfullscreen" allow="autoplay"></iframe></p>
<h3>Lecture 01 - recording (part 2)</h3>
<p><iframe src="https://uos.cloud.panopto.eu/Panopto/Pages/Embed.aspx?id=035acb00-ed50-4baf-9032-b1fc00a2116a&amp;autoplay=false&amp;offerviewer=true&amp;showtitle=true&amp;showbrand=true&amp;captions=false&amp;interactivity=all" height="405" width="100%" style="border: 1px solid #464646;" allowfullscreen="allowfullscreen" allow="autoplay"></iframe></p>
<p></p>
</details>

### Lecture 2
### Lecture 3
### Lecture 4
### Lecture 5
### Lecture 6
### Lecture 7
### Lecture 8
### Lecture 9
### Lecture 10
### Lecture 11
### Lecture 12


### Administrative Module info 

| Module Title  | Cloud Computing for Data Science and AI |
| ------------  | -------------               |
| Module Code   | IPLDSAM03 (apprentices) / IMDSAM03 (mainstream) |
| Level         | 6 (3rd year undergraduate)      |
| School        | School of Technology, Business and Arts |
| Github Repo   | https://github.com/KakiasAcademicAlcove/InformationEngineering/        |

### Offered at
<img src="https://icanbea.org.uk/media/shapes/original/x-large/5000/5100/university-of-suffolk-logo.png" height="100" />

