## resume_builder.py

This module provides functionalities to build and save a resume in HTML format.

### Classes

* **Text:** This class represents a plain text element in the resume. It has the following attributes:
    * `text` (str): The text content.

* **StrLike:** This type alias represents a union type that can be either a string or a `Text` object.

* **OptionalStrLike:** This type alias represents an optional `StrLike` type, which can be either `None` or a `StrLike` value.

* **LinkText:** This class inherits from `Text` and represents a text element with a hyperlink. It has the following attributes in addition to those inherited from `Text`:
    * `url` (str): The URL of the link.
    * `show_icon` (bool, optional): A flag indicating whether to display an icon next to the text (defaults to `False`).

* **BulletedList:** This class inherits from `Text` and represents a bulleted list. It has the following attribute:
    * `items` (List[StrLike]): A list of items in the bulleted list.

* **ItalicsText:** This class inherits from `Text` and represents a text element rendered in italics.

* **UnderlinedText:** This class inherits from `Text` and represents a text element rendered with an underline.

* **BoldText:** This class inherits from `Text` and represents a text element rendered in bold.

* **ConcatText:** This class inherits from `Text` and is used to concatenate multiple text elements. It takes variable number of arguments of type `StrLike`.

* **SectionEntry:** This class represents an entry in a resume section. It has the following attributes:
    * `title` (OptionalStrLike): The title of the entry, this would be the company name.
    * `caption` (OptionalStrLike): A caption for the entry (e.g., job title).
    * `location` (OptionalStrLike): The location of the entry (e.g., Boston, MA).
    * `dates` (OptionalStrLike): The dates associated with the entry (e.g., employment dates).
    * `description` (OptionalStrLike): A description of the entry.

* **Section:** This class represents a section in the resume. It has the following attributes:
    * `title` (StrLike): The title of the section.
    * `entries` (List[SectionEntry]): A list of entries in the section.

* **ContactInfo:** This class represents the contact information section of the resume. It has the following attributes:
    * `name` (StrLike): The name of the person.
    * `details` (Optional[List[StrLike]]): A list of contact details (e.g., email, phone number).
    * `tag_line` (OptionalStrLike): A tagline or objective statement.

* **Resume:** This class represents the entire resume document. It has the following attributes:
    * `contact_info` (ContactInfo): The contact information section of the resume.
    * `sections` (List[Section]): A list of sections in the resume.

### Methods

* **render_contact_info(self) -> str:** This method renders the contact information section of the resume in HTML format.

* **render_section(self, section: Section) -> str:** This method renders a single section of the resume in HTML format.

* **render_sections(self) -> str:** This method renders all sections of the resume in HTML format.

* **render(self) -> str:** This method renders the entire resume in HTML format.

* **save(self, filename: str) -> None:** This method saves the rendered HTML content of the resume to a file.

* **cli_main(self):** This method serves as the entry point for the command-line interface (CLI) functionality. It parses command-line arguments for the output filename and calls the `save` method to generate the HTML file.


This module provides a way to structure and format the content of a resume in an easy-to-use way. By creating instances of the provided classes and organizing them into sections and contact information, you can generate an HTML resume that can be saved to a file.