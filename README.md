# Resume Builder

A no nonsense Python library to build resumes in HTML format.

See the example resume definition [examples/resume.py](./examples/resume.py) and its output [examples/resume.pdf](./examples/resume.pdf).

## Requirements

- Python 3.7 or later (that's it!)

## Installation

3 Ways to do it:

### Devcontainer method

1. Install [Docker](https://www.docker.com/) & [VS Code](https://code.visualstudio.com/)
2. Install [Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) extension in VS Code
3. Clone this repo & reopen it in dev container
4. Proceed to [Usage section](#usage)

### Python method

1. Install [Python](https://www.python.org/downloads/)
2. Download [`resume.py`](examples/resume.py) & [`resume_builder.py`](src/resume_builder.py)
3. Proceed to [Usage section](#usage)

### Installing the package

1. Install this package

   ```bash
   pip install git+https://github.com/koek67/resume-builder.git
   ```

   OR

   ```bash
   uv add https://github.com/koek67/resume-builder
   ```

2. Proceed to [Usage section](#usage)

## Usage

### As a Library

The `examples/` directory contains complete resume examples.
Download & edit it. Once done:

```bash
python resume.py --output resume.html
```

To convert the generated HTML to PDF:

1. Open the HTML file in a web browser
2. Print as PDF (Ctrl+P or Cmd+P)
3. The resume is optimized for PDF printing

You can zoom in/out in the browser to make it fit the page better.

## Resume Definition

Resumes are defined in Python files like [`resume.py`](examples/resume.py). These files provide the best examples for how to configure a Resume.

For more details, see [`resume_builder.py`](src/resume_builder.py) and [Reference doc](reference.md)

## Motivation

As many of us do when we have had to look for a new job, I started making a
resume. Ever since college, this was a document written in either Google Docs
or Microsoft Word but neither tool seemed to fit. Moreover, making small
changes to the resume took time which prevented me from creating custom resumes
for specific job applications.

That's when I decided to create a resume in HTML. This served me for many years
and after helping a few folks modernize their resumes, I decided to open source
my resume-making-tool.

This tool lets you define your resume in **Python**. No custom editors, no
complicated themes, and no cost. Just a plain old resume that is easy to read,
and easy to write.

## Resume Structure

- A Resume consists of:
  - a ContactInfo
  - a Summary (optional)
  - a list of Sections
- A ContactInfo consists of:
  - name (your name)
  - details (a list of strings, can be used for email, location etc.)
- A Summary (optional):
  - a title (Summary, Objective, Purpose, etc.)
  - a description
- A Section consists of:
  - a title
  - a list of SectionEntries
- A SectionEntry consists of:
  - a title (big bold text)
  - a caption (text in parenthesis)
  - a dates string
  - a description
