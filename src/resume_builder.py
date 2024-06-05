import argparse
from textwrap import dedent
from typing import List, Optional, Union



class Text:
    def __init__(self, text: str) -> None:
        self.text = text

    def __str__(self) -> str:
        return self.text


StrLike = Union[str, Text]
OptionalStrLike = Optional[StrLike]


class LinkText(Text):
    def __init__(self, text: str, url: str, show_icon: bool = False) -> None:
        super().__init__(text)
        self.url = url
        self.show_icon = show_icon

    def __str__(self) -> str:
        if not self.show_icon:
            return f'<a target="_blank" href="{self.url}">{self.text}</a>'
        else:
            return f'<a target="_blank" class="open-link" href="{self.url}">{self.text}</a>'


class BulletedList(Text):
    def __init__(self, items: List[StrLike]) -> None:
        self.items = items

    def __str__(self) -> str:
        s = "<ul>\n"
        for item in self.items:
            s += f"<li><p>{item}</p></li>\n"
        s += "</ul>\n"
        return s


class ItalicsText(Text):
    def __init__(self, text: str) -> None:
        super().__init__(text)

    def __str__(self) -> str:
        return f"<i>{self.text}</i>"


class UnderlinedText(Text):
    def __init__(self, text: str) -> None:
        super().__init__(text)

    def __str__(self) -> str:
        return f'<span class="label">{self.text}</span>'


class BoldText(Text):
    def __init__(self, text: str) -> None:
        super().__init__(text)

    def __str__(self) -> str:
        return f"<strong>{self.text}</strong>"


class ConcatText(Text):
    def __init__(self, *args: StrLike) -> None:
        self.args = args

    def __str__(self) -> str:
        return "".join(map(str, self.args))


class SectionEntry:
    def __init__(
        self,
        title: OptionalStrLike = None,
        caption: OptionalStrLike = None,
        location: OptionalStrLike = None,
        dates: OptionalStrLike = None,
        description: OptionalStrLike = None,
    ) -> None:
        self.title = title
        self.caption = caption
        self.location = location
        self.dates = dates
        self.description = description


class Section:
    def __init__(self, title: StrLike, entries: List[SectionEntry]) -> None:
        self.title = title
        self.entries = entries


class ContactInfo:
    def __init__(
        self,
        name: StrLike,
        details: Optional[List[StrLike]] = None,
        tag_line: OptionalStrLike = None,
    ) -> None:
        self.name = name
        self.details = details
        self.tag_line = tag_line


class Summary:
    def __init__(
        self, title: OptionalStrLike = None, description: OptionalStrLike = None
    ) -> None:
        self.title = title
        self.description = description


class Resume:
    def __init__(
        self,
        contact_info: ContactInfo,
        summary: Summary | None,
        sections: List[Section],
    ) -> None:
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
        """)

    def render_contact_info(self) -> str:
        contact_info = f'<h1 id="name">{self.contact_info.name}</h1>\n'

        if self.contact_info.details:
            contact_info += '<ul id="contact">\n'
            for detail in self.contact_info.details:
                contact_info += f"<li>{detail}</li>\n"
            contact_info += "</ul>\n"
        if self.contact_info.tag_line:
            contact_info += f'<p id="objective">{self.contact_info.tag_line}</p>\n'
        else:
            contact_info += '<br>\n'
        return contact_info

    def render_summary(self) -> str:
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
        sections_html = ""
        for section in self.sections:
            sections_html += self.render_section(section)
        return sections_html

    def render(self) -> str:
        s = self.TEMPLATE.replace("__NAME__", str(self.contact_info.name))
        s = s.replace("__CONTACT_INFO__", self.render_contact_info())
        s = s.replace("__SUMMARY__", self.render_summary())
        s = s.replace("__SECTIONS__", self.render_sections())
        return s

    def save(self, filename: str) -> None:
        with open(filename, "w") as f:
            f.write(self.render())

    def cli_main(self):
        parser = argparse.ArgumentParser(description="ResumeBuilder")
        parser.add_argument(
            "-o",
            "--output",
            type=str,
            dest="output_file",
            required=True,
            help="Output HTML file name.",
        )
        args = parser.parse_args()
        self.save(args.output_file)
