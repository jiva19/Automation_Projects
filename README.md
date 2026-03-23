# 🐍 Python Automation Suite: Selenium & Pytest

This repository is a comprehensive collection of my foundational automation work, demonstrating the implementation of three distinct architectural patterns: **Page Object Model (POM)**, **Data-Driven Testing**, and **Hybrid Frameworks**.

---

## 🏢 Project 1: OrangeHRM (Employee Management)
**Architecture:** Page Object Model (POM)

* **Objective:** Automated end-to-end HR workflows, including secure authentication, employee onboarding, document management, and database-style record searching.
* **Technical Deep-Dive:**
    * **Advanced UI Interaction:** Managed complex components including dynamic dropdowns, date-picker calendars, multi-select checkboxes, and HTML tables.
    * **Pytest Mastery:** Utilized `fixtures` for setup/teardown, `markers` for categorization, and `@pytest.mark.parametrize` for data-efficient, reusable test logic.
    * **OS Interaction:** Integrated **PyAutoGUI** to automate local file system interactions and dynamic text file generation.
    * **JavaScript Execution:** Employed `JsExecutors` to handle hidden elements and custom scrolling behaviors beyond standard Selenium capabilities.

---

## 🛍️ Project 2: E-Commerce Automation
**Architecture:** Data-Driven Framework (Excel-to-Test)

* **Objective:** Engineered a robust testing engine for an E-commerce platform where test logic is completely decoupled from test data.
* **Technical Deep-Dive:**
    * **Excel Integration:** Developed custom utilities to retrieve credentials and "Expected Results" directly from external spreadsheets.
    * **Bi-Directional Reporting:** Built a "write-back" feature that automatically updates the source Excel file with **Pass/Fail** status and actual execution results.
    * **Core Workflows:** Automated critical user paths, including account authentication and multi-parameter product search functionality.

---

## 🌐 Project 3: VWO Platform Testing
**Architecture:** Hybrid-Driven Framework (Functional + Data-Driven)

* **Objective:** Validated a complex SaaS platform requiring high-level browser manipulation and sophisticated state management.
* **Technical Deep-Dive:**
    * **Complex DOM Handling:** Successfully managed interactions within **iFrames** and across multiple browser tabs/windows.
    * **Hybrid Logic:** Combined functional step-definitions with external data inputs to maintain a flexible and scalable test suite.
    * **Precision Interaction:** Used JavaScript injection via `JsExecutors` for high-precision interactions within the browser environment.

---

### 🛠️ Tech Stack
* **Language:** Python
* **Libraries:** Selenium WebDriver, Pytest
* **Data Handling:** OpenPyXL (Excel), CSV, PyAutoGUI
* **Design Patterns:** POM, Singleton, Data-Driven, Hybrid
