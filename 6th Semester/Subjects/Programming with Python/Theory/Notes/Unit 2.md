Okay, here are detailed, comprehensive, and explained notes for UNIT-II, designed to be easy to remember, following the same style as before.

---

**UNIT II: Functions, Data Structures (Lists & Dictionaries), and String Manipulation**

---

**PART 1: Functions**

Functions are reusable blocks of code that perform a specific task. They help organize your code, make it more readable, and reduce repetition.

**1. `def` Statements with Parameters**

*   **What is a Function?**
    *   A named sequence of statements that performs a computation.
    *   You "define" a function once and then "call" it (run it) multiple times.
*   **`def` Statement:**
    *   Used to define a new function.
    *   Syntax:
        ```python
        def function_name(parameter1, parameter2, ...):
            # Indented block of code (function's body)
            statement1
            statement2
            # ...
            # Optionally, a return statement
        ```
*   **Parameters (Arguments):**
    *   Variables listed inside the parentheses in the function definition.
    *   They are placeholders for the values (arguments) that will be passed into the function when it's called.
    *   When you call the function, you provide actual values (arguments) for these parameters.
*   **Calling a Function:**
    *   You execute the function by typing its name followed by parentheses, including any arguments.
    *   Example:
        ```python
        # Defining a function
        def greet(name):  # 'name' is a parameter
            print("Hello, " + name + "!")

        # Calling the function
        greet("Alice")    # "Alice" is an argument passed to the 'name' parameter
        greet("Bob")      # "Bob" is an argument
        ```

    *Easy to Remember:*
    *   `def` is like **creating a recipe**.
    *   `function_name` is the **name of your recipe** (e.g., `make_sandwich`).
    *   `parameters` are the **ingredients the recipe needs** (e.g., `bread`, `filling`).
    *   Calling `greet("Alice")` is like saying, "Use the `greet` recipe with the ingredient 'Alice'."

**2. Return Values and `return` Statements**

*   **What is a Return Value?**
    *   The value that a function "sends back" to the part of the program that called it.
    *   Not all functions need to return a value (e.g., `greet` above just prints something).
*   **`return` Statement:**
    *   Used inside a function to specify the value to be returned.
    *   When a `return` statement is executed, the function immediately stops, and the specified value is sent back.
    *   Syntax: `return expression`
*   **Capturing the Return Value:**
    *   You can store the returned value in a variable.
    *   Example:
        ```python
        def add_numbers(x, y):
            sum_result = x + y
            return sum_result  # This function returns the sum

        # Calling the function and storing its return value
        result = add_numbers(5, 3)
        print(result)  # Output: 8

        another_result = add_numbers(10, 20) + 100
        print(another_result) # Output: 130
        ```

    *Easy to Remember:*
    *   `return` is what your **recipe produces or gives back** (e.g., `make_sandwich` returns a sandwich).
    *   If your recipe (function) is `add_numbers(5, 3)`, `return sum_result` gives back the number `8`.

**3. The `None` Value**

*   **What is `None`?**
    *   A special data type in Python (`NoneType`) that represents the **absence of a value** or a null value.
    *   It's the *only* value of `NoneType`.
    *   Often used to indicate that a variable doesn't have a meaningful value yet, or a function didn't explicitly return anything.
*   **Functions that Don't `return` Explicitly:**
    *   If a function doesn't have a `return` statement, or if it has a `return` statement without an expression (just `return`), it implicitly returns `None`.
    *   Example:
        ```python
        def simple_print(message):
            print(message)
            # No explicit return statement

        output = simple_print("Testing None") # "Testing None" is printed
        print(output)                        # Output: None
        ```
*   `None` is not the same as `0`, `False`, or an empty string `""`. It's uniquely `None`.
    You can check for it: `if my_variable is None: ...`

    *Easy to Remember:*
    *   `None` is like an **empty box** or a placeholder signifying "nothing here."
    *   If a recipe (function) is just about doing an action (like cleaning the kitchen) and doesn't produce an item, it implicitly "returns" `None`.

**4. Keyword Arguments and `print()`**

