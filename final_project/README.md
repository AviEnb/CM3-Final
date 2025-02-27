# CM3-Final
*Team: Avi Engbrecht, Pascal Hübner*

This is our final for Computer Sience at Hult International Business School in CM3


Introduction

The Investment Return Calculator is a sophisticated Python-based web application developed using Streamlit. It is designed to provide users with a detailed understanding of how their investments might grow over time under varying financial conditions. The application integrates a range of financial tools, including an investment goal planner, risk and volatility analysis, and a scenario comparison feature with a ±3% deviation from the expected return rate. The design philosophy behind this project focuses on delivering an intuitive user experience while ensuring the financial calculations are both accurate and reliable.

Selecting the Right Libraries

The choice of libraries plays a critical role in shaping the functionality and performance of the Investment Return Calculator. The project utilizes Streamlit for building the web interface, Pandas and Numpy for data management, Matplotlib for visualizing data, FPDF for generating dynamic PDF reports, and Pytest for testing. Each of these libraries was selected based on its specific advantages. Streamlit offers an unparalleled experience for rapidly developing data-driven web applications. Pandas and Numpy provide powerful tools for data manipulation and analysis, which are essential for financial modeling. Matplotlib was chosen for its flexibility in creating detailed and highly customizable visualizations. The inclusion of FPDF allows users to export their investment analysis as PDFs, adding a professional touch to the application's output. Lastly, Pytest was selected for its robust testing capabilities, which help maintain code quality and detect bugs early in development.

Application Structure and Design

The main function of the application, main(), serves as the program’s entry point. It sets up the application’s page using Streamlit's set_page_config method, defining the title, layout, and sidebar state. This is followed by using Streamlit's markdown method to present a welcoming title and a brief description to the user. The main() function then calls setup_sidebar(), a dedicated function that handles all user inputs. This modular approach enhances code maintainability by separating the user interface components from the business logic, allowing each function to focus on a specific task. This method adheres to software development best practices, particularly the principles of modularity and single responsibility, which make the codebase easier to debug and expand upon in future iterations.

Handling User Inputs

The setup_sidebar() function is responsible for collecting and processing all user inputs using Streamlit’s interactive widgets. These inputs include critical investment parameters such as the initial investment amount, monthly contributions, expected annual return rate, investment duration, compounding frequency, and the financial goal. Each input field is clearly labeled, and sensible default values are provided to guide users through the process. Input validation is managed using Streamlit's built-in tools, which help prevent invalid data from being entered. The function also features a 'Calculate Investment Growth' button that activates the calculate_investment_growth() function. Centralizing input handling in this way not only simplifies the user interface but also ensures that the input data is clean and ready for processing.

Financial Calculations and Modeling

The core of the Investment Return Calculator lies in the calculate_investment_growth() function, which performs all necessary financial calculations. The function first converts the selected compounding frequency into a numerical value using a dictionary-based frequency map. This approach allows for easy translation of user-friendly terms (e.g., 'Monthly') into precise numerical equivalents (e.g., 12). The function then calculates the total periods and the periodic interest rate based on the annual return rate and compounding frequency. By employing a loop to compute the investment value at each period, the function accurately models both the effects of compound interest and the impact of regular monthly contributions. This iterative approach is essential for creating a detailed financial projection over the specified investment duration.

User Interaction and Visualization

After completing the investment growth calculations, the function provides users with an estimated portfolio value and assesses whether their financial goal is achievable. By utilizing Streamlit’s subheader, success, and warning components, the application delivers feedback that is both informative and visually distinct. The use of inline feedback rather than requiring users to navigate through multiple pages enhances the overall usability of the application.

For visualization, Matplotlib is used to generate a line chart illustrating the investment growth over time. During the development process, we explored various visualization libraries and found Matplotlib to be particularly well-suited for our needs due to its extensive customization options and well-documented features. The Matplotlib documentation provided clear examples and guidelines on creating line charts, customizing plot elements, and integrating visualizations within a Streamlit app. This helped streamline the development process and ensure that the visual output met the project's requirements. The chart includes a dashed line to represent the investment goal, offering a clear visual benchmark for users to compare against their projected investment performance.

Advanced Financial Features

In addition to basic investment growth calculations, the Investment Return Calculator includes advanced features like risk and volatility analysis and scenario comparison. The calculate_volatility() function assesses the investment's volatility by calculating the standard deviation of percentage changes between periods. This metric is crucial for evaluating the investment's risk profile, offering users deeper insights into potential fluctuations in their investment value. The scenario_comparison() function allows users to explore how their investments might perform under different market conditions by generating projections with ±3% deviations in the expected return rate. These advanced tools transform the application from a simple calculator into a powerful financial planning resource.

Ensuring Code Quality with Testing

To maintain the reliability and stability of the application, Pytest is used extensively for testing. The test_project.py file contains a variety of tests that evaluate the core functions of the application. These tests include standard scenarios as well as edge cases, such as handling negative interest rates or zero initial investments. By employing Pytest's parametrize decorator, the project minimizes repetitive test code and broadens test coverage. This approach ensures that any changes to the codebase are thoroughly vetted, reducing the risk of introducing bugs or miscalculations in the financial models.

Disclaimer

This document was enhanced using AI technology, specifically ChatGPT, to improve clarity, grammar, and presentation. While AI tools were used to refine the content, the original version is available under "notes.txt".