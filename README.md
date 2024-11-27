<p align = "center" dir = "auto">
<img src="https://github.com/Zomoi/Final-Proj-in-Python-and-DBMS/blob/a705c33a5f9267606c4414338a4c181ef9610f1f/pxArt%20(3).png" width="100">
</p>

<h1 align = "center" tabindex="-1" class="heading element" dir="auto">BarangTrack</h1>
<p align = "center" dir= "auto">
<em>
<code>♻️A Community Member Management System♻️</code>
</em>
</p>
<p align = "center" dir="auto">
  <b>IT-2104</b>
  <br>
  <a href="https://github.com/Zomoi">
  Rico, B-jork M.
  </a>
</p>
<hr></hr>
<h2>🔍About</h2>
<ul dir="auto">
  <li>
    <a href="#-project-overview">Project Overview</a>
  </li>
  <li>
    <a href="#-python-concepts">Python Concepts</a>
  </li>
  <li>
    <a href="#-SDG">Chosen SDG</a>
  </li>  
  <li>
    <a href="#-instructions">Instructions on Running the Program</a>
  </li>
  <li>
    <a href="#-acknowledgment">Acknowledgments</a>
  </li>
</ul>
<hr></hr>
<div class ="markdown-heading" dir="auto">
  <h2 tabindex="-1" class="heading-element" dir="auto">📖Project Overview</h2>
</div>
<p dir = "auto">
    This Community Management System is designed to assist local governments, non-profits, and community organizations in efficiently managing and tracking the involvement of community members across a range of programs. By centralizing data on member participation, volunteer hours, and engagement in sustainability initiatives, the system aims to foster greater community involvement and accountability. The system allows for easy access to data such as attendance at events, roles in volunteer programs, and contributions to sustainability projects, empowering organizations to make informed decisions, recognize dedicated individuals, and allocate resources more effectively for community growth and engagement.
</p>
<hr></hr>
<div class ="markdown-heading" dir="auto">
  <h2 tabindex="-1" class="heading-element" dir="auto">🐍Python Concepts</h2>
</div>
<ul dir="auto">
  <li>
    <h2>📚 Classes and Objects (OOP Basics)</h2>
    <p>I designed the system around an organized structure using Python's Object-Oriented Programming (OOP). Each community member is represented as an object, while the database and GUI components are managed through logical groupings in the code. The integration between the GUI (Tkinter) and the MySQL database ensures seamless interaction, like adding, updating, and deleting member records.</p>
  </li>
  <li>
    <h2>💊 Encapsulation</h2>
    <p>Encapsulation ensures that data and the operations on it are bundled within classes. For example, database interactions, such as adding a new member, updating details, or deleting a record, are encapsulated within functions. These methods keep the actual SQL queries hidden, exposing only the relevant actions through user-friendly buttons in the GUI.</p>
  </li>
  <li>
    <h2>🗄️ Abstraction</h2>
    <p>The project abstracts away complex processes, such as establishing a database connection or fetching query results, from the user. For instance:</p>
    <ul>
      <li>Users only interact with the <b>Connect Database</b> button, while the program executes the underlying <code>pymysql.connect()</code> call to link the GUI with MySQL.</li>
      <li>The GUI's <b>Add Member</b> form provides a straightforward interface, abstracting SQL <code>INSERT</code> statements.</li>
    </ul>
  </li>
  <li>
    <h2>📑 Polymorphism</h2>
    <p>The system demonstrates polymorphism in handling diverse GUI widgets and data entries. For example:</p>
    <ul>
      <li>Each frame, button, and input field is created using Tkinter objects, with customized behavior for different operations (e.g., adding members, searching, or exporting data).</li>
      <li>Multiple functions like <code>add_member()</code> and <code>search_member()</code> dynamically modify GUI elements based on the operation being performed.</li>
    </ul>
  </li>
  <li>
    <h2>🗃️ Database Management (MySQL)</h2>
    <p>The system uses a MySQL database for data persistence:</p>
    <ul>
      <li><b>Data Storage:</b> Member information is stored in a structured database table.</li>
      <li><b>SQL Queries:</b> The system uses queries for operations like <code>INSERT</code>, <code>SELECT</code>, and <code>DELETE</code>.</li>
    </ul>
  </li>
  <li>
    <h2>🔁 GUI Features</h2>
    <p>The system uses Tkinter to provide an intuitive interface for managing members:</p>
    <ul>
      <li><b>Left Frame:</b> Contains buttons for major functions (Add, Search, Update, Delete, etc.).</li>
      <li><b>Right Frame:</b> Displays a dynamic table of member data using Tkinter's Treeview widget.</li>
      <li><b>Dynamic Forms:</b> Forms for adding, updating, and searching members are created dynamically.</li>
    </ul>
  </li>
  <li>
    <h2>⏱️ Real-Time Updates</h2>
    <p>Actions such as adding or updating members automatically refresh the displayed data in the member table. A clock function in the GUI displays the current time and updates every second, ensuring the interface feels dynamic.</p>
  </li>
  <li>
    <h2>📋 Lists, Dictionaries, and SQL Queries</h2>
    <p>Python lists and dictionaries interact with the database and GUI components:</p>
    <ul>
      <li><b>Lists:</b> Used to store temporary data, such as member attributes during operations like adding or updating.</li>
      <li><b>Dictionaries:</b> Manage configuration settings, such as database credentials or themes.</li>
      <li><b>SQL Queries:</b> Ensure smooth interaction with the database for operations like adding members or fetching records.</li>
    </ul>
  </li>
  <li>
    <h2>🗳️ Error Handling and User Feedback</h2>
    <p>The system provides user-friendly feedback for all actions:</p>
    <ul>
      <li><b>Error Messages:</b> Displayed using Tkinter’s messagebox for issues like invalid input or database connection errors.</li>
      <li><b>Success Prompts:</b> Notify users of successful operations, such as “Member added successfully!”</li>
    </ul>
  </li>
