"""Resume builder.

This module provides functionalities to build and save a resume in HTML format.
"""

from __future__ import annotations

import argparse
from pathlib import Path
from textwrap import dedent
from typing import Optional, Union


class Text:
    """Represents a plain text element in the resume.

    This class represents a plain text element in the resume. It has
    the following attributes:

    - `text` (str): The text content.
    """

    def __init__(self, text: str) -> None:
        """Initialize the text object.

        Args:
            text (str): The text to display

        """
        self.text = text

    def __str__(self) -> str:
        """Dunder string method.

        Returns:
            str: the text

        """
        return self.text


StrLike = Union[str, Text]
"""This type alias represents a union type that can be either a string or a
`Text` object."""

OptionalStrLike = Optional[StrLike]
"""This type alias represents an optional `StrLike` type, which can be either
`None` or a `StrLike` value."""


class LinkText(Text):
    """Represents a text element with a hyperlink.

    This class inherits from `Text` and represents a text element
    with a hyperlink. It has the following attributes in addition to those
    inherited from `Text`:

    - `url` (str): The URL of the link.
    - `show_icon` (bool, optional): A flag indicating whether to display an icon
      next to the text (defaults to `False`).
    """

    def __init__(self, text: str, url: str, *, show_icon: bool = False) -> None:
        """Initialize Hyperlink text.

        Args:
            text (str): Plain text
            url (str): Link URL
            show_icon (bool, optional): Show link icon? Defaults to False.
        """
        super().__init__(text)
        self.url = url
        self.show_icon = show_icon

    def __str__(self) -> str:
        """Dunder string method.

        Returns:
            str: returns HTML string with hyperlink
        """
        if not self.show_icon:
            return f'<a target="_blank" href="{self.url}">{self.text}</a>'

        return f'<a target="_blank" class="open-link" href="{self.url}">{self.text}</a>'


class BulletedList(Text):
    """Represents a bulleted list.

    This class inherits from `Text` and represents a bulleted
    list. It has the following attribute:

    - `items` (List[StrLike]): A list of items in the bulleted list.
    """

    def __init__(self, items: list[StrLike]) -> None:
        """Initialize the bulleted list.

        Args:
            items (List[StrLike]): List of strings to display as bulleted list
        """
        self.items = items

    def __str__(self) -> str:
        """Dunder string method.

        Returns:
            str: returns HTML string with bulleted list.
        """
        s = "<ul>\n"
        for item in self.items:
            s += f"<li><p>{item}</p></li>\n"
        s += "</ul>\n"
        return s


class ItalicsText(Text):
    """Represents italicized text.

    This class inherits from `Text` and represents a text
    element rendered in italics.
    """

    def __init__(self, text: str) -> None:
        """Initialize the italicized text.

        Args:
            text (str): The text to display in italics.
        """
        super().__init__(text)

    def __str__(self) -> str:
        """Dunder string method.

        Returns:
            str: returns HTML string with italicized text.
        """
        return f'<p class="des">{self.text}</p>'


class UnderlinedText(Text):
    """Represents underlined text.

    This class inherits from `Text` and represents a text
    element rendered with an underline.
    """

    def __init__(self, text: str) -> None:
        """Initialize the underlined text.

        Args:
            text (str): The text to display with underline.
        """
        super().__init__(text)

    def __str__(self) -> str:
        """Dunder string method.

        Returns:
            str: returns HTML string with underlined text.
        """
        return f'<span class="label">{self.text}</span>'


class BoldText(Text):
    """Represents bold text.

    This class inherits from `Text` and represents a text
    element rendered in bold.
    """

    def __init__(self, text: str) -> None:
        """Initialize the bold text.

        Args:
            text (str): The text to display in bold.
        """
        super().__init__(text)

    def __str__(self) -> str:
        """Dunder string method.

        Returns:
            str: returns HTML string with bold text.
        """
        return f"<strong>{self.text}</strong>"


class ConcatText(Text):
    """Represents concatenated text.

    This class inherits from `Text` and is used to concatenate
    multiple text elements. It takes variable number of arguments of type
    `StrLike`.
    """

    def __init__(self, *args: StrLike) -> None:
        """Initialize the concatenated text.

        Args:
            *args (StrLike): The texts to concatenate.
        """
        self.args = args

    def __str__(self) -> str:
        """Dunder string method.

        Returns:
            str: returns concatenated string.
        """
        return "".join(map(str, self.args))


