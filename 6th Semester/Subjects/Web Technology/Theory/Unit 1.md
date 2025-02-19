Okay, here are detailed notes on the topics outlined in your UNIT-I syllabus, covering HTML, CSS, XML/XHTML, with examples.

**UNIT I: HTML, CSS, XML/XHTML**

**I. HTML (HyperText Markup Language)**

*   **Definition:** The standard markup language for creating web pages.  It describes the structure of a webpage. HTML elements tell the browser how to display the content.

*   **Basic Syntax:**
    *   HTML is based on *tags*.  Tags usually come in pairs: an opening tag `<tag>` and a closing tag `</tag>`.
    *   Tags enclose the content they describe.
    *   Tags can have *attributes* that provide additional information about the element.
    *   HTML is case-insensitive (e.g., `<p>` is the same as `<P>`), but lowercase is generally preferred for consistency and best practice.
    *   White space (spaces, tabs, newlines) is generally ignored by browsers, except within the `<pre>` tag.

*   **Standard HTML Document Structure:**
    ```html
    <!DOCTYPE html>  <!-- Declares the document type as HTML5 -->
    <html lang="en">   <!-- The root element of the page -->
    <head>
        <meta charset="UTF-8"> <!-- Character set for encoding -->
        <meta name="viewport" content="width=device-width, initial-scale=1.0"> <!-- For responsive design -->
        <title>Page Title</title> <!-- Title displayed in the browser tab/window -->
    </head>
    <body>
        <!-- Content of the page goes here -->
        <h1>My First Heading</h1>
        <p>My first paragraph.</p>
    </body>
    </html>
    ```

    *   `<!DOCTYPE html>`:  This declaration defines the document to be HTML5. It is always the first thing in the HTML.
    *   `<html>`:  The root element of an HTML page.  The `lang` attribute specifies the language of the document (e.g., "en" for English).
    *   `<head>`: Contains metadata about the HTML document, such as the title, character set, styles, and links to external resources.  This content is not displayed on the page itself.
    *   `<meta>`:  Provides metadata.
        *   `charset`: Defines the character encoding for the document.  `UTF-8` is the standard and supports most characters.
        *   `name="viewport"`: Configures the viewport for responsive design, making the page adapt to different screen sizes.
    *   `<title>`: Specifies a title for the HTML page (which is shown in the browser's title bar or tab).
    *   `<body>`:  Contains the visible page content: text, images, links, etc.

*   **Basic Text Markup:**
    *   `<h1>` to `<h6>`:  Headings (level 1 to level 6).  `<h1>` is the most important.
    *   `<p>`:  Paragraph.  Used to group blocks of text.
    *   `<br>`:  Line break. Inserts a single line break. It is an empty element (no closing tag needed).
    *   `<hr>`:  Horizontal rule.  Creates a horizontal line.  Also an empty element.
    *   `<b>`:  Bold text (use `<strong>` for semantic importance).
    *   `<strong>`:  Important text (usually displayed in bold).
    *   `<i>`:  Italic text (use `<em>` for semantic emphasis).
    *   `<em>`:  Emphasized text (usually displayed in italics).
    *   `<pre>`:  Preformatted text.  Displays text exactly as it's written, including whitespace (useful for code).
    *   `<code>`:  Displays a fragment of computer code.
    *   `<small>`: Makes the text one font size smaller.

    ```html
    <p>This is a <b>bold</b> word and an <i>italicized</i> word.</p>
    <pre>
        This is
        preformatted
        text.
    </pre>
    ```

*   **HTML Styles:**
    *   The `style` attribute can be used to add styles to an element, such as color, font, size, and more. (It is better to use CSS for styling)

    ```html
    <p style="color: blue; font-size: 16px;">This text will be blue and 16 pixels.</p>
    ```

*   **Elements:**
    *   HTML elements are the building blocks of HTML pages.  They are defined by a start tag, some content, and an end tag.
    *   Some elements are *empty* (or void) elements, meaning they only have a start tag and no content or end tag (e.g., `<br>`, `<hr>`, `<img>`).

*   **Attributes:**
    *   Attributes provide additional information about HTML elements.
    *   Attributes are always specified in the start tag.
    *   Attributes usually come in name="value" pairs.

    ```html
    <a href="https://www.example.com" title="Visit Example">Example Link</a>
    ```
    *   `href`: Attribute of `<a>` tag, specifies the URL.
    *   `title`: Attribute of `<a>` tag, specifies extra information.
    *   `src`: Attribute of `<img>` tag, specifies the path to image.
    *   `alt`: Attribute of `<img>` tag, specifies alternative text.
    *   `class`: Assigns a class name to the element, used for CSS styling and JavaScript manipulation.
    *   `id`: Assigns a unique ID to the element, used for CSS styling and JavaScript manipulation.

*   **Headings:**
    *   `<h1>` to `<h6>` elements represent headings of different levels.
    *   `<h1>` is the most important and should generally be used for the main title of the page.
    *   `<h2>` to `<h6>` are used for subheadings.

*   **Layouts:**
    *   HTML layout elements are used to structure the content of a web page.
    *   `<div>`:  Defines a division or section in an HTML document.  Used as a container for other HTML elements and is often styled with CSS.
    *   `<header>`: Specifies a header for a document or section.
    *   `<nav>`: Defines a set of navigation links.
    *   `<article>`: Defines an independent, self-contained article.
    *   `<aside>`: Defines content aside from the page content (e.g., a sidebar).
    *   `<footer>`:  Specifies a footer for a document or section.
    *   `<section>`: Defines a section in a document.

*   **Iframes:**
    *   `<iframe>`:  Defines an inline frame, which is used to embed another HTML document within the current HTML document.

    ```html
    <iframe src="https://www.example.com" height="200" width="300" title="Example Website"></iframe>
    ```
    *   `src`: The URL of the page to embed.
    *   `height`, `width`: Dimensions of the iframe.
    *   `title`:  Provides a title for the iframe, important for accessibility.

*   **Images:**
    *   `<img>`:  Embeds an image in the HTML document.  It's an empty element.

    ```html
    <img src="images/myimage.jpg" alt="Description of the image" width="500" height="300">
    ```
    *   `src`:  The URL of the image.
    *   `alt`:  Alternative text to display if the image cannot be loaded.  Crucial for accessibility and SEO.
    *   `width`, `height`:  Specify the dimensions of the image.  It's best practice to define these to avoid layout shifts.

*   **Hypertext Links:**
    *   `<a>`:  Defines a hyperlink, which is used to link to another document or resource.

    ```html
    <a href="https://www.example.com">Visit Example</a>
    <a href="mailto:info@example.com">Email Us</a>
    <a href="my_document.pdf">Download PDF</a>
    ```
    *   `href`:  The URL of the linked resource.  Can be a URL, an email address (using `mailto:`), or a file path.
    *   `target`: Specifies where to open the linked document.  `_blank` opens it in a new tab/window.

*   **Lists:**
    *   `<ul>`:  Unordered list (bulleted list).
    *   `<ol>`:  Ordered list (numbered list).
    *   `<li>`:  List item (used within `<ul>` and `<ol>`).
    *   `<dl>`:  Definition list.
    *   `<dt>`:  Definition term.
    *   `<dd>`:  Definition description.

    ```html
    <ul>
        <li>Item 1</li>
        <li>Item 2</li>
    </ul>

    <ol>
        <li>First step</li>
        <li>Second step</li>
    </ol>

    <dl>
        <dt>Coffee</dt>
        <dd>Black hot drink</dd>
    </dl>
    ```

*   **Tables:**
    *   `<table>`:  Defines a table.
    *   `<tr>`:  Table row.
    *   `<th>`:  Table heading (usually bold and centered).
    *   `<td>`:  Table data cell.
    *   `<caption>`: Table caption.
    *   `<thead>`: Defines a set of rows defining the head of the columns of the table.
    *   `<tbody>`: Defines a set of rows defining the actual table data.
    *   `<tfoot>`: Defines a set of rows defining the foot of the columns of the table.

    ```html
    <table>
        <caption>My Table</caption>
        <thead>
            <tr>
                <th>Header 1</th>
                <th>Header 2</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>Data 1</td>
                <td>Data 2</td>
            </tr>
            <tr>
                <td>Data 3</td>
                <td>Data 4</td>
            </tr>
        </tbody>
    </table>
    ```

*   **Forms:**
    *   `<form>`:  Defines an HTML form used to collect user input.
    *   `<input>`:  Defines an input field where users can enter data.  `type` attribute specifies the type of input (e.g., text, password, email, radio, checkbox, submit).
    *   `<textarea>`:  Defines a multiline text input area.
    *   `<select>`:  Defines a dropdown list.
    *   `<option>`:  Defines an option in a dropdown list.
    *   `<label>`:  Defines a label for an input element (improves accessibility).
    *   `<button>`:  Defines a clickable button.

    ```html
    <form action="/submit" method="post">
        <label for="name">Name:</label><br>
        <input type="text" id="name" name="name"><br><br>

        <label for="email">Email:</label><br>
        <input type="email" id="email" name="email"><br><br>

        <label for="message">Message:</label><br>
        <textarea id="message" name="message" rows="4" cols="50"></textarea><br><br>

        <input type="submit" value="Submit">
    </form>
    ```
    *   `action`:  Specifies the URL where the form data is sent when the form is submitted.
    *   `method`:  Specifies the HTTP method used to submit the form data (usually `get` or `post`).
    *   `name`:  Specifies a name for the input element, used to identify the data when it's submitted.
    *   `id`:  Used to associate the label with the input field.

*   **Dynamic HTML (DHTML):**
    *   A combination of HTML, CSS, and JavaScript used to create interactive and dynamic web pages.
    *   Allows you to modify the HTML structure, CSS styles, and content of a page in response to user actions (e.g., mouse clicks, form submissions) or other events.
    *   JavaScript is used to manipulate the HTML Document Object Model (DOM).
    *   Example: Changing the text of an element when a button is clicked.

**II. CSS (Cascading Style Sheets)**

*   **Need for CSS:**
    *   Separates content (HTML) from presentation (styling).
    *   Provides a consistent look and feel across multiple web pages.
    *   Simplifies website maintenance.  Changes to CSS are reflected across all linked pages.
    *   Improves accessibility and search engine optimization (SEO).
    *   Enables responsive design, adapting webpages to different screen sizes and devices.

*   **Introduction to CSS:**
    *   A language used to describe the style of an HTML document.
    *   Defines how HTML elements should be displayed (e.g., color, font, size, layout).

*   **Basic Syntax and Structure:**
    ```css
    selector {
        property: value;
        property: value;
        /* more declarations */
    }
    ```
    *   **Selector:**  Specifies the HTML element(s) to style (e.g., `p`, `h1`, `.my-class`, `#my-id`).
    *   **Property:**  The style attribute you want to change (e.g., `color`, `font-size`, `margin`).
    *   **Value:**  The value you assign to the property (e.g., `blue`, `16px`, `10px`).
    *   **Declaration:** A property and value pair.
    *   **Declaration Block:** The set of declarations enclosed in curly braces `{}`.
    *   **Comment:** Start with `/*` and end with `*/`.

*   **Using CSS:**
    *   **Inline CSS:**  Styles are applied directly to an HTML element using the `style` attribute.  (Not recommended for large projects).
        ```html
        <p style="color: red;">This is a red paragraph.</p>
        ```
    *   **Internal (Embedded) CSS:**  Styles are defined within the `<style>` tag inside the `<head>` section of the HTML document.  Good for single-page websites.
        ```html
        <!DOCTYPE html>
        <html>
        <head>
            <style>
                p {
                    color: green;
                }
            </style>
        </head>
        <body>
            <p>This is a green paragraph.</p>
        </body>
        </html>
        ```
    *   **External CSS:**  Styles are defined in a separate `.css` file and linked to the HTML document using the `<link>` tag.  The best practice for most projects.
        ```html
        <!DOCTYPE html>
        <html>
        <head>
            <link rel="stylesheet" href="style.css">
        </head>
        <body>
            <p>This paragraph uses styles from style.css.</p>
        </body>
        </html>
        ```
        In `style.css`:
        ```css
        p {
            color: blue;
        }
        ```
        *   `rel="stylesheet"`: Specifies the relationship between the linked file and the HTML document (it's a stylesheet).
        *   `href="style.css"`:  The path to the CSS file.

*   **CSS Selectors:**
    *   **Element Selector:** Selects all HTML elements of a specific type.  Example: `p`, `h1`, `div`.
    *   **ID Selector:**  Selects the element with a matching `id` attribute.  Example: `#my-paragraph`. ID selectors are unique identifiers.
    *   **Class Selector:**  Selects all elements with a matching `class` attribute.  Example: `.my-class`. Class selectors are for grouping elements with the same style.
    *   **Universal Selector:**  Selects all elements on the page.  Example: `*`.
    *   **Attribute Selector:**  Selects elements based on the presence or value of an attribute.  Example: `a[href]`, `input[type="text"]`.
    *   **Pseudo-classes:**  Selects elements based on their state (e.g., hover, active, visited).  Example: `a:hover`, `button:active`.
    *   **Pseudo-elements:**  Selects a specific part of an element. Example: `p::first-line`, `p::before`, `p::after`.
    *   **Combinators:**  Used to combine selectors in more complex ways.
        *   **Descendant selector (space):** Selects all elements that are descendants of a specified element. Example: `div p` (selects all `<p>` elements inside `<div>` elements).
        *   **Child selector (>):** Selects all elements that are direct children of a specified element. Example: `div > p` (selects all `<p>` elements that are direct children of `<div>` elements).
        *   **Adjacent sibling selector (+):** Selects the element that is immediately preceded by a specified element. Example: `h1 + p` (selects the `<p>` element that immediately follows an `<h1>` element).
        *   **General sibling selector (~):** Selects all elements that are preceded by a specified element. Example: `h1 ~ p` (selects all `<p>` elements that are preceded by an `<h1>` element).

*   **Background Images, Colors, and Properties:**
    *   `background-color`:  Sets the background color of an element.
    *   `background-image`:  Sets an image as the background of an element.
    *   `background-repeat`:  Specifies how the background image is repeated (e.g., `repeat`, `no-repeat`, `repeat-x`, `repeat-y`).
    *   `background-position`: Specifies the starting position of a background image.
    *   `background-size`: Specifies the size of the background images
    *   `background-attachment`: Specifies whether the background image scrolls with the page or is fixed.
    *   `background`:  Shorthand property for setting multiple background properties at once.

    ```css
    body {
        background-color: #f0f0f0;
        background-image: url("images/background.jpg");
        background-repeat: no-repeat;
        background-position: center top;
        background-size: cover;
        background-attachment: fixed;
    }
    ```

*   **Manipulating Texts:**
    *   `color`:  Sets the color of the text.
    *   `text-align`:  Sets the horizontal alignment of the text (e.g., `left`, `center`, `right`, `justify`).
    *   `text-decoration`:  Specifies decorations added to text (e.g., `underline`, `overline`, `line-through`, `none`).
    *   `text-transform`:  Capitalizes, lowercases, or uppercases text (e.g., `uppercase`, `lowercase`, `capitalize`).
    *   `text-indent`: Specifies the indentation of the first line of text in a block.
    *   `letter-spacing`: Increases or decreases the space between characters in a text.
    *   `word-spacing`: Increases or decreases the space between words in a text.
    *   `line-height`: Sets the line height.

    ```css
    p {
        color: #333;
        text-align: justify;
        text-decoration: none;
        text-transform: lowercase;
        text-indent: 20px;
    }
    ```

*   **Using Fonts:**
    *   `font-family`:  Specifies the font family to use (e.g., "Arial", "Helvetica", "Times New Roman"). Use a font stack for fallback.
    *   `font-size`:  Sets the size of the font.
    *   `font-weight`:  Sets the weight (boldness) of the font (e.g., `normal`, `bold`, `lighter`, `bolder`, numeric values like `100`, `400`, `700`).
    *   `font-style`:  Sets the style of the font (e.g., `normal`, `italic`, `oblique`).
    *   `font-variant`: Specifies whether or not the text should be displayed in a small-caps font.
    *   `font`:  Shorthand property for setting multiple font properties at once.
    ```css
    p {
        font-family: "Arial", sans-serif;
        font-size: 14px;
        font-weight: bold;
        font-style: italic;
    }
    ```

*   **Borders:**
    *   `border-width`:  Sets the width of the border.
    *   `border-style`:  Sets the style of the border (e.g., `solid`, `dashed`, `dotted`, `double`).
    *   `border-color`:  Sets the color of the border.
    *   `border-top`, `border-right`, `border-bottom`, `border-left`:  Set the border on specific sides.
    *   `border-radius`:  Rounds the corners of the border.
    *   `border`:  Shorthand property for setting multiple border properties at once.

    ```css
    div {
        border: 2px solid black;
        border-radius: 10px;
    }
    ```

*   **Boxes:**
    *   CSS box model defines how elements are rendered on the page as rectangular boxes.
    *   Each element can be thought of as a box with content, padding, border, and margin.
    *   `width`:  Sets the width of the content area.
    *   `height`:  Sets the height of the content area.
    *   `box-sizing`:  Specifies how the width and height of an element are calculated (e.g., `content-box`, `border-box`).
        *   `content-box`: The default value. The width and height properties (and min/max properties) apply only to the content of the element.
        *   `border-box`: The width and height properties include the content, padding, and border, but do not include the margin.

*   **Margins:**
    *   The space outside the border.
    *   `margin-top`, `margin-right`, `margin-bottom`, `margin-left`:  Set the margin on specific sides.
    *   `margin`:  Shorthand property for setting all margins at once (top, right, bottom, left).  Can use 1-4 values.
    *   `margin: auto;`  Centers the element horizontally (if the element has a defined width).

    ```css
    div {
        margin: 10px 20px 30px 40px; /* top right bottom left */
    }
    ```

*   **Padding:**
    *   The space between the content and the border.
    *   `padding-top`, `padding-right`, `padding-bottom`, `padding-left`:  Set the padding on specific sides.
    *   `padding`:  Shorthand property for setting all padding at once (top, right, bottom, left).  Can use 1-4 values.

    ```css
    div {
        padding: 10px; /* all sides */
    }
    ```

*   **Lists:**
    *   `list-style-type`:  Specifies the type of list marker (e.g., `disc`, `circle`, `square`, `decimal`, `lower-alpha`, `upper-roman`, `none`).
    *   `list-style-position`:  Specifies the position of the list marker (e.g., `inside`, `outside`).
    *   `list-style-image`:  Specifies an image as the list marker.
    *   `list-style`:  Shorthand property for setting multiple list properties at once.

    ```css
    ul {
        list-style-type: square;
        list-style-position: outside;
    }
    ```

*   **Positioning Using CSS:**
    *   `position`: Specifies the positioning method used for an element.
    *   `static`:  The default value.  Elements are positioned in the normal flow of the document.
    *   `relative`:  Elements are positioned relative to their normal position.  You can use `top`, `right`, `bottom`, and `left` to offset the element.
    *   `absolute`:  Elements are positioned relative to their nearest positioned ancestor (an ancestor with `position` set to something other than `static`).  If no positioned ancestor is found, it's positioned relative to the `<html>` element.
    *   `fixed`:  Elements are positioned relative to the viewport (the browser window).  They stay in the same place even when the page is scrolled.
    *   `sticky`: Elements are positioned based on the user's scroll position.
    *   `top`, `right`, `bottom`, `left`:  Used to specify the offset of the element from its normal position or from the edges of its containing block.
    *   `z-index`:  Specifies the stack order of an element (which element is in front of another).

    ```css
    div {
        position: relative;
        top: 20px;
        left: 30px;
    }
    ```

*   **CSS2:**
    *   An older version of CSS, but still widely supported. Introduces a lot of features.

*   **The Box Model:**
    *   As described earlier, the CSS box model consists of:
        *   **Content:**  The actual content of the element (text, images, etc.).
        *   **Padding:**  The space around the content, inside the border.
        *   **Border:**  The border around the padding and content.
        *   **Margin:**  The space outside the border, separating the element from other elements.

**III. Working with XML (Extensible Markup Language)**

*   **Definition:** A markup language designed to store and transport data.  It is *extensible* because you can define your own tags. It does not do anything on its own but acts as a means of data transportation.

*   **Key Features:**
    *   **Self-describing:**  Tags describe the data they contain.
    *   **Hierarchical:**  Data is organized in a tree-like structure.
    *   **Platform-independent:**  XML data can be exchanged between different systems.
    *   **Human-readable:**  XML is generally easy to read and understand.

*   **Basic Syntax:**
    *   XML documents have a single root element.
    *   Tags must be properly nested.
    *   Tags are case-sensitive.
    *   All attributes must be quoted.
    *   Empty elements can be represented with a single tag (e.g., `<empty />`).

    ```xml
    <?xml version="1.0" encoding="UTF-8"?>
    <bookstore>
        <book category="cooking">
            <title lang="en">Everyday Italian</title>
            <author>Giada De Laurentiis</author>
            <year>2005</year>
            <price>30.00</price>
        </book>
        <book category="children">
            <title lang="en">Harry Potter</title>
            <author>J.K. Rowling</author>
            <year>2005</year>
            <price>29.99</price>
        </book>
    </bookstore>
    ```

    *   `<?xml version="1.0" encoding="UTF-8"?>`:  The XML declaration, specifying the XML version and character encoding.

*   **Document Type Definition (DTD):**
    *   A DTD defines the structure of an XML document, specifying the elements, attributes, and their relationships.
    *   It's used to validate that an XML document conforms to a specific structure.

    ```xml
    <!DOCTYPE bookstore [
        <!ELEMENT bookstore (book*)>
        <!ELEMENT book (title,author,year,price)>
        <!ATTLIST book category CDATA #REQUIRED>
        <!ELEMENT title (#PCDATA)>
        <!ATTLIST title lang CDATA #IMPLIED>
        <!ELEMENT author (#PCDATA)>
        <!ELEMENT year (#PCDATA)>
        <!ELEMENT price (#PCDATA)>
    ]>
    ```
    *   `<!DOCTYPE>`: Defines the root element and points to the DTD file (can be internal or external).
    *   `<!ELEMENT>`: Defines an element and its allowed child elements.
    *   `<!ATTLIST>`: Defines the attributes of an element.
    *   `#PCDATA`: Parsed character data (text).
    *   `#REQUIRED`:  The attribute is required.
    *   `#IMPLIED`: The attribute is optional.

*   **XML Schemas (XSD):**
    *   A more powerful alternative to DTDs for defining the structure of XML documents.
    *   Uses XML syntax itself.
    *   Supports data types (e.g., string, integer, date).
    *   Provides more robust validation capabilities.

    ```xml
    <?xml version="1.0"?>
    <xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">
        <xs:element name="bookstore">
            <xs:complexType>
                <xs:sequence>
                    <xs:element name="book" maxOccurs="unbounded">
                        <xs:complexType>
                            <xs:sequence>
                                <xs:element name="title" type="xs:string"/>
                                <xs:element name="author" type="xs:string"/>
                                <xs:element name="year" type="xs:gYear"/>
                                <xs:element name="price" type="xs:decimal"/>
                            </xs:sequence>
                            <xs:attribute name="category" type="xs:string" use="required"/>
                        </xs:complexType>
                    </xs:element>
                </xs:sequence>
            </xs:complexType>
        </xs:element>
    </xs:schema>
    ```

    *   `xs:schema`:  The root element of the schema.
    *   `xs:element`: Defines an element.
    *   `xs:complexType`: Defines a complex type (an element with attributes or child elements).
    *   `xs:sequence`:  Specifies that the child elements must appear in a specific order.
    *   `xs:attribute`:  Defines an attribute.
    *   `type`: Specifies the data type of the element or attribute.
    *   `use="required"`:  Indicates that the attribute is required.

*   **Document Object Model (DOM):**
    *   A platform- and language-neutral interface that allows programs and scripts to dynamically access and update the content, structure, and style of documents.
    *   Represents the XML document as a tree structure.
    *   Allows you to navigate the tree and manipulate the nodes (elements, attributes, text, etc.).

*   **Parsers:**
    *   Software components that read and process XML documents.

    *   **DOM Parser:**
        *   Loads the entire XML document into memory and creates a tree representation (the DOM).
        *   Allows random access to any part of the document.
        *   Memory-intensive, especially for large documents.
        *   Good for manipulating the document structure.

    *   **SAX (Simple API for XML) Parser:**
        *   Event-driven parser.
        *   Reads the XML document sequentially, reporting events (e.g., start tag, end tag, text) to the application.
        *   Less memory-intensive than DOM, as it doesn't load the entire document into memory.
        *   Good for processing very large documents or when you only need to extract specific information.
        *   Does not allow easy modification of the document.

**IV. Introduction to XHTML (Extensible HyperText Markup Language)**

*   **Definition:** A stricter version of HTML that conforms to XML rules.  It's essentially HTML rewritten as XML.

*   **Key Differences from HTML:**
    *   **Well-formed documents:** XHTML documents must be well-formed XML (single root element, properly nested tags, etc.).
    *   **Tags and attributes must be lowercase:**  XHTML is case-sensitive.
    *   **All tags must be closed:**  Empty elements must be closed (e.g., `<br />`, `<img src="image.jpg" alt="My Image" />`).
    *   **Attribute values must be quoted:**  All attribute values must be enclosed in quotes.
    *   **Attribute minimization is forbidden:** You cannot write `<input checked>` you must write `<input checked="checked" />`
    *   **The `id` attribute replaces the `name` attribute:** XHTML favours the use of `id` over `name` attributes, although `name` may still be required in specific cases (e.g. when working with forms).

*   **Why Use XHTML?**
    *   More consistent and predictable rendering across different browsers.
    *   Easier to process and manipulate with XML tools.
    *   Forces good coding practices.
    *   Future-proofs your code.  As web technologies evolve, XHTML's strict standards make it more likely to remain compatible.

*   **Meta Tags:**
    *   Used in the `<head>` section of an HTML or XHTML document to provide metadata about the page.
    *   Examples: character set, description, keywords, author.
    *   Help search engines index the page correctly.

    ```html
    <meta charset="UTF-8">
    <meta name="description" content="Description of the web page.">
    <meta name="keywords" content="keywords, related, to, the, page">
    <meta name="author" content="Your Name">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    ```
    *   `name`:  Specifies the type of metadata.
    *   `content`:  Specifies the value of the metadata.

*   **Character Entities:**
    *   Used to represent characters that cannot be easily typed or that have special meaning in HTML/XHTML (e.g., `<`, `>`, `&`, non-breaking space).
    *   Begin with an ampersand (`&`) and end with a semicolon (`;`).
    *   Examples:
        *   `&lt;`:  Less than (<)
        *   `&gt;`:  Greater than (>)
        *   `&amp;`:  Ampersand (&)
        *   `&quot;`:  Double quote (")
        *   `&apos;`:  Single quote (')
        *   `&nbsp;`:  Non-breaking space

    ```html
    <p> 1 &lt; 5 </p>
    ```

*   **Frames and Frame Sets:**
    *   Frames were a way to divide the browser window into multiple independent regions, each displaying a different HTML document.
    *   **Deprecated:** Frames are largely considered outdated and are not recommended for modern web development. They have accessibility issues, SEO problems, and can make navigation confusing.
    *   **Use `<iframe>` for embedding content or consider modern layout techniques (CSS Grid, Flexbox) instead.**
    *   `frameset` tag was used to define the structure of the frames.
    *   `frame` tag was used to define the content of each frame.

    ```html
    <!DOCTYPE html>
    <html>
    <head>
        <title>Frame Example</title>
    </head>
    <frames