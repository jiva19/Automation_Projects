🐍 Python Automation Suite: Selenium & Pytest
This repository serves as a comprehensive collection of my earlier automation work, focusing on diverse architectural patterns including Page Object Model (POM), Data-Driven Testing, and Hybrid Frameworks.

🏢 Project 1: OrangeHRM (Employee Management)
Architecture: Page Object Model (POM)

Objective: Automated end-to-end HR workflows, including secure login, employee onboarding, document management, and database-style searching.

Technical Deep-Dive:

Advanced Element Interaction: Managed complex UI components such as dynamic/stable dropdowns, date-picker calendars, multi-select checkboxes, and HTML tables.

Pytest Mastery: Leveraged fixtures for setup/teardown, markers for test categorization, and @pytest.mark.parametrize for clean, reusable test logic.

OS Interaction: Integrated PyAutoGUI to automate local file system interactions and text file generation.

Execution: Used JsExecutors to handle hidden elements or scrolling behaviors that standard Selenium clicks couldn't reach.

🛍️ Project 2: E-Commerce Automation (Data-Driven)
Architecture: Data-Driven Framework (Excel-to-Test)

Objective: Built a robust testing engine for an E-commerce platform where the test logic is separated from the test data.

Technical Deep-Dive:

Excel Integration: Developed a custom utility to retrieve usernames, passwords, and "Expected Results" directly from an Excel spreadsheet.

Automated Reporting: Engineered a "write-back" feature where the script automatically updates the Excel file with the "Pass/Fail" status and actual results after each execution.

Workflows: Covered critical user paths including account authentication and multi-parameter product searching.

🌐 Project 3: VWO Platform Testing
Architecture: Hybrid-Driven Framework (Functional + Data-Driven)

Objective: Tested a complex SaaS platform requiring high-level browser manipulation and data handling.

Technical Deep-Dive:

Window & Frame Management: Handled complex DOM structures including iFrames and multiple browser tabs/windows.

State Management: Utilized Hybrid-Driven logic to combine functional step-definition testing with external data inputs.

JavaScript Injection: Used JsExecutors for high-precision interactions within the browser environment.
