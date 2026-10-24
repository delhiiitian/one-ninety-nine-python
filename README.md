# Python in 199 Pages: code

Every runnable example and project from the beginner book **Python in 199 Pages**,
part of the *199* series (one book per language, 199 pages each).

Each subtopic in the book shows only the key lines; the full program is here,
one file per subtopic, one folder per chapter. Every file runs on its own with
Python 3.10 or newer and needs nothing beyond the standard library.

## Quick start

```bash
git clone https://github.com/delhiiitian/one-ninety-nine-python.git
cd one-ninety-nine-python
python ch01_basics/01_hello_world.py
python run_all.py      # run every example and project test
```

## Chapter 1: Python basics

- [1.1 Hello, World](ch01_basics/01_hello_world.py)
- [1.2 Variables](ch01_basics/02_variables.py)
- [1.3 Numbers](ch01_basics/03_numbers.py)
- [1.4 Strings](ch01_basics/04_strings.py)
- [1.5 Booleans and comparisons](ch01_basics/05_booleans.py)
- [1.6 Input and output](ch01_basics/06_input_output.py)
- [1.7 Type conversion](ch01_basics/07_type_conversion.py)
- [1.8 Comments and code style](ch01_basics/08_comments_style.py)
- [1.9 Operators and precedence](ch01_basics/09_operators.py)
- **[Project 1: Bill Splitter](projects/p1_bill_splitter/)**

## Chapter 2: Control flow

- [2.1 if / else](ch02_control_flow/01_if_else.py)
- [2.2 elif](ch02_control_flow/02_elif_chains.py)
- [2.3 Combining conditions with and, or, not.](ch02_control_flow/03_logical_operators.py)
- [2.4 while loops](ch02_control_flow/04_while_loops.py)
- [2.5 for loops](ch02_control_flow/05_for_loops.py)
- [2.6 range()](ch02_control_flow/06_range.py)
- [2.7 break and continue](ch02_control_flow/07_break_continue.py)
- [2.8 Nested loops](ch02_control_flow/08_nested_loops.py)
- [2.9 match / case](ch02_control_flow/09_match_case.py)
- **[Project 2: Number Guessing Game](projects/p2_guessing_game/)**

## Chapter 3: Functions

- [3.1 Defining functions](ch03_functions/01_defining_functions.py)
- [3.2 Parameters and arguments](ch03_functions/02_parameters_arguments.py)
- [3.3 Return values](ch03_functions/03_return_values.py)
- [3.4 Default and keyword arguments.](ch03_functions/04_default_keyword_args.py)
- [3.5 *args and **kwargs](ch03_functions/05_args_kwargs.py)
- [3.6 Scope](ch03_functions/06_scope.py)
- [3.7 Lambda functions](ch03_functions/07_lambda.py)
- [3.8 Recursion](ch03_functions/08_recursion.py)
- [3.9 Docstrings and type hints](ch03_functions/09_docstrings_type_hints.py)
- **[Project 3: Unit Converter](projects/p3_unit_converter/)**

## Chapter 4: Data structures

- [4.1 Lists](ch04_data_structures/01_lists.py)
- [4.2 Slicing](ch04_data_structures/02_slicing.py)
- [4.3 Tuples](ch04_data_structures/03_tuples.py)
- [4.4 Dictionaries](ch04_data_structures/04_dictionaries.py)
- [4.5 Sets](ch04_data_structures/05_sets.py)
- [4.6 List comprehensions](ch04_data_structures/06_list_comprehensions.py)
- [4.7 Nested data](ch04_data_structures/07_nested_structures.py)
- [4.8 Sorting](ch04_data_structures/08_sorting.py)
- [4.9 Choosing the right structure](ch04_data_structures/09_choosing_structure.py)
- **[Project 4: Contact Book](projects/p4_contact_book/)**

## Chapter 5: Error handling

