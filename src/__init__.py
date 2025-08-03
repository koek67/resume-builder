"""Resume builder package.

This package provides functionalities to build and save resumes in HTML format.
"""

from .resume_builder import (
    BoldText,
    BulletedList,
    ConcatText,
    ContactInfo,
    ItalicsText,
    LinkText,
    OptionalStrLike,
    Resume,
    Section,
    SectionEntry,
    StrLike,
    Summary,
    Text,
    UnderlinedText,
)

__version__ = "0.1.0"

# Main public API - what users should import
__all__ = [
    # Core classes for building resumes
    "BoldText",
    "BulletedList",
    "ConcatText",
    "ContactInfo",
    "ItalicsText",
    "LinkText",
    "OptionalStrLike",
    "Resume",
    "Section",
    "SectionEntry",
    "StrLike",
    "Summary",
    "Text",
    "UnderlinedText",
]