*   **Positional Arguments:**
    *   When you call a function, Python matches arguments to parameters based on their order.
    *   `def my_func(a, b): ...` called as `my_func(10, 20)` means `a` gets `10`, `b` gets `20`.
*   **Keyword Arguments:**
    *   You can specify which parameter an argument should go to by using the parameter's name in the function call, followed by an `=` and the value.
    *   This allows you to pass arguments out of order or skip optional parameters that have default values.
    *   Syntax: `function_name(parameter_name=value)`
    *   Example:
        ```python
        def describe_pet(animal_type, pet_name):
            print("I have a " + animal_type + ".")
            print("My " + animal_type + "'s name is " + pet_name + ".")

        describe_pet(animal_type="hamster", pet_name="Harry")
        describe_pet(pet_name="Lucy", animal_type="dog") # Order doesn't matter with keywords
        ```
*   **`print()` Function's Keyword Arguments:**
    *   The built-in `print()` function has useful keyword arguments:
        *   `end`: String appended after the last value, defaults to a newline (`\n`).
        *   `sep`: String inserted between values, defaults to a space (` `).
    *   Example:
        ```python
        print("Hello", "World")           # Output: Hello World (sep=' ')
        print("Hello", "World", sep="---")# Output: Hello---World
        print("One line...", end="")      # No newline, next print is on same line
        print("...continues here.")
        # Output: One line......continues here.
        ```

    *Easy to Remember:*
    *   Keyword arguments are like **labeling your ingredients** when giving them to the recipe, so order doesn't matter: `sugar="1 cup"`, `flour="2 cups"`.
    *   `print(..., end="")` means "print this, but **end with nothing** instead of a new line."
    *   `print(..., sep="-")` means "print these items, **separated by a dash**."

**5. Local and Global Scope**

*   **Scope:** The region of a program where a variable is recognized.
*   **Local Scope:**
    *   Variables defined inside a function (including parameters) are **local** to that function.
    *   They only exist while the function is executing.
    *   They cannot be accessed from outside the function.
    *   When the function finishes, local variables are destroyed.
*   **Global Scope:**
    *   Variables defined outside of all functions are **global**.
    *   They can be accessed from anywhere in your program, including inside functions (for reading).
*   **Name Shadowing:** If a local variable has the same name as a global variable, the local variable "hides" or "shadows" the global variable within that function. The function will use its local variable.
*   Example:
    ```python
    eggs = "global eggs"  # Global variable

    def spam():
        eggs = "spam local eggs"  # Local variable, shadows global 'eggs'
        print(eggs)             # Prints "spam local eggs"

    def bacon():
        # No local 'eggs', so it uses the global 'eggs'
        print(eggs)             # Prints "global eggs"

    def ham():
        # This would cause an error if you try to modify global 'eggs' without 'global' keyword
        # print(eggs) # This would work (read global)
        # eggs = "ham local" # This makes 'eggs' local to ham for this assignment
        # If you assign to a variable in a function, it becomes local unless declared global.
        pass # Example just showing scope rules.

    spam()
    bacon()
    print(eggs)                 # Prints "global eggs" (global variable unchanged by spam())
    ```

    *Easy to Remember:*
    *   **Local Scope:** Variables are like **ingredients kept inside a specific chef's private kitchen (the function)**. Only that chef can use them directly, and they're cleaned up when the chef is done.
    *   **Global Scope:** Variables are like **ingredients in the main pantry, accessible to all chefs**.
    *   If a chef brings their own "salt" (local variable) into their kitchen, they'll use that, not the pantry "salt" (global variable with same name).

**6. The `global` Statement**

*   If you need to **modify** a global variable from *inside* a function, you must explicitly tell Python that you are referring to the global variable using the `global` statement.
*   Syntax: `global variable_name`
*   This statement is typically placed at the beginning of the function body.
*   Example:
    ```python
    count = 0  # Global variable

    def increment_counter():
        global count  # Declare that we are using the global 'count'
        count = count + 1
        print("Inside function, count is:", count)

    increment_counter()
    print("Outside function, count is:", count) # Output: 1 (global variable was modified)
    ```