</ul>
<hr></hr>
<div class ="markdown-heading" dir="auto">
  <h2 tabindex="-1" class="heading-element" dir="auto">🌏Chosen SDG</h2>
</div>
<p dir = "auto">
  <h3>🌇SDG 11 : Sustainable Cities and Communities</h3><br>
    This goal focuses on making cities inclusive, safe, resilient, and sustainable, which includes initiatives for building strong communities, promoting local involvement, and fostering sustainability at the community level. 
  <br>
  <br>
    By providing a system to manage and track community involvement in events, volunteer programs, or sustainability initiatives, this project supports these aims by helping organizations and local governments strengthen community engagement and participation.
</p>
<hr></hr>
<div class ="markdown-heading" dir="auto">
  <h2 tabindex="-1" class="heading-element" dir="auto">⚙️Instructions on Running the Program</h2>
</div>
<ol dir = "auto">
  <li>📚 Download the Libraries : 💡Tkinter and 🗃️MySQL Workbench</li>
  <li>⬇️ Set-up your 🗃️MySQL.</li>
  <li>🛑 Make sure your 🗃️MySQL is running in the background.</li>
  <li>📩Create the projec</li>
  <li>⏬Add the Program Files</li>
  <li>🔄Compile the Program</li>
  <li>▶️Run the Program</li>
  <li>❗Make sure to remember your password! The format will always be localhost, root, {password} </li>
</ol>
<hr></hr>
<div class ="markdown-heading" dir="auto">
  <h2 tabindex="-1" class="heading-elemen" dir="auto">Acknowledgment</h2>
</div>
<ul>
  <li>Our beloved 🎀cute-princess-kawaii🎀 Professor : Ma'am Fatima</li>
  <li>Sa mga aso namin : Ulap, Tala, Ulan, Sinag, at Nyebe</li>
  <li>Sa laptop ko, for not giving up on me</li>
  <li>Kay Indian Guy sa YouTube</li>
  <li>Kay Kim Chaewon na naghihintay sa'kin sa bahay</li>
</ul>
<hr></hr>
<h1>UNO QT!</h1>