class SectionEntry:
    """Represents an entry in a resume section.

    This class represents an entry in a resume section. It has
    the following attributes:

    - `title` (OptionalStrLike): The title of the entry, this would be the
      company name.
    - `caption` (OptionalStrLike): A caption for the entry (e.g., job title).
    - `location` (OptionalStrLike): The location of the entry (e.g., Boston, MA).
    - `dates` (OptionalStrLike): The dates associated with the entry (e.g.,
      employment dates).
    - `description` (OptionalStrLike): A description of the entry.
    """

    def __init__(
        self,
        title: OptionalStrLike = None,
        caption: OptionalStrLike = None,
        location: OptionalStrLike = None,
        dates: OptionalStrLike = None,
        description: OptionalStrLike = None,
    ) -> None:
        """Initialize the section entry.

        Args:
            title (OptionalStrLike, optional): The title of the entry. Defaults to None.
            caption (OptionalStrLike, optional): The caption of the entry. Defaults to None.
            location (OptionalStrLike, optional): The location of the entry. Defaults to None.
            dates (OptionalStrLike, optional): The dates of the entry. Defaults to None.
            description (OptionalStrLike, optional): The description of the entry. Defaults to None.
        """  # noqa: E501
        self.title = title
        self.caption = caption
        self.location = location
        self.dates = dates
        self.description = description


class Section:
    """Represents a section in the resume.

    This class represents a section in the resume. It has the
    following attributes:

    - `title` (StrLike): The title of the section.
    - `entries` (List[SectionEntry]): A list of entries in the section.
    """

    def __init__(self, title: StrLike, entries: list[SectionEntry]) -> None:
        """Initialize the section.

        Args:
            title (StrLike): The title of the section.
            entries (list[SectionEntry]): The entries in the section.
        """
        self.title = title
        self.entries = entries


class ContactInfo:
    """Represents the contact information in the resume.

    This class represents the contact information section of the
    resume. It has the following attributes:

    - `name` (StrLike): The name of the person.
    - `details` (Optional[List[StrLike]]): A list of contact details (e.g.,
      email, phone number).
    - `tag_line` (OptionalStrLike): A tagline or objective statement.
    """

    def __init__(
        self,
        name: StrLike,
        details: list[StrLike] | None = None,
        tag_line: OptionalStrLike = None,
    ) -> None:
        """Initialize the contact information.

        Args:
            name (StrLike): The name of the person.
            details (Optional[list[StrLike]], optional): The details of the person. Defaults to None.
            tag_line (OptionalStrLike, optional): The tag line of the person. Defaults to None.
        """  # noqa: E501
        self.name = name
        self.details = details
        self.tag_line = tag_line


class Summary:
    """This class represents an introductory section.

    This class represents an introductory section like a summary,
    objective, research statement, etc. If you would like to omit a summary
    section, simply set `Summary = None`. It has the following attributes:

    - `title` (OptionalStrLike): The title of the summary section.
    - `description` (OptionalStrLike): A description of the entry.
    """

    def __init__(
        self,
        title: OptionalStrLike = None,
        description: OptionalStrLike = None,
    ) -> None:
        """Initialize the summary section.

        Args:
            title (OptionalStrLike, optional): The title of the summary section.
                Defaults to None.
            description (OptionalStrLike, optional): A description of the entry.
                Defaults to None.
        """
        self.title = title
        self.description = description