*   **Use Sparingly:** Overuse of `global` can make code harder to understand and debug because it's not always clear where a variable is being changed. It's often better to `return` values from functions and reassign them globally.

    *Easy to Remember:*
    *   The `global` statement is like a chef saying, **"I need to change the amount of sugar in the main pantry, not just use my own."** (Use with caution!)

**7. Exception Handling (`try` and `except`)**

*   **What is an Exception?**
    *   An error that occurs during the execution of a program.
    *   When an exception occurs, Python normally stops and generates an error message (traceback).
*   **Exception Handling:**
    *   A way to gracefully manage errors and prevent your program from crashing.
    *   You "try" a block of code that might cause an error.
    *   If an error ("exception") occurs, you "catch" it and execute a specific block of code.
*   **`try` and `except` Blocks:**
    *   Syntax:
        ```python
        try:
            # Code that might cause an exception
            # ...
        except SomeErrorType: # Optional: specify the type of error to catch
            # Code to run if SomeErrorType occurs
            # ...
        except AnotherErrorType as e: # 'as e' stores the error object in variable 'e'
            # Code to run if AnotherErrorType occurs
            # print(e) to see the error message
            # ...
        except: # Catches any exception (generally less preferred than specific ones)
            # Code to run if any other error occurs
            # ...
        else: # Optional
            # Code to run if NO exception occurred in the 'try' block
            # ...
        finally: # Optional
            # Code that ALWAYS runs, whether an exception occurred or not
            # (e.g., for cleanup like closing a file)
            # ...
        ```
*   Example:
    ```python
    def divide(x, y):
        try:
            result = x / y
        except ZeroDivisionError:
            print("Error: Cannot divide by zero!")
            return None # Or handle it some other way
        except TypeError:
            print("Error: Invalid input types for division!")
            return None
        else:
            print("Division successful.")
            return result
        finally:
            print("Executing finally clause.")

    print(divide(10, 2))   # Output: Division successful. Executing finally clause. 5.0
    print(divide(10, 0))   # Output: Error: Cannot divide by zero! Executing finally clause. None
    print(divide("10", 2)) # Output: Error: Invalid input types for division! Executing finally clause. None
    ```

    *Easy to Remember:*
    *   `try`: **"Let's TRY this risky operation..."**
    *   `except`: **"...and if THIS specific problem (error) happens, do THIS instead of crashing."**
    *   `else`: "...if everything in `try` went fine, then do this."
    *   `finally`: "...no matter what happened (error or not), ALWAYS do this clean-up step."
    *   It's like having a **safety net** or a contingency plan.

---

**PART 2: Lists**

Lists are ordered, mutable (changeable) collections of items.

**8. The List Data Type**

*   A list is a sequence of values (items or elements).
*   Items can be of different data types.
*   Defined by enclosing comma-separated values in square brackets `[]`.
*   Examples:
    ```python
    empty_list = []
    numbers = [1, 2, 3, 4, 5]
    fruits = ["apple", "banana", "cherry"]
    mixed_list = [1, "hello", 3.14, True]
    ```

    *Easy to Remember:*
    *   Lists are like a **shopping list** or a **numbered sequence of boxes** where each box can hold an item.

**9. Working with Lists**

*   **a. Accessing Items (Indexing):**
    *   Use square brackets `[]` with an index number (0-based).
    *   `my_list[0]` is the first item, `my_list[1]` is the second, etc.
    *   Negative indexing: `my_list[-1]` is the last item, `my_list[-2]` is the second-to-last.
    *   Example:
        ```python
        fruits = ["apple", "banana", "cherry"]
        print(fruits[0])    # Output: apple
        print(fruits[-1])   # Output: cherry
        ```
*   **b. Slicing:**
    *   Get a sub-list (a "slice") from a list.
    *   `my_list[start:end]` (end index is exclusive).
    *   `my_list[:end]` (from beginning up to, not including, end).
    *   `my_list[start:]` (from start to the end).
    *   `my_list[:]` (a copy of the whole list).
    *   Example:
        ```python
        numbers = [0, 1, 2, 3, 4, 5]
        print(numbers[1:4])  # Output: [1, 2, 3]
        print(numbers[:3])   # Output: [0, 1, 2]
        print(numbers[3:])   # Output: [3, 4, 5]
        ```