- [5.1 Reading error messages (tracebacks).](ch05_error_handling/01_reading_tracebacks.py)
- [5.2 try / except](ch05_error_handling/02_try_except.py)
- [5.3 Handling several kinds of errors.](ch05_error_handling/03_multiple_exceptions.py)
- [5.4 else and finally](ch05_error_handling/04_else_finally.py)
- [5.5 Raising exceptions](ch05_error_handling/05_raising_exceptions.py)
- [5.6 Custom exceptions](ch05_error_handling/06_custom_exceptions.py)
- [5.7 Validating user input](ch05_error_handling/07_validating_input.py)
- [5.8 Assertions](ch05_error_handling/08_assertions.py)
- [5.9 Logging](ch05_error_handling/09_logging.py)
- **[Project 5: ATM Simulator](projects/p5_atm_simulator/)**

## Chapter 6: Files and I/O

- [6.1 Reading files.](ch06_files_io/01_reading_files.py)
- [6.2 Writing files.](ch06_files_io/02_writing_files.py)
- [6.3 The with statement](ch06_files_io/03_with_statement.py)
- [6.4 Paths with pathlib.](ch06_files_io/04_paths_pathlib.py)
- [6.5 CSV files](ch06_files_io/05_csv_files.py)
- [6.6 JSON files](ch06_files_io/06_json_files.py)
- [6.7 Working with folders.](ch06_files_io/07_directories.py)
- [6.8 Binary files and bytes.](ch06_files_io/08_binary_files.py)
- [6.9 Command-line arguments with argparse.](ch06_files_io/09_command_line_args.py)
- **[Project 6: Expense Tracker](projects/p6_expense_tracker/)**

## Chapter 7: Modules and tooling

- [7.1 Importing modules](ch07_modules_tooling/01_importing_modules.py)
- [7.2 Creating your own module.](ch07_modules_tooling/02_creating_modules.py)
- [7.3 Packages](ch07_modules_tooling/03_packages.py)
- [7.4 A tour of the standard library ("batteries included").](ch07_modules_tooling/04_standard_library_tour.py)
- [7.5 pip](ch07_modules_tooling/05_pip_and_packages.py)
- [7.6 Virtual environments](ch07_modules_tooling/06_virtual_environments.py)
- [7.7 if __name__ == "__main__"](ch07_modules_tooling/07_main_guard.py)
- [7.8 Testing with unittest.](ch07_modules_tooling/08_testing_unittest.py)
- [7.9 Debugging](ch07_modules_tooling/09_debugging.py)
- **[Project 7: textkit, a Text Analysis Toolkit](projects/p7_text_toolkit/)**

## Chapter 8: Python's strengths

- [8.1 Classes and objects](ch08_python_strengths/01_classes_objects.py)
- [8.2 Inheritance](ch08_python_strengths/02_inheritance.py)
- [8.3 Special (dunder) methods](ch08_python_strengths/03_dunder_methods.py)
- [8.4 Dataclasses](ch08_python_strengths/04_dataclasses.py)
- [8.5 Iterators](ch08_python_strengths/05_iterators.py)
- [8.6 Generators](ch08_python_strengths/06_generators.py)
- [8.7 Decorators](ch08_python_strengths/07_decorators.py)
- [8.8 Writing your own context managers.](ch08_python_strengths/08_context_managers_custom.py)
- [8.9 Pythonic idioms](ch08_python_strengths/09_pythonic_idioms.py)
- **[Project 8: Library Manager](projects/p8_library_manager/)**

## Chapter 9: Real-world Python

- [9.1 Dates and times.](ch09_real_world/01_dates_times.py)
- [9.2 Regular expressions](ch09_real_world/02_regular_expressions.py)
- [9.3 Making HTTP requests](ch09_real_world/03_http_requests.py)
- [9.4 Working with REST APIs](ch09_real_world/04_working_with_apis.py)
- [9.5 Databases with SQLite.](ch09_real_world/05_sqlite_database.py)
- [9.6 A tiny web server.](ch09_real_world/06_web_server.py)
- [9.7 Automating boring tasks.](ch09_real_world/07_automation_scripts.py)
- [9.8 Doing several things at once with threads.](ch09_real_world/08_concurrency_threads.py)
- [9.9 Simple data analysis.](ch09_real_world/09_data_analysis.py)
- **[Project 9: To-do REST API](projects/p9_todo_api/)**

## Layout

```
ch01_basics/ ... ch09_real_world/   # one file per subtopic, 01_ to 09_
projects/p1_... p9_.../           # one project per chapter, each with README and tests
run_all.py                        # runs every example and every project test
```