class Resume:
    """Represents the entire resume document.

    This class represents the entire resume document. It has the
    following attributes:

    - `contact_info` (ContactInfo): The contact information section of the resume.
    - `sections` (List[Section]): A list of sections in the resume.
    - `summary` (Summary | None): The summary section, optional.
    """

    def __init__(
        self,
        contact_info: ContactInfo,
        sections: list[Section],
        summary: Summary | None = None,
    ) -> None:
        """Initialize the resume.

        Args:
            contact_info (ContactInfo): The contact information.
            sections (list[Section]): The sections in the resume.
            summary (Summary | None, optional): The summary section. Defaults to None.
        """
        self.contact_info = contact_info
        self.summary = summary
        self.sections = sections
        self.TEMPLATE = dedent(
            """
        <!DOCTYPE html>
        <html>
        <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width; initial-scale=1.0; maximum-scale=1.0; user-scalable=0;" />
        <title>__NAME__&rsquo;s Resume</title>
        <style>
        html{font-family:sans-serif;-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%}body{margin:0}article,aside,details,figcaption,figure,footer,header,hgroup,main,menu,nav,section,summary{display:block}audio,canvas,progress,video{display:inline-block;vertical-align:baseline}audio:not([controls]){display:none;height:0}[hidden],template{display:none}a{background-color:transparent}a:active,a:hover{outline:0}abbr[title]{border-bottom:1px dotted}b,strong{font-weight:bold}dfn{font-style:italic}h1{font-size:2em;margin:0.67em 0}mark{background:#ff0;color:#000}small{font-size:80%}sub,sup{font-size:75%;line-height:0;position:relative;vertical-align:baseline}sup{top:-0.5em}sub{bottom:-0.25em}img{border:0}svg:not(:root){overflow:hidden}figure{margin:1em 40px}hr{-moz-box-sizing:content-box;box-sizing:content-box;height:0}pre{overflow:auto}code,kbd,pre,samp{font-family:monospace, monospace;font-size:1em}button,input,optgroup,select,textarea{color:inherit;font:inherit;margin:0}button{overflow:visible}button,select{text-transform:none}button,html input[type="button"],input[type="reset"],input[type="submit"]{-webkit-appearance:button;cursor:pointer}button[disabled],html input[disabled]{cursor:default}button::-moz-focus-inner,input::-moz-focus-inner{border:0;padding:0}input{line-height:normal}input[type="checkbox"],input[type="radio"]{box-sizing:border-box;padding:0}input[type="number"]::-webkit-inner-spin-button,input[type="number"]::-webkit-outer-spin-button{height:auto}input[type="search"]{-webkit-appearance:textfield;-moz-box-sizing:content-box;-webkit-box-sizing:content-box;box-sizing:content-box}input[type="search"]::-webkit-search-cancel-button,input[type="search"]::-webkit-search-decoration{-webkit-appearance:none}fieldset{border:1px solid #c0c0c0;margin:0 2px;padding:0.35em 0.625em 0.75em}legend{border:0;padding:0}textarea{overflow:auto}optgroup{font-weight:bold}table{border-collapse:collapse;border-spacing:0}td,th{padding:0}
        </style>
        <style>
        body{font-family:Georgia;font-size:14px;padding:1em;line-height:1.6}.container,footer,header{max-width:72em;margin:auto}a{color:black;text-decoration:none;border-bottom:1px dashed}p{margin-top:0;margin-bottom:0;line-height:1.6em}header{text-align:center;margin-bottom:1em}#name{font-size:2.6em;font-variant:small-caps}#objective{font-style:italic}@media screen and (min-width: 72em){body{padding:2em 4em;line-height:inherit}#name{float:left;text-align:left}#contact,#objective{text-align:right}}.date{float:right;text-align-last:right}@media screen{.print-only{display:none}}header ul{list-style:none;padding:0;margin:0}header li{display:inline-block;line-height:1.5em}header li::after{content:" |"}header li:last-child::after{content:""}footer{text-align:center}h1,h2,h3,h4{font-weight:normal;margin:0}.container .label{border-bottom:1px solid}section{margin:1.25em 0}section:first-child{margin-top:0.25em}h2{font-style:italic;border-bottom:1px solid grey;margin-bottom:0.5em}.container ul{margin-top:0.1em;margin-bottom:0.1em;padding-left:20px}.entry{margin:0.75em 0}h3{display:inline-block;font-weight:bold}.entry .role{}.entry .role::before{content:"("}.entry .role::after{content:")"}.entry .loc{font-style:italic}.entry .des{font-style:italic}p .entry .des{margin-top:0.1em}.resume-objective{}.resume-project .project-name{font-weight:bold;line-height:1.6em}.resume-project h3{}.meta{}.open-link{padding-right:1.2em;background-image:url('data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHg9IjBweCIgeT0iMHB4IiB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZpZXdCb3g9IjAgMCAyNCAyNCI+CjxwYXRoIGQ9Ik0gNSAzIEMgMy45MDY5MzcyIDMgMyAzLjkwNjkzNzIgMyA1IEwgMyAxOSBDIDMgMjAuMDkzMDYzIDMuOTA2OTM3MiAyMSA1IDIxIEwgMTkgMjEgQyAyMC4wOTMwNjMgMjEgMjEgMjAuMDkzMDYzIDIxIDE5IEwgMjEgMTIgTCAxOSAxMiBMIDE5IDE5IEwgNSAxOSBMIDUgNSBMIDEyIDUgTCAxMiAzIEwgNSAzIHogTSAxNCAzIEwgMTQgNSBMIDE3LjU4NTkzOCA1IEwgOC4yOTI5Njg4IDE0LjI5Mjk2OSBMIDkuNzA3MDMxMiAxNS43MDcwMzEgTCAxOSA2LjQxNDA2MjUgTCAxOSAxMCBMIDIxIDEwIEwgMjEgMyBMIDE0IDMgeiI+PC9wYXRoPgo8L3N2Zz4=');background-repeat:no-repeat;background-size:1em 1em;background-position:right center}.open-link::after{font-size:0.8em}
        </style>
        <style media="print">
        body{padding:0;margin:0;font-size:13px;line-height:inherit}a{text-decoration:none;border-bottom:none}.no-print{display:none}#name{float:left;text-align:left}#contact,#objective{text-align:right}
        </style>
        </head>
        <body>
        <header>
        __CONTACT_INFO__
        </header>
        <div class="container">
        __SUMMARY__
        </div>
        <div class="container">
        __SECTIONS__
        </div>
        </body>
        </html>
        """,  # noqa: E501
        )

    def render_contact_info(self) -> str:
        """Renders the contact information section of the resume in HTML format.

        Returns:
            str: returns HTML string with contact information.
        """
        contact_info = f'<h1 id="name">{self.contact_info.name}</h1>\n'

        if self.contact_info.details:
            contact_info += '<ul id="contact">\n'
            for detail in self.contact_info.details:
                contact_info += f"<li>{detail}</li>\n"
            contact_info += "</ul>\n"
        if self.contact_info.tag_line:
            contact_info += f'<p id="objective">{self.contact_info.tag_line}</p>\n'
        else:
            contact_info += "<br>\n"
        return contact_info

    def render_summary(self) -> str:
        """Renders the summary section.

        Returns:
            str: returns HTML string with summary section.
        """
        if not self.summary:
            return ""

        summary_html = "<div class='container'>\n"
        summary_html += "<section>\n"
        summary_html += f"<h2>{self.summary.title}</h2>\n"
        summary_html += '<div class="entry">\n'
        summary_html += f"<p>\n{self.summary.description}</p>\n"
        summary_html += "</div>"
        summary_html += "</section>\n"
        summary_html += "</div>\n"

        return summary_html

    def render_section(self, section: Section) -> str:
        """Renders a single section of the resume in HTML format.

        Args:
            section (Section): The section to render.

        Returns:
            str: returns HTML string with section.
        """
        section_html = "<div class='container'>\n"
        section_html += "<section>\n"
        if section.title:
            section_html += f"<h2>{section.title}</h2>\n"
        for entry in section.entries:
            section_html += '<div class="entry">\n'
            if entry.title:
                section_html += f"<h3>{entry.title}</h3>\n"
            if entry.caption:
                section_html += f'<span class="role">{entry.caption}</span>\n'
            if entry.location:
                section_html += f'<span class="loc">{entry.location}</span>\n'
            if entry.dates:
                section_html += f'<span class="date">{entry.dates}</span>\n'
            if entry.description:
                section_html += f"<p>\n{entry.description}</p>\n"
            section_html += "</div>\n"
        section_html += "</section>\n"
        section_html += "</div>\n"
        return section_html

    def render_sections(self) -> str:
        """Renders all sections of the resume in HTML format.

        Returns:
            str: returns HTML string with all sections.
        """
        sections_html = ""
        for section in self.sections:
            sections_html += self.render_section(section)
        return sections_html

    def render(self) -> str:
        """Renders the entire resume in HTML format.

        Returns:
            str: returns HTML string with entire resume.
        """
        s = self.TEMPLATE.replace("__NAME__", str(self.contact_info.name))
        s = s.replace("__CONTACT_INFO__", self.render_contact_info())
        return s.replace("__SECTIONS__", self.render_sections())

    def save(self, filename: str | None = None) -> None:
        """Saves the rendered HTML content of the resume to a file.

        Args:
            filename (str | None, optional): The name of generated resume file.
                Defaults to `NAME_resume.html`.
        """
        if filename is None:
            filename = f"{self.contact_info.name}_resume.html"
        with Path(filename).open("w") as f:
            f.write(self.render())

    def cli_main(self) -> None:
        """Serves as the entry point for the command-line interface (CLI) functionality.

        Parses command line arguments for the output file name & calls the
        `save` method to save the resume to the file.
        """
        parser = argparse.ArgumentParser(description="ResumeBuilder")
        parser.add_argument(
            "-o",
            "--output",
            type=str,
            dest="output_file",
            required=False,
            help="Output HTML file name.",
            default=f"{self.contact_info.name}_resume.html",
        )
        args = parser.parse_args()
        self.save(args.output_file)