*   **c. `len()` Function:**
    *   Returns the number of items in a list.
    *   `length = len(my_list)`
*   **d. Changing Items:**
    *   Lists are mutable, so you can change an item at a specific index.
    *   `my_list[index] = new_value`
    *   Example:
        ```python
        colors = ["red", "green", "blue"]
        colors[1] = "yellow"
        print(colors)  # Output: ['red', 'yellow', 'blue']
        ```
*   **e. Concatenation (`+`) and Replication (`*`):**
    *   Same as with strings.
    *   `list1 + list2` creates a new list with elements from both.
    *   `list1 * integer` creates a new list by repeating items.
    *   Example:
        ```python
        list_a = [1, 2]
        list_b = [3, 4]
        combined = list_a + list_b  # [1, 2, 3, 4]
        repeated = list_a * 3       # [1, 2, 1, 2, 1, 2]
        ```
*   **f. `in` and `not in` Operators:**
    *   Check if an item exists in a list. Returns `True` or `False`.
    *   Example:
        ```python
        pets = ["cat", "dog", "bird"]
        print("dog" in pets)    # Output: True
        print("fish" not in pets) # Output: True
        ```

    *Easy to Remember:*
    *   Think of a list as a **train with numbered cars**.
    *   Indexing: "What's in car #0?"
    *   Slicing: "Give me cars #1 through #3."
    *   `len()`: "How many cars are in this train?"

**10. Augmented Assignment Operators**

*   Shorthand operators for performing an operation and assigning the result back to the same variable.
*   Common ones for lists (and numbers):
    *   `+=` (add and assign): `my_list += [4, 5]` is like `my_list = my_list + [4, 5]`
    *   `*=` (multiply and assign): `my_list *= 2` is like `my_list = my_list * 2`
*   Example:
    ```python
    spam = [1, 2, 3]
    spam += [4, 5]  # spam is now [1, 2, 3, 4, 5]
    print(spam)

    eggs = ['a']
    eggs *= 3       # eggs is now ['a', 'a', 'a']
    print(eggs)
    ```

    *Easy to Remember:*
    *   They are **shortcuts** for common operations. `x += 1` is quicker than `x = x + 1`.

**11. List Methods**

