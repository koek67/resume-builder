# Resume Builder

A no nonsense tool to build resumes in pure Python.

See my resume definition [resume.py](./resume.py) and its output [resume.pdf](./resume.pdf).

## Requirements

* Python 3.7 or later (that's it!)

## Installation

The entire library is a single python file `resume_builder.py`. Download this file.

## Usage

To generate a resume:

```bash
python resume.py --output resume.html
```

To convert to a PDF, open in a web browser and Print as PDF. The resume generated is optimized for PDF.
In the browser, you can zoom in/out your PDF to make it fit to a page better.

## Resume Definition

Resumes are defined in Python files like `resume.py`. These files provide the best examples for how to configure a Resume.

For more details, see `resume_builder.py` and reference.md.

## Motivation

As many of us do when we have had to look for a new job, I started making a resume. Ever since college, this was a document written in either Google Docs or Microsoft Word but neither tool seemed to fit. Moreover, making small changes to the resume took time which prevented me from creating custom resumes for specific job applications.

That's when I decided to create a resume in HTML. This served me for many years and after helping a few folks modernize their resumes, I decided to open source my resume-making-tool.

This tool lets you define your resume in __Python__. No custom editors, no complicated themes, and no cost. Just a plain old resume that is easy to read, and easy to write.

## Resume Structure

* A Resume consists of:
  * a ContactInfo
  * a list of Sections
* A ContactInfo consists of:
  * name (your name)
  * details (a list of strings, can be used for email, location etc.)
* A Section consists of:
  * a title
  * a list of SectionEntries
* A SectionEntry consists of:
  * a title (big bold text)
  * a caption (text in parenthesis)
  * a dates string
  * a description