*   Methods are functions that are "attached" to objects (like lists). You call them using dot notation: `list_name.method_name()`.
*   Many list methods modify the list **in-place** (they change the original list and don't return a new one; they return `None`).

*   **a. `index(value)`:**
    *   Returns the index of the *first* occurrence of `value` in the list.
    *   Raises a `ValueError` if the value is not found.
    *   `idx = my_list.index("apple")`
*   **b. `append(value)`:**
    *   Adds `value` to the *end* of the list. Modifies the list in-place.
    *   `my_list.append("orange")`
*   **c. `insert(index, value)`:**
    *   Inserts `value` at the specified `index`. Items from that index onwards are shifted to the right. Modifies in-place.
    *   `my_list.insert(1, "grape")` (inserts "grape" at index 1)
*   **d. `remove(value)`:**
    *   Removes the *first* occurrence of `value` from the list.
    *   Raises a `ValueError` if the value is not found. Modifies in-place.
    *   `my_list.remove("banana")`
*   **e. `del` statement (not a method, but related):**
    *   Deletes an item at a specific `index`.
    *   `del my_list[0]` (deletes the item at index 0)
*   **f. `pop(index=-1)`:**
    *   Removes and *returns* the item at `index`.
    *   If `index` is not specified, it defaults to `-1` (removes and returns the last item). Modifies in-place.
    *   `last_item = my_list.pop()`
    *   `first_item = my_list.pop(0)`
*   **g. `sort(reverse=False, key=None)`:**
    *   Sorts the items of the list in ascending order by default. Modifies the list in-place.
    *   `my_list.sort()` (sorts ascending)
    *   `my_list.sort(reverse=True)` (sorts descending)
    *   For sorting complex objects, you can use the `key` argument with a function. (e.g., `my_list.sort(key=str.lower)` for case-insensitive sort of strings).
*   **h. `reverse()`:**
    *   Reverses the order of elements in the list. Modifies the list in-place.
    *   `my_list.reverse()`

    *Easy to Remember:*
    *   List methods are like **actions you can tell the list to do to itself.**
    *   `append()`: **Add to tail.**
    *   `insert()`: **Squeeze in at this spot.**
    *   `remove()`: **Find this item and remove it.**
    *   `pop()`: **Take an item off (and give it to me).**
    *   `sort()`: **Line up in order!**

---

**PART 3: Dictionaries and Structuring Data**

Dictionaries store key-value pairs, allowing you to associate pieces of data.

**12. The Dictionary Data Type (`dict`)**

*   An unordered (in Python < 3.7, ordered in Python 3.7+) collection of `key:value` pairs.
*   Keys must be unique and immutable (e.g., strings, numbers, tuples). Values can be any data type.
*   Defined by enclosing comma-separated `key:value` pairs in curly braces `{}`.
*   Examples:
    ```python
    empty_dict = {}
    my_cat = {'name': 'Zophie', 'age': 7, 'color': 'gray'}
    student_grades = {'Alice': 85, 'Bob': 92, 'Charlie': 78}
    ```
*   **Accessing Values:**
    *   Use the key in square brackets `[]`.
    *   `value = my_dict[key]`
    *   If the key doesn't exist, it raises a `KeyError`.
    *   Example: `print(my_cat['name'])` # Output: Zophie
*   **Adding/Modifying Pairs:**
    *   `my_dict[new_key] = new_value`
    *   `my_dict[existing_key] = updated_value`
    *   Example:
        ```python
        my_cat['species'] = 'cat'   # Adds new key-value
        my_cat['age'] = 8           # Updates existing key's value
        print(my_cat)
        ```
*   **`len()` Function:** Returns the number of key-value pairs.
*   **`in` and `not in` Operators:** Check if a *key* exists in the dictionary.
    *   `'name' in my_cat` (True)
    *   `'breed' not in my_cat` (True)
*   **Dictionary Methods:**
    *   **`keys()`:** Returns a view object displaying a list of all keys.
        *   `list(my_cat.keys())` gives `['name', 'age', 'color', 'species']`
    *   **`values()`:** Returns a view object displaying a list of all values.
        *   `list(my_cat.values())` gives `['Zophie', 8, 'gray', 'cat']`
    *   **`items()`:** Returns a view object displaying a list of key-value tuple pairs.
        *   `list(my_cat.items())` gives `[('name', 'Zophie'), ('age', 8), ...]`
    *   **`get(key, default_value)`:**
        *   Returns the value for `key` if `key` is in the dictionary.
        *   If `key` is not found, it returns `default_value` instead of raising a `KeyError`. If `default_value` is not specified, it defaults to `None`.
        *   `color = my_cat.get('color', 'unknown')`
    *   **`setdefault(key, default_value)`:**
        *   If `key` is in the dictionary, returns its value.
        *   If `key` is not in the dictionary, inserts `key` with a value of `default_value` and returns `default_value`.
        *   `my_cat.setdefault('breed', 'unknown_breed')` (if 'breed' isn't there, it's added)

    *Easy to Remember:*
    *   Dictionaries are like a **real-world dictionary** or a **phone book**: you look up a `key` (word/name) to find its `value` (definition/phone number).
    *   Keys are unique labels on **filing cabinet drawers**; values are the contents of the drawers.

**13. Pretty Printing (`pprint` module)**

*   When you have complex dictionaries or lists (especially nested ones), `print()` can produce output that's hard to read.
*   The `pprint` module (pretty print) formats these structures in a more human-readable way.
*   You need to `import pprint`.
*   Use `pprint.pprint(your_data_structure)`.
*   Example:
    ```python
    import pprint

    messy_data = {'name': 'Alice', 'pets': [{'name': 'Whiskers', 'species': 'cat'}, {'name': 'Buddy', 'species': 'dog'}], 'city': 'New York'}
    print("Regular print:")
    print(messy_data)

    print("\nPretty print:")
    pprint.pprint(messy_data)
    ```
    Output of `pprint` will be nicely formatted and indented.

    *Easy to Remember:*
    *   `pprint` is like an **organizer for your messy data display**, making it neat and tidy.

**14. Using Data Structures to Model Real-World Things**

*   Lists and dictionaries can be combined to represent complex, structured data.
*   **Lists of Dictionaries:** Useful for a collection of items where each item has several properties.
    *   Example: A list of employees, where each employee is a dictionary with keys like 'name', 'id', 'department'.
    ```python
    all_guests = [
        {'name': 'Alice', 'apples': 5, 'pretzels': 12},
        {'name': 'Bob', 'ham_sandwiches': 3, 'apples': 2},
        {'name': 'Carol', 'cups': 3, 'apple_pies': 1}
    ]
    ```
*   **Dictionaries with List Values:** Useful when a key is associated with multiple items.
    *   Example: A dictionary mapping categories to a list of items in that category.
    ```python
    picnic_items = {'apples': 5, 'cups': 2, 'cookies': 80} # Simple dictionary

    # A more complex example:
    inventory = {
        'rope': 1,
        'torch': 6,
        'gold coin': 42,
        'dagger': 1,
        'arrow': 12,
        'backpack_contents': ['map', 'compass', 'water bottle'] # List as a value
    }
    ```

    *Easy to Remember:*
    *   Think about the **structure of the real-world thing**.
    *   If it's a **collection of similar things with properties**, use a list of dictionaries (e.g., `list_of_students`).
    *   If it's **one thing with different labeled parts**, some of which might be collections themselves, use a dictionary (e.g., `car_details` with a key `passengers` having a list value).

---

**PART 4: Manipulating Strings**

Strings are sequences of characters. While immutable, Python provides many methods to work with them and create new strings.

**15. Working with Strings (Recap & More)**

*   **Immutable:** Strings cannot be changed in-place. String methods always return *new* strings.
*   **Indexing and Slicing:** Work just like with lists.
    *   `my_string[0]`, `my_string[-1]`, `my_string[1:5]`
*   **`in` and `not in`:** Check for substrings.
    *   `'ell' in 'Hello'` (True)
*   **Concatenation (`+`) and Replication (`*`):**
    *   `"Hello" + " " + "World"`
    *   `"Ha" * 3`
*   **Multi-line Strings:** Use triple quotes (`'''...'''` or `"""..."""`).
    ```python
    multi = """This is a
    multi-line string."""
    ```
*   **Escape Characters:** Special characters preceded by a backslash (`\`).
    *   `\n` (newline), `\t` (tab), `\\` (backslash), `\'` (single quote), `\"` (double quote).
    *   `print("She said, \"Hi!\"")`
*   **Raw Strings:** Prefix with `r`. Ignores escape characters. Useful for regular expressions or Windows paths.
    *   `print(r"C:\Users\new_folder")`

**16. Useful String Methods**

These methods are called on a string object and return a *new* string (or a Boolean/integer for check methods).

*   **Case Conversion:**
    *   `upper()`: Returns a new string with all characters in uppercase. ` "Hello".upper() ` -> `"HELLO"`
    *   `lower()`: Returns a new string with all characters in lowercase. ` "Hello".lower() ` -> `"hello"`
    *   `capitalize()`: Returns a new string with the first character uppercase and the rest lowercase. `"hello world".capitalize()` -> `"Hello world"`
    *   `title()`: Returns a new string with the first character of each word uppercase. `"hello world".title()` -> `"Hello World"`
*   **Checking Methods (`is...()` - return `True` or `False`):**
    *   `isupper()`: `True` if all cased characters are uppercase and there's at least one cased character.
    *   `islower()`: `True` if all cased characters are lowercase and there's at least one cased character.
    *   `isalpha()`: `True` if all characters are letters and there's at least one character.
    *   `isalnum()`: `True` if all characters are letters or numbers and there's at least one character.
    *   `isdecimal()`: `True` if all characters are decimal digits (0-9) and there's at least one character.
    *   `isspace()`: `True` if all characters are whitespace (space, tab, newline) and there's at least one character.
    *   `istitle()`: `True` if the string is title-cased (first letter of each word is uppercase).
*   **Searching and Replacing:**
    *   `startswith(substring)`: `True` if the string starts with `substring`.
    *   `endswith(substring)`: `True` if the string ends with `substring`.
    *   `find(substring, start=0, end=len(string))`: Returns the lowest index of `substring` found; returns `-1` if not found.
    *   `rfind()`: Like `find()`, but searches from the right.
    *   `count(substring)`: Returns the number of non-overlapping occurrences of `substring`.
    *   `replace(old, new, count=-1)`: Returns a new string with all occurrences of `old` replaced by `new`. If `count` is given, only replaces that many.
*   **Joining and Splitting:**
    *   `join(iterable_of_strings)`: Joins elements of an iterable (e.g., a list of strings) into a single string, with the original string as the separator.
        *   `", ".join(["apple", "banana", "cherry"])` -> `"apple, banana, cherry"`
        *   `"-".join("123")` -> `"1-2-3"`
    *   `split(separator=None, maxsplit=-1)`: Returns a list of strings by splitting the original string at occurrences of `separator`.
        *   If `separator` is not specified or `None`, splits by whitespace.
        *   `"apple,banana,cherry".split(",")` -> `['apple', 'banana', 'cherry']`
        *   `"Hello World".split()` -> `['Hello', 'World']`
*   **Stripping Whitespace:**
    *   `strip(chars=None)`: Returns a new string with leading and trailing `chars` removed. If `chars` is `None` or not specified, removes whitespace.
        *   `"  hello  ".strip()` -> `"hello"`
        *   `"xxhelloxx".strip("x")` -> `"hello"`
    *   `lstrip(chars=None)`: Strips from the left side.
    *   `rstrip(chars=None)`: Strips from the right side.
*   **Alignment and Padding:**
    *   `center(width, fillchar=' ')`: Returns a new string centered in a string of `width` length, padded with `fillchar`.
    *   `ljust(width, fillchar=' ')`: Left justifies.
    *   `rjust(width, fillchar=' ')`: Right justifies.
        *   `"hello".center(10, "-")` -> `"--hello---"`

    *Easy to Remember:*
    *   String methods are **tools to transform or inspect text**.
    *   `is...()` methods ask **yes/no questions** about the string.
    *   `upper()/lower()`: SHOUT or whisper.
    *   `join()`: **Glue pieces together** with a string.
    *   `split()`: **Chop a string into pieces** at a separator.
    *   `strip()`: **Trim the edges.**
    *   `replace()`: **Find and substitute.**

---

**Key Takeaways & Mnemonics Summary (UNIT-II):**

*   **Functions (`def`):** Reusable recipes. Parameters are ingredients, `return` is the dish.
    *   **`None`:** Empty box, "nothing here."
    *   **Keyword Args:** Label your ingredients (`name="value"`).
    *   **Scope:** Local (chef's kitchen) vs. Global (main pantry). `global` to change pantry items.
    *   **Exception Handling (`try`/`except`):** Safety net for errors.
*   **Lists (`[]`):** Ordered shopping list/train cars. Mutable.
    *   **Indexing `[0]`, Slicing `[1:3]`**.
    *   **Methods (`.append()`, `.sort()`):** Actions on the list itself.
*   **Dictionaries (`{}`):** Real dictionary/phone book (`key:value`). Keys are unique.
    *   **`.keys()`, `.values()`, `.items()`:** Get parts of the dict.
    *   **`.get(key, default)`:** Safe way to get a value.
    *   **`pprint`:** Makes complex dicts/lists readable.
*   **Structuring Data:** Combine lists and dicts to model real things (e.g., `list_of_employee_dictionaries`).
*   **Strings (`""`):** Text. Immutable.
    *   **Methods (`.upper()`, `.split()`, `.join()`, `.strip()`):** Tools for text; return *new* strings.

---

This should provide a comprehensive yet memorable guide to UNIT-II. Consistent practice with these concepts is key to mastering them!